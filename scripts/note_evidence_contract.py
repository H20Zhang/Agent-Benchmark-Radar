"""Validate recorded source coverage and displayed evidence, never factual truth."""
from __future__ import annotations
import hashlib
import json
import re
from datetime import date
from pathlib import Path

STATUSES = {"full-text-reviewed", "primary-protocol-reviewed", "partial", "unavailable"}
COVERAGE = {"method", "experimental_setup", "results", "limitations"}
KINDS = {"reading", "method", "setup", "quantitative", "limitations", "context"}
LANGUAGES = ("zh", "en")
NUMBER = re.compile(r"(?<![A-Za-z])[-+−]?\d+(?:\.\d+)?(?:e[-+]?\d+)?")
MARKER = re.compile(r"<!-- EVIDENCE:([a-z0-9-]+):START -->")

def note_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def _bilingual(value):
    return isinstance(value, dict) and all(isinstance(value.get(l), str) and value[l].strip() for l in LANGUAGES)

def _body(text: str, key: str):
    start, end = f"<!-- EVIDENCE:{key}:START -->", f"<!-- EVIDENCE:{key}:END -->"
    if text.count(start) != 1 or text.count(end) != 1:
        return None
    a = text.index(start) + len(start)
    b = text.index(end)
    return text[a:b] if b > a else None

def _table_rows(body):
    rows = {}
    in_table = False
    for line in body.splitlines():
        if not line.strip().startswith("|"):
            in_table = False
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells):
            in_table = True
            continue
        if not in_table:
            continue
        key = cells[0].replace("**", "").replace("`", "")
        if key in rows:
            raise ValueError(f"duplicate result row {key}")
        rows[key] = tuple(tuple(NUMBER.findall(re.sub(r"(?<=\d),(?=\d{3}(?:\D|$))", "", c).replace("−", "-"))) for c in cells[1:])
    return rows

