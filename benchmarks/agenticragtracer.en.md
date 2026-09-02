# AgenticRAGTracer: after the final answer fails, locate the first broken hop

[中文](agenticragtracer.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2602.19127) · [Code](https://github.com/YqjMartin/AgenticRAGTracer)

## What it measures

AgenticRAGTracer provides 1,305 multi-domain instances with hop-level intermediate validation for multi-step agentic RAG. The evaluation object is not only final exact match but whether retrieval and reasoning progress through verifiable intermediate states.

## Compared with what

Standard multi-hop QA only reveals a wrong final answer, while standalone capability tests may be detached from actual trajectories. AgenticRAGTracer places validation inside the chain so first-hop retrieval misses, poor hop allocation, and downstream reasoning over bad evidence can be separated.

## Score boundary

Hop-level correctness localizes deviation relative to the benchmark-defined chain; it does not prove that chain is the unique causal trajectory. Automatically generated hop structures may represent only one valid path, so an alternative successful route can look like a tracing failure.

## Fair comparison conditions

Align hop definitions, instance version, retrieval interface, backbone, and final evaluator. Systems allowed different tools or alternative valid trajectories need a tolerant track rather than direct comparison with strict-hop scores.

## Next evaluation coordinate

A stronger test performs counterfactual repair: replace one intermediate evidence item or decision and measure whether final success recovers, identifying genuinely load-bearing failure points.
