# AutoResearchBench: literature search needs both target finding and unknown-size set discovery

[中文](autoresearchbench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2604.25256) · [Code](https://github.com/CherYou/AutoResearchBench)

## What it measures

AutoResearchBench contains 1,000 queries across eight computer-science areas: 600 Deep Research tasks seek one target paper, while 400 Wide Research tasks collect an unknown-size relevant set over a fixed DeepXiv corpus of more than 3M full-text papers.

## Compared with what

Known-item search has an obvious stopping rule: stop when the target is found. Wide Research makes set size unknown, forcing an agent to trade recall against search cost and turning stopping behavior into an evaluation object.

## Score boundary

Deep accuracy and Wide IoU/recall support targeted and exhaustive search under the fixed CS corpus. Wide gold sets can still be incomplete, and DeepXiv does not cover paywalls, live scholarly APIs, or cross-domain literature drift.

## Fair comparison conditions

Align corpus snapshot, gold-set version, search/index backend, agent harness, and budget, and report Deep and Wide tracks separately.

## Next evaluation coordinate

The next step models gold-set uncertainty and marginal-value stopping: how much new high-value evidence does one more search actually discover?
