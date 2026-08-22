from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def simplify_table_block(text: str, label: str) -> str:
    start_marker = f"<!-- {label}:START -->"
    end_marker = f"<!-- {label}:END -->"
    start = text.index(start_marker) + len(start_marker)
    end = text.index(end_marker, start)
    block = text[start:end]
    out: list[str] = []
    for line in block.splitlines():
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            cells = line.split("|")[1:-1]
            if len(cells) == 5:
                line = "|" + "|".join(cells[:4]) + "|"
        out.append(line)
    return text[:start] + "\n".join(out) + text[end:]


def simplify_readme(path: str, *, english: bool) -> None:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")

    legacy_start = '<a id="timeline"></a><a id="latest"></a><a id="frontier"></a>'
    start = text.index(legacy_start)
    end = text.index('<a id="field-map"></a>', start)
    aliases = (
        '<a id="timeline"></a><a id="latest"></a><a id="frontier"></a>\n'
        '<a id="periods"></a><a id="changes"></a><a id="evolution"></a>\n'
    )
    text = text[:start] + aliases + text[end:]

    for label in (
        "TABLE-FIRST:RECENT",
        "TABLE-FIRST:AREA:agent-memory",
        "TABLE-FIRST:AREA:rag",
        "TABLE-FIRST:AREA:data-agent",
    ):
        text = simplify_table_block(text, label)

    if english:
        memory_intro = (
            "### Agent Memory\n"
            "From cross-session factual recall toward online updating, structured memory, multimodal evidence, action, authority, and implicit user state.\n"
        )
        memory_chain = (
            "\n**Defining chain:** [Beyond Goldfish Memory](https://aclanthology.org/2022.acl-long.356/) → "
            "[LoCoMo](https://aclanthology.org/2024.acl-long.747/) / [LongMemEval](https://arxiv.org/abs/2410.10813) → "
            "[MemoryAgentBench](https://arxiv.org/abs/2507.05257) → "
            "[StructMemEval](https://arxiv.org/abs/2602.11243) / [MemoryArena](https://arxiv.org/abs/2602.16313) → "
            "[MemEye](https://arxiv.org/abs/2605.15128) / [WorldMemArena](https://arxiv.org/abs/2605.29341) → "
            "[DynamicMem](https://arxiv.org/abs/2606.22877) / [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/) → "
            "[GateMem](https://arxiv.org/abs/2606.18829) / [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) / "
            "[PAST-Bench](https://arxiv.org/abs/2608.04003) / [SP-Mem](https://arxiv.org/abs/2608.16551)\n"
        )
        data_intro = (
            "### Data Agents\n"
            "From text-to-SQL / code generation toward complete data workflows, exploration, statistical/causal analysis, and business-semantic reliability.\n"
        )
        data_chain = (
            "\n**Defining chain:** [WikiSQL](https://arxiv.org/abs/1709.00103) → "
            "[Spider](https://aclanthology.org/D18-1425/) / [DS-1000](https://arxiv.org/abs/2211.11501) → "
            "[MLAgentBench](https://arxiv.org/abs/2310.03302) / [InsightBench](https://arxiv.org/abs/2407.06423) → "
            "[Spider 2.0](https://arxiv.org/abs/2411.07763) / [KramaBench](https://arxiv.org/abs/2506.06541) → "
            "[DataClawBench](https://arxiv.org/abs/2605.02503) / [DSGym](https://arxiv.org/abs/2601.16344) → "
            "[StatABench](https://arxiv.org/abs/2606.22977) / [CausalDS](https://arxiv.org/abs/2607.08093) → "
            "[DataSpace](https://arxiv.org/abs/2608.03451) / [DSAgentBench](https://arxiv.org/abs/2608.10366) → "
            "[Data Exploration Benchmark](https://arxiv.org/abs/2608.16045) / [WarehouseReliabilityBench](https://arxiv.org/abs/2608.09254) / "
            "[data-eng-bench](https://github.com/Snowflake-Labs/data-eng-bench)\n"
        )
    else:
        memory_intro = (
            "### Agent Memory\n"
            "从跨会话事实召回，逐步走向在线更新、结构化记忆、多模态证据、行动、权限与隐式用户状态。\n"
        )
        memory_chain = (
            "\n**主干：** [Beyond Goldfish Memory](https://aclanthology.org/2022.acl-long.356/) → "
            "[LoCoMo](https://aclanthology.org/2024.acl-long.747/) / [LongMemEval](https://arxiv.org/abs/2410.10813) → "
            "[MemoryAgentBench](https://arxiv.org/abs/2507.05257) → "
            "[StructMemEval](https://arxiv.org/abs/2602.11243) / [MemoryArena](https://arxiv.org/abs/2602.16313) → "
            "[MemEye](https://arxiv.org/abs/2605.15128) / [WorldMemArena](https://arxiv.org/abs/2605.29341) → "
            "[DynamicMem](https://arxiv.org/abs/2606.22877) / [LoCoMo-Plus](https://aclanthology.org/2026.acl-long.1150/) → "
            "[GateMem](https://arxiv.org/abs/2606.18829) / [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) / "
            "[PAST-Bench](https://arxiv.org/abs/2608.04003) / [SP-Mem](https://arxiv.org/abs/2608.16551)\n"
        )
        data_intro = (
            "### Data Agents\n"
            "从 Text-to-SQL / code generation，逐步走向完整数据工作流、探索、统计/因果分析与业务语义可靠性。\n"
        )
        data_chain = (
            "\n**主干：** [WikiSQL](https://arxiv.org/abs/1709.00103) → "
            "[Spider](https://aclanthology.org/D18-1425/) / [DS-1000](https://arxiv.org/abs/2211.11501) → "
            "[MLAgentBench](https://arxiv.org/abs/2310.03302) / [InsightBench](https://arxiv.org/abs/2407.06423) → "
            "[Spider 2.0](https://arxiv.org/abs/2411.07763) / [KramaBench](https://arxiv.org/abs/2506.06541) → "
            "[DataClawBench](https://arxiv.org/abs/2605.02503) / [DSGym](https://arxiv.org/abs/2601.16344) → "
            "[StatABench](https://arxiv.org/abs/2606.22977) / [CausalDS](https://arxiv.org/abs/2607.08093) → "
            "[DataSpace](https://arxiv.org/abs/2608.03451) / [DSAgentBench](https://arxiv.org/abs/2608.10366) → "
            "[Data Exploration Benchmark](https://arxiv.org/abs/2608.16045) / [WarehouseReliabilityBench](https://arxiv.org/abs/2608.09254) / "
            "[data-eng-bench](https://github.com/Snowflake-Labs/data-eng-bench)\n"
        )

    text = replace_once(text, memory_intro, memory_intro + memory_chain, f"{path} Agent Memory chain")
    text = replace_once(text, data_intro, data_intro + data_chain, f"{path} Data Agents chain")
    p.write_text(text, encoding="utf-8")


