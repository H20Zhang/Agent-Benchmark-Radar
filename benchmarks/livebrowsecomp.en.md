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
