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

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use EvoBrowseComp to explore refreshable bilingual search evaluation, while distinguishing a regeneration pipeline from a single public snapshot. Long-term contamination resistance requires cross-version operation and difficulty calibration. Regenerability does not make scores directly comparable across versions.

### What a concrete task looks like

Illustrative task: a generation pipeline builds complex questions from live pages, and agents search in Chinese and English before returning short answers. Language versions may access different sources or reflect generator style, so inspect language slices rather than only a bilingual average.

### Most discriminating experiment

Compare systems on one fixed release, then retain auditable anchor tasks across refreshes to separate model change from task change. Vary generators and filtering models to test ranking stability, and inspect whether evidence difficulty is aligned across languages.

### Pair with

[livebrowsecomp](livebrowsecomp.en.md) · [gisa](gisa.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