def update_daily_workflow() -> None:
    path = ROOT / "docs" / "DAILY_WORKFLOW.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "timestamps, atomic publication, bilingual projection, period boundaries, and retries.",
        "timestamps, atomic publication, bilingual projection, and retries.",
    )
    text = text.replace(
        "5. Update any secondary acceptance/deep-read projection, rolling-period synthesis, and gated Field Map from the same canonical state. These layers may use `radar_published_at` where provenance matters, but they never replace the public release chronology.",
        "5. Update the gated Field Map only when durable evaluation coordinates or defining chains change. Do not add per-item deep-read or rolling 7-day/30-day synthesis sections to the public README; audit detail belongs in canonical records, benchmark notes, and digests.",
    )
    text = text.replace(
        "7. Publish canonical data, both README languages, any deep note / acceptance projection, due digest, and gated map together in one atomic Git commit; never create a public operational or daily-run file.",
        "7. Publish canonical data, both README languages, due digest, and gated map together in one atomic Git commit; never create a public operational or daily-run file.",
    )
    start = text.index("## Reader projection")
    end = text.index("## Publication validation", start)
    projection = """## Reader projection

The public reader contract is **signal-first, then table-first**:

0. **30-day frontier signal table** — the first visible research content after the language switch. Exactly three rows: Agent Memory, RAG / Agentic Retrieval, and Data Agents. Each row states one concrete research/evaluation shift supported by representative benchmark links from the current window. It is synthesis, not a list of new papers; say `no material shift` rather than manufacture a trend.
1. **Recent release timeline table** — show every verified benchmark in the rolling six-month source-release window, reverse chronological by `released`, preserving day/month precision and the whole boundary month. No fixed item cap and no editorial sampling. The reader-facing columns are time, area, benchmark, and one concise `What it tests / 考察内容` field; do not add a parallel `what changed / 相较以往` column.
2. **Benchmark Map** — for each of the three areas, keep one short evolution sentence plus one visible **Defining chain / 主干** of representative benchmarks. Do not add a separate “three areas” summary layer.
3. **Complete area tables in README** — every canonical Agent Memory, RAG / Agentic Retrieval, and Data Agent record remains directly scannable in the main page. Each row has one concise `What it tests / 考察内容` description rather than a second change/explanation column. Do not replace these tables with links to the Library.
4. **Reading Paths and Library** — guide deeper study and provide the canonical alternate browse surface. The Library may retain richer genealogy and change-oriented explanation.

Per-item `<details>` deep reads and rolling 7-day/30-day synthesis are not public README surfaces. Full audit metadata, acceptance provenance, confounder analysis, and closed-period synthesis belong in canonical records, benchmark notes, the Library, and digests. Compatibility anchors may remain invisible so old links continue to land near the release timeline or Benchmark Map.

`radar_published_at` is maintenance provenance. It may support audit history, but it must **never** replace `released` as the ordering key of the public research timeline. Likewise, `last_verified`, scheduler execution time, and Git commit time must never be presented as paper release time.

Chinese is the default surface and English is its full counterpart. Identity, source release time, decisive evidence, caveat, map status, and links are one judgment projected twice. Chinese prose keeps Chinese verbs, connectives, and descriptive phrases while retaining canonical English names and search terms where useful.

"""
    text = text[:start] + projection + text[end:]
    text = re.sub(
        r"Validation must additionally guard the signal-first and table-first contract:.*?exclusively into `library/`\.\n",
        "Validation must additionally guard the signal-first and table-first contract: both README languages must begin their research content with the three-row 30-day frontier-signal table, put the rolling release table immediately after it, contain no public per-item deep-read or rolling 7-day/30-day synthesis surface, keep one defining chain for each Benchmark Map area, keep one `What it tests / 考察内容` column rather than a parallel change column in the main README tables, retain all three complete area tables in README, and never move those tables exclusively into `library/`.\n",
        text,
        flags=re.S,
    )
    path.write_text(text, encoding="utf-8")


