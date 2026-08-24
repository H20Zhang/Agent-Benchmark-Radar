# Agent Memory Bakeoff: cross-vocabulary retrieval and write-time enrichment

[中文](agent-memory-bakeoff.md) | **English** · [Back to entry](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Code, data, and protocol](https://github.com/JaysonRawlins/agent-memory-bakeoff)

## Question

Can a memory system retrieve an incident or runbook when the later query uses different vocabulary, and does enriching memory at write time improve that access?

## Evidence

The suite crosses BM25, vector, and hybrid retrieval with plain versus write-enriched memory over 497 synthetic documents from 225 scenarios and 390 independently generated queries. It reports MRR@10 and recall@1/@5 with sibling-aware gold. Write enrichment raises BM25 MRR from 0.678 to 0.783 and symptom-query recall@5 from 60.0% to 83.8%.

## Caveat

The corpus is synthetic and constructed around the proposed enrichment mechanism, only one local embedder is tested, and the protocol stops at retrieval. The gains therefore support cross-vocabulary access under this corpus, not better downstream agent answers or actions.

## Map

`map_delta=early_signal`, bound to `memory-component-attribution`. It adds a controlled write-side intervention but does not change the durable memory chain.
