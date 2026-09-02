# Agent Memory Bakeoff: lexical mismatch and write-time enrichment

**English** | [中文](agent-memory-bakeoff.md) · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Code, data, and protocol](https://github.com/JaysonRawlins/agent-memory-bakeoff)

## What it actually measures

This benchmark measures whether **the representation written into memory changes future accessibility**. When later queries no longer reuse the vocabulary of the original incident or runbook, can the system still retrieve the relevant memory, and does write-time enrichment bridge that lexical mismatch better than storing the raw text? The protocol makes write-side representation a controlled variable in the memory pipeline.

## What changed relative to conventional memory benchmarks

Benchmarks such as LoCoMo and LongMemEval mostly observe downstream QA, where retrieval failures and answerer failures can be entangled. Agent Memory Bakeoff stops at the retrieval layer and crosses **BM25, vector, and hybrid retrieval with plain versus write-enriched memory**, making it easier to isolate whether enrichment itself improves access to the same underlying facts.

## Decisive evidence

The suite contains **225 scenarios, 497 synthetic memory documents, and 390 independently generated queries**, with sibling-aware gold labels and MRR@10 plus recall@1/@5. Write-time enrichment raises **BM25 MRR from 0.678 to 0.783** and symptom-query **recall@5 from 60.0% to 83.8%**. In the constructed lexical-shift setting, enrichment therefore materially changes the accessibility of memory to a lexical retriever.

## What the score supports

The result supports improved cross-vocabulary retrieval accessibility in this synthetic corpus with the tested local embedder. It does not establish better downstream answers or actions because the protocol ends at retrieval, and it does not show that enrichment dominates stronger embedding or reranking methods because the corpus is designed around the enrichment mechanism.

## Fair comparison contract

Query set, gold definition, retrieval top-k, embedder, BM25 configuration, and document granularity should be fixed when comparing write representations. Changing the memory enrichment and the embedder or reranker simultaneously prevents component attribution. Reporting lexical, semantic, and hybrid retrievers separately is useful for showing whether the gain is specific to one retrieval family.

## How to use it in research

The benchmark is useful for **memory component attribution**. A system that claims summarization, entity expansion, or semantic rewriting at write time improves future recall can first test the claim at this retrieval-only layer, then move to LongMemEval or MemoryAgentBench to determine whether higher accessibility translates into downstream utility.

## Next discriminating validation

The main gaps are natural corpora, multiple embedders, broader query distributions, and evidence that retrieval gains propagate to final answers or actions. A particularly informative next experiment would compare equal-budget write enrichment, query expansion, and reranking on the same memory corpus and query set, answering whether computation is best spent at write, query, or read time.

## Genealogy

`map_delta=early_signal`, bound to `memory-component-attribution`. The suite adds a controlled write-side intervention coordinate but does not yet justify changing the durable memory benchmark chain; that would require stable long-term utility gains across tasks and model families.
