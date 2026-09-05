# BRIGHT: when relevance itself requires reasoning

[中文](bright.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2407.12883) · [Official leaderboard](https://brightbenchmark.github.io/) · **Area: RAG / Retrieval**

BRIGHT asks a harder question than whether a retriever understands query semantics: **does recognizing relevance itself require reasoning?** When the query and the correct document have little direct lexical or embedding similarity, one-shot vector matching can fail systematically.

## What it actually measures

BRIGHT contains **1,384 real-world queries** spanning economics, psychology, mathematics, coding, and other domains.

Many relevant documents become relevant only after the system understands the problem, infers hidden constraints, or constructs intermediate reasoning. nDCG@10 therefore reflects more than representation similarity; it also exposes whether:

- the query is decomposed correctly;
- implicit constraints are recognized;
- retrieval needs reasoning-driven expansion;
- reranking can identify evidence that is logically relevant despite weak surface similarity.

## Compared with what

BEIR emphasizes **zero-shot generalization across domains**: does retrieval remain robust after moving to a new domain?

BRIGHT adds a different axis: even within a known domain, **the relevance judgment itself may require reasoning**.

The two benchmarks are complementary rather than substitutes:

- BEIR is primarily a robustness test;
- BRIGHT is primarily a reasoning-aware relevance test.

A retriever may generalize well on BEIR and still struggle on BRIGHT because it cannot infer the hidden relation between query and evidence.

## How the evaluation works

The endpoint is still a ranking metric such as nDCG@10: how highly are relevant documents ranked?

But the pipelines producing that ranking can differ substantially:

- direct dense retrieval from the raw query;
- LLM-generated reasoning or query expansion;
- multi-query retrieval;
- retrieve-then-rerank;
- dataset-specific preprocessing.

A BRIGHT score therefore needs to be reported together with the **reasoning budget, reranking stage, and index setting**.

## Decisive evidence and current results

The most important result from the original paper was not one absolute score, but the broad degradation of strong retrievers when relevance required reasoning compared with conventional retrieval benchmarks. BRIGHT therefore exposed a genuine blind spot of similarity-based retrieval.

The official leaderboard continues to evolve. Radar tracks the short-document 12-dataset mean nDCG@10 separately. Any “current best” should mean only **the highest verified result for that leaderboard track, at that date, under that protocol**. It should not be generalized to long-document settings, other subsets, or agentic search.

## What a score supports

A higher BRIGHT nDCG supports the claim that, under the named dataset mixture, document setting, and retrieval pipeline, a system is better at finding reasoning-dependent relevant documents.

It does not by itself establish:

- stronger multi-step search;
- better final QA answers;
- reasoning as the causal source of the gain;
- better system efficiency.

For example, an expensive query-expansion plus reranking pipeline may improve nDCG substantially without being a better production retriever.

## Main confounders

The first is **reasoning-expansion budget**. A strong LLM generating many candidate queries can itself move the score.

The second is **reranking**. A single-stage retriever and a pipeline using an expensive cross-encoder or LLM judge after top-k retrieval operate at very different cost points.

The third is **dataset aggregation**. Macro averages can hide severe failures in individual domains.

The fourth is **short versus long document setting**. Changing document granularity changes both retrieval difficulty and indexing cost.

## Fair comparison contract

At minimum, align:

- short/long-document setting;
- dataset subset;
- index preprocessing and chunking;
- whether reasoning expansion or multi-query retrieval is allowed;
- reranker type and candidate depth;
- LLM, token, and call budgets;
- metric and aggregation rule.

When these differ, results should be reported as separate tracks rather than merged into one ranking.

## What is still missing

BRIGHT remains fundamentally a **static ranking benchmark**. It does not fully measure:

- active query reformulation after a failed first retrieval;
- evidence chaining across multiple search steps;
- live corpora and newly appearing information;
- failure localization over a search trajectory;
- latency, token, tool-call, and index-serving cost;
- whether the generator actually uses retrieved evidence correctly.

## Most discriminating next test

A high-value extension is to turn BRIGHT from one ranking pass into a **reasoning-controlled retrieval trajectory**. Give agents the same query, allow a limited number of searches or reformulations, and record both newly recovered relevant evidence and cost at every step.

This would separate systems with stronger first-hop retrieval from systems that are better at recognizing a bad first search and correcting it.

## Evolution position

`semantic-similarity retrieval → reasoning-aware relevance → iterative reasoning-controlled evidence search`

BRIGHT occupies the middle step: it made “relevance requires reasoning” measurable, but does not yet evaluate the full search process.
