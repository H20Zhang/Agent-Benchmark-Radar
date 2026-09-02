# EvoBrowseComp: if a benchmark becomes stale, make regeneration part of the benchmark infrastructure

[中文](evobrowsecomp.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2606.13120) · [Data](https://huggingface.co/datasets/Krystalan/EvoBrowseComp)

## What it measures

EvoBrowseComp currently releases 800 complex live-web questions, 400 English and 400 Chinese, generated through a multi-agent web-traversal, synthesis, and filtering pipeline designed for periodic regeneration. It measures bilingual agentic web search and reasoning-graph following.

## Compared with what

LiveBrowseComp uses human-authored recent facts but is expensive to refresh. EvoBrowseComp makes the question-generation pipeline part of the benchmark design so evaluation can evolve with the web.

## Score boundary

A score supports only the named generation/filter/judge pipeline and web date. Automatic regeneration does not guarantee equal difficulty across versions, so generations should not be treated as a progress curve without calibration.

## Fair comparison conditions

Align snapshot, generation/filter models, judge, language, search provider, and tool interface. English/Chinese and different generations need separate tracks.

## Next evaluation coordinate

The key next step is cross-generation calibration: prove that a new release is fresher rather than merely harder, easier, or stylistically closer to the generator.
