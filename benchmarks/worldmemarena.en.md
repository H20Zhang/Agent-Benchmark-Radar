# WorldMemArena: localizing multimodal memory failure to lifecycle stages

[中文](worldmemarena.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2605.29341) · [Code](https://github.com/UCSB-AI/WorldMemArena)

## What it measures

WorldMemArena uses multi-session action-world trajectories with visual observations and evaluates writing, maintenance, retrieval, and use as four memory-lifecycle stages. The current artifact contains 461 samples with a balanced 150-sample subset; the paper describes about 400 annotated multimodal tasks.

## Compared with what

Most multimodal memory benchmarks report only final QA. Gold memory points and stage-level diagnosis separate writing errors, stale maintenance, retrieval misses, and failures to use correctly retrieved memory.

## Score boundary

Stage-level accuracy supports failure localization under the constructed trajectories. It does not establish utility in real persistent environments because checkpoint QA, judge, multimodal backbone, and storage representation remain important variables.

## Fair comparison conditions

Align artifact/sample version, backbone, memory representation, judge, compute budget, and the four-stage interface. Different sample counts must be versioned explicitly.

## Next evaluation coordinate

The next step connects lifecycle diagnosis to irreversible future actions, permissions, and recovery so each memory failure has an observable consequence.
