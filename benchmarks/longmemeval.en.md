# LongMemEval: retrieval keys, temporal filters and answer evidence

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2024-10-14 · paper v1<br>
> **GPT-4o + round values / fact-expanded keys (top-10) — LongMemEval-M QA accuracy: 72.0%**<br>
> Best end-to-end QA in the indexing-design experiment of Table 2; not LongMemEval-S, oracle retrieval, or a maximum across all budgets. [Original source](https://arxiv.org/html/2410.10813v1)<br>
> Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.
<!-- RELEASE-REFERENCE:END -->

[中文](longmemeval.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Main 1–6, reproducibility/ethics and Appendices A–E inspected. PDF supplemental prompt text checked for Figures 7–8 and 10–13; numerical figure curves not digitized. Official README checked for September 2025 data cleaning. No rerun.

[arXiv 2410.10813v2 (2025-03-04)](https://arxiv.org/html/2410.10813v2)

[Supplementary source 2410.10813v2, inspected 2026-09-30](https://arxiv.org/pdf/2410.10813v2)

[Official source observed 2026-09-30 (mutable page)](https://github.com/xiaowu0162/LongMemEval)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

Embed human-curated evidence sessions in timestamped user-assistant histories, then ask 500 questions covering extraction, cross-session synthesis, temporal reasoning, updates and abstention. The framework separates stored values, index keys, retrieval queries and reading. A round is one user message plus its assistant reply.

Editorial placement: Relative to LoCoMo’s long-dialogue memory, LongMemEval focuses on retrieval representation, temporal reasoning, updates and abstention at different history scales. Its retrieval/reading comparisons are diagnostic, while aggregate QA alone cannot localize the failed component. This is an evaluation-coordinate comparison, not a claim of direct dataset inheritance.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

S is about 115k tokens/question; M has 500 sessions/about 1.5M tokens. Main memory experiments use Stella V5 1.5B retrieval, Llama3.1 8B Instruct extraction, timestamp-ordered values, JSON and Chain-of-Note. Keys/extraction keep user-side messages; retrieved values retain their chosen granularity. Greedy generation, max 800 tokens. GPT-4o-2024-08-06 judges binary answer correctness with type-specific rubrics.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Fact-expanded keys improve retrieval and QA

Recall and QA fractions,[0,1]. Fact text expands retrieval keys; extracted facts do not replace returned raw rounds. GPT-4o QA gain is 5.0 percentage points.

LongMemEval-M: 500 questions; top 10 retrieved rounds; same values, retriever and reading template within each reader comparison

| System | Recall@10 | GPT-4o QA@10 | Llama3.1-70B QA@10 | Llama3.1-8B QA@10 |
|---|---|---|---|---|
| Stella V5 / K=V | 0.692 | 0.67 | 0.624 | 0.534 |
| Stella V5 / K=V+fact | 0.784 | 0.72 | 0.682 | 0.572 |

Locator: v2 Table 3, round values · [Source](https://arxiv.org/html/2410.10813v2)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Visible evidence does not guarantee reliable full-history reading

Judge accuracy,[0,1]. Oracle supplies only evidence sessions; S includes full history. Direct 87.0→60.6 is 26.4 percentage points, 30.3% relative decline. Different evidence volume; not isolated write/retrieval failure.

500 questions

| System | Oracle QA | LongMemEval-S QA |
|---|---|---|
| GPT-4o / direct | 0.87 | 0.606 |
| GPT-4o / Chain-of-Note | 0.924 | 0.64 |

Locator: v2 Figure 3(b) · [Source](https://arxiv.org/html/2410.10813v2)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Temporal filters primarily improve evidence recall

Temporal-subset evidence recall,[0,1]. Stella V5 retrieval; different query time-range extraction models. Recall only, not end-to-end QA.

Temporal-reasoning subset; exact per-cell effective denominator not stated in table

| System | Recall@10 |
|---|---|
| No temporal filter | 0.55 |
| GPT-4o temporal filter | 0.722 |
| Llama3.1-8B temporal filter | 0.57 |

Locator: v2 Table 4, round values and K=V+fact · [Source](https://arxiv.org/html/2410.10813v2)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

In these fixed cells, expanded keys improve recall and QA; visible evidence still does not guarantee correct reading. A strict recall failure may merely omit superseded facts although the updated answer is correct. The judge accepts off-by-one duration errors and answers containing old plus correct updated information, so the metric is not strict chronology or clean deletion. Oracle is a model-conditioned reference.

v2 Table 9 Stella K=V retrieval cells differ from main Table 3/Table 10, despite related labels; use Table 3 explicitly and do not silently reconcile. Commercial pilot used 97 shortened 3–6-session histories in August 2024, excluded assistant-side recall/abstention and some temporal questions. It is neither 500-question S nor current product evaluation. Main prose/ontology framing is five abilities but seven question types; distinguish ability grouping from type labels.

Next: Hold cleaned-data revision, reader and token budget fixed. Compare raw versus fact-expanded keys while preserving returned values, then supply evidence directly. Pair updates with StateMemBench and implicit-use probes with InMind; report question-type scores and cost separately.
<!-- EVIDENCE:limitations:END -->
