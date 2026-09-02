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

## Genealogy

`local code/SQL → repository data engineering + open-ended analysis → integrated data-intelligence lifecycle`

DAComp shows why “data agent” should be decomposed by work product, not treated as one leaderboard number.