#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import time
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "benchmarks.json"
README_ZH = ROOT / "README.md"
README_EN = ROOT / "README.en.md"
S2_BATCH = "https://api.semanticscholar.org/graph/v1/paper/batch?fields=title,citationCount,url,externalIds"
S2_MATCH = "https://api.semanticscholar.org/graph/v1/paper/search/match"
S2_SEARCH = "https://api.semanticscholar.org/graph/v1/paper/search"
AREA_LABELS = ("agent-memory", "rag", "data-agent")
BENCHMARK_ID_RE = re.compile(r"<!--\s*benchmark-id:([a-z0-9-]+)\s*-->")


def _s2_external_id(record: dict[str, object]) -> str | None:
    artifacts = record.get("artifacts")
    if not isinstance(artifacts, dict):
        return None
    paper = artifacts.get("preprint") or artifacts.get("paper")
    if not isinstance(paper, str) or not paper.strip():
        return None
    url = paper.strip()
    parsed = urlsplit(url)
    host = parsed.netloc.lower()
    path = parsed.path.strip("/")

    if host.endswith("arxiv.org"):
        match = re.search(r"(?:^|/)(?:abs|pdf)/([^/?#]+)", parsed.path)
        if match:
            arxiv_id = match.group(1).removesuffix(".pdf")
            arxiv_id = re.sub(r"v\d+$", "", arxiv_id)
            return f"ARXIV:{arxiv_id}"
    if host.endswith("aclanthology.org") and path:
        return f"DOI:10.18653/v1/{path.split('/')[0]}"
    if host.endswith("doi.org") and path:
        return f"DOI:{path}"
    if host.endswith("semanticscholar.org"):
        return f"URL:{url}"
    if host.endswith("acm.org") or host.endswith("biorxiv.org") or host.endswith("aclweb.org"):
        return f"URL:{url}"
    return None


def _request_json(url: str, *, payload: dict[str, object] | None = None) -> object:
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    headers = {
        "Accept": "application/json",
        "User-Agent": "Agent-Benchmark-Radar/1.0 (+https://github.com/H20Zhang/Agent-Benchmark-Radar)",
    }
    if body is not None:
        headers["Content-Type"] = "application/json"
    api_key = os.environ.get("S2_API_KEY")
    if api_key:
        headers["x-api-key"] = api_key
    request = Request(url, data=body, headers=headers, method="POST" if body is not None else "GET")

    delay = 2.0
    last_error: Exception | None = None
    for attempt in range(4):
        try:
            with urlopen(request, timeout=45) as response:
                return json.loads(response.read().decode("utf-8"))
        except HTTPError as exc:
            last_error = exc
            if exc.code not in {429, 500, 502, 503, 504} or attempt == 3:
                raise
        except URLError as exc:
            last_error = exc
            if attempt == 3:
                raise
        time.sleep(delay)
        delay *= 2
    assert last_error is not None
    raise last_error


class _CitationTitleParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "meta" or self.title is not None:
            return
        values = {key.lower(): value for key, value in attrs if key and value}
        if values.get("name", "").lower() == "citation_title":
            title = html.unescape(values.get("content", "")).strip()
            self.title = title or None


def _request_text(url: str) -> str:
    headers = {
        "Accept": "text/html,application/xhtml+xml",
        "User-Agent": "Agent-Benchmark-Radar/1.0 (+https://github.com/H20Zhang/Agent-Benchmark-Radar)",
    }
    request = Request(url, headers=headers, method="GET")
    delay = 2.0
    last_error: Exception | None = None
    for attempt in range(4):
        try:
            with urlopen(request, timeout=45) as response:
                return response.read().decode("utf-8", errors="replace")
        except HTTPError as exc:
            last_error = exc
            if exc.code not in {429, 500, 502, 503, 504} or attempt == 3:
                raise
        except URLError as exc:
            last_error = exc
            if attempt == 3:
                raise
        time.sleep(delay)
        delay *= 2
    assert last_error is not None
    raise last_error


def _normalized_title(value: str) -> str:
    return " ".join(re.sub(r"[\W_]+", " ", html.unescape(value).casefold()).split())


