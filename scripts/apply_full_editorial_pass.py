#!/usr/bin/env python3
"""Apply the authored bilingual editorial pass without inventing benchmark facts.

This is a one-shot migration. Existing source-backed narrative is preserved;
editorial judgments, illustrative examples, and proposed experiments are explicit.
The persistent guide file is the source for the corresponding editorial blocks.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-05"
NOTES = ROOT / "benchmarks"
GUIDE_PATH = ROOT / "data/editorial/reading_guides.json"
MARKER = "<!-- EDITORIAL-GUIDE:v1 -->"


def dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_guides() -> dict[str, dict]:
    if GUIDE_PATH.exists():
        records = json.loads(GUIDE_PATH.read_text(encoding="utf-8"))
    else:
        inputs = sorted((ROOT / ".editorial").glob("*.json"))
        if len(inputs) != 9:
            raise RuntimeError(f"Expected nine authored guide batches, found {len(inputs)}")
        records = [record for path in inputs for record in json.loads(path.read_text(encoding="utf-8"))]
    guides = {record["id"]: record for record in records}
    if len(guides) != len(records):
        raise RuntimeError("Duplicate authored guide identity")
    return guides


def parse_note(text: str) -> tuple[str, list[tuple[str, str]]]:
    title = next((line[2:].strip() for line in text.splitlines() if line.startswith("# ")), "")
    sections: list[tuple[str, str]] = []
    heading, lines = "", []

    def flush() -> None:
        nonlocal lines
        body = "\n".join(lines).strip()
        if body:
            sections.append((heading, body))
        lines = []

    for line in text.splitlines():
        if line.startswith("# "):
            continue
        match = re.match(r"^##\s+(.+)$", line)
        labeled = re.match(r"^-\s+\*\*([^*]+?)[：:]\*\*\s*(.*)$", line)
        if match:
            flush()
            heading = match.group(1).strip()
        elif labeled and labeled.group(1).strip().lower() in {
            "测量对象", "最近前身", "决定性证据", "结论上限", "最强混淆", "未覆盖", "谱系",
            "measurement object", "closest predecessor", "decisive evidence", "score ceiling",
            "strongest confounder", "remaining gap", "genealogy",
        }:
            flush()
            heading = labeled.group(1).strip()
            lines = [labeled.group(2)]
        else:
            # GitHub language/navigation chrome is replaced by one consistent line.
            if re.search(r"\*\*中文\*\*.*\[English\]|\*\*English\*\*.*\[中文\]|\[返回(?:入口|Radar)\]", line):
                continue
            lines.append(line)
    flush()
    return title, sections


def source_links(item: dict, lang: str) -> str:
    names = {"paper": "论文", "code": "代码", "data": "数据", "project": "项目", "leaderboard": "官方成绩", "preprint": "预印本"}
    links = []
    for key, url in item.get("artifacts", {}).items():
        if isinstance(url, str) and url.startswith("https://"):
            links.append(f"[{names.get(key, key) if lang == 'zh' else key.replace('_', ' ').title()}]({url})")
    return " · ".join(links)


def integrate_note(item: dict, guide: dict, lang: str, names: dict[str, str]) -> bool:
    suffix = ".en.md" if lang == "en" else ".md"
    path = NOTES / (item["id"] + suffix)
    original = path.read_text(encoding="utf-8")
    if MARKER in original:
        return False
    title, sections = parse_note(original)
    if not title or not sections:
        raise RuntimeError(f"Cannot safely parse existing note: {path}")
    alternate = item["id"] + (".en.md" if lang == "zh" else ".md")
    root_readme = "../README.md" if lang == "zh" else "../README.en.md"
    navigation = (f"**中文** · [English]({alternate}) · [返回全部基准]({root_readme}#all-benchmarks)" if lang == "zh"
                  else f"[中文]({alternate}) · **English** · [All benchmarks]({root_readme}#all-benchmarks)")
    result = [f"# {title}", "", navigation, "", source_links(item, lang), "", MARKER, ""]
    result += ["## 选型判断" if lang == "zh" else "## Selection judgment", "", guide["judgment"][lang], ""]
    result += ["## 任务示意" if lang == "zh" else "## Illustrative task", "", guide["example"][lang], ""]
    result += [("以上为帮助理解测量机制的示意，不是数据集原题。" if lang == "zh" else "This illustration explains the measurement mechanism; it is not a quoted dataset example."), ""]
    # Keep the benchmark-specific evidence and limitations, rather than replacing
    # them with registry prose or counting section labels as quality evidence.
    heading_map = {
        "结论上限": "结果支持什么判断", "最强混淆": "比较条件与主要限制", "未覆盖": "适用范围与限制",
        "Score ceiling": "What the evidence supports", "Strongest confounder": "Comparison conditions and limitations",
        "Remaining gap": "Scope and limitations",
    }
    for heading, body in sections:
        if not heading:
            # Preserve substantive introductory text but remove duplicate link-only chrome.
            filtered = []
            for line in body.splitlines():
                stripped = line.strip()
                if stripped and re.sub(r"\[[^\]]+\]\([^)]*\)|[·|*\s]", "", stripped):
                    filtered.append(line)
            body = "\n".join(filtered).strip()
            if body:
                result += ["## 评测背景" if lang == "zh" else "## Evaluation context", "", body, ""]
            continue
        result += ["## " + heading_map.get(heading, heading), "", body, ""]
    result += ["## 建议的判别实验" if lang == "zh" else "## Suggested discriminating experiment", "", guide["experiment"][lang], ""]
    result += [("这是针对上述限制提出的实验建议，不是原论文已经完成的实验或已经观察到的结果。" if lang == "zh" else "This is a proposed experiment addressing the limitations above, not an experiment or result claimed to have been reported by the benchmark authors."), ""]
    result += ["## 相邻基准" if lang == "zh" else "## Related benchmarks", ""]
    for related in guide["related"]:
        result.append(f"- [{names[related]}]({related}{suffix})")
    result += ["", "## 来源与版本" if lang == "zh" else "## Sources and versions", "", source_links(item, lang), ""]
    verified = item.get("last_verified", "—")
    result.append((f"编辑整理：{DATE}。元数据最近核验：{verified}。两者不是同一日期含义；本次文字整理不代表所有论文与排行榜已重新核验。正文中来自原论文的数字保留其原始设置与历史语境；跨版本、轨道或预算不直接排名。" if lang == "zh" else f"Editorial revision: {DATE}. Last recorded metadata verification: {verified}. These dates describe different activities; editing is not a fresh verification of every paper or leaderboard. Paper-reported numbers retain their original configuration and historical scope; different releases, tracks, or budgets are not directly ranked."))
    result += ["", "<!-- /EDITORIAL-GUIDE:v1 -->", ""]
    path.write_text("\n".join(result), encoding="utf-8")
    return True


def update_overlays(registry: list[dict], guides: dict[str, dict]) -> None:
    directory = ROOT / "data/editorial/benchmarks"
    for item in registry:
        path = directory / (item["id"] + ".json")
        current = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"id": item["id"]}
        guide = guides[item["id"]]
        current.update({
            "score_supports": guide["judgment"],
            "next_validation": guide["experiment"],
            "evidence_brief": guide["judgment"],
            "editorial_revised_at": DATE,
        })
        dump(path, current)


def update_readme(path: Path, lang: str) -> None:
    text = path.read_text(encoding="utf-8")
    if "<!-- FULL-EDITORIAL-HOME:v1 -->" in text:
        return
    is_zh = lang == "zh"
    other = "README.en.md" if is_zh else "README.md"
    intro = (f'''<!-- ONBOARDING:START -->
<!-- FULL-EDITORIAL-HOME:v1 -->
<div align="center">

<h1>Agent Benchmark Radar</h1>

<p><strong>找到合适的评测，看清分数能够证明什么。</strong></p>

<p>Agent Memory · RAG / Agentic Retrieval · Data Agents</p>
<p><strong>中文</strong> · <a href="{other}">English</a></p>
<p><strong>网站待完善；当前内容以本 README 为准。</strong></p>

<p><a href="https://github.com/H20Zhang/Agent-Benchmark-Radar/actions/workflows/validate.yml"><img alt="Validation" src="https://github.com/H20Zhang/Agent-Benchmark-Radar/actions/workflows/validate.yml/badge.svg"></a></p>
</div>

本页负责**发现与选型**；每个基准的详情负责**任务机制、证据、比较条件与实验设计**。收录包含完整 benchmark，也包含有独立测量贡献的诊断与审计；它们不是可互换的统一排行榜。

## 从这里开始

| 研究动作 | 入口 | 用它解决的问题 |
|---|---|---|
| **Pick** | [Benchmark Library](#all-benchmarks) | 找到任务、数据与测量对象匹配的基准。 |
| **Build** | [Evaluation Recipes](#evaluation-recipes) | 从研究主张出发，组合主评测、对照与补充验证。 |
| **Discover** | [下一阶段关键评测方向](#evaluation-frontiers) | 判断尚缺哪项证据，而不是把低分直接当作研究机会。 |
| **Track** | [近 30 天变化](#frontier-signals) · [最近半年发布](#release-timeline) | 区分新发布、协议变化与持续成立的演化方向。 |

| 方向 | 先看脉络 | 配一套评测 | 完整列表 |
|---|---|---|---|
| **Agent Memory** | [Memory Map](#benchmark-memory) | [Memory Recipes](#recipe-memory) | [Memory Benchmark](#registry-memory) |
| **RAG / Agentic Retrieval** | [Retrieval Map](#benchmark-rag) | [Retrieval Recipes](#recipe-rag) | [Retrieval Benchmark](#registry-rag) |
| **Data Agents** | [Data Agent Map](#benchmark-data) | [Data Agent Recipes](#recipe-data) | [Data Agent Benchmark](#registry-data) |

**读分数前先对齐：**任务与切分、数据与环境版本、模型与工具、预算与重试、指标与评分器。详情中的“示意任务”帮助理解机制；“建议的判别实验”是研究建议，不冒充原论文结果。引用量表示传播情况，不等于基准质量。

[收录与证据标准](CURATION.md) · [详情页写作规范](docs/BENCHMARK_DETAIL_PAGE_GUIDE.md)

---
<!-- ONBOARDING:END -->''' if is_zh else f'''<!-- ONBOARDING:START -->
<!-- FULL-EDITORIAL-HOME:v1 -->
<div align="center">

<h1>Agent Benchmark Radar</h1>

<p><strong>Find the right evaluation. Know what its score can establish.</strong></p>

<p>Agent Memory · RAG / Agentic Retrieval · Data Agents</p>
<p><a href="{other}">中文</a> · <strong>English</strong></p>
<p><strong>The website is under improvement; use this README as the current content entry.</strong></p>

<p><a href="https://github.com/H20Zhang/Agent-Benchmark-Radar/actions/workflows/validate.yml"><img alt="Validation" src="https://github.com/H20Zhang/Agent-Benchmark-Radar/actions/workflows/validate.yml/badge.svg"></a></p>
</div>

This page supports **discovery and selection**. Individual benchmark notes explain **task mechanics, evidence, comparison conditions, and experimental design**. The registry includes complete benchmarks as well as diagnostics and audits with independent measurement contributions; they are not interchangeable entries in a universal leaderboard.

## Start here

| Research action | Entry | Decision supported |
|---|---|---|
| **Pick** | [Benchmark Library](#all-benchmarks) | Match the task, data, and measurement object to your research. |
| **Build** | [Evaluation Recipes](#evaluation-recipes) | Combine a primary evaluation, controls, and complementary validation around a claim. |
| **Discover** | [Next evaluation frontiers](#evaluation-frontiers) | Identify missing evidence rather than equating a low score with a research opportunity. |
| **Track** | [Changes over 30 days](#frontier-signals) · [Six-month releases](#release-timeline) | Separate new releases, protocol changes, and durable shifts in evaluation. |

| Area | Evolution | Evaluation suite | Complete list |
|---|---|---|---|
| **Agent Memory** | [Memory Map](#benchmark-memory) | [Memory Recipes](#recipe-memory) | [Memory Benchmarks](#registry-memory) |
| **RAG / Agentic Retrieval** | [Retrieval Map](#benchmark-rag) | [Retrieval Recipes](#recipe-rag) | [Retrieval Benchmarks](#registry-rag) |
| **Data Agents** | [Data Agent Map](#benchmark-data) | [Data Agent Recipes](#recipe-data) | [Data Agent Benchmarks](#registry-data) |

**Before comparing scores, align:** tasks and splits, data and environment versions, models and tools, budgets and retries, metrics and graders. Illustrative tasks explain mechanisms; suggested experiments are research proposals, not reported results. Citation counts describe dissemination, not benchmark quality.

[Curation and evidence standards](CURATION.md) · [Detail-page writing guide](docs/BENCHMARK_DETAIL_PAGE_GUIDE.md)

---
<!-- ONBOARDING:END -->''')
    pattern = r"<!-- ONBOARDING:START -->.*?<!-- ONBOARDING:END -->"
    if len(re.findall(pattern, text, flags=re.S)) != 1:
        raise RuntimeError(f"Expected one onboarding region in {path}")
    text = re.sub(pattern, lambda _: intro, text, count=1, flags=re.S)
    # The homepage does not advertise historical source snapshots as current leaders.
    score_headings = [r"^### 当前成绩追踪\s*$", r"^### Current results tracking\s*$", r"^### Current result tracking\s*$", r"^### Current results\s*$"]
    for expression in score_headings:
        match = re.search(expression, text, flags=re.M)
        if match:
            tail = re.search(r"^#{1,3}\s", text[match.end():], flags=re.M)
            end = match.end() + tail.start() if tail else len(text)
            section = text[match.end():end]
            # Do not remove neighboring canonical markers or anchors when the score section ends.
            boundary = re.search(r"<!--\s*[A-Z][A-Z-]*:(?:START|END)\s*-->|<a\s+id=", section)
            if boundary:
                end = match.end() + boundary.start()
            replacement = ("### 如何查看成绩\n\n成绩需要连同轨道、版本、模型、工具与预算阅读。本页不将不同测量对象排成一张总榜；详情页保留原论文证据，已整理的数值见[结构化结果记录](data/results/)。记录的核验日期不代表实时排行榜状态。\n\n" if is_zh else "### Reading results\n\nRead results with their track, version, model, tools, and budget. This homepage does not pool different measurement objects into a league table. Detail notes retain paper-specific evidence; normalized numbers are available in the [structured result records](data/results/). A recorded verification date is not a live-leaderboard claim.\n\n")
            text = text[:match.start()] + replacement + text[end:]
            break
    # Put current changes before suite construction, without dropping any canonical content.
    recipe = re.search(r"<!-- EVALUATION-RECIPES:START -->.*?<!-- EVALUATION-RECIPES:END -->", text, flags=re.S)
    if recipe:
        block = recipe.group(0)
        text = text[:recipe.start()] + text[recipe.end():]
        # Keep recipes near the library, after orientation and current evidence.
        destination = re.search(r'<a id="all-benchmarks"></a>', text)
        if destination:
            text = text[:destination.start()] + block + "\n\n" + text[destination.start():]
        else:
            text += "\n\n" + block + "\n"
    path.write_text(text, encoding="utf-8")


def remove_runtime_padding() -> None:
    path = ROOT / "web/src/lib/deep-reads.mjs"
    text = path.read_text(encoding="utf-8")
    start = text.find("const DEPTH_WITNESSES")
    finish = text.find("export function loadDeepRead", start)
    if start < 0 or finish < 0:
        raise RuntimeError("Unexpected deep-read module; refusing an unsafe source rewrite")
    text = text[:start] + text[finish:]
    text = text.replace('import { loadRegistry } from "./registry.mjs";\n', "")
    function_start = text.index("export function loadDeepRead")
    text = text[:function_start] + '''export function loadDeepRead(id, lang) {
  if (!/^[a-z0-9][a-z0-9-]*$/.test(id) || !["zh", "en"].includes(lang)) return undefined;
  const filename = `${id}${lang === "en" ? ".en" : ""}.md`;
  const path = fromRepositoryRoot("benchmarks", filename);
  if (!existsSync(path)) return undefined;
  const markdown = readFileSync(path, "utf8");
  return { id, lang, markdown, html: renderDeepReadMarkdown(markdown), canonicalAppendixAdded: false };
}
'''
    # Source prose is no longer globally rewritten, and all editorial content lives in the notes.
    path.write_text(text, encoding="utf-8")
    test_path = ROOT / "web/tests/deep-reads.test.mjs"
    tests = test_path.read_text(encoding="utf-8")
    tests = re.sub(r'test\("thin deep reads.*?\n\}\);\n', '''test("authored notes are rendered without synthetic canonical appendices", () => {
  for (const lang of ["zh", "en"]) {
    const note = loadDeepRead("scale-qa", lang);
    assert.equal(note.canonicalAppendixAdded, false);
    assert.match(note.markdown, /EDITORIAL-GUIDE:v1/);
    assert.doesNotMatch(note.html, /Canonical evaluation contract|规范评测契约/);
    assert.match(note.html, lang === "zh" ? /建议的判别实验/ : /Suggested discriminating experiment/);
  }
});
''', tests, count=1, flags=re.S)
    test_path.write_text(tests, encoding="utf-8")


def replace_audit() -> None:
    (ROOT / "scripts/audit_detail_pages.py").write_text('''#!/usr/bin/env python3
"""Structural integrity audit, not a semantic-quality or factual-validity grade."""
from __future__ import annotations
import json
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def main() -> int:
    registry = json.loads((ROOT / "data/benchmarks.json").read_text(encoding="utf-8"))
    guides = json.loads((ROOT / "data/editorial/reading_guides.json").read_text(encoding="utf-8"))
    by_id = {item["id"]: item for item in guides}
    expected = {item["id"] for item in registry}
    errors = []
    if len(by_id) != len(guides) or set(by_id) != expected:
        errors.append("Authored-guide identities differ from the canonical registry")
    checked = 0
    for item in registry:
        guide = by_id.get(item["id"])
        if not guide:
            continue
        for field in ("judgment", "example", "experiment"):
            if not all(isinstance(guide.get(field, {}).get(lang), str) and guide[field][lang].strip() for lang in ("zh", "en")):
                errors.append(f"{item['id']}: missing bilingual {field}")
        for related in guide.get("related", []):
            if related not in expected or related == item["id"]:
                errors.append(f"{item['id']}: invalid related benchmark {related}")
        for lang, suffix in (("zh", ".md"), ("en", ".en.md")):
            path = ROOT / "benchmarks" / (item["id"] + suffix)
            if not path.exists():
                errors.append(f"Missing {path.name}")
                continue
            text = path.read_text(encoding="utf-8")
            checked += 1
            if text.count("<!-- EDITORIAL-GUIDE:v1 -->") != 1:
                errors.append(f"{path.name}: missing or duplicate authored editorial block")
            for field in ("judgment", "example", "experiment"):
                value = guide.get(field, {}).get(lang, "")
                if not value or text.count(value) != 1:
                    errors.append(f"{path.name}: authored {field} missing, duplicated, or out of sync")
            primary = item.get("artifacts", {}).get("paper")
            if primary and primary not in text:
                errors.append(f"{path.name}: canonical primary source is missing")
            if "规范评测契约" in text or "Canonical evaluation contract" in text:
                errors.append(f"{path.name}: generated appendix is not authored evidence")
            for target in re.findall(r"\\]\\(([^)\\s]+\\.md)(?:#[^)]*)?\\)", text):
                if "://" not in target and not (path.parent / target).resolve().is_file():
                    errors.append(f"{path.name}: broken local link {target}")
    print(f"Structural editorial audit: {len(registry)} benchmarks; {checked} bilingual notes")
    print("Checks cover presence, synchronization and local references; they do not certify factual accuracy or semantic quality.")
    for error in errors:
        print("ERROR: " + error)
    print(f"Integrity errors: {len(errors)}")
    return int(bool(errors))

if __name__ == "__main__":
    raise SystemExit(main())
''', encoding="utf-8")


def main() -> None:
    registry = json.loads((ROOT / "data/benchmarks.json").read_text(encoding="utf-8"))
    guides = load_guides()
    expected = {item["id"] for item in registry}
    if set(guides) != expected or len(registry) != 126:
        raise RuntimeError(f"Coverage mismatch: missing={expected-set(guides)} extra={set(guides)-expected}; re-review changed registry before proceeding")
    for guide in guides.values():
        for field in ("judgment", "example", "experiment"):
            assert all(guide.get(field, {}).get(lang, "").strip() for lang in ("zh", "en")), guide["id"]
        assert all(related in expected and related != guide["id"] for related in guide["related"]), guide["id"]
    names = {item["id"]: item["name"] for item in registry}
    dump(GUIDE_PATH, [guides[item["id"]] for item in registry])
    count = sum(integrate_note(item, guides[item["id"]], lang, names) for item in registry for lang in ("zh", "en"))
    update_overlays(registry, guides)
    update_readme(ROOT / "README.md", "zh")
    update_readme(ROOT / "README.en.md", "en")
    remove_runtime_padding()
    replace_audit()
    guide_doc = ROOT / "docs/BENCHMARK_DETAIL_PAGE_GUIDE.md"
    guide_doc.write_text('''# Benchmark detail pages: evidence and decision guide

A detail page must help a researcher select an evaluation and interpret evidence, not merely restate an abstract.

## Separate evidence from editorial work

Preserve source-backed task definitions, protocols, quantitative evidence and limitations. Attribute numerical results to their original track, release, model, budget and source. An editorial revision date is not a new factual-verification date. Do not advertise paper snapshots as a live leaderboard.

Selection judgments are editorial interpretations. Illustrative tasks must explicitly say they are not quoted dataset examples. Suggested discriminating experiments are proposals, never reported results. Include specific comparison controls and nearby benchmarks that measure different objects.

## Author the page, do not pad the renderer

Every canonical benchmark has Chinese and English Markdown notes. Authored guide blocks are recorded in `data/editorial/reading_guides.json` and embedded in the corresponding notes; keep both in sync when changing a block. Related references must resolve to canonical benchmark identities. Preserve useful existing evidence rather than replacing it with metadata templates.

Do not manufacture missing numbers, apply global wording substitutions that change meaning, or append a generic evaluation contract to make a short note look complete. Chinese and English must preserve the same factual scope, examples, proposed controls and limits; identical lengths are not a goal.

## Validation and maintenance

`audit_detail_pages.py` checks structural presence, synchronization and references. It does not award quality grades or certify facts. Factual accuracy, semantic parity and decision usefulness require review of the relevant sources and prose. Run the Python contracts, note validators, web tests, Astro check and static build before publication.

README supports discovery, selection, release orientation and the complete catalog. Track-specific numeric evidence belongs in detail notes and versioned result records. The website consumes the authored notes rather than inventing a second narrative layer.
''', encoding="utf-8")
    for path in (ROOT / ".editorial").glob("*.json"):
        path.unlink()
    if (ROOT / ".editorial").exists() and not any((ROOT / ".editorial").iterdir()):
        (ROOT / ".editorial").rmdir()
    # Temporary export machinery has no role in the maintained project.
    (ROOT / ".github/workflows/editorial-snapshot.yml").unlink(missing_ok=True)
    print(f"Integrated {count} authored bilingual notes; updated 126 editorial overlays and both homepages.")
    print("All source-verification dates remain unchanged. No new leaderboard facts were invented.")


if __name__ == "__main__":
    main()
