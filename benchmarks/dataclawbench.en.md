# DataClawBench: long data work needs a progress curve, not only the last answer before timeout

[中文](dataclawbench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2605.02503)

## What it measures

DataClawBench contains 492 tasks across seven categories, each with 2–9 gold milestones, over roughly 2.06M real records and a maximum agent budget around 1,200 seconds. Evaluation tracks milestone progress, final correctness, and efficiency so long-task stagnation becomes observable.

## Compared with what

Many data-agent benchmarks return only binary final success. DataClawBench distinguishes an agent that discovered and cleaned the data but failed late from one that never entered a correct workflow.

## Score boundary

Progress, final, and efficiency metrics support long-horizon performance under the current milestone annotations, records, and time budget. Gold milestones are not necessarily the only valid workflow, so path-sensitive interpretation requires care.

## Fair comparison conditions

Align time/step/tool budget, task data, milestone version, runtime, scaffold, and final evaluator.

## Next evaluation coordinate

The next step allows multiple valid workflows and uses counterfactual intervention to determine which milestones are genuinely necessary for final success.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use DataClawBench for autonomous exploration with little prior guidance and noisy raw data. Milestones distinguish productive investigation from aimless tool use, but reaching them does not guarantee correct conclusions. Domain and temporal concentration limit external validity.

### What a concrete task looks like

Illustrative task: an agent enters an unfamiliar financial-data environment, discovers tables, documents, and policies, and develops a verifiable conclusion. It can find the right source yet misread fields or stop early, motivating both progress and endpoint assessment.

### Most discriminating experiment

Fix tools, web policy, and time budget and compare autonomous runs with correct-source and correct-schema hints. Report milestones, final correctness, and time, reviewing high-progress but wrong-answer cases to locate the break between exploration and reasoning.

### Pair with

[kramabench](kramabench.en.md) · [ddr-bench](ddr-bench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
