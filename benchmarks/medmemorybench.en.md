# MedMemoryBench: streaming memory accumulation in personalized healthcare

[中文](medmemorybench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2605.11814) · [Code](https://github.com/AQ-MedAI/MedMemoryBench)

## What it actually measures

MedMemoryBench evaluates memory under **streaming clinical accumulation**: patient history grows over time, relevant medical state must remain precise, and increasing information density can actively make retrieval and reasoning worse. The benchmark treats memory saturation as a measurable failure mode.

## What changed relative to prior evaluation

Open-domain conversation memory typically treats longer history as a scale challenge. Healthcare changes the cost of error and the structure of state: old information can remain clinically relevant, become superseded, or interact with new symptoms. MedMemoryBench uses an evaluate-while-constructing protocol to observe performance as memory is incrementally built.

## Decisive evidence

The dataset contains roughly 2,000 sessions and 16,000 interaction turns generated from clinically grounded synthetic patient archetypes and expert validation. The released framework includes 14 memory-method baselines. Experiments expose severe bottlenecks in complex medical reasoning, noise resilience, and memory saturation as the stream grows.

## What the score supports

The benchmark supports claims about memory robustness under synthetic but clinically structured histories. It does not constitute clinical validation or evidence that a system is safe for patient care; the downstream medical model and synthetic trajectory assumptions remain major confounders.

## Fair comparison contract

Fix patient trajectory, clinical backbone, streaming checkpoint, retrieval budget, and evaluator. Report performance as a function of accumulated memory size instead of one final average. Stale/superseded medical state and irrelevant noise should be separated because they stress different mechanisms.

## What remains unmeasured

Real EHR data includes missing records, coding artifacts, provider disagreement, legal constraints, and distribution shift. Prospective clinical outcomes and harm are outside a synthetic benchmark.

## Next discriminating validation

Build stage-level saturation curves for write compression, retrieval, and reasoning, with oracle retrieval at each checkpoint. This would identify whether longer clinical memory primarily fails because the right evidence is lost, not found, or misused.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use MedMemoryBench for streaming state maintenance and memory saturation, not as clinical deployment validation. Its research value is locating when errors emerge as histories accumulate. Synthetic medical-dialogue QA and real clinical outcomes are different levels of evidence.

### What a concrete task looks like

Illustrative task: a simulated user's state is revised over many sessions, with questions at repeated checkpoints. Relevant earlier facts may be displaced by noise, while newer state may fail to supersede old records. Diagnose these failures over time.

### Most discriminating experiment

Evaluate historical-fact and current-state questions on the same stream, plotting checkpoint quality and cumulative ingestion cost. Add a supplied-current-state control to separate updating failures from domain reasoning, and keep conclusions scoped to the simulated setting.

### Pair with

[memoryagentbench](memoryagentbench.en.md) · [statemembench](statemembench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`long conversation memory → streaming clinical state → saturation-aware high-stakes memory`

MedMemoryBench makes memory degradation with accumulation a first-class production concern.