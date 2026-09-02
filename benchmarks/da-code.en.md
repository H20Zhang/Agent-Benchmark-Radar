# DA-Code: turning data-analysis decomposition into an executable coding benchmark

[中文](da-code.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

## What it measures

DA-Code contains 500 executable Python/SQL tasks covering data wrangling, machine learning, and exploratory analysis, testing whether an agent can decompose natural-language analytical requirements into runnable data operations.

## Compared with what

DS-1000 mostly measures local library coding. DA-Code moves closer to analysis workflows by combining SQL/Python and multi-step data operations, bringing task decomposition and execution into one evaluation.

## Score boundary

Execution success supports completing analytical operations under the current sandbox, assets, and task specification. It does not cover autonomous question discovery, business semantics, or final report quality.

## Fair comparison conditions

Align Python/SQL runtime, package versions, task data, allowed tools, step/retry budget, and completion criteria.

## Next evaluation coordinate

Successors need to combine executable analysis with uncertain ground truth, visualization, reporting, and cross-system data access.
