# MAPLE: RAG / multi-aspect scientific retrieval

[中文](maple.md) | **English** · [Back to the entry](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2608.15624) · [Code](https://github.com/Ggballs/MAPLE) · [Data](https://huggingface.co/datasets/kai-02/MAPLE)

Splits single-query relevance from consistent retrieval of one paper across motivation, method, and result aspects.

## What It Follows

Earlier evaluation usually compressed this problem into a shorter final score or a single proxy. This object turns its predecessor critique into an explicit capability × environment × protocol delta and retains an executable or auditable artifact.

## How It Is Evaluated

**Question:** Can a retriever recover the same target paper across queries about different aspects?

**Measurement object:** Scientific retrieval benchmark that measures whether one paper remains retrievable across motivation, method, and result aspects.

**Scale and protocol:** 2,095 queries over 210 positive papers, 73,973 corpus papers, and 23,739 hard negatives. The protocol includes allaspect-at-k, anyaspect-at-k, aspect-coverage, matched-single-query-control.

## What a Score Can Support

Across 2,095 queries and 210 papers, the matched single-query recall versus AllAspect gap shows how one-hit relevance hides cross-aspect failure. It supports system-level evidence under this environment, harness, model/tool, and resource configuration; unmatched variables prevent attribution to one component.

## Strongest Confounder

Generated queries, a single domain, and model-validated hard negatives can introduce style bias and label noise. The load-bearing confounders are llm-generated-queries, single-domain-corpus, hard-negative-label-noise.

## What It Still Does Not Measure

Generated questions, similarity selection, one ICLR-style domain, and model-validated negatives can create style bias and false negatives.

## Where It Fits in the Map

`map_delta=reinforces`. One paper is only a signal; a durable direction needs independent records bound to the same canonical direction key.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use MAPLE to test whether a paper is consistently discoverable through motivation, method, and result aspects. Any-aspect success differs from all-aspect success. Average recall can hide a representation that encodes only the most salient aspect.

### What a concrete task looks like

Illustrative task: several information needs target the same paper through its motivation, method structure, or experimental finding. Retrieval should identify the work across these expressions, not only when the query resembles its title.

### Most discriminating experiment

Pair evaluations by paper and report any-aspect, all-aspect, and per-aspect coverage under a fixed representation budget. Compare one summary, multi-aspect representations, and full-text indexing, reviewing hard negatives to avoid inflated differences from false-negative labels.

### Pair with

[bright-pro](bright-pro.en.md) · [sage](sage.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->


## Remaining gap and next validation

What remains unmeasured is stability across settings and transfer to realistic workflows. The next experiment should hold model and budget fixed and add deployment-like tasks to test whether gains come from the target capability itself.

## What changed relative to precursors

Compared with precursors on the same research line, its value is the newly explicit task boundary described above. The meaningful comparison is the added measurement coordinate, not dataset size alone.