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

## Genealogy

`long conversation memory → streaming clinical state → saturation-aware high-stakes memory`

MedMemoryBench makes memory degradation with accumulation a first-class production concern.