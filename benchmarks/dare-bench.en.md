# DARE-bench: real-world data transformation needs exact outputs, not judge impressions

[中文](dare-bench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

## What it measures

The DARE-bench paper describes about 6,300 tasks (5,948 train plus 352 eval), while the current public repository is smaller at roughly 4,274 train and 324 eval. Tasks use exact reference outputs, macro-F1, clipped R², and repeated runs to measure realistic data-transformation and modeling artifacts.

## Compared with what

Open-ended data-agent benchmarks often depend on LLM judges. DARE-bench is closer to “given raw data, produce a verifiable target artifact,” directly quantifying transformation correctness and stochastic reliability.

## Score boundary

Exact or numerical metrics support artifact correctness for the current task/data release. The paper/repository size difference requires versioning rather than mixing results across releases.

## Fair comparison conditions

Align task release, runtime/packages, reference outputs, number of runs, scaffold, and resource budget.

## Next evaluation coordinate

The next step adds source discovery, business semantics, and downstream use so matching an output is not confused with solving the correct analytical objective.