def update_protocol() -> None:
    path = ROOT / "docs" / "RADAR_AGENT_PROTOCOL.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace("# Radar Agent Protocol v2", "# Radar Agent Protocol v3", 1)
    text = text.replace("Period / Map Synthesizer", "Map Synthesizer")
    text = text.replace(
        "- **Period / Map Synthesizer:** Compare accepted canonical records against repository history. Produce direction status, support identities, confidence, implication, and `map_delta`. Never infer causality from temporal proximity or summarize summaries.\n",
        "- **Map Synthesizer:** Compare accepted canonical records against repository history. Update durable map coordinates and defining chains only when evidence clears the map gate. Never infer causality from temporal proximity or summarize summaries.\n",
    )
    text = text.replace(
        "- **Publisher + QA:** Derive both languages, rolling periods, closed digests, and library routes from accepted canonical state, then preserve public provenance in one atomic Git commit. Do not invent or soften research judgments during rendering.\n",
        "- **Publisher + QA:** Derive both languages, the source-release timeline, complete area tables, closed digests, and library routes from accepted canonical state, then preserve public provenance in one atomic Git commit. Do not invent or soften research judgments during rendering.\n",
    )
    text = text.replace(
        "| `radar_published_at` | First accepted public publication in this Radar | Latest Timeline inclusion and order |",
        "| `radar_published_at` | First accepted public publication in this Radar | Maintenance provenance and audit; never public source-release ordering |",
    )
    start = text.index("## Acceptance and publication gates")
    end = text.index("## Bilingual projection", start)
    gates = """## Acceptance and publication gates

### Release timeline gate

An item enters the public recent timeline only after identity resolution, domain acceptance, full-text or equivalent primary evidence, skeptical audit, and canonical update. The public timeline is ordered by the work's honest source `released` date/month, not by scheduler time or Radar acceptance time. It contains the complete rolling six-month source-release projection with no fixed item cap or editorial sampling.

Every accepted identity must also appear exactly once in its canonical area table in both README languages and in the Library. The main README does not publish per-item acceptance cards, per-item `<details>` deep reads, or a second acceptance-timestamp timeline. Main README tables expose one concise `What it tests / 考察内容` description, while richer comparison/genealogy explanation stays in the Library, benchmark notes, and digests.

### Field Map gate

Every accepted record receives exactly one `map_delta` status:

`none | early_signal | reinforces | revises | splits | retires`

`early_signal` may affect the compact 30-day frontier signal but does not rewrite a durable node. `reinforces` requires independent evidence beyond one work. `revises`, `splits`, and `retires` require the prior map claim, new claim-level evidence, and the smallest reversible edit. If the gate is not met, preserve the existing map and defining chain.

The public Benchmark Map is deliberately compact: one evolution sentence plus one defining chain per area. A separate “three areas” summary and rolling 7-day/30-day synthesis are not public README surfaces.

"""
    text = text[:start] + gates + text[end:]
    start = text.index("## Bilingual projection")
    end = text.index("## Transaction, atomicity, and retry", start)
    bilingual = """## Bilingual projection

Chinese and English are projections of one accepted judgment, not separate editorial decisions. Canonical identity, source release date and order, area membership, primary links, recent-timeline membership, complete area-table membership, and defining-chain benchmark identities must stay aligned. Natural phrasing may differ.

Invisible compatibility anchors may be retained for old inbound links, but removed reader surfaces must not reappear behind those anchors. Any bilingual drift, unresolved local link, incomplete canonical projection, or validation failure aborts publication.

"""
    text = text[:start] + bilingual + text[end:]
    text = text.replace(
        "preflight → discovery → identity resolution → scope judgment → full-text reading → skeptical audit → acceptance → canonical update → Timeline → periods → closed digest if due → Field Map if gated → bilingual projection → validation → one commit",
        "preflight → discovery → identity resolution → scope judgment → full-text reading → skeptical audit → acceptance → canonical update → source-release timeline → complete area tables → closed digest if due → Field Map if gated → bilingual projection → validation → one commit",
    )
    text = text.replace(
        "Accepted outcomes are already projected into canonical data, the complete Timeline, rolling periods, closed digests when due, gated maps, and one atomic Git commit.",
        "Accepted outcomes are already projected into canonical data, the source-release timeline, complete area tables, closed digests when due, gated maps, and one atomic Git commit.",
    )
    text = text.replace(
        "- **Every successful material run:** update canonical records, Timeline, and rolling periods when evidence changes them; preserve the complete accepted projection in one atomic commit without a public run log.",
        "- **Every successful material run:** update canonical records, the 30-day frontier signal when warranted, the source-release timeline, complete area tables, and gated Benchmark Map; preserve the complete accepted projection in one atomic commit without a public run log.",
    )
    path.write_text(text, encoding="utf-8")


