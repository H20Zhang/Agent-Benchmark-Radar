# Agent Retrieval Bench: Coding agents must find the right context before writing the patch

[中文](agent-retrieval-bench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2607.24882) · [Code and data](https://github.com/eyuansu62/agent-retrieval-bench)

## What it measures

Agent Retrieval Bench (ARB) isolates the **context-acquisition layer** of coding agents. Given a real workflow signal and a frozen base commit, a retriever must find files the agent needs to read next or abstain when the repository contains no useful local context. Relevance is defined by workflow need rather than query–file textual similarity.

## What changed relative to prior evaluation

Conventional code retrieval often defines gold context through semantic similarity or known edited files. ARB covers code2test, comment2context, trace2code, and edit2ripple workflow relations and adds natural no-gold and wrong-repository counterfactual controls for selective retrieval.

## Decisive evidence

The current release contains 427 samples across 25 repositories: 345 positive examples, 50 natural no-gold examples, and 32 counterfactual controls. The paper reports no single retrieval family dominating across tasks and metrics; logged agent trajectories miss every gold file on 27–35% of samples.

## What the score supports

It supports file-level upstream context-acquisition claims, not the claim that higher recall necessarily improves patch success. The official scope explicitly notes that file hits do not establish function/span localization and the current seed intervention studies context selection rather than full repair success.

## Fair comparison contract

Pin repository/base commits, candidate filtering, token packing, top-k/context budget, selective threshold, and metric version. Disclose release bundles and corpus inventory; legacy packing fields are not canonical BCY.

## What remains unmeasured

Function/line localization, edit generation, test-passing repair, multi-round tool exploration, and the impact of retrieval cost on complete repair latency.

## Next discriminating validation

Under one repair agent, intervene on initial context with random non-gold, retrieved, and oracle-gold seeds while fixing post-seed exploration budget. Measure both file/context quality and final test-passing repair.

<!-- RESEARCH-DECISION:START -->
## Research decision card
### When to use it
Use ARB when the claim concerns a context engine, repository retriever, or agent search policy finding the next useful coding context. It enables cleaner attribution than jumping directly to patch benchmarks.
### What a concrete task looks like
Illustrative task: a failure trace exposes a test file while the needed next read is a root-cause implementation in another module. Retrieval must bridge the workflow relation rather than match surface vocabulary.
### Most discriminating experiment
Fix the repair agent and post-seed exploration budget; replace only initial context with random, retrieved, and oracle-gold seeds, then measure context quality and final tests.
### Pair with
[BEIR](beir.en.md) · [The Recall Trap](recall-trap.en.md) · [BrowseComp-Plus_CM](browsecomp-plus-cm.en.md)
> **Score-reading rule:** file-level retrieval is an upstream coordinate, not end-to-end coding-agent success.
<!-- RESEARCH-DECISION:END -->

## Evolution position
`semantic code retrieval → workflow-conditioned context acquisition → selective retrieval / downstream intervention`
