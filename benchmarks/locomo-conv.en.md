# LoCoMo-Conv: separating query framing, evidence recall and response quality

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-09-03<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2609.03467)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](locomo-conv.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Read main Sections 1–8 and Appendices A–H, including all prompts, human questionnaires, qualitative cases and stochastic-source tables; PDF extraction checked for prompt availability. Read pinned README and complete retrieval/compute_retrieval_metrics.py at 1925e924c36e632283ea91f2212157829f4e0e45. No full result-cache audit or independent run.

[arXiv 2609.03467v2 (2026-09-22)](https://arxiv.org/html/2609.03467v2)

[Auxiliary material (checked 2026-09-30)](https://github.com/MiuLab/LoCoMo-Conv/blob/1925e924c36e632283ea91f2212157829f4e0e45/README.md)

[Auxiliary material (checked 2026-09-30)](https://github.com/MiuLab/LoCoMo-Conv/blob/1925e924c36e632283ea91f2212157829f4e0e45/retrieval/compute_retrieval_metrics.py)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

LoCoMo-Conv directly inherits LoCoMo10 conversations, answers and evidence IDs, rewriting requests as explicit first-person dialogue, implicit situations, false premises and composed requests. Dialog/implicit each contain 1986 items; counterfactual excludes 446 unanswerable adversarial items, leaving 1540. The composed set contains 1069 source-QA pairs with overlapping but nonidentical evidence. Fixed history isolates changes in how retrieval targets are expressed.

Genealogy: This is actual LoCoMo data reuse, not merely a conceptual comparison. Unlike LoCoMo-Plus’s latent-constraint consistency, it preserves specific answers/evidence IDs and separately measures source retrieval and fact use. Those scores are not interchangeable measures of dialogue quality.
Illustrative rewrite: an explicit question about a previously mentioned hobby becomes a situation needing advice related to that hobby. History stays fixed, but the system must infer which personal fact the request needs.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

Five systems share all-MiniLM-L6-v2 embeddings and gemma-4-31B-it, retrieving ten memory units; answers use temperature zero and at most 300 tokens. AnchorMem units are chunks averaging 12.8 turns, so text budgets differ. Memora’s default 0.4 threshold is disabled because it otherwise returns nothing for 42–71% of conversational queries. Retrieval recall uses verbatim substring or metadata dia_id coverage, not guaranteed answer preservation in a summary. Dialog/implicit score fact use at 0/0.5/1; counterfactual scores unaware/hedged/corrected; composed scores atomic-fact coverage. GPT-5.4-mini rewrites and primarily judges; Claude-Opus-4.7 handles three-dimensional quality comparisons.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Table 4, selected retrieval-to-response contrasts

Scores are 0–1, with per-query recall averaging and partial-credit fact use. mem0 has higher implicit recall than AnchorMem but lower fact use; retrieved source IDs do not establish semantic preservation or use.

Published pools: 1986 dialog and 1986 implicit items. The inspected scorer aggregates processed cache records; exact completed per-row cache counts were not independently audited.

| System | Dialog recall | Implicit recall | Dialog fact use | Implicit fact use |
|---|---|---|---|---|
| AnchorMem | 0.659 | 0.368 | 0.598 | 0.364 |
| mem0 | 0.547 | 0.456 | 0.366 | 0.33 |
| Memora | 0.608 | 0.445 | 0.501 | 0.388 |

Locator: Table 4, selected retrieval-to-response contrasts · [Source](https://arxiv.org/html/2609.03467v2)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Table 4, selected query-rewriting effects

Same backbone/index; additional GPT-5.4-mini rewrites into 3–5 facets, searched separately and fused with RRF into ten results. Calls/candidates increase without matched-cost controls. Composed coverage differs from implicit fact-use scoring.

Published implicit pool 1986; composed release 1069 clusters. Main-table selected values are kept separate from Appendix H’s older 300-cluster sampling study.

| Configuration | Implicit recall | Implicit fact use | Composed recall | Composed coverage |
|---|---|---|---|---|
| AnchorMem baseline | 0.368 | 0.364 | 0.279 | 0.31 |
| AnchorMem + rewriting | 0.524 | 0.47 | 0.432 | 0.413 |
| mem0 baseline | 0.456 | 0.33 | 0.374 | 0.29 |
| mem0 + rewriting | 0.453 | 0.337 | 0.364 | 0.284 |

Locator: Table 4, selected query-rewriting effects · [Source](https://arxiv.org/html/2609.03467v2)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Appendix F Table 13, selected counterfactual prompt interventions

Identical top-ten memories with answer prompts changed; correction score is 0/0.5/1. Restating the user situation first hurts performance and citation selection recovers only part. This concerns the tested prompt, not all reasoning strategies.

1540 counterfactual items in the released pool; one greedy main run.

| System | Plain answer | Reasoning only | Reasoning + selection |
|---|---|---|---|
| AnchorMem | 0.653 | 0.49 | 0.523 |
| mem0 | 0.548 | 0.381 | 0.387 |

Locator: Appendix F Table 13, selected counterfactual prompt interventions · [Source](https://arxiv.org/html/2609.03467v2)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:result-4:START -->
## Appendix G Tables 15 and 18, selected human diagnostics

Three annotators, majority vote for categorical labels. The first row is a count; other rows are 0–1 proportions. Composed agreement is per-fact over 50 sampled items. Humans prefer oracle more often on relevance, so aggregate direction does not establish per-dimension CoT equivalence.

Sampling scopes appear in each row; validation covers subsets, not every generated rewrite.

| Check | Count or proportion | Sampled items |
|---|---|---|
| Implicit has no explicit question | 36 | 40 |
| Fact-use judge agreement | 0.72 | 50 |
| Counterfactual judge agreement | 0.76 | 50 |
| Composed judge agreement | 0.79 | 50 |
| Human relevance: CoT win | 0.12 | 50 |
| Human relevance: oracle win | 0.3 | 50 |

Locator: Appendix G Tables 15 and 18, selected human diagnostics · [Source](https://arxiv.org/html/2609.03467v2)
<!-- EVIDENCE:result-4:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

Silent-grounding analysis selects 332 implicit cases where oracle responses still omit the gold fact, then compares oracle, no-memory and three random nongold turns. It shows limits of explicit-fact scoring, not prevalence across all questions. Quality judging uses the memory available to each answer and rewards specific memory use, so information volume and judgment context can differ. supportive_memory is derived from successful CoT selections, not independent human-gold evidence. mem0–Memora differences also mix indexing, prompts and retained content, preventing compression-only attribution.

Table 4 AnchorMem composed recall rises .279→.432, a 15.3-point change, whereas prose says 14.7. Appendix H Table 20 explicitly uses the original 300 composed clusters and reports much lower scores than Table 4; its claim of matching the main table within 0.4 points does not hold for those cells. Do not attach those SDs to the expanded main results. Appendix F says 1112 flips and 175–195 per system despite five evaluated systems; the totals do not reconcile. The scorer skips missing caches and assigns zero to empty gold sets; coverage and category composition need explicit audit when reproducing. Sparse human samples and source-sharing between rewrites limit broad causal or significance claims.



Next: Retain existing rewriting, memory-off, random-memory and oracle controls on matched source questions/backbones/token budgets. Audit whether summaries preserve answer semantics separately from source-ID coverage. Use common evidence views for human quality comparisons, disclose completed row counts and keep the older 300-cluster variance study separate from expanded results.
<!-- EVIDENCE:limitations:END -->