def update_editorial_standard() -> None:
    path = ROOT / "docs" / "EDITORIAL_STANDARD.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "- Layer-level attention navigation (`30 sec → 3 min → 5 min → 15 min → browse all`) is a stable reader contract; it names the depth of a route, not the value of an individual item.",
        "- Layer-level attention navigation is `frontier signal → release timeline → Benchmark Map → complete area tables → Reading Paths → Library`; each layer answers a different reader question without repeating the previous one.",
    )
    start = text.index("## README disclosure contract")
    end = text.index("## Epistemic language", start)
    contract = """## README scan contract

The main README is a scanning surface, not a per-item audit log. Recent and per-area tables use one descriptive field: `考察内容 / What it tests`. That field may be slightly longer when needed, but it should compactly name the task/environment/capability being measured rather than restating novelty, importance, or “compared with before.”

Keep comparison, predecessor critique, decisive evidence, caveats, and genealogy in canonical records, benchmark notes, the Library, and digests. Do not reintroduce per-item `<details>` deep reads, rolling 7-day/30-day synthesis, or a separate three-area evolution section into the main README.

"""
    text = text[:start] + contract + text[end:]
    path.write_text(text, encoding="utf-8")


def patch_validator() -> None:
    path = ROOT / "scripts" / "validate_reading.py"
    text = path.read_text(encoding="utf-8")
    insert_at = text.index("def main() -> int:")
    helper = r'''
def validate_public_readme(
    zh: str,
    en: str,
    records: list[dict[str, object]],
) -> list[str]:
    """Validate the compact v3 reader projection without the retired deep/period layers."""

    errors: list[str] = []
    record_ids = {str(record.get("id")) for record in records}
    cases = (
        ("README.md", zh, "**主干：**"),
        ("README.en.md", en, "**Defining chain:**"),
    )
    banned = (
        "## 最新条目深读",
        "## 7 天 / 30 天：评价对象发生了什么变化",
        "## 三个方向的演化",
        "## 7 days / 30 days: What Changed in the Evaluation Object",
        "## Three Areas",
    )

    for language, text, chain_label in cases:
        for phrase in banned:
            if phrase in text:
                errors.append(f"{language}: retired reader surface returned: {phrase}")

        release = text.find('<a id="release-timeline"></a>')
        field_map = text.find('<a id="field-map"></a>')
        if release < 0 or field_map < 0 or release >= field_map:
            errors.append(f"{language}: release timeline must precede Benchmark Map")
        elif "<details" in text[release:field_map].lower():
            errors.append(f"{language}: per-item deep reads returned to the main README")

        for label in (
            "TABLE-FIRST:RECENT",
            "TABLE-FIRST:AREA:agent-memory",
            "TABLE-FIRST:AREA:rag",
            "TABLE-FIRST:AREA:data-agent",
        ):
            start_marker = f"<!-- {label}:START -->"
            end_marker = f"<!-- {label}:END -->"
            if text.count(start_marker) != 1 or text.count(end_marker) != 1:
                errors.append(f"{language}: expected exactly one {label} block")
                continue
            block = text.split(start_marker, 1)[1].split(end_marker, 1)[0]
            for line in block.splitlines():
                visible = strip_html_comments(line).strip()
                if visible.startswith("|") and visible.endswith("|"):
                    cells = visible.split("|")[1:-1]
                    if len(cells) != 4:
                        errors.append(f"{language}: {label} must have exactly four visible columns")
                        break
            for forbidden in ("相较以往", "带来的变化", "What changed", "Why it changed the question"):
                if forbidden in block:
                    errors.append(f"{language}: {label} still exposes parallel change column {forbidden}")

        sections = (
            ("benchmark-memory", "benchmark-rag"),
            ("benchmark-rag", "benchmark-data"),
            ("benchmark-data", "all-benchmarks"),
        )
        for anchor, next_anchor in sections:
            start = text.find(f'<a id="{anchor}"></a>')
            end = text.find(f'<a id="{next_anchor}"></a>', start + 1)
            if start < 0 or end < 0:
                errors.append(f"{language}: missing Benchmark Map section {anchor}")
                continue
            if text[start:end].count(chain_label) != 1:
                errors.append(f"{language}: {anchor} needs exactly one defining chain")

        for label in ("TABLE-FIRST:AREA:agent-memory", "TABLE-FIRST:AREA:rag", "TABLE-FIRST:AREA:data-agent"):
            block = text.split(f"<!-- {label}:START -->", 1)[1].split(f"<!-- {label}:END -->", 1)[0]
            for identity in BENCHMARK_ID_RE.findall(block):
                if identity not in record_ids:
                    errors.append(f"{language}: unknown benchmark identity {identity} in {label}")

    try:
        zh_recent = BENCHMARK_ID_RE.findall(zh.split("<!-- TABLE-FIRST:RECENT:START -->", 1)[1].split("<!-- TABLE-FIRST:RECENT:END -->", 1)[0])
        en_recent = BENCHMARK_ID_RE.findall(en.split("<!-- TABLE-FIRST:RECENT:START -->", 1)[1].split("<!-- TABLE-FIRST:RECENT:END -->", 1)[0])
        if zh_recent != en_recent:
            errors.append("Chinese/English recent release table identity or order drift")
    except IndexError:
        pass

    return errors


'''
    text = text[:insert_at] + helper + text[insert_at:]
    text = text.replace("    errors.extend(validate_pair(zh, en))\n", "", 1)
    text = text.replace(
        "    errors.extend(validate_benchmark_projection(zh, en, records))\n",
        "    errors.extend(validate_public_readme(zh, en, records))\n",
        1,
    )
    path.write_text(text, encoding="utf-8")


