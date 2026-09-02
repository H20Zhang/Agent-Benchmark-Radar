import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
registry_path = ROOT / "data/benchmarks.json"
records = json.loads(registry_path.read_text(encoding="utf-8"))
if any(item.get("id") == "claimprobe" for item in records):
    raise SystemExit("ClaimProbe is already present; refusing duplicate transaction")

records.append({
    "id": "claimprobe",
    "name": "ClaimProbe",
    "area": "rag",
    "evolution_role": "frontier",
    "released": "2026-08-12",
    "importance": 4,
    "status": "active",
    "summary": "Audits deep-research reports at claim-source granularity to distinguish unsupported claims, citation misattribution, uncited support, and missing necessary facts while holding retrieved evidence fixed for writer-side comparisons.",
    "capabilities": ["claim-level-faithfulness-audit", "citation-attribution", "necessary-fact-recall", "writer-side-evaluation"],
    "environment": ["deep-research-reports", "retrieved-web-evidence", "fixed-evidence-writer-comparison"],
    "protocol": ["source-fact-extraction", "claim-citation-extraction", "embedding-top-20-source-shortlist", "llm-judge", "human-judge-calibration", "fixed-evidence-writer-intervention"],
    "scale": "ClaimProbe is run on 100 deep-research tasks across three host systems; human calibration uses 100 annotations, with holistic RACE evaluation on 50 English tasks and a 10-task stronger-judge subset.",
    "measurement_strength": "Separates writer-side claim faithfulness from upstream retrieval by keeping the evidence set fixed, exposing unsupported claims and source misattribution that holistic report scores can hide.",
    "coverage_gap": "The hallucination judge reaches only moderate human agreement, support search is limited to an embedding top-20 shortlist, and the dynamic-update study covers only five DeepResearch Bench tasks.",
    "confounders": ["llm-judge", "moderate-hallucination-judge-agreement", "embedding-shortlist-support-misses", "generator-model", "readability-tradeoff", "small-dynamic-update-study"],
    "artifacts": {"paper": "https://arxiv.org/abs/2608.28643", "code": "https://github.com/SalesforceAIResearch/claimwriter-deep-research"},
    "last_verified": "2026-09-02",
    "published_at": "2026-08-12T18:01:55Z",
    "first_seen_at": "2026-09-02T00:29:13Z",
    "radar_published_at": "2026-09-02T00:39:05Z",
    "time_provenance": "native_v2",
    "map_delta": "early_signal",
    "citations": {"count": None, "source": "semantic-scholar", "updated_at": "2026-09-02", "status": "unmatched", "paper_id": None, "url": None},
})
registry_path.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def replace_once(path, old, new):
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    n = text.count(old)
    if n != 1:
        raise AssertionError(f"{path}: expected one occurrence of {old!r}, found {n}")
    p.write_text(text.replace(old, new, 1), encoding="utf-8")


def regex_once(path, pattern, replacement):
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    new, n = re.subn(pattern, replacement, text, count=1)
    if n != 1:
        raise AssertionError(f"{path}: pattern {pattern!r} matched {n} times")
    p.write_text(new, encoding="utf-8")


def insert_after_marker_line(path, marker, row, which):
    p = ROOT / path
    lines = p.read_text(encoding="utf-8").splitlines()
    if any("benchmark-id:claimprobe" in line for line in lines):
        raise AssertionError(f"{path}: ClaimProbe already present")
    positions = [i for i, line in enumerate(lines) if marker in line]
    if not positions:
        raise AssertionError(f"{path}: marker {marker!r} missing")
    idx = positions[0] if which == "first" else positions[-1]
    lines.insert(idx + 1, row)
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")


regex_once("README.md", r"最后更新：\*\*2026-08-28\*\*", "最后更新：**2026-09-02**")
regex_once("README.en.md", r"Last updated: \*\*2026-08-28\*\*", "Last updated: **2026-09-02**")
replace_once("README.md", "以下是 registry 中的全部 125 个基准。", "以下是 registry 中的全部 126 个基准。")
replace_once("README.en.md", "All 125 registry benchmarks remain directly scannable in the README", "All 126 registry benchmarks remain directly scannable in the README")

insert_after_marker_line("README.md", "benchmark-id:data-exploration-benchmark", "| 2026-08-12 | RAG | [ClaimProbe](https://arxiv.org/abs/2608.28643) <!-- benchmark-id:claimprobe --> | 在固定检索证据下，以 claim-source 粒度区分 unsupported claim、citation misattribution、未引用但有支持的 claim 与必要事实遗漏。 |", "first")
insert_after_marker_line("README.en.md", "benchmark-id:data-exploration-benchmark", "| 2026-08-12 | RAG | [ClaimProbe](https://arxiv.org/abs/2608.28643) <!-- benchmark-id:claimprobe --> | Claim-source audit of unsupported claims, citation misattribution, uncited support, and necessary-fact omission while holding retrieved evidence fixed. |", "first")
insert_after_marker_line("README.md", "benchmark-id:recall-trap", "| 🔭 前沿 | [ClaimProbe](https://arxiv.org/abs/2608.28643) <!-- benchmark-id:claimprobe --> | — | 2026-08-12 | 在固定检索证据下，按 claim-source 对齐审计无依据 claim、引用错配、漏引支持与必要事实覆盖。 |", "last")
insert_after_marker_line("README.en.md", "benchmark-id:recall-trap", "| 🔭 Frontier | [ClaimProbe](https://arxiv.org/abs/2608.28643) <!-- benchmark-id:claimprobe --> | — | 2026-08-12 | Claim-source faithfulness audit for unsupported claims, citation misattribution, uncited support, and necessary-fact coverage under fixed retrieved evidence. |", "last")

