# MEMLENS: long context versus memory agents on genuinely multimodal evidence

[中文](memlens.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2605.14906) · [Code](https://github.com/xrenaf/MEMLENS)

## What it actually measures

MEMLENS compares **long-context vision-language models and memory-augmented agents** on multimodal, multi-session memory under controlled context lengths. It covers information extraction, multi-session reasoning, temporal reasoning, knowledge update, and answer refusal from 32K to 256K tokens.

## What changed relative to prior evaluation

The benchmark is designed to rule out text-only shortcuts. An image-ablation study verifies that visual evidence is necessary for most questions, allowing a direct comparison between keeping raw multimodal context and compressing it into an external memory representation.

## Decisive evidence

MEMLENS contains 789 questions at four standard context lengths. Removing evidence images drives two frontier LVLMs below 2% accuracy on the 80.4% of questions whose evidence includes images. Across 27 LVLMs and seven memory agents, long-context models are strong at shorter lengths but degrade as histories grow; memory agents are more length-stable yet lose visual fidelity through storage-time compression. Multi-session reasoning keeps most systems below 30%.

## What the score supports

The benchmark supports a real architecture trade-off: **raw-context visual fidelity versus compressed-memory scalability**. It does not show that either paradigm dominates in general, because backbone capability, compression format, and context implementation differ across systems.

## Fair comparison contract

Match VLM backbone when possible, use the same cross-modal token accounting, evidence images, context cutoff, and query set, and report memory construction/storage cost. Comparing a 256K raw-context system with an external-memory agent without counting ingestion and retained bytes is incomplete.

## What remains unmeasured

Contexts stop at 256K, below years of personal media. The benchmark is QA-centric and does not test future multimodal action, continual video ingestion, or update/delete operations.

## Next discriminating validation

Build hybrid systems that retain selectively chosen raw visual evidence while compressing the rest, then trace accuracy versus retained bytes and context length. This directly tests the architecture suggested by the benchmark's failure modes.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use MEMLENS to distinguish length degradation in long-context vision-language models from visual information lost by external-memory compression. The systems may be evaluated on different subsets. Align samples, visual input, and budgets before claiming memory outperforms long context.

### What a concrete task looks like

Illustrative task: a multimodal history grows across sessions and later questions require old visual details or state updates. Failure while original images remain accessible differs from losing the decisive information during compression.

### Most discriminating experiment

Compare long context and external memory on their common question subset. Supply original images and correct textual evidence as diagnostic controls. Hold questions fixed during length sweeps and account separately for compression, retrieval, and answering rather than only final-context tokens.

### Pair with

[memeye](memeye.en.md) · [mem-gallery](mem-gallery.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`long-context multimodal QA ↔ external memory agents → hybrid selective visual retention`

MEMLENS is valuable because it reveals why the two dominant memory architectures fail differently.