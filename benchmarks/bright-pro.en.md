# Bright-Pro: retrieval should cover complementary reasoning aspects, not just relevant passages

[中文](bright-pro.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://aclanthology.org/2026.acl-long.1705/) · [Code](https://github.com/yale-nlp/Bright-Pro)

## What it measures

Bright-Pro contains 739 queries across seven StackExchange domains, 2,763 reasoning aspects, 5,272 gold passages, and 526,319 documents; 175 queries form an agentic-search subset. α-nDCG and weighted aspect recall measure whether an evidence portfolio covers complementary reasoning aspects, with fixed-round and adaptive agentic search protocols.

## Compared with what

BRIGHT established that relevance can require reasoning, but its relevant sets remain comparatively narrow. Bright-Pro decomposes each query into weighted aspects, so repeatedly retrieving similar passages does not look like complete evidence coverage.

## What the reported results show

Static and agentic results are separate comparisons. In the ACL paper, BGE-Reasoner-8B records Overall α-nDCG@25 of 68.0 on the static set (Table 2). With a fixed three-round GPT-5-mini search agent, its round-three answer quality is 4.31/5 (Table 3). The adaptive-round protocol additionally accounts for search cost using AER. Rankings can change with the agent backbone, so this site keeps protocols and backbones separate rather than defining a cross-protocol total. [Tables 2–4](https://aclanthology.org/2026.acl-long.1705.pdf#page=7).

## Score boundary

High α-nDCG or aspect recall supports evidence-portfolio coverage under the fixed corpus and annotation version. Agentic-search outcomes also depend on agent-retriever coupling, round budget, and judge. Static retrieval and the 175-query agentic subset are different evaluation objects and require separate tracks.

## Fair comparison conditions

Align the corpus, aspect annotations, number of rounds or stopping protocol, top-k per round, agent backbone, and judge. In particular, AER values from GPT-5-mini and Qwen3.5-122B-A10B search agents must remain separate. Version annotation revisions with results; the full static set and 175-query agentic subset are not interchangeable.

## Next evaluation coordinate

Align aspect coverage with the claims in the final answer: which aspects change the conclusion and which only add redundancy? Include tokens, search rounds, and latency in the cost comparison to establish whether better retrieval permits earlier stopping without losing completeness.

## Research decision card

### When to use it

Use Bright-Pro for complementary reasoning-aspect coverage across an evidence set, not only relevance of individual documents. Static retrieval, fixed-round search, and adaptive search answer different questions. Do not pool coverage, answer quality, and efficiency into an undefined overall ranking.

### What a concrete task looks like

Illustrative task: a question needs several complementary aspects; early retrieval covers one, so the next search should target a missing aspect. More evidence of the same type may remain relevant without increasing useful coverage.

### Most discriminating experiment

Fix the agent backbone and search budget and compare relevance ranking with selection targeting uncovered aspects. Align aspect coverage with claims in the final answer and test whether earlier stopping preserves completeness. Report efficiency separately for different backbones.

### Pair with

[bright](bright.en.md) · [claimprobe](claimprobe.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
