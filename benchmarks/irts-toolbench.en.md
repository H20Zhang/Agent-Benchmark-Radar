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
