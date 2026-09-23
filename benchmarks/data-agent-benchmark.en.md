# Data Agent Benchmark (DAB): enterprise questions across heterogeneous databases

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2026-03-21 · paper v1<br>
> **Gemini-3-Pro / paper ReAct agent — Pass@1: 38%**<br>
> Best of five generic-model baselines in Table 3: 50 trials per query and a 12-dataset average. Excludes the PromptQL case study and later rescored boards. [Original source](https://arxiv.org/html/2603.20576v1)<br>
> Original-paper history only; later validators, hints, and task-specific prompts change comparability.
<!-- RELEASE-REFERENCE:END -->

[中文](data-agent-benchmark.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2603.20576) · [Project](https://ucbepic.github.io/DataAgentBench/) · [Code](https://github.com/ucbepic/DataAgentBench)

## What it actually measures

DAB evaluates whether agents can answer enterprise data questions when relevant information is **fragmented across multiple heterogeneous database systems**, references are inconsistent, and useful context may be buried in unstructured fields.

## What changed relative to prior evaluation

Text-to-SQL assumes one database and a known schema. DAB moves the target to integration, transformation, and analysis across PostgreSQL, MongoDB, SQLite, and DuckDB, making data-location discovery and cross-system reconciliation part of the task.

## Decisive evidence

DAB contains 54 queries across 12 datasets, nine domains, and four DBMSes, derived from a formative study of enterprise workloads across six industries. The paper's initial experiment reports 38% pass@1 for Gemini-3-Pro. This is a historical result under that experiment's model and protocol, not a current capability ceiling.

## What the score supports

The benchmark is evidence for end-to-end enterprise data-question answering under a heterogeneous backend. It cannot attribute failure to semantic mapping, integration, transformation, SQL/NoSQL generation, or answer synthesis without trajectory analysis.

## Fair comparison contract

Fix database snapshots, credentials/access, tool interfaces, model, retry policy, and number of trials; the leaderboard asks for at least five trials per query. Report pass@1 and variance, since stochastic agents can look substantially different under best-of-n evaluation.

## What remains unmeasured

The suite is small and read-oriented. Production agents face permissions, writes, lineage, semantic layers, changing schemas, cost constraints, and ambiguous business definitions.

## Next discriminating validation

Annotate each query with a ground-truth integration/semantic plan and score intermediate relation resolution before final execution. That would reveal whether heterogeneous data access or business semantics is the dominant bottleneck.

<!-- PROTOCOL-AUDIT-20260923:START -->

## 2026-09-23 protocol audit: inspect denominators, hints, and validator versions

Official Pass@1 first averages repeated-run pass rates per query, then within each dataset, and finally across datasets. It is **not success on at least one of five attempts**. Submissions require five runs per query and execution traces; missing, contaminated, or unsupported runs must not simply disappear from the denominator. [Official methodology and submission rules](https://github.com/ucbepic/DataAgentBench/blob/main/README.md)

The leaderboard separates `Tuned prompt` and `Hints`. For example, the official table records Permute EQ at 0.9467 dated 2026-09-11 and Scout at 0.9062 dated 2026-09-08; both declare tuned prompts, hints, and five trials. These are conditional source snapshots, not isolated backbone effects, and should not be subtracted directly from the historical paper's 38% result.

Validators changed materially. The official methodology records a 2026-06-12 rescore with updated validators and regenerated PATENTS references. On 2026-08-18, DEPS_DEV_V1 query 1 was corrected to accept any of 95 packages tied at fifth place rather than one package in the old reference. **A changed score can reflect repaired labels or validators rather than improved systems.** Preserve database and validator versions, complete per-query outputs, prompts, and traces before comparing results.

This update preserves DAB's original release date and citation snapshot. The date 2026-09-23 identifies this Radar's protocol verification, not a new benchmark release. Official submissions were not independently rerun.

<!-- PROTOCOL-AUDIT-20260923:END -->

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use the Data Agent Benchmark for discovery, transformation, and analysis across database systems rather than single-query SQL. On a small task set, hints, tuning, repeated trials, and grader versions materially affect rankings. Treat original-paper scores as historical evidence, not current ceilings.

### What a concrete task looks like

Illustrative task: an analysis reads several database systems, normalizes formats, joins records, and converts semi-structured content into computable fields. Connecting to the databases is only the beginning; field semantics and result validation determine success.

### Most discriminating experiment

Pin data and validator versions, disclose hints and task-specific tuning, and report repeated runs using the official aggregation. Retain missing, failed, and contaminated trials in the denominator. Compare raw access, static derived representations, and online updates to distinguish representation gains from answer or query caching.

### Pair with

[dataspace](dataspace.en.md) · [spider-2](spider-2.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`single-database text-to-SQL → cross-database integration → enterprise data agent`

DAB makes backend heterogeneity a first-class evaluation property.
