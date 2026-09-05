# The Memory Trust Gap: stronger models can still over-trust stale memory

[中文](memory-trust-gap.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2609.01852) · **Area: Agent Memory**

## What it measures
The benchmark measures when a persistent-memory agent trusts a stale stored fact over current authoritative evidence. A Benefit suite requires memory to solve the task; a Safety suite always exposes the correct current value through an authoritative tool, separating useful memory from harmful over-trust.

## Compared with what
StateMemBench and MemTrapBench already expose stale-state and memory-induced failures. This work adds model-capability scale as an explicit coordinate and uses controlled interventions over labeling, recency, source authority, and position.

## Protocol and decisive evidence
Across Qwen3 0.6B, 1.7B, 4B, and 8B, memory is heavily used in the Benefit suite. In the Safety suite, larger models can be harmed more strongly under conditions where stale memory is made to look newer. The main pattern is also tested on a Llama-Instruct size series and two external datasets.

## Score boundary
The evidence supports capability-dependent memory-trust behavior; it does not establish that stronger models are generally less safe. The tasks are frozen, closed-set, and controlled, and the observed interaction depends on presentation and conflict construction.

## Remaining gap and next validation
Open-world agents with multiple tools, multiple sources, and long write histories remain unmeasured. A useful minimum design is three-arm rather than memory/no-memory: no memory, stale memory, and stale memory plus current authoritative tool evidence, run across a same-family model-size series.

Primary: https://arxiv.org/abs/2609.01852