def rewrite_projection_tests() -> None:
    path = ROOT / "tests" / "test_benchmark_v2_contract.py"
    path.write_text(r'''from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_reading


class CanonicalTimeContractTest(unittest.TestCase):
    def test_repository_registry_satisfies_time_contract(self):
        records = json.loads((ROOT / "data" / "benchmarks.json").read_text(encoding="utf-8"))
        self.assertEqual([], validate_reading.validate_benchmark_registry(records))

    def test_partial_v2_record_is_rejected(self):
        record = {"id": "partial", "released": "2026-08", "map_delta": "early_signal"}
        errors = validate_reading.validate_record_time_contract(record)
        self.assertTrue(errors)

    def test_native_v2_event_order_is_enforced(self):
        record = {
            "id": "native",
            "released": "2026-08-20",
            "published_at": "2026-08-20T02:00:00Z",
            "first_seen_at": "2026-08-20T01:00:00Z",
            "radar_published_at": "2026-08-20T03:00:00Z",
            "time_provenance": "native_v2",
            "map_delta": "early_signal",
        }
        self.assertTrue(any("published_at <= first_seen_at <= radar_published_at" in e for e in validate_reading.validate_record_time_contract(record)))


class PublicProjectionV3Test(unittest.TestCase):
    def setUp(self):
        self.zh = (ROOT / "README.md").read_text(encoding="utf-8")
        self.en = (ROOT / "README.en.md").read_text(encoding="utf-8")
        self.records = json.loads((ROOT / "data" / "benchmarks.json").read_text(encoding="utf-8"))

    def test_repository_projection_is_compact_and_bilingual(self):
        self.assertEqual([], validate_reading.validate_public_readme(self.zh, self.en, self.records))

    def test_retired_deep_read_surface_is_rejected(self):
        mutated = self.zh.replace('<a id="field-map"></a>', '## 最新条目深读\n\n<a id="field-map"></a>', 1)
        errors = validate_reading.validate_public_readme(mutated, self.en, self.records)
        self.assertTrue(any("retired reader surface" in e for e in errors), errors)

    def test_parallel_change_column_is_rejected(self):
        mutated = self.en.replace("| Time | Area | Benchmark | What it tests |", "| Time | Area | Benchmark | What it tests | What changed |", 1)
        errors = validate_reading.validate_public_readme(self.zh, mutated, self.records)
        self.assertTrue(any("four visible columns" in e or "parallel change column" in e for e in errors), errors)


if __name__ == "__main__":
    unittest.main()
''', encoding="utf-8")


