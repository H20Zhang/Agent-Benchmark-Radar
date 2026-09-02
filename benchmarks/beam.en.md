# BEAM: pushing long-term memory to coherent 10M-token conversations

[中文](beam.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2510.27246) · [Code](https://github.com/mohammadtavakoli78/BEAM)

## What it measures

BEAM uses 100 coherent conversations and 2,000 validated questions across 128K, 500K, 1M, and 10M-token histories, covering ten memory abilities. Unlike random needle concatenation, it preserves narrative coherence and cross-event relations so that degradation with history length becomes directly observable for long-context and retrieval-augmented systems.

## Compared with what

LoCoMo moved multi-session dialogue to roughly 16K tokens. BEAM pushes the same class of memory problem into million- and multi-million-token regimes while retaining conversational structure. Its central coordinate is how memory quality scales with horizon, not merely the best accuracy at one context size.

## Decisive evidence and score boundary

The paper reports that even LLMs supporting 1M-token contexts, with or without retrieval augmentation, degrade as dialogues lengthen. LIGHT, the authors' memory framework, improves average performance by roughly 3.5%–12.69% over the strongest baseline depending on the backbone, and ablations show complementary contributions from episodic memory, working memory, and a scratchpad. This demonstrates that BEAM exposes scale-induced failure. The LIGHT gain remains bundled-system evidence; the aggregate score alone does not prove any one component has a universal causal advantage.

## Fair comparison conditions

Align the backbone, actual context-window support, length bucket, retrieval budget, and question type. Scores from 128K and 10M should not be collapsed into an opaque current-best number, and models that truncate input are operating under a different evidence contract.

## Next evaluation coordinate

BEAM remains synthetic coherent conversation plus QA. The stronger next test is to apply comparable million-token pressure to real agent trajectories, continual writes/updates, and future action success.
