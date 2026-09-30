# StructMemEval: where memory structure helps, and what remains unsolved

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-02<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2602.11243)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](structmemeval.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated primary-paper version, method, setup, key results and limitations; no independent experiment reproduction.

v3 main text and Appendices A–F; use printed table values, without digitizing graphical curves into exact results.

[arXiv:2602.11243v3](https://arxiv.org/html/2602.11243v3) · [arXiv:2602.11243v2](https://arxiv.org/html/2602.11243v2)

The tables reorganize selected sourced facts. The title-level historical reference may use a different version, split or model; do not pool scores across those settings.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Measurement, method and comparison

Synthetic conversation streams test whether an agent maintains structures needed for state updates, hierarchical relations, aggregation/counting and recommendations. Compare retrieval and memory-writing systems, with and without hints about useful organization.

[Primary source](https://arxiv.org/html/2602.11243v3)
Illustrative task: after a user moves, neighbor relations change with location; matching the word “neighbor” can return people from the old address unless the relevant relations are maintained.

<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and denominators

Main set: 51 hard problems (10 tree, 15 counting, 14 state, 12 recommendation), each at least 250 messages. Extended set: 207 scenarios and over 2,000 questions. Main selected rows share Gemini-3.1-Pro without hints; GPT-4o-mini judges factual correctness. Main retrieval uses text-embedding-3-large, top 10; extended state retrieval below uses top 20 and a different backbone.

[Setup source](https://arxiv.org/html/2602.11243v3)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Main set: same backbone, no hints

v3 main set of 51 problems; Gemini-3.1-Pro, no hints. Total equally weights four categories rather than pooling all 51 problems.

| Configuration | State correctness (0–1) | Tree correctness (0–1) | Counting correctness (0–1) | Recommendation correctness (0–1) | Equal-category Total (0–1) |
|---|---|---|---|---|---|
| Retrieval | 0.0 | 0.0 | 0.0 | 0.22 | 0.06 |
| Mem-agent | 0.84 | 0.98 | 0.0 | 0.37 | 0.55 |
| Mem0 | 0.29 | 0.72 | 0.0 | 0.18 | 0.3 |

Writable memory helps some structural tasks, but counting is zero in these rows. The table does not support claiming that hints reliably solve the entire benchmark.

Fact source: v3 Table 1 · [Source](https://arxiv.org/html/2602.11243v3)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Extended state set: hints help under different conditions

42 extended state-tracking scenarios, Gemini-2.5-Pro; retrieval takes top 20 and has no hint intervention. A dash means unreported.

| Configuration | No-hint correctness (%) | Hint correctness (%) |
|---|---|---|
| Retrieval (top 20) | 26 | — |
| Mem-agent | 64 | 79 |
| Mem0 | 62 | 81 |

Backbone, dataset, units and retrieval budget differ from the main table; 79 or 81 does not mean the main set is solved.

Fact source: v3 Appendix, Table 6 · [Source](https://arxiv.org/html/2602.11243v3)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## Limitations, remaining gaps and next experiment

Under the main tested configuration, writable memory improves several structure-sensitive categories, while counting remains unsolved in these rows. Hints can help extended state tracking but are not a universal remedy. Synthetic tasks, default/minimally tuned adapters, different retrieval budgets and distinct main/extended backbones limit architecture-wide rankings.

Compared with retrieving raw chunks, writable memory can maintain task-relevant structure during ingestion; this does not mean all differences have been isolated by matched budgets. The existing structured result file retains a v2 snapshot (Mem-agent Total 66.0%, Mem0 39.0%); the tables here use v3 and do not overwrite old-version scores. Only v2 Tables 1–2 were rechecked here, not the entire older version.

Pair with ordinary long-conversation recall to separate retrieval from maintaining usable structure. Use a fixed backbone, token budget and stream; compare no hint versus hint and raw notes versus structured state. Report every category and the exact averaging rule, plus counting behavior as the stream grows.

[Primary evidence](https://arxiv.org/html/2602.11243v3)
<!-- EVIDENCE:limitations:END -->

<!-- RESEARCH-DECISION:START -->

Use the method, comparisons and limitations together to decide whether this benchmark fits a claim. These tables are not a cross-protocol leaderboard; structural checks do not certify factual correctness or reproduction.

Related measurements and controls: [LongMemEval](longmemeval.en.md) · [MemoryAgentBench](memoryagentbench.en.md) · [StateMemBench](statemembench.en.md)

<!-- RESEARCH-DECISION:END -->