def rewrite_table_tests() -> None:
    path = ROOT / "tests" / "test_table_first_readme.py"
    path.write_text(r'''from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class TableFirstReadmeContractTest(unittest.TestCase):
    def setUp(self):
        self.readmes = {
            "README.md": (ROOT / "README.md").read_text(encoding="utf-8"),
            "README.en.md": (ROOT / "README.en.md").read_text(encoding="utf-8"),
        }

    @staticmethod
    def _block(text: str, label: str) -> str:
        return text.split(f"<!-- {label}:START -->", 1)[1].split(f"<!-- {label}:END -->", 1)[0]

    def test_release_table_precedes_compact_benchmark_map(self):
        for language, text in self.readmes.items():
            with self.subTest(language=language):
                release = text.index('<a id="release-timeline"></a>')
                field_map = text.index('<a id="field-map"></a>')
                self.assertLess(release, field_map)
                self.assertNotIn("<details", text[release:field_map].lower())
                for heading in (
                    "## 最新条目深读",
                    "## 7 天 / 30 天：评价对象发生了什么变化",
                    "## 三个方向的演化",
                    "## 7 days / 30 days: What Changed in the Evaluation Object",
                    "## Three Areas",
                ):
                    self.assertNotIn(heading, text)

    def test_main_tables_use_one_what_it_tests_column(self):
        for language, text in self.readmes.items():
            with self.subTest(language=language):
                for label in (
                    "TABLE-FIRST:RECENT",
                    "TABLE-FIRST:AREA:agent-memory",
                    "TABLE-FIRST:AREA:rag",
                    "TABLE-FIRST:AREA:data-agent",
                ):
                    block = self._block(text, label)
                    for line in block.splitlines():
                        visible = line.split("<!--", 1)[0].strip()
                        if visible.startswith("|") and visible.endswith("|"):
                            self.assertEqual(4, len(visible.split("|")[1:-1]), (language, label, line))
                    self.assertNotIn("相较以往", block)
                    self.assertNotIn("带来的变化", block)
                    self.assertNotIn("What changed", block)
                    self.assertNotIn("Why it changed the question", block)

    def test_each_map_area_has_a_defining_chain(self):
        cases = (("README.md", "**主干：**"), ("README.en.md", "**Defining chain:**"))
        for filename, label in cases:
            text = self.readmes[filename]
            sections = (
                ("benchmark-memory", "benchmark-rag"),
                ("benchmark-rag", "benchmark-data"),
                ("benchmark-data", "all-benchmarks"),
            )
            for start_anchor, end_anchor in sections:
                start = text.index(f'<a id="{start_anchor}"></a>')
                end = text.index(f'<a id="{end_anchor}"></a>', start)
                self.assertEqual(1, text[start:end].count(label), (filename, start_anchor))

    def test_complete_area_tables_remain_in_main_readme(self):
        for language, text in self.readmes.items():
            with self.subTest(language=language):
                before_library = text[: text.index('<a id="library"></a>')]
                for area in ("agent-memory", "rag", "data-agent"):
                    self.assertIn(f"TABLE-FIRST:AREA:{area}:START", before_library)


if __name__ == "__main__":
    unittest.main()
''', encoding="utf-8")


def main() -> None:
    simplify_readme("README.md", english=False)
    simplify_readme("README.en.md", english=True)
    update_daily_workflow()
    update_protocol()
    update_editorial_standard()
    patch_validator()
    rewrite_projection_tests()
    rewrite_table_tests()

    # The workflow and this script are migration-only; remove them from the final tree.
    (ROOT / ".github" / "workflows" / "readme-v3-migration.yml").unlink(missing_ok=True)
    Path(__file__).unlink(missing_ok=True)


if __name__ == "__main__":
    main()
