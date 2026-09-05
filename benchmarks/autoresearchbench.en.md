# AutoResearchBench: literature search needs both target finding and unknown-size set discovery

[中文](autoresearchbench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2604.25256) · [Code](https://github.com/CherYou/AutoResearchBench) · **Area: RAG / Agentic Retrieval**

AutoResearchBench separates scholarly search into two fundamentally different problems: **finding one target paper** and **discovering a relevant set whose true size is unknown**. The second makes “when should the search stop?” a first-class evaluation target.

## What it actually measures

The benchmark contains **1,000 queries across eight computer-science areas**:

- 600 Deep Research tasks seek one target paper;
- 400 Wide Research tasks collect an unknown-size relevant set.

Search runs over a fixed DeepXiv corpus with more than **3M full-text papers**. The frozen corpus improves reproducibility while retaining a large and realistic scholarly search space.

## Compared with what

Known-item retrieval has an easy stopping rule: stop when the target is found. Many deep-research benchmarks also emphasize the final answer rather than separately measuring literature-collection coverage.

AutoResearchBench adds **unknown-size set discovery**. The agent must reason about:

- whether important papers remain undiscovered;
- whether one more search is worth the cost;
- whether query expansion has covered the major terminology and subtopics;
- when stopping is justified rather than premature or exhaustive.

This makes search stopping, coverage estimation, and breadth management independently researchable.

## How the evaluation works

The Deep track is closer to target finding and naturally supports hit-style metrics. The Wide track uses set metrics such as IoU and recall to measure coverage.

Interpreting results requires a fixed corpus snapshot, gold-set version, search/index backend, agent harness, and budget. Search-call and token budgets directly influence Wide-track recall, so a higher score can simply reflect more search expenditure.

Deep and Wide should not be collapsed into one headline score because they reward very different policies: precise localization versus coverage and stopping.

## What a score supports

Deep accuracy supports a claim about whether an agent can find a target paper through multi-step search in the fixed scholarly corpus. Wide recall or IoU supports a claim about coverage relative to the current reference set.

The Wide track has a fundamental boundary: **the gold set may itself be incomplete**. If the construction process misses genuinely relevant work, a system can discover correct extra papers and still be penalized as if they were false positives.

Wide Research should therefore be interpreted as coverage and precision relative to a reference set, not as proof that the system has exhaustively found a research topic.

## Main confounders

The first is **gold-set completeness**. Unknown-size discovery is precisely the setting where exhaustive ground truth is difficult.

The second is the **retrieval backend**. Different indexes, metadata fields, citation graphs, or full-text parsing can materially affect outcomes independently of the agent policy.

The third is **budget sensitivity**. More searches can often improve recall, but may not be practically worthwhile; systems with very different latency and API cost should not be ranked on recall alone.

The fourth is corpus scope. A fixed DeepXiv snapshot excludes paywalls, live scholarly APIs, newly released papers, non-CS literature, and an evolving citation graph.

## Fair comparison contract

At minimum, align:

- DeepXiv or corpus snapshot;
- query and gold-set version;
- index, metadata, and full-text visibility;
- whether citation or graph navigation is allowed;
- model, harness, and tool interface;
- search-call, token, and wall-clock budgets;
- whether stopping is agent-controlled.

A system with citation-graph access and one limited to keyword search should be treated as a different tool setting.

## What is still missing

AutoResearchBench does not yet fully measure:

- live literature drift and newly released work;
- value-weighted relevance rather than equal value for all relevant items;
- uncertainty in the gold set itself;
- duplicates, versions, surveys, and original-work relationships;
- evidence extraction, disagreement handling, and synthesis after retrieval;
- real search cost under a fixed quality target.

## Most discriminating next test

A high-value extension is **marginal-value stopping**. After every search step, record the number and value of newly discovered important papers, and ask the system to estimate how much important evidence likely remains.

This yields a coverage–cost curve instead of a single terminal recall. A stronger research agent should not only find more, but know **when another search is worth doing and when the evidence is already sufficient**.

## Evolution position

`known-item scholarly retrieval → unknown-size literature discovery → value-aware, live, cost-sensitive research search`

AutoResearchBench is important in the middle step: it makes coverage and stopping first-class evaluation objects.
