# MEMLENS: the multimodal trade-off between long context and external memory

[中文](memlens.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2605.14906) · [Code](https://github.com/xrenaf/MEMLENS)

## What it measures

MEMLENS has 789 questions and 4,695 unique images across controlled 32K, 64K, 128K, and 256K contexts; memory agents use a fixed 195-question subset. It compares native long-context VLMs with external-memory agents on visual memory, multi-session/temporal reasoning, updates, and abstention.

## Compared with what

Expanding context and compressing experience into external memory are different strategies. Controlled length scaling and visual-necessity ablations expose native length degradation separately from visual-fidelity loss introduced by memory compression.

## Decisive evidence and score boundary

Experiments show that removing evidence images drives some frontier VLMs close to failure on many visually dependent questions, while multi-session reasoning remains difficult. This supports preserving visual evidence during storage-time compression. The 195-question memory-agent subset and 789-question full set are different contracts and must not be merged into one leaderboard.

## Fair comparison conditions

Align context length, question subset, multimodal backbone, memory adapter/compression, answerer, and judge. Full-set and memory-agent-subset scores need separate tracks.

## Next evaluation coordinate

A stronger benchmark jointly measures visual fidelity, memory bytes/cost, and future action success rather than QA alone.
