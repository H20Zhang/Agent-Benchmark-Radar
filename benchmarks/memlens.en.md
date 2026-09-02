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

## Genealogy

`long-context multimodal QA ↔ external memory agents → hybrid selective visual retention`

MEMLENS is valuable because it reveals why the two dominant memory architectures fail differently.