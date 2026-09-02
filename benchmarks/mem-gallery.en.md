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
