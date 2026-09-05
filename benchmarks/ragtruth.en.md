# RAGTruth: moving RAG hallucination evaluation from answer-level to word-level

[中文](ragtruth.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2401.00396)

## What it measures

RAGTruth contains nearly 18K naturally generated RAG responses with manual hallucination annotations at case and word level, including severity. The target is localized grounding failure relative to retrieved evidence rather than a single faithful/unfaithful label for an entire answer.

## Compared with what

Earlier hallucination evaluation often depended on automatic judges or coarse answer labels. Fine-grained human spans make it possible to locate exactly where generation exceeds the evidence and to compare failure patterns across domains and source LLMs.

## Decisive evidence and score boundary

The dataset shows that an apparently correct long RAG answer can still contain local unsupported spans with different severity. Detector performance supports hallucination detection on the annotated distribution. It does not measure adaptive retrieval policy, and a lower hallucination rate cannot automatically be credited to the retriever because source LLM and retrieval setup are load-bearing confounders.

## Fair comparison conditions

Align the response set, annotation policy, severity definition, and detector input. Changing the source generator or retrieval pipeline changes the hallucination distribution and belongs in a separate track.

## Next evaluation coordinate

The next step is closed-loop correction: once an unsupported claim is detected, can an agent find missing evidence, revise the answer, and retain a citation-level audit trace?

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use RAGTruth for localized hallucination detection and faithfulness assessment. Fine-grained labels expose error locations, but detecting an error does not establish that the original system can prevent or repair it. Keep detection and generation claims distinct.

### What a concrete task looks like

Illustrative task: most of an answer is supported, but a sentence or a few words overstate the evidence. A superficially correct answer still needs localized annotation; a single whole-answer truth label loses that diagnostic information.

### Most discriminating experiment

Test detection on held-out generators and domains, separating span localization from response-level classification. Use detections for repair and evaluate both support and completeness afterward, so deleting substantial content cannot masquerade as improved faithfulness.

### Pair with

[ragbench](ragbench.en.md) · [claimprobe](claimprobe.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
