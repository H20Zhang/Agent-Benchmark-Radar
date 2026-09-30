# Data Engineering Benchmark: executable data-engineering tasks in containers

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-07-29<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://github.com/Snowflake-Labs/data-eng-bench)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](data-eng-bench.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated official protocol, implementation settings and available results; no independent reproduction or full-paper-reading claim.

Read the official README, submission protocol, metric-computation source and stated configurations, and checked the repair-commit description; not every one of the 103 tasks was audited and no official paper was identified.

[Official repository documentation · a3278ad102829a6084dde086244a0ef665a8011c · 2026-09-30](https://github.com/Snowflake-Labs/data-eng-bench/blob/a3278ad102829a6084dde086244a0ef665a8011c/README.md)

Model-result gap: the official Harbor scores could not be retrieved, and the pinned repository contains no model-result rows; task counts and example configurations are not experimental scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

data-eng-bench places agents in containerized dbt projects with ticket-style requirements to edit or create models, run transformations and repair failures. Hidden pytest verifiers compare materialized rows against references. The 103 tasks share a synthetic retail warehouse and run either locally on DuckDB or in isolated Snowflake clones, covering analytics, bug fixes, dimensions/snapshots and incremental data engineering.

[Source](https://github.com/Snowflake-Labs/data-eng-bench/blob/a3278ad102829a6084dde086244a0ef665a8011c/README.md)

<!-- EDITORIAL-METHOD:START -->
Editorial placement: compared with SQL-only tasks such as Spider, Data Engineering Benchmark targets engineered artifacts, environment constraints and executable tests, closer to DAComp’s engineering side. It adds implementation/validation workflow, while the accessible evidence supports protocol placement rather than a model ranking.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

The submission protocol pins the dataset, requires every task with at least three trials, and counts errors and disqualified trials as zero. Current metric code defines Accuracy as successful trials divided by all trials; task-averaged pass@2/pass@3 are separate. The example Claude Code/Claude Opus 4.8/high configuration uses three attempts and four-way concurrency; it is a runnable configuration, not a measured result. One inspected task allocates 4,000 agent seconds, 3,000 verifier seconds, 2 CPUs and 8,000 MB RAM; these are not asserted as uniform across uninspected tasks.

[Source](https://github.com/Snowflake-Labs/data-eng-bench/blob/a3278ad102829a6084dde086244a0ef665a8011c/README.md)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, source limitations and next experiment

This audit fully read the official overview, submission protocol, metric computation and stated configurations, but did not audit every task. No official paper was identified. The linked Harbor leaderboard was unreadable through this retrieval and the repository contains no submitted result rows, leaving model scores and post-fix reruns unverified rather than absent. Confirmed fixes address Snowflake connections and cleanup; compile/parse checks are not end-to-end reproduction.

One timezone-sensitive DuckDB task is explicitly advisory. Older Harbor versions can silently ignore web-tool disabling; public reference solutions require verified isolation.

Pin verifier and backend revisions, run the same model three times on every task, and separately report trial accuracy, task-level pass@k, environment failures and disqualifications. Rerun identical agents across protocol fixes and isolate public references to reduce leakage.

[Source](https://github.com/Snowflake-Labs/data-eng-bench/blob/a3278ad102829a6084dde086244a0ef665a8011c/README.md)
<!-- EVIDENCE:limitations:END -->
