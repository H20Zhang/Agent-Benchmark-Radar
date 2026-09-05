# BEIR: testing zero-shot retriever generalization across heterogeneous domains

[中文](beir.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2104.08663) · [Code](https://github.com/beir-cellar/beir) · **Area: RAG / Retrieval**

BEIR's historical importance is that it turned an often-neglected question into a standard test: **does a retriever that is strong on familiar data still work after moving to very different domains?** It made cross-domain zero-shot robustness a core retrieval criterion rather than an optional appendix experiment.

## What it actually measures

BEIR originally combines **18 retrieval datasets** spanning different domains, task types, query styles, and document distributions under a common ranking protocol.

The goal is not maximum performance on one familiar train/test distribution, but whether:

- ranking quality survives without target-domain retraining;
- lexical, dense, hybrid, and reranking methods trade off differently across domains;
- gains are specific to one dataset's vocabulary, length distribution, or training overlap.

That makes BEIR a foundational coordinate for asking whether a retrieval method truly generalizes.

## Compared with what

Early dense-retrieval progress was heavily centered on benchmarks such as MS MARCO. A model could dominate near its training distribution and still fail to retain that advantage in biomedical, finance, argument retrieval, or fact-verification settings.

BEIR's key change is the **heterogeneous suite**. The question becomes not “can this model optimize one benchmark?” but “does this retrieval inductive bias remain useful across distinct information needs?”

It also re-established BM25 as an important baseline: if a dense method cannot consistently beat lexical retrieval across domains, it is hard to claim a universal retrieval improvement.

## How the evaluation works

A standard BEIR evaluation builds or uses each dataset's corpus, queries, and relevance judgments, computes ranking metrics such as nDCG and Recall per dataset, then aggregates results under a chosen rule.

Any aggregate score must be interpreted together with:

- the exact BEIR subset;
- corpus and query preprocessing;
- reranker use;
- whether the retriever was trained on the target benchmark or related data;
- the aggregation rule.

A “BEIR score” is therefore not one uniquely defined number. Different subsets, training regimes, and reranking settings correspond to different experimental questions.

## Decisive evidence and score boundary

One durable early finding is that **strong dense retrieval on a single benchmark does not guarantee zero-shot superiority across domains; lexical baselines such as BM25 remain highly competitive in several datasets.**

BEIR therefore provides evidence about cross-domain ranking robustness, not a blanket conclusion that dense retrieval beats sparse retrieval or vice versa.

Modern results also mix stronger backbones, synthetic training data, instruction tuning, and rerankers. An aggregate nDCG today supports ranking quality only under the named dataset mixture, training data, and indexing protocol.

It does not directly establish end-to-end RAG answer quality or better iterative / agentic search.

## Main confounders

The first is **training-data overlap**. Modern retrievers train on far larger corpora than early BEIR systems, so “zero-shot” need not mean genuinely unseen in a data-provenance sense.

The second is **subset selection**. Evaluating only the datasets favorable to one method can materially change the average.

The third is **reranking budget**. A bi-encoder plus an expensive reranker and a single-stage retriever may reach similar nDCG with very different latency and system cost.

The fourth is **query/corpus preprocessing**. Chunking, title concatenation, normalization, and index parameters can all move the result.

## Fair comparison contract

At minimum, align:

- BEIR dataset subset and version;
- corpus/query preprocessing;
- retriever training data;
- index and search parameters;
- whether reranking is allowed and at what candidate depth;
- metric and aggregation rule;
- latency, hardware, and cost when efficiency is part of the claim.

Partial-suite averages should not be ranked directly against full-suite averages.

## What is still missing

BEIR remains fundamentally a **static retriever-only benchmark**. It does not fully measure:

- agents reformulating queries based on intermediate evidence;
- multi-step evidence discovery;
- corpus drift over time;
- whether downstream generators actually use retrieved evidence correctly;
- latency, token, index-size, and serving cost;
- whether a system knows when the first retrieval step was insufficient.

## Most discriminating next test

For modern agentic retrieval, the highest-value use of BEIR is not to discard it but to treat it as a **retrieval floor**. First verify that first-hop cross-domain retrieval has not regressed, then add iterative search, reformulation, and evidence-use evaluation over the same domains.

If a complex agent improves final QA while weakening BEIR-style first-hop retrieval, the system should explain where the gain comes from rather than attributing everything to “better search.”

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use BEIR to ask whether a retriever generalizes across domains rather than fits one training distribution. BM25 is a meaningful systems baseline. Worst-domain performance, indexing cost, and query latency can change the ranking of approaches beyond average retrieval quality.

### What a concrete task looks like

Illustrative task: one retriever handles domains with different vocabulary, document lengths, and relevance definitions without retraining for each. A model strong on familiar text may lose to lexical retrieval in terminology-heavy or shifted domains.

### Most discriminating experiment

Fix dataset versions and the hyperparameter-selection rule; compare BM25, dense, and hybrid retrieval with per-dataset results. Separate per-domain tuning from zero-shot evaluation and repeat the comparison under matched latency or cost constraints.

### Pair with

[bright](bright.en.md) · [commercial-tax](commercial-tax.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Evolution position

`single-domain retrieval → heterogeneous zero-shot retrieval → reasoning-intensive retrieval → iterative / agentic evidence search`

BEIR defines the second step and the baseline question many later retrieval systems should still answer: **does the method remain valid once it leaves its training distribution?**