def _s2_title_fallback(record: dict[str, object]) -> dict[str, object] | None:
    artifacts = record.get("artifacts")
    if not isinstance(artifacts, dict):
        return None
    paper_url = artifacts.get("paper")
    if not isinstance(paper_url, str) or not urlsplit(paper_url).netloc.lower().endswith("aclanthology.org"):
        return None

    try:
        parser = _CitationTitleParser()
        parser.feed(_request_text(paper_url))
        if not parser.title:
            return None
        target = _normalized_title(parser.title)
        fields = "title,citationCount,url,externalIds"

        # Semantic Scholar documents /paper/search/match as the endpoint
        # intended for retrieving one paper by closest title match. This
        # avoids the relevance-search failure mode for hyphenated titles.
        time.sleep(1.05)
        match_query = urlencode({"query": parser.title, "fields": fields})
        match_response = _request_json(f"{S2_MATCH}?{match_query}")
        match_candidates: list[dict[str, object]] = []
        if isinstance(match_response, dict):
            data = match_response.get("data")
            if isinstance(data, list):
                match_candidates = [item for item in data if isinstance(item, dict)]
            elif isinstance(match_response.get("paperId"), str):
                match_candidates = [match_response]
        exact_match = [
            candidate
            for candidate in match_candidates
            if isinstance(candidate.get("title"), str)
            and _normalized_title(candidate["title"]) == target
        ]
        if len(exact_match) == 1:
            return exact_match[0]

        # Conservative fallback to relevance search: replace hyphens,
        # then accept only a unique normalized exact-title match.
        time.sleep(1.05)
        search_title = re.sub(r"[-‐‑‒–—]", " ", parser.title)
        query = urlencode(
            {
                "query": search_title,
                "limit": 10,
                "fields": fields,
            }
        )
        response = _request_json(f"{S2_SEARCH}?{query}")
    except (HTTPError, URLError, UnicodeError, ValueError):
        return None

    if not isinstance(response, dict) or not isinstance(response.get("data"), list):
        return None
    matches = [
        candidate
        for candidate in response["data"]
        if isinstance(candidate, dict)
        and isinstance(candidate.get("title"), str)
        and _normalized_title(candidate["title"]) == target
    ]
    if len(matches) == 1:
        return matches[0]

    anthology_id = urlsplit(paper_url).path.strip("/").split("/")[0]
    expected_doi = f"10.18653/v1/{anthology_id}".casefold()
    doi_matches = [
        candidate
        for candidate in matches
        if isinstance(candidate.get("externalIds"), dict)
        and str(candidate["externalIds"].get("DOI", "")).casefold() == expected_doi
    ]
    return doi_matches[0] if len(doi_matches) == 1 else None


def _refresh_citations(records: list[dict[str, object]], today: str) -> bool:
    indexed: list[tuple[dict[str, object], str]] = []
    changed = False
    for record in records:
        external_id = _s2_external_id(record)
        if external_id is None:
            artifacts = record.get("artifacts")
            has_paper = isinstance(artifacts, dict) and bool(artifacts.get("paper"))
            desired = {
                "count": None,
                "source": "semantic-scholar",
                "updated_at": today,
                "status": "unmatched" if has_paper else "no-paper",
                "paper_id": None,
                "url": None,
            }
            if record.get("citations") != desired:
                record["citations"] = desired
                changed = True
        else:
            indexed.append((record, external_id))

    if not indexed:
        return changed

    response = _request_json(S2_BATCH, payload={"ids": [external_id for _, external_id in indexed]})
    if not isinstance(response, list) or len(response) != len(indexed):
        raise RuntimeError("Semantic Scholar batch response shape drift")

    for (record, _external_id), paper in zip(indexed, response):
        if not isinstance(paper, dict):
            paper = _s2_title_fallback(record)
        if not isinstance(paper, dict):
            desired = {
                "count": None,
                "source": "semantic-scholar",
                "updated_at": today,
                "status": "unmatched",
                "paper_id": None,
                "url": None,
            }
        else:
            count = paper.get("citationCount")
            paper_id = paper.get("paperId")
            paper_url = paper.get("url")
            if not isinstance(count, int) or count < 0 or not isinstance(paper_id, str):
                desired = {
                    "count": None,
                    "source": "semantic-scholar",
                    "updated_at": today,
                    "status": "unmatched",
                    "paper_id": None,
                    "url": None,
                }
            else:
                desired = {
                    "count": count,
                    "source": "semantic-scholar",
                    "updated_at": today,
                    "status": "ok",
                    "paper_id": paper_id,
                    "url": paper_url if isinstance(paper_url, str) else f"https://www.semanticscholar.org/paper/{paper_id}",
                }
        if record.get("citations") != desired:
            record["citations"] = desired
            changed = True
    return changed


def _citation_cell(record: dict[str, object]) -> str:
    citation = record.get("citations")
    if not isinstance(citation, dict) or citation.get("status") != "ok":
        return "—"
    count = citation.get("count")
    if not isinstance(count, int):
        return "—"
    display = f"{count:,}"
    target = citation.get("url")
    return f"[{display}]({target})" if isinstance(target, str) and target else display


