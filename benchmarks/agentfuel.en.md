# AgentFuel: stateful analysis must prove its value through reuse across queries

[中文](agentfuel.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2603.12483)

## What it measures

AgentFuel currently contains 72 queries across three time-series domains, 24 per domain with 12 stateless and 12 stateful or incident-oriented queries, over about 13.5MB of generated data. It compares agents starting fresh with agents retaining analytical state across queries.

## Compared with what

Most benchmarks run each task independently. AgentFuel makes persistence an experimental variable and asks whether notebook, context, or memory state reduces repeated exploration and improves later incident analysis.

## Score boundary

A stateful advantage supports reusable analysis state under the current synthetic time-series generation and query order. Missing full public generator implementation limits reproduction, and gains may come from simple caching rather than deeper semantic memory.

## Fair comparison conditions

Align query order, persistence policy, data generator, scaffold, model, budget, and evaluator, and report matched stateless/stateful pairs.

## Next evaluation coordinate

The next step separates cache, structured semantic state, and learned workflow experience and tests whether stale state hurts after data changes.
