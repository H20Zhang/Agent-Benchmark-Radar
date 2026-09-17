# Q2D-Web

## Measurement object

Tests document retrieval for agent-rewritten queries against a large production-derived corpus, with citation, production-ranking, and pooled relevance labels.

## What changed compared with predecessors

Shifts retrieval evaluation toward the distribution of queries actually emitted by search agents; it is not an end-to-end agent benchmark.

## Protocol and comparison controls

Recall@1000 is the primary metric. Citation-based, production-ranker, and pooled labels are separate targets. Evaluations truncate documents to 512 tokens; late-interaction query limits and prompts also require alignment.

## Decisive evidence and score ceiling

The RRF corpus reduction retains the tested ranking on 31.7% of the corpus but raises absolute recall. The authors explicitly withhold documents, queries, and relevance labels; evaluation is hosted rather than a downloadable dataset.

## Strongest confounders and limitations

Production-selected documents and LLM/pooling judgments can privilege familiar retrieval patterns. Ranking preservation on existing models is not a guarantee for a new retriever or a different corpus.

## Coverage gap and next experiment

Private inputs limit independent auditing; retrieval scores do not measure whether an agent uses the evidence correctly.

Use a downloadable control such as BrowseComp-Plus alongside this hosted test. Hold the answerer and evidence budget fixed before asking whether retrieval gains improve task success.

## Genealogy and use

[BEIR](beir.en.md) · [BrowseComp-Plus](browsecomp-plus.en.md)

This entry is an `early_signal`: acceptance of a useful evaluation object does not promote one paper into a durable field-map claim.

## Primary sources and version

[Paper](https://arxiv.org/abs/2609.08887) · [Reviewed full text](https://arxiv.org/html/2609.08887v1)

[leaderboard](https://huggingface.co/spaces/perplexity-ai/q2d-web-leaderboard)

First public event: **2026-09-08**. Reviewed: **2026-09-17**. Source release and Radar acceptance are separate events.

[中文](q2d-web.md) · [Complete index](../library/README.en.md)
