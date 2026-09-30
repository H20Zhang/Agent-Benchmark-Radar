# LiveSQLBench: evolving cross-database SQL evaluation

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2025-05-28<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://livesqlbench.ai/)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](livesqlbench.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated official protocol, implementation settings and available results; no independent reproduction or full-paper-reading claim.

Read the official project page, root README, Agent and CLI documentation, and baseline call/configuration source; the official paper link remains Coming Soon.

[Official repository documentation · e15cd221267e06fabfaf6a3d4a69308280ce9a7c · 2026-09-30](https://github.com/bird-bench/livesqlbench/blob/e15cd221267e06fabfaf6a3d4a69308280ce9a7c/README.md)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

LiveSQLBench is a family of recurring releases. Base-Lite contains 18 PostgreSQL databases and 270 tasks (180 queries and 90 management operations); Base-Full v1 has 22 databases and 600 tasks; Large-v1 has 18 and 480. Tasks rely on schemas, column meanings and hierarchical business knowledge. Each release can be frozen for evaluation; continuing releases do not mean one persistent agent must retain state and adapt online across releases.

[Source](https://github.com/bird-bench/livesqlbench/blob/e15cd221267e06fabfaf6a3d4a69308280ce9a7c/README.md)

<!-- EDITORIAL-METHOD:START -->
Editorial placement: Spider and BIRD provide fixed public sets; LiveSQLBench emphasizes adding databases/queries and tracking versioned SQL performance. The coordinate is refreshed evaluation over time. This is not automatically a controlled schema/business-rule-drift experiment or a guarantee of equal difficulty across releases.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

Query tasks compare execution results; management tasks check custom postconditions. Model Base means direct SQL generation, while agent and CLI tracks permit tool-based exploration. The current ADK agent spends one step per tool call, defaults to 30 steps and permits one final SQL submission. Historical Agent I uses 20 steps on the website and must be tracked separately. The selected table reports only the root README’s historical Base-Lite model results, not current live-board or cross-release comparisons.

[Source](https://github.com/bird-bench/livesqlbench/blob/e15cd221267e06fabfaf6a3d4a69308280ce9a7c/README.md)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Selected historical Base-Lite results from the official README

README historical Base-Lite Model Base results labeled 2025-05-28; 270 PostgreSQL tasks; fraction passing corresponding tests; costs are historical author-reported values. Exact model snapshots, call budgets and repetitions are missing, preventing a matched causal comparison.

| Model | Success rate (%) | Mean cost (USD/task) |
| --- | --- | --- |
| o3-mini | 47.78 | 0.0233 |
| GPT-4.1 | 44.10 | 0.0336 |

Source location: Root README, Model Performance on LiveSQLBench; official website Discussion: Current Model Performance · [Source](https://github.com/bird-bench/livesqlbench/blob/e15cd221267e06fabfaf6a3d4a69308280ce9a7c/README.md)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, source limitations and next experiment

The official page still marks the paper Coming Soon. This note uses the fully read official protocol documentation and does not claim a full-paper reading. Historical rows lack complete model snapshots, budgets and uncertainty; current code does not reconstruct every row. Refreshing releases and withholding answers mitigate some leakage risks but do not prove absence of contamination.

Database counts and old setup comments differ between root and Agent documents; explicit release metadata takes precedence. Current baseline code does not directly run every historical model, so a uniform budget is not inferred.

Pin task data, databases, business rules and scorer revisions, then construct paired before/after rule changes for the same tasks. Separately measure query correctness, management postconditions and stale-rule cache invalidation.

[Source](https://github.com/bird-bench/livesqlbench/blob/e15cd221267e06fabfaf6a3d4a69308280ce9a7c/README.md)
<!-- EVIDENCE:limitations:END -->
