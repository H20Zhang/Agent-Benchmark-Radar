# KramaBench: real data agents must first discover, clean, and integrate a data lake

[中文](kramabench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Project](https://kramabench.org/)

## What it measures

KramaBench contains 104 tasks, 633 subtasks, 1,764 files totaling about 1.7GB, 24 sources, and six domains. Agents perform discovery, cleaning, integration, analysis, and modeling rather than starting from a curated table.

## Compared with what

Many benchmarks begin after the relevant data has already been selected. KramaBench brings file/source discovery and heterogeneous integration into the early workflow, making data-selection errors visible alongside downstream analysis errors.

## Score boundary

Subtask or task completion supports the full workflow under the named data-lake artifact, tools, and harness. It does not isolate one catalog, retrieval, or cleaning mechanism as causally superior.

## Fair comparison conditions

Align file corpus, source connectors, tool set, subtask definitions, agent budget, and evaluator. Extra schema or catalog hints change the evaluation object.

## Next evaluation coordinate

The next step adds access control, schema drift, incremental updates, and derived-artifact lineage to resemble a persistent production data lake.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use KramaBench for discovery and pipeline construction from messy heterogeneous file lakes. Full, trimmed, and oracle inputs impose different discovery demands. Gains with relevant files already selected do not establish better understanding of a real data lake.

### What a concrete task looks like

Illustrative task: an answer requires finding relevant files, cleaning and joining them, then constructing an analytical pipeline. Correct code for a subtask cannot rescue the workflow if file selection or column interpretation is wrong.

### Most discriminating experiment

Compare full lakes, supplied-correct-file sets, and supplied-intermediate tables for the same tasks, recording subtask artifacts. Match model and budgets and account for discovery cost and amortization across repeated queries to test the practical value of prebuilt representations.

### Pair with

[dataspace](dataspace.en.md) · [data-exploration-benchmark](data-exploration-benchmark.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
