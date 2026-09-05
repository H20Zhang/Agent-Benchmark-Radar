# Mem-Gallery: multimodal memory is more than turning images into captions

[中文](mem-gallery.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://aclanthology.org/2026.acl-long.1892/) · [Code](https://github.com/YuanchenBei/Mem-Gallery)

## What it measures

Mem-Gallery uses multi-session visual-text conversations and compares 12 memory systems under one framework across memory extraction, test-time adaptation, reasoning, knowledge management, multimodal retention, and efficiency.

## Compared with what

Text-memory benchmarks can often reduce images to captions and continue unchanged. Mem-Gallery makes visual retention and cross-modal reasoning first-class capabilities, exposing information lost during visual writing or compression.

## Score boundary

The common framework improves relative comparison across memory systems, but QA and efficiency remain sensitive to the multimodal backbone, memory harness, and judge. A higher score supports the complete package under this visual-dialogue contract, not a causal advantage of one compression or retrieval component.

## Fair comparison conditions

Align multimodal backbone, image encoding/compression, memory budget, answerer, and judge, and report capability slices together with efficiency.

## Next evaluation coordinate

The next step connects visual memory to real environment actions and asks whether fine-grained visual evidence changes later tool choice or state updates.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use Mem-Gallery for retention and management of visual information in long-term conversations. First establish that visual evidence is necessary: when a textual paraphrase already reveals the answer, gains may reflect language reasoning rather than better multimodal memory.

### What a concrete task looks like

Illustrative task: an early session contains an image, and a later text query asks about a detail or a difference from another image. The system should trace back to visual evidence; a coarse caption may omit the attribute that determines the answer.

### Most discriminating experiment

Fix the vision-language backbone and compare access to original images, captions only, and compressed visual memory. Report genuinely image-dependent questions separately and distinguish information lost during writing from retrieval failure, rather than conflating visual encoding with the memory mechanism.

### Pair with

[memeye](memeye.en.md) · [memlens](memlens.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
