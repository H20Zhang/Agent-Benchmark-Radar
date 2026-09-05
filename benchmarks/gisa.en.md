# GISA: web search can combine deterministic structured answers with complete human trajectories

[中文](gisa.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2602.08543) · [Code](https://github.com/RUC-NLPIR/GISA)

## What it measures

GISA contains 373 human-crafted queries across ten topic groups with item, set, list, and table answer formats, split into stable and live subsets. Every query has a complete human search trajectory, while final structured answers support deterministic exact-match and periodic live-answer refresh.

## Compared with what

Many deep-search benchmarks use short answers or LLM judges. GISA combines human process traces with structured verifiable outputs, evaluating both deep lookup and broad aggregation with less dependence on a judge.

## Score boundary

Structured exact match supports information seeking under the current answer refresh and web snapshot. Trajectory similarity only measures resemblance to a human path and does not mean that path is uniquely correct. Because the live subset changes, result date is part of the evaluation contract.

## Fair comparison conditions

Align stable/live split, answer refresh date, search provider, tool interface, and output normalization. Different refresh generations require separate snapshots.

## Next evaluation coordinate

Human traces can next support efficiency and repair analysis: does the agent reach equivalent evidence coverage with fewer unproductive searches rather than merely imitate human sequences?

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use GISA for information seeking that combines depth and breadth, particularly set, list, and table outputs. Structured answers enable deterministic grading, but content and formatting are separate concerns. Live tasks additionally require an answer-refresh date.

### What a concrete task looks like

Illustrative task: an agent must collect objects satisfying several constraints and return a list or table, not one representative example. Missing an object, mismatching a field, or violating order can change whether the task is complete.

### Most discriminating experiment

Separate content mismatches from serialization errors, compare policies under one search backend, and keep stable and live subsets distinct. Use human search traces to locate omissions without treating every alternative path as an error.

### Pair with

[sgr-bench](sgr-bench.en.md) · [wandr](wandr.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