def _patch_area_block(block: str, records_by_id: dict[str, dict[str, object]], language: str) -> str:
    out: list[str] = []
    header_done = False
    separator_done = False
    for line in block.splitlines(keepends=True):
        newline = "\n" if line.endswith("\n") else ""
        raw = line[:-1] if newline else line
        visible = raw.strip()
        if visible.startswith("|") and visible.endswith("|"):
            cells = [cell.strip() for cell in visible.split("|")[1:-1]]
            if not header_done:
                expected_header = "引用数 (S2)" if language == "zh" else "Citations (S2)"
                if len(cells) == 4:
                    cells.insert(2, expected_header)
                elif len(cells) == 5:
                    cells[2] = expected_header
                raw = "| " + " | ".join(cells) + " |"
                header_done = True
                out.append(raw + newline)
                continue
            if not separator_done and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
                if len(cells) == 4:
                    cells.insert(2, "---:")
                elif len(cells) == 5:
                    cells[2] = "---:"
                raw = "|" + "|".join(cells) + "|"
                separator_done = True
                out.append(raw + newline)
                continue
            identities = BENCHMARK_ID_RE.findall(raw)
            if len(identities) == 1:
                record = records_by_id.get(identities[0])
                if record is None:
                    raise RuntimeError(f"README row has unknown benchmark id {identities[0]}")
                if len(cells) == 4:
                    cells.insert(2, _citation_cell(record))
                elif len(cells) == 5:
                    cells[2] = _citation_cell(record)
                else:
                    raise RuntimeError(f"unexpected area-table column count {len(cells)} for {identities[0]}")
                raw = "| " + " | ".join(cells) + " |"
        out.append(raw + newline)
    return "".join(out)


def _citation_note(language: str, today: str) -> str:
    if language == "zh":
        body = f"引用数来自 Semantic Scholar，最后刷新 **{today}**；`—` 表示暂无可匹配论文。引用数仅作影响力上下文，不参与阶段划分。"
    else:
        body = f"Citation counts are from Semantic Scholar, last refreshed **{today}**; `—` means no paper could be matched. Counts are context for adoption, not an input to stage labels."
    return f"<!-- CITATION-META:START -->\n{body}\n<!-- CITATION-META:END -->"


