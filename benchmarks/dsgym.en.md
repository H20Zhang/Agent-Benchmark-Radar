# DSGym: data-science agents should work inside a stateful Jupyter environment, not answer isolated questions

[中文](dsgym.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

## What it measures

DSGym contains 972 analysis tasks plus 114 prediction tasks, 1,086 total, with an additional 90-task DSBio slice. Docker and stateful Jupyter execution require agents to analyze, model, debug, and reuse notebook state, with shortcut audits included.

## Compared with what

DS-1000 is isolated coding. DSGym makes code, data, runtime state, and later steps interdependent, closer to analyst notebook workflows and able to expose shortcut solutions.

## Score boundary

Execution or task success supports performance under the current notebook environment and release. Stateful semantics, package versions, and shortcut detection are load-bearing protocol variables.

## Fair comparison conditions

Align Docker image, Jupyter-state semantics, datasets, packages, step budget, shortcut policy, and evaluator.

## Next evaluation coordinate

The next step connects notebook execution to final reports/artifacts, review and recovery, and persistent project state.