insert_after_marker_line("library/README.md", "benchmark-id:commercial-tax", "| 2026-08-12 | [ClaimProbe](https://arxiv.org/abs/2608.28643) <!-- benchmark-id:claimprobe --> | RAG / Agentic Retrieval | 🔭 前沿 | 把 deep-research 成品评价从整体分数拆到固定检索证据下的 claim→source 忠实度与引用归因。 |", "first")
insert_after_marker_line("library/README.en.md", "benchmark-id:commercial-tax", "| 2026-08-12 | [ClaimProbe](https://arxiv.org/abs/2608.28643) <!-- benchmark-id:claimprobe --> | RAG / Agentic Retrieval | 🔭 Frontier | Decomposes deep-research report evaluation into claim→source faithfulness and attribution under fixed retrieved evidence. |", "first")
insert_after_marker_line("library/README.md", "benchmark-id:recall-trap", "| 🔭 前沿 | [ClaimProbe](https://arxiv.org/abs/2608.28643) <!-- benchmark-id:claimprobe --> | 2026-08-12 | 在固定检索证据下，按 claim-source 对齐审计无依据 claim、引用错配、漏引支持与必要事实覆盖。 | 把 writer-side faithfulness 从 retrieval/search 质量中隔离出来，使 holistic report score 掩盖的 provenance failure 可见。 |", "last")
insert_after_marker_line("library/README.en.md", "benchmark-id:recall-trap", "| 🔭 Frontier | [ClaimProbe](https://arxiv.org/abs/2608.28643) <!-- benchmark-id:claimprobe --> | 2026-08-12 | Claim-source audit of unsupported claims, citation misattribution, uncited support, and necessary-fact coverage under fixed retrieved evidence. | Isolates writer-side faithfulness from retrieval/search quality so provenance failures hidden by holistic report scores become observable. |", "last")

(ROOT / "benchmarks/claimprobe.md").write_text("""# ClaimProbe：Deep Research 报告的 claim-source 忠实度审计

**中文** | [English](claimprobe.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2608.28643) · [代码](https://github.com/SalesforceAIResearch/claimwriter-deep-research)

**一句话：** ClaimProbe 在固定检索证据后逐 claim 审计“有没有依据、引对没引对、漏没漏引、关键事实有没有写进来”，从而把 writer-side faithfulness 与 retrieval/search 质量分开。

**问题。** DeepResearch Bench、DAS-Bench 与 LitReview Arena 已覆盖整体报告、citation/discourse 和专家偏好，但整体分数仍会把 retrieval、writer 与成品质感混在一起。

**证据。** Enterprise Deep Research 的 fixed-evidence writer intervention 中，hallucination 15.89→5.02、misattribution 18.94→5.43、necessary fact recall 36.83→45.85；上游 evidence 不变，因此支持 writer-side evidence materialization / attribution 改变，而不是 retrieval 或 planning 变好。

**限制。** 主 hallucination judge 与人工的一致性只有 Cohen κ=0.484，support search 还受 top-20 embedding shortlist 限制；动态更新只覆盖 5 个 DeepResearch Bench tasks，整体 RACE 变化也较小且 readability 有时下降。

**地图。** `early_signal`：新增 `retrieved evidence → written claim → cited source` 的独立诊断坐标，但单篇证据不改 durable Benchmark Map。

**链接。** [Primary](https://arxiv.org/abs/2608.28643) · [Code](https://github.com/SalesforceAIResearch/claimwriter-deep-research)
""", encoding="utf-8")

(ROOT / "benchmarks/claimprobe.en.md").write_text("""# ClaimProbe: claim-source faithfulness auditing for Deep Research reports

[中文](claimprobe.md) | **English** · [Back to entry](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2608.28643) · [Code](https://github.com/SalesforceAIResearch/claimwriter-deep-research)

**One line.** ClaimProbe audits each claim after retrieval for support, correct attribution, uncited support, and necessary-fact coverage, separating writer-side faithfulness from retrieval/search quality.

**Question.** DeepResearch Bench, DAS-Bench, and LitReview Arena cover holistic reports, citation/discourse quality, and expert preference, but aggregate scores can still mix retrieval, writing, and presentation quality.

**Evidence.** In the Enterprise Deep Research fixed-evidence writer intervention, hallucination drops 15.89→5.02, misattribution 18.94→5.43, and necessary fact recall rises 36.83→45.85. Because upstream evidence is held fixed, this supports a writer-side evidence-materialization/attribution effect, not better retrieval or planning.

**Caveat.** The main hallucination judge reaches only Cohen κ=0.484 with humans, support search is limited to a top-20 embedding shortlist, the dynamic-update study covers only five DeepResearch Bench tasks, and holistic RACE gains are small with readability sometimes lower.

**Map.** `early_signal`: adds a distinct `retrieved evidence → written claim → cited source` diagnostic coordinate, but one paper does not change the durable Benchmark Map.

**Links.** [Primary](https://arxiv.org/abs/2608.28643) · [Code](https://github.com/SalesforceAIResearch/claimwriter-deep-research)
""", encoding="utf-8")