def _patch_readme(path: Path, records: list[dict[str, object]], language: str, today: str) -> bool:
    original = path.read_text(encoding="utf-8")
    text = original
    records_by_id = {str(record.get("id")): record for record in records}
    for area in AREA_LABELS:
        label = f"TABLE-FIRST:AREA:{area}"
        start_marker = f"<!-- {label}:START -->"
        end_marker = f"<!-- {label}:END -->"
        if text.count(start_marker) != 1 or text.count(end_marker) != 1:
            raise RuntimeError(f"{path.name}: malformed {label} block")
        prefix, rest = text.split(start_marker, 1)
        block, suffix = rest.split(end_marker, 1)
        text = prefix + start_marker + _patch_area_block(block, records_by_id, language) + end_marker + suffix

    note = _citation_note(language, today)
    note_re = re.compile(r"<!-- CITATION-META:START -->.*?<!-- CITATION-META:END -->", re.S)
    if note_re.search(text):
        text = note_re.sub(note, text, count=1)
    else:
        first_area = "### Agent Memory"
        if first_area not in text:
            raise RuntimeError(f"{path.name}: cannot locate first complete-area heading")
        text = text.replace(first_area, note + "\n\n" + first_area, 1)

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def _migrate_contract() -> bool:
    changed = False

    validator = ROOT / "scripts" / "validate_reading.py"
    text = validator.read_text(encoding="utf-8")
    old = '''            for line in block.splitlines():\n                visible = strip_html_comments(line).strip()\n                if visible.startswith("|") and visible.endswith("|"):\n                    cells = visible.split("|")[1:-1]\n                    if len(cells) != 4:\n                        errors.append(f"{language}: {label} must have exactly four visible columns")\n                        break\n'''
    new = '''            expected_columns = 4 if label == "TABLE-FIRST:RECENT" else 5\n            for line in block.splitlines():\n                visible = strip_html_comments(line).strip()\n                if visible.startswith("|") and visible.endswith("|"):\n                    cells = visible.split("|")[1:-1]\n                    if len(cells) != expected_columns:\n                        errors.append(\n                            f"{language}: {label} must have exactly {expected_columns} visible columns"\n                        )\n                        break\n'''
    if old in text:
        validator.write_text(text.replace(old, new, 1), encoding="utf-8")
        changed = True
    elif new not in text:
        raise RuntimeError("validate_reading.py table-column contract changed unexpectedly")

    test_path = ROOT / "tests" / "test_table_first_readme.py"
    text = test_path.read_text(encoding="utf-8")
    old = '''                    for line in block.splitlines():\n                        visible = line.split("<!--", 1)[0].strip()\n                        if visible.startswith("|") and visible.endswith("|"):\n                            self.assertEqual(4, len(visible.split("|")[1:-1]), (language, label, line))\n'''
    new = '''                    expected_columns = 4 if label == "TABLE-FIRST:RECENT" else 5\n                    for line in block.splitlines():\n                        visible = line.split("<!--", 1)[0].strip()\n                        if visible.startswith("|") and visible.endswith("|"):\n                            self.assertEqual(\n                                expected_columns,\n                                len(visible.split("|")[1:-1]),\n                                (language, label, line),\n                            )\n'''
    if old in text:
        test_path.write_text(text.replace(old, new, 1), encoding="utf-8")
        changed = True
    elif new not in text:
        raise RuntimeError("test_table_first_readme.py table-column contract changed unexpectedly")

    schema = ROOT / "SCHEMA.md"
    text = schema.read_text(encoding="utf-8")
    marker = "## Citation metadata"
    if marker not in text:
        insertion = '''\n## Citation metadata\n\nEvery registry record carries a `citations` object so the complete area tables can expose a consistent, auditable influence signal without turning citation count into a quality ranking:\n\n- `count`: Semantic Scholar citation count, or `null` when no paper can be matched;\n- `source`: currently `semantic-scholar`;\n- `updated_at`: `YYYY-MM-DD` refresh date;\n- `status`: `ok`, `no-paper`, or `unmatched`;\n- `paper_id` and `url`: the resolved Semantic Scholar paper identity when `status=ok`.\n\nA real zero must remain `0`; unknown is `null`. Citation count is age- and source-dependent context only. It must not determine `importance`, `evolution_role`, genealogy, or frontier status.\n'''
        text = text.replace("\n## Evolution role\n", insertion + "\n## Evolution role\n", 1)
        schema.write_text(text, encoding="utf-8")
        changed = True

    workflow = ROOT / "docs" / "DAILY_WORKFLOW.md"
    text = workflow.read_text(encoding="utf-8")
    needle = "1. Update `data/benchmarks.json` first, preserving canonical identity, aliases/version lineage, source release precision, area, role, capabilities, environment, protocol, scale, measurement strength, coverage gap, confounders, artifacts, verification time, and v2 provenance."
    replacement = "1. Update `data/benchmarks.json` first, preserving canonical identity, aliases/version lineage, source release precision, area, role, capabilities, environment, protocol, scale, measurement strength, coverage gap, confounders, artifacts, citation metadata, verification time, and v2 provenance. Citation counts use Semantic Scholar and may be refreshed mechanically without changing editorial role/importance."
    if needle in text:
        text = text.replace(needle, replacement, 1)
        changed = True
    elif replacement not in text:
        raise RuntimeError("DAILY_WORKFLOW canonical-location text changed unexpectedly")
    needle = "3. **Complete area tables in README** — every canonical Agent Memory, RAG / Agentic Retrieval, and Data Agent record remains directly scannable in the main page. Each row has one concise `What it tests / 考察内容` description rather than a second change/explanation column. Do not replace these tables with links to the Library."
    replacement = "3. **Complete area tables in README** — every canonical Agent Memory, RAG / Agentic Retrieval, and Data Agent record remains directly scannable in the main page. Each row has stage, benchmark, Semantic Scholar citation count, release time, and one concise `What it tests / 考察内容` description. Citation count is context only and must not drive stage ordering. Do not replace these tables with links to the Library."
    if needle in text:
        text = text.replace(needle, replacement, 1)
        changed = True
    elif replacement not in text:
        raise RuntimeError("DAILY_WORKFLOW reader-projection text changed unexpectedly")
    workflow.write_text(text, encoding="utf-8")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--migrate", action="store_true", help="update the reader/validator contract once")
    parser.add_argument("--date", default=date.today().isoformat(), help="citation refresh date (YYYY-MM-DD)")
    args = parser.parse_args()

    records = json.loads(REGISTRY.read_text(encoding="utf-8"))
    if not isinstance(records, list):
        raise RuntimeError("benchmark registry must be a JSON array")

    changed = _refresh_citations(records, args.date)
    if changed:
        REGISTRY.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    changed = _patch_readme(README_ZH, records, "zh", args.date) or changed
    changed = _patch_readme(README_EN, records, "en", args.date) or changed
    if args.migrate:
        changed = _migrate_contract() or changed

    print("citation refresh changed files" if changed else "citation refresh: no changes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
