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
