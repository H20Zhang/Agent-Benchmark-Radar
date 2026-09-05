# Spider: generalizing text-to-SQL to unseen database schemas

[中文](spider.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/1809.08887) · [Project](https://yale-lily.github.io/spider)

## What it actually measures

Spider evaluates **complex cross-domain text-to-SQL generalization**. It contains 10,181 questions and 5,693 unique SQL queries over 200 multi-table databases spanning 138 domains, with databases separated between train and test so systems must handle unseen schemas.

## What changed relative to prior evaluation

WikiSQL largely operates on one table at a time with a constrained grammar. Spider makes joins, nested queries, set operations, aggregation, and new database schemas central. The benchmark changed the core question from memorizing query patterns to aligning language with an unfamiliar relational structure.

## Decisive evidence

At release, the strongest reported model achieved only 12.4% exact match on the database split. The low score was not merely a scale effect: train and test differ in both SQL programs and schemas, deliberately blocking direct template reuse.

## What the score supports

Spider strongly supports schema-generalization and complex SQL-generation claims under a static, relatively compact database setting. High scores do not establish robustness to dirty values, huge catalogs, dialect documentation, business-rule drift, or multi-query workflows.

## Fair comparison contract

Use the same database split, schema serialization, value-access policy, SQL evaluator, and model/tool budget. Distinguish exact-match from execution-based evaluation and disclose any schema-linking retrieval or external metadata added beyond the benchmark input.

## What remains unmeasured

Schemas are small compared with enterprise warehouses, database contents are not the main difficulty, and each task still has a well-formed query intent. Real analysts must search metadata, resolve ambiguous business terms, and sometimes decide that no query should be executed.

## Next discriminating validation

Treat Spider as the schema-generalization rung and measure the same agent on BIRD, Spider 2.0, and reliability-oriented warehouse tasks. The degradation across rungs is more informative than one Spider leaderboard number.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use Spider for SQL generalization across schemas, while recognizing that static question-to-query mapping does not cover enterprise analysis. Distinguish SQL generation from business-semantic understanding, and structural matching from result equivalence.

### What a concrete task looks like

Illustrative task: a query requires several joins over an unseen schema, with nested operations or aggregation. Executable SQL can still be wrong because of join direction, aggregation scope, or duplicated rows.

### Most discriminating experiment

Preserve database-level splits and compare schema-linking and query-generation strategies under one backbone. Supplement structural matching with execution-equivalence checks and supplied-relevant-table controls. Do not describe tuning on test schemas as zero-shot generalization.

### Pair with

[bird](bird.en.md) · [spider-2](spider-2.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`single-table SQL → unseen multi-table schema → enterprise SQL workflow`

Spider established cross-schema generalization; later benchmarks mainly make the database and workflow more real.