# BrowseComp-Plus_CM: projecting agentic search onto an independent large corpus

[中文](browsecomp-plus-cm.md) | **English** · [Back to entry](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2608.20317) · [Code](https://github.com/castorini/cmass) · [Data](https://huggingface.co/datasets/castorini/cmass)

It keeps the BrowseComp-Plus questions and BM25 tool interface while replacing a roughly 100K-document, query-built collection with 553 million independently assembled ClimbMix documents.

## What it follows

BrowseComp places deep search on the live web, where opaque search APIs, page drift, and answer leakage confound the agent, retriever, and environment. BrowseComp-Plus freezes the corpus, but gathers both positives and hard negatives around the test questions and contains only about 100K documents. BrowseComp-Plus_CM retains the 830 questions and accepts a projection only when every hop is grounded in ClimbMix and survives independent-agent and human review; 57 questions remain with question-level qrels.

## How it is evaluated

**Question:** When the question, agent, search/document interface, and judge stay fixed, how much harder does evidence discovery become in a much larger independently built corpus?

**Measurement object:** agentic retrieval of all evidence needed for multi-hop questions over a fixed 400B-token, 553M-document web corpus, reported through answer accuracy, evidence recall, and tool calls.

**Scale and protocol:** the pipeline starts from 830 questions, retains 326 after answerability checks, 65 after automatic all-hop verification, and 57 after human review. The controlled comparison swaps only the BM25 index between BrowseComp-Plus and ClimbMix while keeping the agent, search/get_document tools, and GPT gold-answer judge fixed.

## What a score can support

For the same GPT-5.6 Sol agent, evidence recall falls from 84.3% to 21.4% and mean retrieval calls rise from 60.2 to 98.3, while answer accuracy falls only from 86.0% to 80.7%. This supports the claim that a small query-built corpus can substantially understate evidence-discovery difficulty, and that final-answer accuracy cannot replace retrieval-process metrics. It does not establish the general superiority of one retriever or agent architecture.

## Strongest confounder

The 57 questions are a projection-survivor subset, and GPT-5.6 Sol already answers 70.2% of them closed-book. Hop decomposition, support judgments, and qrel expansion also use GPT-5.5 / Claude Opus 5 judgments, while the released comparison exposes only a BM25 interface. The current Hugging Face card also says both that `qrels` has 6,695 rows and that duplicate expansion should produce 12,140 rows; the downloadable size and reproduction guide point to 6,695, so the expansion version is unresolved. The corpus-swap result is strong, but cross-retriever, cross-model, and contamination generalization remains limited.

## What remains uncovered

The result needs replication on larger independently authored question sets, more retrieval interfaces, and protocols that require explicit citations—especially to separate evidence exposure, evidence use, and parametric recall.

## Genealogy consequence

`map_delta=revises`, bound to `retrieval-harness-validity`. Its matched corpus swap directly qualifies the durable BrowseComp-Plus claim: a fixed corpus is necessary for drift control and attribution, but query-conditioned construction, scale, and qrels remain load-bearing variables. The map receives only that smallest qualification; one projection is not promoted into a universal trend.
