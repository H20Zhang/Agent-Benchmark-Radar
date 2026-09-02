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
