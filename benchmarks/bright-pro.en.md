# Bright-Pro: retrieval should cover complementary reasoning aspects, not just relevant passages

[中文](bright-pro.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://aclanthology.org/2026.acl-long.1705/) · [Code](https://github.com/yale-nlp/Bright-Pro)

## What it measures

Bright-Pro contains 739 queries across seven StackExchange domains, 2,763 reasoning aspects, 5,272 gold passages, and 526,319 documents; 175 queries form an agentic-search subset. α-nDCG and weighted aspect recall measure whether an evidence portfolio covers complementary reasoning aspects, with fixed-round and adaptive agentic search protocols.

## Compared with what

BRIGHT established that relevance can require reasoning, but its relevant sets remain comparatively narrow. Bright-Pro decomposes each query into weighted aspects, so repeatedly retrieving similar passages does not look like complete evidence coverage.

## Score boundary

High α-nDCG or aspect recall supports evidence-portfolio coverage under the fixed corpus and annotation version. Agentic-search outcomes also depend on agent-retriever coupling, round budget, and judge. Static retrieval and the 175-query agentic subset are different evaluation objects and require separate tracks.

## Fair comparison conditions

Align corpus, aspect annotations, search-round budget, agent backbone, judge, and static/adaptive protocol. Annotation revisions must be versioned with results.

## Next evaluation coordinate

The next step aligns aspect coverage with final claim coverage: which evidence aspects actually change the answer and which are redundant?
