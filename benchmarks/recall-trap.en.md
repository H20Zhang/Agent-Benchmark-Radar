# The Recall Trap: RAG / retrieval validity

[中文](recall-trap.md) | **English** · [Back to the entry](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2608.14838) · [Reproduction artifact](https://doi.org/10.5281/zenodo.21879550)

Audits the proxy assumption that higher recall is better using downstream executable outcomes.

## What It Follows

Earlier evaluation usually compressed this problem into a shorter final score or a single proxy. This object turns its predecessor critique into an explicit capability × environment × protocol delta and retains an executable or auditable artifact.

## How It Is Evaluated

**Question:** Under fixed context slots, does higher file recall actually improve issue resolution?

**Measurement object:** Validity audit showing that higher file recall can reduce downstream repair success under a fixed-slot code-retrieval protocol.

**Scale and protocol:** Paired fixed-pack evaluations on SWE-bench Verified with an open-weight preregistered replication. The protocol includes paired-dedup-ablation, official-docker-grading, repository-clustered-inference.

## What a Score Can Support

Paired fixed-pack evaluation with official Docker grading shows that higher recall can coincide with a lower resolve rate for dense retrieval, with an open-weight replication. It supports system-level evidence under this environment, harness, model/tool, and resource configuration; unmatched variables prevent attribution to one component.

## Strongest Confounder

The compound dedup treatment changes breadth, depth, rank, position, tokens, and distractors together; the causal result is limited to fixed slots. The load-bearing confounders are compound-packing-treatment, fixed-slot-context, single-shot-no-tools-harness.

## What It Still Does Not Measure

The dedup flag changes breadth, depth, rank, position, token count, and distractors together in a single-shot no-tools harness.

## Where It Fits in the Map

`map_delta=reinforces`. One paper is only a signal; a durable direction needs independent records bound to the same canonical direction key.
