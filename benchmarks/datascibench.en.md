# DataSciBench: programmatic evaluation for multi-step data-science prompts

[中文](datascibench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2502.13897) · [Project](https://datascibench.github.io/) · [Code](https://github.com/THUDM/DataSciBench)

## What it actually measures

DataSciBench evaluates LLMs/agents on **multi-step data-science prompts** spanning six task types: cleaning/preprocessing, exploration/statistics, visualization, predictive modeling, data mining/pattern recognition, and interpretability/report generation.

## What changed relative to prior evaluation

Data-science evaluation is difficult once outputs are not single code snippets with obvious ground truth. DataSciBench introduces Task–Function–Code (TFC): 25 aggregate functions plus programmatic rules map complex outputs into 519 ground-truth test cases over 222 curated prompts.

## Decisive evidence

The benchmark evaluates 23 models: six API models and 17 open-source general/code models. Its key contribution is measurement infrastructure rather than a single leaderboard number: LLM self-consistency plus human verification is used to construct ground truth, then TFC evaluates execution outcomes at multiple granularities.

## What the score supports

DataSciBench supports broad data-science task completion under the TFC ontology. It does not fully measure autonomous workflow control if the prompt already specifies the analysis goal, and visualization/report metrics still have more evaluator subjectivity than deterministic transformations.

## Fair comparison contract

Fix prompt/data versions, execution environment, TFC rules, model, tool access, and retry budget. Report task-type and aggregate-function results rather than only a final score; a system can pass routine transformations while failing modeling or interpretation.

## What remains unmeasured

Long-horizon project state, repository maintenance, data discovery, business semantics, collaboration, and production deployment are beyond the bounded prompt episodes.

## Next discriminating validation

Measure whether TFC categories predict failure in longer agent trajectories: when an end-to-end project fails, can the benchmark correctly identify the missing primitive capability?

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use DataSciBench to evaluate executable outputs across diverse data-science tasks rather than code text alone. Task-specific scoring broadens coverage but complicates aggregation. Inspect task categories and whether validation functions capture the user's objective before interpreting totals.

### What a concrete task looks like

Illustrative task: a natural-language request asks for cleaning, computation, or an analysis artifact, requiring executable decomposition. An output can have the expected format but the wrong semantics, which file-existence checks alone would miss.

### Most discriminating experiment

Fix runtime and task functions, report analysis, modeling, and artifact slices, and add supplied-task-decomposition or intermediate-data controls. Distinguish planning, code, and evaluator failures, reviewing borderline scores independently.

### Pair with

[da-code](da-code.en.md) · [dsgym](dsgym.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`single code task → multi-step data-science prompt → decomposable execution evaluation`

DataSciBench's durable contribution is making complex analysis outputs more mechanically testable.