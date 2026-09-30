# MEMPROBE / MemAudit: what remains in memory after assistance

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-06-23<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2606.24595)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](memprobe.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated primary-paper version, method, setup, key results and limitations; no independent experiment reproduction.

Paper v2 substantive main text and Appendices A–K, including PDF prompts/cases; official reproduction and result documentation also checked.

[arXiv:2606.24595v2](https://arxiv.org/html/2606.24595v2) · [main@2026-09-30](https://github.com/sora1998/MEMAUDIT-bench/blob/main/docs/reproduction.md) · [main@2026-09-30](https://github.com/sora1998/MEMAUDIT-bench)

The tables reorganize selected sourced facts. The title-level historical reference may use a different version, split or model; do not pool scores across those settings.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Measurement, method and comparison

MEMPROBE is the June benchmark name; the September v2 paper is titled MemAudit. It is distinct from the other September MemProbe stability–plasticity paper. An agent first assists a simulated user with ordinary tasks. Its final memory is then frozen and probed for hidden structured user state through full-store access or top-5 retrieval per target, separating immediate assistance from what can later be reconstructed.

[Primary source](https://arxiv.org/html/2606.24595v2)
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and denominators

There are 50 simulated users with 31 targets each, 1,550 targets in total, and a 25-turn interaction cap. Reconstruction reading/judging uses GPT-5.4-mini. B averages within categories then equally across five categories; it is not pooled binary accuracy over all targets. SD is across-user standard deviation, not a confidence interval. The published Mem-T condition is memt_memonly: Mem-T-4B handles memory while the shared backbone provides final answers.

[Setup source](https://arxiv.org/html/2606.24595v2)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Same final store, different access

Paper v2 Table 2, 50 users × 31 targets; five-category-balanced recovery, probing the same final store from one trajectory through full-store or top-5 access.

| System | Full-store B (0–1) | Full-store SD | Top-5 B (0–1) | Top-5 SD |
|---|---|---|---|---|
| amem | 0.611 | 0.062 | 0.54 | 0.062 |
| longctx_full | 0.624 | 0.067 | 0.503 | 0.075 |
| mem0 | 0.613 | 0.06 | 0.473 | 0.079 |

Both full-store and retrieved access can lose recovery, but not all loss is storage deletion: representation, readout, queries and truncation contribute. Even longctx_full's verbatim transcripts do not yield perfect recovery.

Fact source: v2 Table 2 · [Source](https://arxiv.org/html/2606.24595v2)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Immediate completion and durable recovery differ

No-memory control from v2 Table 2; completion and category-balanced recovery have different targets/aggregation and are not interchangeable.

| Configuration | Task completion (%) | Full-store B (0–1) |
|---|---|---|
| nomem | 99.935 | 0.0 |

The diagnostic point is that near-complete ordinary assistance does not establish preserved user state. An unreported no-memory top-5 value must not be filled with zero.

Fact source: v2 Table 2 · [Source](https://arxiv.org/html/2606.24595v2)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## Limitations, remaining gaps and next experiment

Recovery is rubric-scored reconstruction, not direct pure storage fidelity. Synthetic users, disclosable-trait selection and diverging trajectories limit generalization and attribution. Mem-T full-store access overflows context and is not a fair worst-memory ranking: v2 reports 0.130±0.251, while the README gives 0.131±0.251, an unresolved source discrepancy. Mem-T can use up to six ReAct search steps rather than one nearest-neighbor pool. The official guide distinguishes the current main simulator from archived paper-v1 artifacts; a new main run is not an original-experiment replay. Compared with downstream success alone, the contribution is memory-artifact auditing. Next, fix transcripts/store/read budget and pair recovery with later personalization. Keep the title's initial-release reference separate from these v2 results.

[Primary evidence](https://arxiv.org/html/2606.24595v2)
<!-- EVIDENCE:limitations:END -->

<!-- RESEARCH-DECISION:START -->

Use the method, comparisons and limitations together to decide whether this benchmark fits a claim. These tables are not a cross-protocol leaderboard; structural checks do not certify factual correctness or reproduction.

Related measurements and controls: [LoCoMo](locomo.en.md) · [LongMemEval](longmemeval.en.md) · [MemProbe (stability–plasticity)](memprobe-stability-plasticity.en.md)

<!-- RESEARCH-DECISION:END -->
