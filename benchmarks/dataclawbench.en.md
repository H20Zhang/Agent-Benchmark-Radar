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
