# ImplicitMemBench: memory can change the first action without an explicit recall request

[中文](implicitmembench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://aclanthology.org/2026.acl-long.1301/) · [Code](https://github.com/qinchonghanzuibang/ImplicitMemBench)

## What it measures

ImplicitMemBench contains 300 items evenly split across procedural memory, priming, and classical conditioning over 18 task families. A `learning → interference → test` protocol scores the first attempt, asking whether prior experience automatically changes behavior without an explicit instruction to recall it.

## Compared with what

Most agent-memory benchmarks are declarative: a query points back to past information. ImplicitMemBench makes non-declarative memory an explicit object so procedures, priming, and conditioned associations can be observed without a recall request.

## Score boundary

Paired priming controls support an effect of prior experience on first behavior, but short in-context episodes can still be explained by recency or in-context learning rather than durable external memory. Backbone susceptibility also matters.

## Fair comparison conditions

Align learning/interference/test order, first-attempt scoring, answerer, judge, and context placement, and retain paired controls instead of reporting treatment accuracy alone.

## Next evaluation coordinate

The next test should reproduce implicit effects across sessions and external memory under longer interference, including when they should be updated or suppressed.
