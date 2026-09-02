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
