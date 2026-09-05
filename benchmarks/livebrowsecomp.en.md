# LiveBrowseComp: using low-salience facts from the previous 90 days to reduce “the model already knew it”

[中文](livebrowsecomp.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2605.28721) · [Data](https://huggingface.co/datasets/Forival/LiveBrowseComp)

## What it measures

LiveBrowseComp contains 335 human-authored questions based on low-salience facts published during the preceding 90 days across six frequently updated source families. Closed-book diagnostics and answer-source-removal ablations distinguish fresh evidence discovery from web-assisted verification of facts already in model parameters.

## Compared with what

BrowseComp is hard, but over time its questions can become familiar to models. LiveBrowseComp makes freshness and intrinsic-knowledge diagnosis explicit variables, separating knowledge cutoff from search ability more directly.

## Score boundary

Short-answer accuracy supports fresh retrieval for a dated web snapshot and model cutoff. The benchmark ages quickly, so current scores must carry result dates rather than being frozen as timeless SOTA.

## Fair comparison conditions

Align benchmark snapshot, search provider, tool interface, model cutoff, and source-removal protocol. Results from different dates need separate tracking.

## Next evaluation coordinate

The next step creates a continuous refresh lineage: does the same search agent remain strong across multiple fresh snapshots rather than one batch of recent facts?

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use LiveBrowseComp to test dependence on recent evidence rather than web-assisted confirmation of known answers. Freshness is relative to model and construction dates. An unchanged release may not preserve its original low-memorization condition as time passes.

### What a concrete task looks like

Illustrative task: the answer comes from a low-salience fact published shortly before construction, requiring a specific source. Closed-book success or success after removing that source weakens the evidence that the task measures discovery.

### Most discriminating experiment

Repeat closed-book and source-removal controls for each model, slicing by fact date and source under a fixed search budget. When refreshing questions, report set changes rather than treating scores across different snapshots as a direct model-progress curve.

### Pair with

[browsecomp](browsecomp.en.md) · [evobrowsecomp](evobrowsecomp.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
