# EvoBrowseComp: if a benchmark becomes stale, make regeneration part of the benchmark infrastructure

[中文](evobrowsecomp.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2606.13120) · [Data](https://huggingface.co/datasets/Krystalan/EvoBrowseComp)

## What it measures

EvoBrowseComp currently releases 800 complex live-web questions, 400 English and 400 Chinese, generated through a multi-agent web-traversal, synthesis, and filtering pipeline designed for periodic regeneration. It measures bilingual agentic web search and reasoning-graph following.

## Compared with what

The paper compares EvoBrowseComp with BrowseComp and BrowseComp-ZH, whose fixed questions can become stale or contaminated. EvoBrowseComp makes question regeneration part of the benchmark design. LiveBrowseComp is a useful complementary recent-fact benchmark, but it is not the reported comparison baseline in the paper’s Table 3.

## What the reported results show

Paper v1 uses Search and Visit tools, a 128K context limit, at most 40 tool calls, GLM-5-Chat as judge, and the mean of three evaluations. Claude-Opus-4.6 obtains 44.8% on English and 36.8% on Chinese with tools. Without tools, DeepSeek-V3.2 obtains 6.3% and 10.3%, respectively. These are separate language/tool settings, not one bilingual success rate. The three data-generation agents use DeepSeek-V3.2; the judge is a different role. [Paper v1, §3 and Tables 2–3](https://arxiv.org/html/2606.13120v1#S3).

## Score boundary

A score supports only the named generation/filter/judge pipeline and web date. Automatic regeneration does not guarantee equal difficulty across versions, so generations should not be treated as a progress curve without calibration.

## Fair comparison conditions

Align the snapshot, generator and filtering models, language, search provider, tool interface, context limit, maximum tool calls, decoding settings, and judge. Keep English/Chinese, tool-based/tool-free, and different generated releases in separate tracks. Repeat runs under the same protocol before interpreting score changes.

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
