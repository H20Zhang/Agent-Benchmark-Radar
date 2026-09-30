# InMind: direct recall does not guarantee indirect use

<!-- RELEASE-REFERENCE:START -->
> **Release diagnostic (historical reference)** · 2026-07 · paper v1<br>
> **Naive RAG / text-embedding-3-large / GPT-5-mini — Indirect application, Table 1: 16.0%**; **Always-in-state / GPT-5-mini — Indirect application, Table 2: 68.8%**<br>
> 125 tasks: best retrieval configuration in Table 1 and always-visible-state diagnostic in Table 2. The 84.0% oracle is not a normal retrieval score. [Original source](https://arxiv.org/html/2607.24368v1)<br>
> Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.
<!-- RELEASE-REFERENCE:END -->

[中文](inmind.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated primary-paper version, method, setup, key results and limitations; no independent experiment reproduction.

Main Sections 1–8, supplementary Sections 9–18 and PDF prompt images, including injection, adapter-specific protocols and human scoring audits.

[arXiv:2607.24368v1](https://arxiv.org/html/2607.24368v1)

The tables reorganize selected sourced facts. The title-level historical reference may use a different version, split or model; do not pool scores across those settings.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Measurement, method and comparison

Each item pairs a personal fact with a direct recall query and an indirect query requiring an unstated world-knowledge bridge. Content filtering removes obvious lexical/semantic cues; expert review checks relevance and correctness. Compare direct recall, whether the actual answer context contains the target, and whether the answer applies it.

[Primary source](https://arxiv.org/html/2607.24368v1)
A paper case illustrates the gap: the system recalls a tree-nut allergy on direct request but fails to apply it during an indirect dessert recommendation. The challenge is surfacing a fact whose wording is unlike the current question.

<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and denominators

125 English tasks across 10 domains: 113 public-source grounded and 12 expert-authored. One fixed 47-session LongMemEval-s background trace. GPT-5-mini answers and judges all tasks; most memory builders use GPT-4o-mini. Naive RAG retrieves five raw chunks; A-Mem retrieves ten, while other budgets differ. Always-in-State uses a GPT-5-mini updater with a 200-line/25,000-byte state budget.

[Setup source](https://arxiv.org/html/2607.24368v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Separate direct recall from indirect application

125 tasks with GPT-5-mini answering/binary judging; target recall is answer-blind. The supplied-target backbone and adapters have different evidence access.

| Configuration | Direct recall (%) | Target recall (%) | Application (%) |
|---|---|---|---|
| Naive RAG (emb3-large) | 97.6 | 6.4 | 16.0 |
| MemoryOS (emb3-large) | 96.8 | 7.2 | 14.4 |
| A-Mem (emb3-large) | 100.0 | 12.0 | 9.6 |
| Backbone (GPT-5-mini) | — | 100.0 | 84.0 |

The 14.4% maximum among six memory frameworks and 16.0% for the separate Naive RAG reference have different scopes. Application above target recall does not prove memory use: generic caution can receive false-positive personalized-application credit.

Fact source: Table 1; §4.2–4.4 · [Source](https://arxiv.org/html/2607.24368v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Always-visible state is a different intervention

Same 125 tasks; Always-in-State uses a GPT-5-mini updater and 200-line/25,000-byte state budget, not a retrieval-only toggle.

| Configuration | Direct recall (%) | Application (%) |
|---|---|---|
| Always-in-State | 98.4 | 68.8 |

68.8% belongs to this updater/visible-state configuration; the entire gap from 16.0% cannot be attributed solely to query conditioning.

Fact source: Table 2; §5.2 · [Source](https://arxiv.org/html/2607.24368v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## The scorer's own errors

Appendix 14.2 audits 100 records for each judgment; these are scorer-audit counts, not model accuracy on the 125 tasks.

| Judgment | Human-audited records | Agreement count | False-positive count |
|---|---|---|---|
| Target recall | 100 | 97 | 3 |
| Original application | 100 | 85 | 15 |

Read the original application scorer's 15/100 false positives alongside the main table; a personalized-looking response does not establish successful personal-fact retrieval.

Fact source: Appendix 14.2 human audit · [Source](https://arxiv.org/html/2607.24368v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## Limitations, remaining gaps and next experiment

The selected results expose a substantial direct-recall versus indirect-use gap on deliberately difficult associations. They do not establish how often such failures occur in normal traffic or prove one architecture universally superior. The 84.0% backbone is a model-conditioned reference, not a hard ceiling; the answer-only post-hoc metric is separate from the main application metric.

The main text describes 38 subsequent sessions broadly, but appendices document prebuilt-bank/raw-target paths for A-Mem and HippoRAG 2. Do not describe every row as the same longitudinal ingestion intervention. Compared with explicit-recall cases in LongMemEval, this benchmark separately controls indirect use requiring a world-knowledge bridge.

Pair with LongMemEval for explicit recall, then freeze a memory bank and answerer while varying retrieval expansion or an equally budgeted visible-state policy. Report target recall and application separately, audit false positives, and match updater model and target exposure before attributing causality.

[Primary evidence](https://arxiv.org/html/2607.24368v1)
<!-- EVIDENCE:limitations:END -->

<!-- RESEARCH-DECISION:START -->

Use the method, comparisons and limitations together to decide whether this benchmark fits a claim. These tables are not a cross-protocol leaderboard; structural checks do not certify factual correctness or reproduction.

Related measurements and controls: [LongMemEval](longmemeval.en.md) · [LoCoMo](locomo.en.md) · [LoCoMo-Plus](locomo-plus.en.md)

<!-- RESEARCH-DECISION:END -->
