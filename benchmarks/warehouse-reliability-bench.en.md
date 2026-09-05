# WarehouseReliabilityBench: business truth instead of executable SQL

[中文](warehouse-reliability-bench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2608.09254)

## What it actually measures

WarehouseReliabilityBench (WRB) evaluates whether an analytics agent returns **business-correct behavior** under standard, ambiguous, unanswerable, schema-drift, and adversarial questions. Roughly half of the 400 frozen tasks over two synthetic warehouses have no correct SQL; the correct action is clarification, abstention, or refusal.

## What changed relative to prior evaluation

Execution-match assumes every question maps to a query. Production analytics often fails one level earlier: “revenue” has two valid definitions, a requested quantity is absent, or a deprecated column still executes but means the wrong thing. WRB evaluates semantic behavior contracts and false success, not syntax alone.

## Decisive evidence

On an 80-task frozen test split, QueryProof improves Business Truth Rate over a direct-prompted 32B baseline by +0.237 with a reported 95% interval [+0.112, +0.375], and reduces false-success rate from 0.754 to 0.351. But the paper explicitly warns that the comparison is scaffold-confounded; template-family resampling widens intervals enough to include zero, so direction is better supported than effect magnitude.

## What the score supports

WRB strongly supports the benchmark claim that **successful execution is not business correctness**. The QueryProof result supports a system-level deterministic semantic/rule-gating direction, not a claim that 7B models outperform 32B models or that any single component caused the gain.

## Fair comparison contract

Fix warehouse seed/snapshot, semantic-layer definitions, physical catalog, task split, model, scaffold, and cost accounting. Report Business Truth Rate, False Success Rate, coverage, abstention/clarification behavior, and cost separately. Never compare model sizes when scaffolding differs.

## What remains unmeasured

The evidence base is narrow: two synthetic domains, one seed, one model family, one SQL dialect, and disclosed test exposure. Transfer to BIRD/Spider or real warehouses is unproven.

## Next discriminating validation

Run the same semantic/rule scaffold over the larger baseline model on a fresh unseen warehouse family, then ablate semantic resolution and post-execution checks separately. That is the experiment needed for causal attribution.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use WarehouseReliabilityBench for false successes where executable SQL violates business semantics, and for clarification, abstention, or refusal. The target is semantic reliability rather than syntax and execution alone. Rule-layer quality must be separated from model contribution.

### What a concrete task looks like

Illustrative task: a requested business metric admits several definitions under the schema or lacks necessary data. The agent can generate executable SQL with a result even when the correct behavior is to clarify the definition or explain unanswerability.

### Most discriminating experiment

Fix business rules and databases, separate answerable tasks from non-answer behavior, and report business correctness and false success. Cross rule layers with models to test whether gains primarily come from hand-authored rules rather than autonomous semantic understanding.

### Pair with

[livesqlbench](livesqlbench.en.md) · [dabstep](dabstep.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`SQL execution correctness → semantic business truth → reliability-aware analytics agent`

WRB moves evaluation above the query language: sometimes the correct data-agent output is no query at all.