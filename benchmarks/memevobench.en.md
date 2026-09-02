# MemEvoBench: memory safety failures can accumulate through repeated writeback

[中文](memevobench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2604.15774) · [Code](https://github.com/xiewwee11/MemEvoBench)

## What it measures

MemEvoBench contains 108 QA risk cases across seven domains and 36 risk types plus 83 workflow cases. Misleading memories, noisy tool outputs, and biased feedback are repeatedly written back so gradual behavioral drift, attack success, and correction quality become measurable.

## Compared with what

Conventional safety evaluation treats prompts independently, while memory evaluation often assumes writes are trustworthy. Repeated writeback makes it possible to observe small unsafe errors being amplified across a memory lifecycle.

## Score boundary

Attack and correction metrics support drift resistance under the named memory-pool scaffold, base safety policy, and simulated feedback. They do not establish real tool consequences or shared-memory authorization, and system-level safety differences do not isolate one write filter.

## Fair comparison conditions

Align memory scaffold, base-model safety policy, judge, attack schedule, and simulated tool feedback, and keep single-round and multi-round conditions separate.

## Next evaluation coordinate

The next step traces each poisoned write to an external consequence and tests selective repair rather than clearing the entire memory.
