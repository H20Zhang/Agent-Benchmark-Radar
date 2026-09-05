# IRTS-ToolBench: for irregular time series, fix the time axis before claiming analytical competence

[中文](irts-toolbench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2606.15107)

## What it measures

IRTS-ToolBench contains 1,700 questions across ten task types and 13 domains with 30 tools: seven irregularity-handling operations and 23 analytical tools. Agents must first handle irregular sampling, missingness, or temporal alignment before statistical or predictive analysis.

## Compared with what

Conventional time-series benchmarks often provide a regularized matrix. IRTS-ToolBench makes preprocessing and tool routing the agent's responsibility, separating malformed temporal handling from downstream analytical failure.

## Score boundary

Task success supports tool-use competence under the current irregularity generator, tool library, and domains. It does not establish robustness to real sensor or financial streams where drift, streaming, and operational latency matter.

## Fair comparison conditions

Align task/domain split, tool library/version, irregularity pattern, agent budget, runtime, and grader.

## Next evaluation coordinate

The next step adds streaming updates, concept drift, and delayed labels, testing whether agents maintain temporal state rather than clean one dataset once.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use IRTS-ToolBench for temporal reasoning and tool selection on irregular time series. Regular-grid methods can hide interpolation or synchronization assumptions. Correct answers should be examined alongside whether tools preserve informative observation gaps.

### What a concrete task looks like

Illustrative task: unevenly spaced observations require trend or event analysis using appropriate tools. Treating adjacent records as equally spaced can produce executable computations with incorrect temporal meaning.

### Most discriminating experiment

Vary sampling patterns over the same underlying signal, comparing original timestamps, regularized interpolation, and irregularity-aware tools with matched queries and budgets. Allow functionally equivalent tool combinations and separate selection, parameterization, and question-format shortcuts.

### Pair with

[agentfuel](agentfuel.en.md) · [statabench](statabench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
