# AgenticRAGTracer: locating failure along the retrieval-reasoning chain

[中文](agenticragtracer.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2602.19127) · [Code](https://github.com/YqjMartin/AgenticRAGTracer)

## What it actually measures

AgenticRAGTracer adds **hop-aware intermediate validation** to multi-step retrieval reasoning. Instead of providing only a final question and answer, it exposes intermediate hop questions that connect atomic evidence needs to the final query.

## What changed relative to prior evaluation

A failed multi-hop answer does not reveal whether an agent stopped too early, followed an unnecessary branch, retrieved wrong evidence, or reasoned incorrectly after retrieval. Hop labels make step allocation and chain shape observable.

## Decisive evidence

The benchmark contains 1,305 automatically constructed instances across multiple domains with no overlap with mainstream benchmarks. On the hardest subset, GPT-5 reaches only 22.6% exact match. Hop-aware diagnosis attributes many failures to distorted chains that either collapse prematurely or over-extend beyond the logical structure.

## What the score supports

The benchmark provides diagnostic evidence about reasoning-chain allocation and intermediate retrieval. Because much of the benchmark is LLM-generated, the annotated hop structure should not automatically be treated as the unique causal decomposition of a problem.

## Fair comparison contract

Fix model, tools, step/call budget, and hop evaluator. Report final EM together with hop completion and chain length. Penalizing an alternative valid reasoning path merely because it differs from the generated hop template would measure conformity rather than search competence.

## What remains unmeasured

Real web research often has multiple valid decompositions, uncertain subgoals, and evidence discovered opportunistically. Automatically generated hop chains can encode construction artifacts.

## Next discriminating validation

Annotate a subset with multiple human-validated solution graphs and evaluate whether diagnostic conclusions survive equivalent alternative paths. This would test whether “wrong chain” truly means wrong reasoning rather than different reasoning.

## Genealogy

`multi-hop final answer → hop-level trace → causal diagnosis of search allocation`

AgenticRAGTracer turns the length and shape of a reasoning chain into an evaluation object.