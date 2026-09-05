# DAComp: data engineering and data analysis are different agent capabilities

[中文](dacomp.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2512.04324) · [Project](https://da-comp.github.io/) · [Code](https://github.com/ByteDance-Seed/DAComp)

## What it actually measures

DAComp spans the **full data-intelligence lifecycle** with two distinct workloads: repository-level data engineering (DE) and open-ended data analysis (DA). DE requires designing/evolving multi-stage SQL pipelines; DA requires planning, iterative coding, interpreting intermediate results, and producing actionable recommendations.

## What changed relative to prior evaluation

Text-to-SQL and code benchmarks isolate local transformations. DAComp treats enterprise data work as a repository/workflow problem and, critically, refuses to collapse engineering correctness and analytical insight into one capability.

## Decisive evidence

The benchmark contains 210 tasks. State-of-the-art agents achieve under 20% success on DE and average below 40% on DA. The divergence shows that holistic pipeline orchestration and open-ended analytical reasoning remain separate bottlenecks rather than one generic “data agent” ability.

## What the score supports

Execution-based DE results strongly support repository/workflow correctness. DA scores depend on a validated rubric-guided LLM judge, so claims about analytical quality inherit evaluator assumptions. Aggregate scores should not erase the DE/DA split.

## Fair comparison contract

Fix repository snapshot, environment, agent harness, model, execution budget, and DA judge version. Report DE and DA separately with cost; a scaffold optimized for iterative coding may have different economics from one optimized for report synthesis.

## What remains unmeasured

Real enterprise systems add permissions, production writes, incidents, stakeholder negotiation, semantic-layer evolution, and long-running maintenance. Open-ended DA still uses curated rubrics rather than realized business impact.

## Next discriminating validation

Chain DE and DA tasks: require an agent to build/repair a transformation pipeline and then answer business questions from its outputs. This would test error propagation across the actual data lifecycle.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use DAComp to cover both data engineering and open-ended analysis, without pooling their tracks into an unexplained average. Repository transformations rely more on executable verification, while analytical reports depend more on rubrics. These mechanisms imply different uncertainty in the conclusions.

### What a concrete task looks like

Illustrative task: an engineering task modifies a data pipeline to produce correct output, while an analysis task explores a business problem and writes a report. The first tests code and state changes; the second also tests analytical framing and evidence interpretation.

### Most discriminating experiment

Fix engineering test environments and report evaluators separately, showing quality, time, and calls by track. Supply correct edit locations for engineering and intermediate results for analysis to diagnose discovery versus reasoning. Establish gains in each track before claiming generality.

### Pair with

[data-eng-bench](data-eng-bench.en.md) · [insightbench](insightbench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`local code/SQL → repository data engineering + open-ended analysis → integrated data-intelligence lifecycle`

DAComp shows why “data agent” should be decomposed by work product, not treated as one leaderboard number.