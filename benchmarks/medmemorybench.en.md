# MedMemoryBench: measuring saturation in streaming clinical memory

[中文](medmemorybench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2605.11814) · [Code](https://github.com/AQ-MedAI/MedMemoryBench)

## What it measures

MedMemoryBench constructs 20 longitudinal patient personas with about 2,020 sessions, 16K turns, and 1,986 Chinese/English queries. Periodic evaluation during memory construction measures clinical-state tracking, updates, temporal localization, medical reasoning, noise resilience, and saturation.

## Compared with what

Conventional medical QA is a one-shot case and static memory QA hides degradation over time. An evaluate-while-constructing protocol makes it possible to observe when continuing clinical information starts to overwhelm the system.

## Score boundary

Streaming QA supports longitudinal retention under the synthetic patient trajectory, medical reader, and judge. It is not clinical deployment-safety evidence or a health-outcome metric, and different memory adapters/readers can move the saturation point.

## Fair comparison conditions

Align patient generation, stream checkpoints, reader, memory adapter, judge, and noise condition, and report performance over time rather than only a final average.

## Next evaluation coordinate

The next step connects real clinical tools, provenance, consent, and decision consequences, especially whether stale medical state can be corrected safely.
