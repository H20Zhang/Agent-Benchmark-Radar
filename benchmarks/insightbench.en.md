# InsightBench: a data analyst delivers useful insights, not SQL

[中文](insightbench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2407.06423) · [Code](https://github.com/ServiceNow/insight-bench)

## What it measures

InsightBench constructs 100 business-use-case datasets with verifiable planted insights. An agent performs question formulation, EDA, insight discovery, and recommendation, with evaluators judging whether the final report captures important findings rather than only executing a predefined query.

## Compared with what

Text-to-SQL benchmarks already specify what question to answer. InsightBench adds deciding what to analyze and what is worth reporting, closer to open-ended analyst work.

## Score boundary

Insight coverage supports discovery under the planted-insight distribution and judge. It does not establish real business value because synthetic patterns and the evaluator define what counts as an insight.

## Fair comparison conditions

Align dataset generation, reference insights, analysis budget, agent scaffold, and evaluator generation. Different judges or planted-insight density require separate snapshots.

## Next evaluation coordinate

The next step moves from planted insights to real business semantics, stakeholder goals, and decision impact, measuring whether analysis changes actual decisions.
