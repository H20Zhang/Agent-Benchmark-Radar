# EvoMemBench: separating update schedules from task capabilities

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-05-18<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2605.18421)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](evomembench.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Read main Sections 1–6 and Appendices A–C, including construction prompts, metrics, baseline applicability and all supplementary result tables. Inspected PDF Figure 3–4 heatmap labels and the official repository overview. No implementation audit, reconstructed-data count audit or independent execution.

[arXiv 2605.18421v2 (2026-06-15)](https://arxiv.org/html/2605.18421v2)

[Auxiliary material (checked 2026-09-30)](https://github.com/DSAIL-Memory/EvoMemBench)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

EvoMemBench crosses within-episode versus cross-episode scope with knowledge versus execution demands, instantiated as six suites. Self-evolution means updating external memory, not training model parameters. Within an episode, updates follow each information block or interaction turn. Across episodes, tasks sharing a background run sequentially and write experience back; independent contexts reset memory. Transfer first builds source-environment memory, then freezes it on the target.

Genealogy: Retention/revision directly reuse MemoryAgentBench retrieval and selective-forgetting tasks; tool tasks actually reconstruct BFCL; cross-episode knowledge derives from CL-Bench, with xbench, WebWalkerQA and ALFWorld also reused. The contribution is a unified update schedule across inherited tasks, not a new memory algorithm. For example, a later request refers to the directory just created without repeating its name, while preserving gold action order. Planning, tool use and evaluators remain involved, so failures cannot all be attributed to memory.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

The six reported pools total 5754 samples: InEp-Know 2800, InEp-Exec 800, CrossEp-Know 884, CrossEp-Tool 800, CrossEp-Web 270 and CrossEp-Emb 200. Fifteen memory methods share DeepSeek-V3.2. Gemini-3-Flash and GPT-5-mini are different-backbone long-context references, not controls isolating memory. Only applicable methods are evaluated, rather than a complete 15-by-6 matrix. Default embeddings are text-embedding-v4; retrieval uses ten units for knowledge and three for execution, without matching unit length or computation. InEp-Exec uses 16K/32K/64K/128K windows, preserving current input and memory while truncating early history. Knowledge uses answer accuracy; execution uses final-goal success. Progress separately averages passed checkpoints within each task and then across tasks. Token usage includes all input/output calls of both agent and memory module.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Table 3, selected retention and revision results

Same DeepSeek-V3.2 backbone. Revision columns are FactConsolidation categories, not physical-deletion checks. Better retrieval-task scores do not guarantee better conflicting-fact revision.

InEp-Know pools: 2000 accurate-retrieval and 800 selective-forgetting samples; these columns are different subsets, not four measurements on one common denominator.

| Method | EventQA accuracy % | LongMemEval S* accuracy % | Multi-hop revision accuracy % | Single-hop revision accuracy % |
|---|---|---|---|---|
| DeepSeek-V3.2 | 83 | 32.33 | 10 | 65 |
| BM25 | 88.8 | 50.33 | 7 | 54 |
| Mem0 | 79.2 | 52 | 7 | 49 |
| A-MEM | 91.2 | 51 | 5 | 35 |

Locator: Table 3, selected retention and revision results · [Source](https://arxiv.org/html/2605.18421v2)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Table 4, selected InEp-Exec context-budget results

Reported Overall success with the same backbone. Windows contain current input, memory and retained history; increasing them does not monotonically improve every method.

Table 2 reports 800 InEp-Exec samples, 200 per domain. Exact completed per-cell counts and repeated-run uncertainty are not printed; do not infer counts from rounded rates.

| Method | 16K success % | 32K success % | 64K success % | 128K success % |
|---|---|---|---|---|
| DeepSeek-V3.2 | 28.5 | 35.5 | 45.3 | 39.5 |
| BM25 | 36.5 | 44.5 | 47.2 | 40.5 |
| ReasoningBank | 43 | 49.5 | 47.1 | 48 |
| AWM | 31.5 | 43 | 53.1 | 35 |

Locator: Table 4, selected InEp-Exec context-budget results · [Source](https://arxiv.org/html/2605.18421v2)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Table 5, selected CrossEp-Know difficulty results

Sequential write-back within shared contexts; difficulty groups are tertiles of the DeepSeek-V3.2 baseline score. Overall values correspond to equal means across four domains, not pooled accuracy over 884 items. The zero Hard baseline is conditioned on that grouping.

120 contexts, 884 samples: domain knowledge 294, rules 257, procedures 306, empirical discovery 27. Exact per-domain difficulty-cell counts are not given.

| Method | Easy accuracy % | Medium accuracy % | Hard accuracy % |
|---|---|---|---|
| DeepSeek-V3.2 | 52.1 | 12.6 | 0 |
| BM25 | 47.2 | 13.8 | 10.1 |
| A-MEM | 43.8 | 10 | 6.7 |
| ACE | 44.8 | 16.5 | 13 |

Locator: Table 5, selected CrossEp-Know difficulty results · [Source](https://arxiv.org/html/2605.18421v2)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:result-4:START -->
## Tables 6 and 9, selected embodied performance-cost contrasts

Cross-episode experience on ALFWorld. Success columns are two categories; token usage is the sample-weighted mean across all six categories, not the cost of just those two subsets.

Clean & Place 37 tasks; Pick Two & Place 45; six-category token mean over the reported 200-task pool.

| Method | Clean & Place success % | Pick Two & Place success % | Mean total tokens |
|---|---|---|---|
| DeepSeek-V3.2 | 56.8 | 57.8 | 37175 |
| A-MEM | 81.1 | 84.4 | 57338 |
| ReasoningBank | 81.1 | 73.3 | 43609 |

Locator: Tables 6 and 9, selected embodied performance-cost contrasts · [Source](https://arxiv.org/html/2605.18421v2)
<!-- EVIDENCE:result-4:END -->

<!-- EVIDENCE:result-5:START -->
## Tables 4, 14, 15 and 16, selected 16K performance-cost controls

Same-backbone InEp-Exec at 16K. Progress credits partial completion while success requires the final goal. Steps/tokens include unsuccessful runs and are not cost per successful task.

Reported 800-task pool; per-cell completed counts and confidence intervals are unspecified.

| Method | Final success % | Progress % | Mean steps | Mean total tokens |
|---|---|---|---|---|
| DeepSeek-V3.2 | 28.5 | 50.9 | 12.59 | 74630 |
| BM25 | 36.5 | 57 | 13.58 | 109255 |
| ReasoningBank | 43 | 58.9 | 15.47 | 151345 |

Locator: Tables 4, 14, 15 and 16, selected 16K performance-cost controls · [Source](https://arxiv.org/html/2605.18421v2)
<!-- EVIDENCE:result-5:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

Results support task-, budget- and representation-specific choices rather than one best system or a single memory-capability score. Procedural methods, retrieval and compression jointly change content, prompting and computation without component-level causal isolation. Transfer heatmaps contain positive and negative changes, but alignment with the target decision process is an interpretation rather than a directly manipulated mechanism. Repeated seeds, intervals and complete temperature/output limits are not supplied, so small differences do not establish stable rankings. There is no common human or oracle-memory ceiling; different-model long-context references are not ceilings either.

The paper’s sample totals describe pools, not independently verified completed runs. Most tool-use percentages move in two-point increments, but that alone cannot establish a 50-task denominator or contradict the stated 200 per domain. Table 5 Overall numerically matches an unweighted four-domain mean despite unequal domain sizes; this aggregation qualification is necessary. Current README names BFCL_v4_multi_turn_ours files whereas Appendix A describes BFCL-V3-MultiTurn. This is a provenance detail requiring implementation reconciliation, not proof that every paper score used BFCL v4.



Next: Pair with MemoryAgentBench while holding tasks, backbone, prompts and visible tokens fixed; compare no update, raw-history retrieval and experience write-back. Repeat on difficulty groups defined in advance by another backbone, reporting common samples, seeds and cost. For transfer, retain no-memory, frozen source-memory and target-domain learning controls to separate generic context assistance from reusable experience.
<!-- EVIDENCE:limitations:END -->
