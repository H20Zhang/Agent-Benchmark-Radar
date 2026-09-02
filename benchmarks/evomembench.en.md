# EvoMemBench: comparing memory systems on a scope × content coordinate system

[中文](evomembench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2605.18421) · [Code](https://github.com/DSAIL-Memory/EvoMemBench)

## What it measures

EvoMemBench organizes memory along two axes: in-episode versus cross-episode, and knowledge-oriented versus execution-oriented. The released suite has 5,754 samples across six settings; the paper compares 15 representative memory methods and reports answer/execution success together with token efficiency.

## Compared with what

Memory papers often report on different source benchmarks, so “method A is better” may actually reflect task mix. EvoMemBench introduces a common taxonomy and comparison protocol that places declarative knowledge and procedural/tool-use experience in one coordinate system.

## Score boundary

The standardized comparison improves coverage analysis, but the suite aggregates heterogeneous source benchmarks. Aggregate rank remains sensitive to source mixture, preprocessing, and task backbone, so it is better interpreted as a capability profile than universal memory quality.

## Fair comparison conditions

Align source benchmark versions, preprocessing, backbone, agent harness, and long-context budget, and report all scope/content cells rather than an aggregate alone.

## Next evaluation coordinate

A stronger benchmark creates all four forms of memory demand inside one controlled environment, enabling genuinely matched component comparisons.
