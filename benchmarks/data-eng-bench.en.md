# data-eng-bench: Data Agent / executable data engineering

[中文](data-eng-bench.md) | **English** · [Back to the entry](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Benchmark repository](https://github.com/Snowflake-Labs/data-eng-bench) · [Protocol fix](https://github.com/Snowflake-Labs/data-eng-bench/commit/35b83370bd9ae06d9ac8a2beb95d2544c90d88a5)

Moves code generation into repository-scale dbt transformation with hidden row-level verification.

## What It Follows

Earlier evaluation usually compressed this problem into a shorter final score or a single proxy. This object turns its predecessor critique into an explicit capability × environment × protocol delta and retains an executable or auditable artifact.

## How It Is Evaluated

**Question:** Can an agent implement, execute, and repair data transformations under real project constraints?

**Measurement object:** Executable data-engineering benchmark for repository-scale dbt transformations with hidden row-level verification on DuckDB and Snowflake.

**Scale and protocol:** 103 dbt tasks with hidden verifier coverage across DuckDB and Snowflake. The protocol includes hidden-pytest-verifiers, row-level-output-comparison, dual-backend-execution.

## What a Score Can Support

Across 103 dbt tasks on DuckDB and Snowflake, hidden row-level verifiers inspect outputs; the August repair exposes evaluator reliability as a measurement condition. It supports system-level evidence under this environment, harness, model/tool, and resource configuration; unmatched variables prevent attribution to one component.

## Strongest Confounder

The Snowflake verifier fix without a rerun means pre-fix leaderboard results are not directly comparable with the repaired environment. The load-bearing confounders are backend-environment-drift, verifier-defects, missing-post-fix-rerun.

## What It Still Does Not Measure

The August verifier repair has no published post-fix leaderboard rerun, so earlier Snowflake results require qualification.

## Where It Fits in the Map

`map_delta=early_signal`. One paper is only a signal; a durable direction needs independent records bound to the same canonical direction key.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use data-eng-bench for repository-level dbt transformation and repair. Hidden row-level verification is stronger than compilation alone, but backend and verifier versions affect scores. A verifier fix does not automatically validate an older leaderboard.

### What a concrete task looks like

Illustrative task: an agent edits a transformation project so models execute on a target database and produce correct rows. Dialect, type, and runtime differences between DuckDB and Snowflake can make the same change behave differently.

### Most discriminating experiment

Pin project, backend, and hidden-verifier commits and re-run the same patch across backends, separating execution failures from output differences. Recompute all compared methods after verifier changes and retain versioned old results rather than attributing environment repairs to agents.

### Pair with

[spider-2](spider-2.en.md) · [dacomp](dacomp.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->


## Remaining gap and next validation

What remains unmeasured is stability across settings and transfer to realistic workflows. The next experiment should hold model and budget fixed and add deployment-like tasks to test whether gains come from the target capability itself.