# EvoMemBench: comparing memory systems on a scope × content coordinate system

[中文](evomembench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2605.18421) · [Code](https://github.com/DSAIL-Memory/EvoMemBench)

## What it measures

EvoMemBench organizes memory along two axes: in-episode versus cross-episode, and knowledge-oriented versus execution-oriented. The released suite has 5,754 samples across six settings; the paper compares 15 representative memory methods and reports answer/execution success together with token efficiency.

## Compared with what

Memory papers often report on different source benchmarks, so “method A is better” may actually reflect task mix. EvoMemBench introduces a common taxonomy and comparison protocol that places declarative knowledge and procedural/tool-use experience in one coordinate system.

## Score boundary

The standardized comparison improves coverage analysis, but the suite aggregates heterogeneous source benchmarks. Aggregate rank remains sensitive to source mixture, preprocessing, and task backbone, so it is better interpreted as a capability profile than universal memory quality.

## Fair comparison conditions

Align source benchmark versions, preprocessing, backbone, agent harness, and long-context budget, and report all scope/content cells rather than an aggregate alone.

## Next evaluation coordinate

A stronger benchmark creates all four forms of memory demand inside one controlled environment, enabling genuinely matched component comparisons.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use EvoMemBench to place memory systems on shared axes: within versus across episodes, and knowledge versus execution. It is a composite evaluation framework, not one task with identical conditions for every method. Inspect where gains occur before interpreting an aggregate.

### What a concrete task looks like

Illustrative task: one setting retains evidence within a long task, while another transfers experience from earlier tasks. Both involve memory, but write timing, accessible history, and outputs differ. One retrieval score cannot substitute for both.

### Most discriminating experiment

Match backbone, tools, and budgets within each of the four cells and report cell-level quality and cost. Add no-persistence controls for cross-episode tasks and full-context controls for within-episode tasks. Do not let source-dataset size silently determine the weight of the conclusion.

### Pair with

[memoryagentbench](memoryagentbench.en.md) · [memoryarena](memoryarena.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
