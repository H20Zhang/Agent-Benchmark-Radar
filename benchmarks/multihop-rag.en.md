# MultiHop-RAG: retrieval must compose evidence, not only rank passages

[中文](multihop-rag.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2401.15391) · [Code](https://github.com/yixuantt/MultiHop-RAG)

## What it actually measures

MultiHop-RAG evaluates whether a RAG pipeline can retrieve **multiple mutually necessary pieces of evidence** and reason over their composition. The benchmark provides a news knowledge base, multi-hop queries, ground-truth answers, and supporting evidence, so retrieval and answer reasoning can be inspected separately.

## What changed relative to prior evaluation

Single-hop retrieval can look strong even when the final answer requires evidence that is individually weakly related to the query. MultiHop-RAG makes evidence composition the retrieval target instead of assuming one relevant chunk is sufficient.

## Decisive evidence

The paper evaluates embedding retrievers and several strong LLM readers and finds both stages unsatisfactory on multi-hop queries. This establishes a useful separation: improving the reader with gold evidence does not fix missing-hop retrieval, while a better retriever cannot compensate for a reader unable to compose the evidence.

## What the score supports

Retrieval metrics support evidence-discovery claims; answer metrics support the combined retriever-reader pipeline. Neither alone identifies adaptive search quality because the corpus and retrieval process are static rather than interactive.

## Fair comparison contract

Fix corpus snapshot, chunking, embedding/index configuration, top-k budget, and reader model. Report supporting-evidence recall together with answer quality. A larger top-k that increases reader context should be treated as a resource change, not a free retrieval improvement.

## What remains unmeasured

The corpus is static news and the protocol does not require iterative query reformulation, source selection, tool calls, or stopping. It therefore captures multi-evidence composition but not the control loop of modern agentic retrieval.

## Next discriminating validation

Allow iterative search under a fixed retrieval/token budget and compare one-shot top-k against adaptive hop-by-hop retrieval. The key question is when adaptive control reduces evidence volume rather than merely spending more calls.

## Genealogy

`single-hop relevance → multi-evidence retrieval → adaptive multi-step search`

MultiHop-RAG is a foundation for asking whether retrieval quality should be measured as evidence coverage rather than passage similarity.