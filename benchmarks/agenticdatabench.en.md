# AgenticDataBench: the target is a complete data-agent deliverable, not one query

[中文](agenticdatabench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Project](https://agenticdatabench.github.io/)

## What it measures

AgenticDataBench covers 344 realistic end-to-end data tasks, 97 datasets, 15 domains, roughly 27.3GB and 123.1M rows, with 433 skill labels. It evaluates full data-agent workflows and compares scaffolds such as Codex, Claude Code, Smolagents, and DA-Agent paired with different backbones.

## Compared with what

DAB focuses on enterprise questions spanning databases. AgenticDataBench emphasizes complete analytical workflows and skill coverage. Strong SQL alone is insufficient if data understanding, transformation, analysis, or delivery fails.

## How to interpret current scores

In the official 2026-07-02 snapshot, the best system is about 49.39%, with the other agent/model combinations spanning roughly 31.83%–47.77%. These are packaged scaffold+model comparisons, not causal evidence for one orchestration idea. The web stores the full 12-row official snapshot while README remains score-free.

## Fair comparison conditions

Align benchmark snapshot, scaffold, model, tool/runtime, task limits, and evaluator. Agent+model combinations are system entries rather than raw model rankings.

## Next evaluation coordinate

The next step separates business truth, artifact correctness, recovery, and cost so end-to-end failure can be localized to workflow stages.
