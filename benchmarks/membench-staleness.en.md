# membench (staleness): ranking current facts above superseded ones

[中文](membench-staleness.md) | **English** · [Back to entry](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Code, scenarios, and results](https://github.com/Ps23102004/membench)

## Question

Does a memory store rank the current fact above a forbidden stale fact under updates, negation, entity confusion, temporal scope, and distractors?

## Evidence

Sixty executable probes expose recall, precision, `staleness@1`, leakage, abstention, contradiction resolution, and Wilson intervals through a pluggable write/query/reset interface. A published correction replaces invalid top-k staleness and closes abstention gaming. The embedding baseline returns a stale answer in 11/12 supersession probes; recency reranking reduces that count to 0/12.

## Caveat

The benchmark has only 60 correlated hand-written probes, exact-substring grading, tiny stores, and one author. Recency behavior is k-sensitive, and no downstream long-horizon task establishes that the ranking improvement helps an agent.

## Map

`map_delta=early_signal`, bound to `memory-update-and-staleness`. The corrected metric is useful as a component diagnostic, not yet a durable field shift.
