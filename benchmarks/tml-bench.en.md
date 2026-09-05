# TML-Bench: autonomous ML comparisons must lock the wall-clock budget

[中文](tml-bench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2603.05764)

## What it measures

TML-Bench uses four Kaggle competitions, compares ten open-source LLMs, and defines 240, 600, and 1,200-second wall-clock budgets with five successful runs per condition. Evaluation checks valid submissions, private holdout scores, and stability across runs.

## Compared with what

MLAgentBench has iterative experiments, but compute and time can still be hidden variables. TML-Bench makes wall-clock budget an explicit track so running ten times more experiments is not mistaken for pure agent intelligence.

## Score boundary

Holdout score supports autonomous modeling under a concrete competition, hardware/runtime, and time budget. Different budgets or hardware are not apples-to-apples, and the best single run is not sufficient evidence.

## Fair comparison conditions

Align time budget, hardware, competition data, submission validator, model/scaffold, and run count, and report stability.

## Next evaluation coordinate

The next step jointly measures experiment efficiency, reproducible artifacts, and invalid-result detection rather than only leaderboard score.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use TML-Bench for reliable delivery of valid tabular-ML results within a time budget. With few tasks, stability and failures are central. Medians over successful runs can hide configurations that rarely finish, so report all attempts as well.

### What a concrete task looks like

Illustrative task: an agent inspects data, selects features and a model, and delivers a valid prediction file before a deadline. A strong model without a valid submission is not a completed task, and more time need not improve reliability.

### Most discriminating experiment

Keep hardware and instructions fixed while varying time budget. Track valid submissions, hidden-set quality, and variability across all attempts. Separate conditions with budget-dependent prompt changes so instruction changes are not mistaken for time-scaling gains.

### Pair with

[dare-bench](dare-bench.en.md) · [mle-bench](mle-bench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
