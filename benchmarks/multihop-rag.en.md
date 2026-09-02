# MultiHop-RAG: putting multi-hop retrieval failure back inside the RAG pipeline

[中文](multihop-rag.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2401.15391) · [Code](https://github.com/yixuantt/MultiHop-RAG)

## What it measures

MultiHop-RAG uses a news-based knowledge base and questions requiring multiple pieces of supporting evidence, evaluating retrieval and answers together. Systems must find evidence across hops instead of relying on the generator to perform multi-hop reasoning after one retrieval step.

## Compared with what

HotpotQA already introduced multi-document QA. MultiHop-RAG more directly targets a RAG pipeline and observes retrieval failure alongside answer failure, preventing a strong reader from completely hiding a missing first-hop evidence problem.

## Decisive evidence and score boundary

Its key contribution is exposing systematic gaps in single-shot retrieval on multi-hop questions. Retrieval recall and answer accuracy support evidence discovery under the fixed news corpus and pipeline; they do not support claims about live web search, adaptive retrieval policy, or general tool orchestration. If retriever and reader both change, the end-to-end delta remains packaged-system evidence.

## Fair comparison conditions

Align corpus, query set, retriever-reader boundary, candidate budget, and answer evaluator. Results using a different snapshot or external search need separate tracks.

## Next evaluation coordinate

The stronger successor lets the agent choose the next hop from evidence already found and measures stopping, query reformulation, evidence sufficiency, and search cost.
