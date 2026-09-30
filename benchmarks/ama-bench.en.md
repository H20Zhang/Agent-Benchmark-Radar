# AMA-Bench: trajectory QA, tool retrieval and bounded execution tests

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2026-02 · paper v1<br>
> **AMA-Agent — Average accuracy: 57.22%**<br>
> Best AMA-Agent average accuracy reported in the v1 abstract under the memory-QA protocol, not downstream action success. [Original source](https://arxiv.org/html/2602.22769v1)<br>
> Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.
<!-- RELEASE-REFERENCE:END -->

[中文](ama-bench.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Main 1–7 and Appendices A–L; PDF-only construction/routing/code prompts and WebArena/BabyAI/TextWorld examples read. Tables and cross-table inconsistencies checked; no experiments rerun.

[arXiv 2602.22769v4 (2026-05-27)](https://arxiv.org/html/2602.22769v4)

[Supplementary source 2602.22769v4, inspected 2026-09-30](https://arxiv.org/pdf/2602.22769v4)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

Benchmark QA probes recall, causal dependencies, state changes and abstraction from action-observation trajectories. AMA-Agent is a separate method: LLM-extracted state graph, top 5 node retrieval, then selective neighborhood lookup or Python search over raw trajectory JSON.

Editorial placement: Unlike user-dialogue suites such as LoCoMo and LongMemEval, AMA-Bench uses agent execution traces and adds causal, update and abstraction questions. Version 4 also adds bounded online execution checks; trajectory QA and executed-task outcomes should remain distinct. This is an evaluation-coordinate comparison, not a claim of direct dataset inheritance.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

Table 9: six domains, 208 trajectories/2496 QA, average 57,506 tokens; synthetic 1200 QA across 8K–128K. Core memory is built once and frozen across independent questions. Qwen3-32B binary judge; main method comparison uses Qwen3-32B answerer. LongContext uses 32,768 tokens reserves 4K output and truncates the middle.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Four abilities under a shared Qwen3-32B backbone

LLM-judged accuracy,[0,1]; parenthetical paper values are F1, not uncertainty. Common Qwen3-32B backbone; unmatched memory/tool pipelines.

2496 QA; categories 839/596/647/414; reported Average is not an equal-weight four-category mean

| System | Recall | Causal inference | State updating | State abstraction | Average accuracy |
|---|---|---|---|---|---|
| AMA-Agent | 0.6238 | 0.6145 | 0.5305 | 0.4719 | 0.5722 |
| MemoRAG | 0.4708 | 0.5497 | 0.4257 | 0.3659 | 0.4606 |
| EMem | 0.4631 | 0.4925 | 0.4512 | 0.3421 | 0.461 |

Locator: v4 Table 5 · [Source](https://arxiv.org/html/2602.22769v4)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Graph and tool removal change operational packages

 Graph replacement uses direct Qwen3-Embedding-4B context index; tool ablation disables calls. Operational package interventions, not independent proof of causal graph semantics.

The subset and protocol are specified above; exact per-cell sample counts are not supplied.

| System | Average accuracy |
|---|---|
| AMA-Agent | 0.57 |
| AMA-Agent without causality graph | 0.43 |
| AMA-Agent without tool retrieval | 0.44 |

Locator: v4 Table 7 · [Source](https://arxiv.org/html/2602.22769v4)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## The revised paper includes bounded execution tests

 Same Qwen3-32B execution agent; in-episode rollouts. Table 19 instead reports AMA TextWorld 50.5%.

Rollout sample counts not specified in these tables/Appendix H; do not infer from offline QA totals

| System | TextWorld E2E (%) | TextWorld QA (%) | Spider2 E2E (%) | Spider2 QA (%) |
|---|---|---|---|---|
| AMA-Agent | 51.5 | 40.4 | 26.2 | 57.4 |
| LongContext | 47.5 | 33.0 | 23.5 | 50.9 |

Locator: v4 Table 6; discrepancy with Table 19 noted · [Source](https://arxiv.org/html/2602.22769v4)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:result-4:START -->
## Judge calibration covers one answer model

Judge agreement 92.67%. Calibration sample is one answer model, not all systems or full benchmark.

300 GPT-5.2 output instances, 50 per domain; human adjudication

| Judgment | Count |
|---|---|
| True positive | 190 |
| False positive | 7 |
| False negative | 15 |
| True negative | 88 |

Locator: v4 Table 17 · [Source](https://arxiv.org/html/2602.22769v4)
<!-- EVIDENCE:result-4:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

Evidence supports trajectory-QA improvements and a bounded rollout check. Graph extraction remains lossy semantic abstraction; the code fallback has raw-log access. Correlation across six systems does not establish individual-example QA predictiveness. No cross-task transfer claim is warranted.

Table 6 TextWorld AMA 51.5 vs Table 19 50.5; no reconciliation supplied. Table 22 Qwen3-32B AMA 0.5629 vs Table 5 0.5722; ordering across models also not fully preserved despite caption. Table 8 selected counts 33 embodied / 34 software-engineering trajectories conflict Table 9 30/36 and 208 total. Abstract strongest-margin 11.16 pp matches MemoRAG, not later Table 5 EMem. Judge prose “within 8.1 points” conflicts Table 16 agreement 84.7%; use table and do not claim rankings judge-invariant. EMem/HiMem references are unresolved Anonymous/TODO citations in v4; exact implementation identity incompletely traceable. PDF Appendix K construction prompt receives previous_state_text although main §5.1 describes independent local extraction; no unconditional no-error-propagation claim.

Next: Match raw-log access, tool calls, embeddings and token budget; compare state graph versus equally detailed non-graph records. Retain rollout validation but add matched unseen follow-on tasks for experience transfer.
<!-- EVIDENCE:limitations:END -->
