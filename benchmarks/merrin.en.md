# MERRIN: infer the needed modality before retrieving evidence from the noisy web

[中文](merrin.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2604.13418) · [Code](https://github.com/HanNight/MERRIN)

## What it measures

MERRIN contains 162 human-annotated short-answer questions whose evidence may come from images, video, audio, charts, or modality combinations, without explicit modality cues. It compares no-search, native-search, and agentic-search settings and analyzes resource use.

## Compared with what

Most web-search benchmarks are text-first, while multimodal QA usually supplies the image in advance. MERRIN places modality inference before retrieval, making wrong-medium selection a distinct failure mode.

## Score boundary

Short-answer accuracy supports evidence discovery under the current live web, provider, and multimodal backbone. It cannot define a stable long-term SOTA because web drift and proprietary search interfaces change candidate evidence.

## Fair comparison conditions

Align result date, search provider, tool interface, backbone, judge, and allowed modalities. Different providers or web snapshots require separate tracks.

## Next evaluation coordinate

The next step uses citation-level multimodal evidence portfolios and replayable snapshots to separate modality selection, retrieval, and final reasoning.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use MERRIN to study discovery of suitable image, video, or audio evidence without explicit modality cues. Knowing what kind of evidence to seek is part of the task. Live-web and proprietary-interface variation generally make results system-level evidence first.

### What a concrete task looks like

Illustrative task: a text question is answered by a video frame or chart, while text search provides only clues. The agent must choose a modality, locate relevant content, and resolve noisy or conflicting sources instead of treating snippets as final evidence.

### Most discriminating experiment

Fix the multimodal backbone and tools and compare autonomous modality choice, a correct modality hint, and supplied evidence. Track calls and latency by modality and include closed-book answering to distinguish routing, content understanding, and prior knowledge.

### Pair with

[mc-search](mc-search.en.md) · [browsecomp](browsecomp.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