def validate_review(identity: str, review: dict, texts: dict[str, str]) -> list[str]:
    if not isinstance(review, dict):
        return [f"{identity}: review must be an object"]
    errors = []
    fail = lambda message: errors.append(f"{identity}: {message}")
    status = review.get("status")
    if status not in STATUSES:
        fail("invalid source-reading status")
    try:
        date.fromisoformat(review.get("reviewed_at", ""))
    except (ValueError, TypeError):
        fail("invalid reviewed_at date")
    if not _bilingual(review.get("status_text")):
        fail("missing bilingual visible reading status")
    for lang in LANGUAGES:
        if review.get("note_sha256", {}).get(lang) != note_hash(texts.get(lang, "")):
            fail(f"{lang} reviewed note hash changed; reassess evidence before updating its record")

    sources = review.get("sources", [])
    if not isinstance(sources, list) or not sources:
        fail("missing reviewed sources")
        sources = []
    urls = set()
    coverage = set()
    for item in sources:
        if not isinstance(item, dict):
            fail("invalid source record")
            continue
        url = item.get("url", "")
        if not isinstance(url, str) or not url.startswith("https://") or not isinstance(item.get("version"), str) or not item.get("version", "").strip():
            fail("source needs HTTPS URL and explicit version")
        else:
            urls.add(url)
        covered = item.get("coverage", [])
        if not isinstance(covered, list) or any(not isinstance(x, str) or x not in COVERAGE for x in covered):
            fail("invalid source coverage")
        else:
            coverage.update(covered)
    if status == "full-text-reviewed":
        full = [s for s in sources if isinstance(s, dict) and s.get("kind") == "paper-full-text"]
        if not full:
            fail("full reading requires a full-text source")
        full_coverage = set().union(*(set(x for x in s.get("coverage", []) if isinstance(x, str)) for s in full if isinstance(s.get("coverage"), list))) if full else set()
        if not COVERAGE <= full_coverage:
            fail("full-text coverage must include method, experimental_setup, results and limitations")
    elif status == "primary-protocol-reviewed":
        if not any(isinstance(s, dict) and s.get("kind") == "official-protocol" for s in sources):
            fail("protocol reading requires an official-protocol source")
        if not COVERAGE <= coverage:
            fail("primary-protocol coverage is incomplete")
    if status in {"partial", "unavailable"} and not _bilingual(review.get("gaps")):
        fail("partial/unavailable reading requires explicit bilingual gaps")

    blocks = review.get("blocks", [])
    if not isinstance(blocks, list):
        fail("blocks must be a list")
        return errors
    if any(not isinstance(b, dict) for b in blocks):
        fail("invalid evidence block record")
        return errors
    ids = [b.get("id") for b in blocks]
    if len(ids) != len(set(ids)) or any(not isinstance(k, str) or not re.fullmatch(r"[a-z0-9-]+", k) for k in ids):
        fail("duplicate or invalid evidence block id")
    for kind in ("reading", "method", "setup", "limitations"):
        if not any(b.get("kind") == kind for b in blocks):
            fail(f"missing {kind} block")
    quantitative = [b for b in blocks if b.get("kind") == "quantitative"]
    mode = review.get("evidence_mode")
    if mode not in {"quantitative", "protocol-only", "unavailable"}:
        fail("invalid evidence mode")
    if mode == "quantitative" and not quantitative:
        fail("quantitative conclusions require an evidence table")
    if mode != "quantitative" and not _bilingual(review.get("non_numeric_reason")):
        fail("non-numeric evidence needs an explicit reason; never fabricate a table")

    for lang in LANGUAGES:
        declared = set(ids)
        if set(MARKER.findall(texts[lang])) != declared:
            fail(f"{lang} contains missing or undeclared evidence blocks")
    for item in blocks:
        key, kind = item.get("id"), item.get("kind")
        if kind not in KINDS:
            fail(f"{key}: unknown block kind")
        bodies = {}
        for lang in LANGUAGES:
            body = _body(texts[lang], key)
            if body is None:
                fail(f"{lang}/{key}: expected exactly one ordered evidence block")
            elif not re.sub(r"<!--.*?-->", "", body, flags=re.S).strip():
                fail(f"{lang}/{key}: empty evidence block")
            else:
                bodies[lang] = re.sub(r"<!--.*?-->", "", body, flags=re.S)
        if len(bodies) != 2:
            continue
        if kind == "reading":
            for lang, body in bodies.items():
                if _bilingual(review.get("status_text")) and review["status_text"][lang] not in body:
                    fail(f"{lang}: missing visible reading status")
                for s in sources:
                    if not isinstance(s, dict):
                        continue
                    if s.get("url") not in body or s.get("version") not in body:
                        fail(f"{lang}: reading block omits source/version")
                if status in {"partial", "unavailable"} and _bilingual(review.get("gaps")) and review["gaps"][lang] not in body:
                    fail(f"{lang}: missing visible evidence gap")
                if mode != "quantitative" and _bilingual(review.get("non_numeric_reason")) and review["non_numeric_reason"][lang] not in body:
                    fail(f"{lang}: non-numeric reason is not visible")
        if kind != "quantitative":
            continue
        url = item.get("source_url")
        if not isinstance(url, str) or url not in urls:
            fail(f"{key}: table does not identify a reviewed source")
        if not item.get("source_locator"):
            fail(f"{key}: missing precise source locator")
        if not _bilingual(item.get("conditions")):
            fail(f"{key}: missing bilingual experimental conditions")
        expected = item.get("row_ids")
        if not isinstance(expected, list) or not expected or any(not isinstance(x, str) for x in expected) or len(expected) != len(set(expected)):
            fail(f"{key}: result rows need unique canonical identities")
            expected = []
        parsed = {}
        for lang, body in bodies.items():
            if not isinstance(url, str) or url not in body:
                fail(f"{lang}/{key}: missing visible source")
            if _bilingual(item.get("conditions")) and item["conditions"][lang] not in body:
                fail(f"{lang}/{key}: missing visible experimental conditions")
            labels = item.get("metric_labels", {}).get(lang, [])
            if not isinstance(labels, list) or not labels or any(not isinstance(label, str) or not label or label not in body for label in labels):
                fail(f"{lang}/{key}: missing visible metric labels/units")
            try:
                rows = _table_rows(body)
            except ValueError as exc:
                fail(f"{lang}/{key}: {exc}")
                continue
            labels = item.get("row_labels", {}).get(lang, {k: k for k in expected})
            if not isinstance(labels, dict) or set(labels) != set(expected) or any(not isinstance(x, str) for x in labels.values()) or len(set(labels.values())) != len(labels):
                fail(f"{lang}/{key}: invalid localized row labels")
                labels = {k: k for k in expected}
            if set(rows) != set(labels.values()) or not rows:
                fail(f"{lang}/{key}: evidence table rows differ from declared identities")
            if not any(any(c for c in values) for values in rows.values()):
                fail(f"{lang}/{key}: evidence table has no numerical result")
            parsed[lang] = {key: rows[label] for key, label in labels.items() if label in rows}
        if len(parsed) == 2 and parsed["zh"] != parsed["en"]:
            fail(f"{key}: bilingual row-bound numeric parity differs")
    return errors

def validate_evidence_state(records: list[dict], root: Path):
    path = root / "data" / "note-evidence.json"
    if not path.is_file():
        return ["missing data/note-evidence.json source-coverage contract"], []
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return [f"invalid source-coverage contract: {exc}"], []
    errors, backlog = [], []
    if not isinstance(state, dict):
        return ["source-coverage contract must be an object"], []
    if state.get("schema_version") != 1:
        errors.append("unsupported note-evidence schema version")
    reviews, baseline = state.get("reviews", {}), state.get("legacy_baseline", {})
    if not isinstance(reviews, dict) or not isinstance(baseline, dict):
        return ["reviews and legacy_baseline must be objects"], []
    known = {r["id"] for r in records}
    for key in set(reviews) | set(baseline):
        if key not in known:
            errors.append(f"orphan source-coverage identity {key}")
    for identity in sorted(known):
        paths = {"zh": root/"benchmarks"/f"{identity}.md", "en": root/"benchmarks"/f"{identity}.en.md"}
        if not all(p.is_file() for p in paths.values()):
            continue  # Existing paired-note gate reports this.
        texts = {lang: p.read_text(encoding="utf-8") for lang,p in paths.items()}
        if identity in reviews:
            if identity not in baseline and isinstance(reviews[identity], dict) and reviews[identity].get("status") in {"partial", "unavailable"}:
                errors.append(f"{identity}: unresolved evidence cannot admit a new benchmark")
            errors.extend(validate_review(identity, reviews[identity], texts))
        else:
            backlog.append(identity)
            for lang, text in texts.items():
                legacy = baseline.get(identity, {})
                if not isinstance(legacy, dict) or legacy.get(lang) != note_hash(text):
                    errors.append(f"{identity}/{lang}: new or revised note needs a source-reading/evidence record; do not rebaseline")
    return errors, backlog
