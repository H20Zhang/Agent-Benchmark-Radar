# The Commercial Tax: RAG / deployment validity

[中文](commercial-tax.md) | **English** · [Back to the entry](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2608.16096) · [Code](https://github.com/Toryx-AI/commercial-tax-multihop-retrieval) · [Reproduction artifact](https://doi.org/10.5281/zenodo.21972866)

Rebinds a raw retrieval number to license, query format, index construction, and recurring cost.

## Genealogy: What It Follows

Earlier evaluation usually compressed this problem into a shorter final score or a single proxy. This object turns its predecessor critique into an explicit capability × environment × protocol delta and retains an executable or auditable artifact.

## How It Is Evaluated

**Question:** Can a benchmark embedding score transfer to production under licensing, formatting, and cost constraints?

**Measurement object:** Retrieval reproducibility audit that binds raw embedder scores to licensing, query formatting, index construction, and deployment cost.

**Scale and protocol:** Thirteen embedders on the same 11,656-passage, 1,000-question retrieval floor. The protocol includes exact-cosine-search, paired-bootstrap, license-provenance, separate-construction-query-cost.

## What a Score Can Support

Thirteen embedders with paired bootstrap, license provenance, and separated construction/query cost show that similar raw recall does not imply the same deployment meaning. It supports system-level evidence under this environment, harness, model/tool, and resource configuration; unmatched variables prevent attribution to one component.

## Strongest Confounder

Uneven format tuning, hosted drift, and a single corpus limit portability across models, systems, and time. The load-bearing confounders are uneven-query-format-search, hosted-endpoint-drift, single-corpus.

## Remaining Gap: What It Still Does Not Measure

Uneven query-format tuning, drifting hosted endpoints, and a single main corpus limit generality to raw exact-search retrieval.

## Genealogy: Where It Fits in the Map

`map_delta=reinforces`. One paper is only a signal; a durable direction needs independent records bound to the same canonical direction key.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use The Commercial Tax to interpret embedding-retrieval scores alongside licensing, query format, and deployment cost. Controlled exact-search comparisons are useful, but one corpus and unequal tuning do not establish a production ranking for all workloads.

### What a concrete task looks like

Illustrative task: several embedding models index one corpus and serve queries through the same similarity search. Document-encoding cost, query cost, and applicable licensing can change the deployment choice independently of retrieval quality.

### Most discriminating experiment

Allocate equal query-format tuning budgets, freeze models and indexes, and report construction and query costs separately. Add a differently distributed corpus and approximate-search settings to test whether exact-search rankings persist under practical latency limits.

### Pair with

[beir](beir.en.md) · [bright](bright.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
