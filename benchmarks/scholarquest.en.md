# ScholarQuest: academic search usually returns an intent-conditioned paper set

[中文](scholarquest.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2606.20235) · [Code](https://github.com/pty12345/ScholarQuest)

## What it measures

ScholarQuest contains 1,111 queries across more than 1,000 computer-science topics and four research intents. Each answer set has 5–200 arXiv papers over a shared roughly 3M-paper backend and citation graph, with recall@100, recall@all, and search-efficiency metrics.

## Compared with what

SAGE and AutoResearchBench already evaluate open-ended literature discovery. ScholarQuest makes user intent explicit: the same topic can require a survey set, method comparison, or evidence for a specific purpose.

## Score boundary

Recall supports set retrieval under the generated queries, LLM relevance adjudication, and corpus snapshot. Gold sets for open literature are inherently incomplete, so absolute recall reflects reference construction as well as agent quality.

## Fair comparison conditions

Align intent slice, corpus/citation graph, gold-set version, search budget, and relevance adjudicator. Different intents should be presented separately.

## Next evaluation coordinate

The next step measures marginal evidence utility: does each additional paper cover a new claim or aspect rather than simply hit another item in the reference set?

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use ScholarQuest for iterative paper collection conditioned on research intent, not merely title similarity. Answers are sets: missing a research branch differs from adding near-duplicates. Evaluate efficiency together with coverage.

### What a concrete task looks like

Illustrative task: an agent searches a topic, expands through citations, and adjusts scope to the research intent. An introductory overview and a comprehensive related-work search on the same topic can require different set boundaries and stopping rules.

### Most discriminating experiment

Fix the paper backend and call budget and compare keyword search, citation expansion, and intent-conditioned policies with per-intent recall. Review valid out-of-gold papers and track deduplicated coverage growth so incomplete gold sets and repeated results do not distort evaluation.

### Pair with

[sage](sage.en.md) · [autoresearchbench](autoresearchbench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
