# WarehouseReliabilityBench: answerability, abstention and correction in warehouses

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08-10<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2608.09254)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](warehouse-reliability-bench.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked the selected results; no independent experiment reproduction.

Read all 20 pages and Appendices A–E, covering construction, prior test exposure, the state machine, all results, six scorer corrections, replay protocol, training gate and metric denominators; visually checked the main result tables.

[arXiv 2608.09254v1 · 2026-08-10](https://arxiv.org/pdf/2608.09254v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

WarehouseReliabilityBench v0.2.0 has 400 frozen synthetic tasks over e-commerce and SaaS DuckDB warehouses, split by template family into 240 development, 80 validation and 80 test tasks. Required behavior may be answering, clarifying, abstaining or refusing. QueryProof uses a semantic layer and physical catalog to select behavior, asks Qwen2.5-Coder-7B to propose meanings and SQL, and applies static and post-execution checks. The routed version can escalate to a larger model, whose output faces the same checks.

[Source](https://arxiv.org/pdf/2608.09254v1)

<!-- EDITORIAL-METHOD:START -->
Editorial placement: Spider/BIRD generally assume questions should be answered by queries; WarehouseReliabilityBench makes clarification, abstention and refusal valid outcomes. The coordinate shifts from executable SQL to whether answering is justified under the semantics/evidence, with coverage and false-answer risk measured together. Small synthetic warehouses do not establish enterprise governance reliability.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

All six systems use locally quantized Qwen2.5-Coder models at temperature 0, with one run per system on 80 test tasks. Business Truth Rate (BTR) averages over all tasks and rewards correct clarification/abstention/refusal. False Success Rate (FSR) is the fraction of ANSWER outputs that are incorrect or should not have been returned; coverage is restricted to answerable tasks. CPCA divides variable cost on answerable tasks by correct returned answers. Costs assume approximately USD 0.50 per hardware hour, not market API prices, and exclude development.

[Source](https://arxiv.org/pdf/2608.09254v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Selected system results on 80 frozen test tasks

One test pass per system; BTR denominator 80 tasks; FSR denominators 37, 41 and 65 ANSWER outputs respectively; CPCA is cost on answerable tasks divided by correct answers, not average cost per task; 32B has unmatched scaffolding.

| System | BTR (0–1) | FSR (0–1) | CPCA (USD/correct answer) |
| --- | --- | --- | --- |
| QueryProof routed | 0.537 | 0.351 | 0.0017 |
| QueryProof base | 0.562 | 0.366 | 0.0012 |
| 32B direct | 0.300 | 0.754 | 0.0058 |

Source location: Table 2 p. 9; Table 7 and Appendix E pp. 18–19 · [Source](https://arxiv.org/pdf/2608.09254v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## QueryProof minus 32B BTR by bootstrap unit

Same 80-task outcomes; preregistered task-level and exploratory family-level bootstrap; 2,000 resamples; only ten families, making the cluster interval itself unstable rather than a precise effect estimate.

| Resampling unit | Difference | 95% CI lower | 95% CI upper |
| --- | --- | --- | --- |
| Task (80) | 0.237 | 0.112 | 0.375 |
| Template family (10) | 0.237 | -0.125 | 0.562 |

Source location: Table 8 p. 19; Section 6.3 · [Source](https://arxiv.org/pdf/2608.09254v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, source limitations and next experiment

Routed QueryProof makes no numeric error among 24 answers returned to answerable questions, but gives 13 answers where clarification or abstention was required, leaving FSR 13/37. Its BTR 0.537 is below the unrouted 0.562, providing no evidence that routing helps on this test. One author co-designed data, rules and labels; only ten test families and prior test exposure limit the findings to this frozen system experiment.

Retain the author’s disclosure: test content had been exposed during development, and deleting five test-only phrases does not restore a clean holdout. The 0.920 agreement is a blind retest by the same author, not inter-annotator agreement. Section 6.1’s shorthand baseline coverage 1.000/answer accuracy 0.350 does not apply to the 32B row’s 0.900/0.444; system-specific table values take precedence.

Collect genuinely unseen families and real warehouses, compare 7B and 32B under identical scaffolding, then separately remove semantic layers, post-execution checks and routing. Report family-clustered intervals together with coverage and false-answer risk.

[Source](https://arxiv.org/pdf/2608.09254v1)
<!-- EVIDENCE:limitations:END -->
