# BRIGHT: when relevance itself requires reasoning

[中文](bright.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2407.12883) · [Official leaderboard](https://brightbenchmark.github.io/)

## What it measures

BRIGHT contains 1,384 real-world queries from economics, psychology, mathematics, coding, and other domains. Relevant documents often become relevant only after reasoning about an implicit requirement, so nDCG@10 exposes both query understanding and ranking quality beyond lexical or embedding similarity.

## Compared with what

BEIR primarily tests zero-shot domain generalization. BRIGHT asks a different question: even within a known domain, does recognizing relevance itself require reasoning? This makes the ceiling of pure semantic similarity visible and creates a distinct coordinate for reasoning-augmented retrieval.

## Decisive evidence and current results

The original paper showed strong retrievers performing far below their levels on conventional retrieval benchmarks. The official leaderboard continues to update. As of 2026-09-02 Radar tracks the short-document 12-dataset mean nDCG@10 separately, including Mira-Reasoning-Retrieval at 66.9 and INF-X-Retriever at 63.4. “Current best” refers only to that leaderboard track and does not transfer to long-document settings, other dataset subsets, or agentic search.

## Fair comparison conditions

Align short/long-document setting, the 12-dataset subset, reasoning expansion or reranking, index preprocessing, and aggregation. Scores from different tracks should not be merged.

## Next evaluation coordinate

BRIGHT remains static ranking. The next coordinate is reasoning that controls multi-step evidence discovery while accounting for latency, token, and tool cost.
