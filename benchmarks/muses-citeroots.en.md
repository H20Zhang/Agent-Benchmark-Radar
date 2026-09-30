# MUSES / CiteRoots

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08-31<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2609.00313)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](muses-citeroots.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Sections 1–5, prospective contract, familiarity/function axes, all comparisons and limitations; appendices inspected: A–D, complete release funnel, rhetorical taxonomy/prompt/human guide/distillation, endorsement outreach and training/reranking recipes. Not performed: No release-code audit; incompatible cohort/ceiling statements remain unresolved

[arXiv 2609.00313v1 — arXiv 2609.00313v1; PDF margin 2026-08-31](https://arxiv.org/pdf/2609.00313v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Unlike SAGE/AutoResearchBench retrieval from explicit current requests, MUSES predicts future citations from prior author trajectories, separating citation behavior, local rhetoric and author endorsement. It adds prospective discovery and familiarity control rather than generic relevance; changing cohorts across layers require separate interpretation.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

MUSES builds last-author publication trajectories from S2ORC dated 2026-03-10. Given pre-time-t history, it predicts which existing papers enter a subsequent bibliography. A fixed 2,330,779-paper pool is filtered per instance to publication≤t. The 1,038,780 instances use author-disjoint career-midpoint splits of 687,624/182,543/168,613. CiteNext contains future citations; CiteNew removes previously cited works; CiteNew-Isolated additionally removes five-year coauthor-exposure targets. CiteRoots separately measures local citation rhetoric and retrospective author-confirmed inspiration. Of six rhetorical roles, theoretical foundation, method extension and generative motivation are roots; comparison, tools and background are not. At least one linked root-labeled passage makes a focal-to-candidate edge positive.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

Retrieval receives historical titles/abstracts, never future text, bibliography or author responses. MC-SPECTER2 embeds history with unfine-tuned specter2_base, clusters into K=16 and scores candidates by maximum centroid cosine. BM25 uses Pyserini k1=0.9, b=0.4; candidate encoding costs about 48 A100-80GB hours. BGE trains three epochs and the sequence model five. Both rerankers start from the MC top thousand; greedy Qwen2.5-14B processes twenty candidates per page and merges within-page ranks. Hit@k means at least one target, not target recall. GPT-5.4-mini at medium effort is the rhetorical teacher, distilled into Qwen3-8B for release labeling; teacher κ0.896 does not validate every student label. Author endorsement shrinks from 1,518 pairs/753 papers to 402 in-pool pairs/134 papers, including 145 habitual and 257 novel pairs.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Retrieval under familiarity restrictions

Denominators are 168,613/167,568/166,180 author–paper instances. Zero-to-one any-hit rates use the fixed 2,330,779 pool with time filtering. Empty-target removal slightly changes cohorts across tiers; these are not citation-count recall.

| Retriever | CiteNext Hit@100 | CiteNew Hit@100 | Isolated Hit@100 |
|---|---|---|---|
| BM25 | 0.307 | 0.248 | 0.217 |
| Single-centroid SPECTER2 | 0.447 | 0.347 | 0.296 |
| MC-SPECTER2 K=16 | 0.534 | 0.424 | 0.366 |

Source: Table 1 · [Paper](https://arxiv.org/pdf/2609.00313v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Endorsed-cohort multi-centroid gains are not uniform

402 endorsed target pairs across 134 papers, including 145 habitual and 257 novel pairs; all metrics zero-to-one. Do not mix this with the body’s 0.171 on novel pairs only. K16 leads Hit@100, while K8 has higher Hit@1000 and single-centroid higher MRR.

| History retriever | Hit@10 | Hit@100 | Hit@1000 | MRR |
|---|---|---|---|---|
| Single centroid | 0.102 | 0.201 | 0.346 | 0.051 |
| Multi centroid K=8 | 0.109 | 0.234 | 0.376 | 0.044 |
| Multi centroid K=16 | 0.122 | 0.251 | 0.371 | 0.046 |

Source: Table 14 · [Paper](https://arxiv.org/pdf/2609.00313v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

MC retrieval reaches 0.424 Hit@100 on broad CiteNew,0.205 on rhetorical CiteNew and 0.171 on novel endorsed pairs, but cohorts and scoring units change. The 3.1-fold headline decline is not a same-question controlled intervention. Last-author history proxies public citation behavior, not complete reading or inspiration. Teacher agreement of κ0.896 with human rhetoric but κ0.037 with endorsement suggests distinct constructs; because unselected author items are not negatives, endorsement-recovery negative-label provenance and denominators need clarification.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

Candidate-date filtering does not prove that pretrained encoders never saw future citation structure; time filtering of global citation counts/coauthor edges needs verification. Career-midpoint splits are not simple paper-year splits, and last-author conventions vary across fields. The response-conditioned endorsement sample is not an influence census and misses uncited or conversational inspiration. Teacher/student agreement, the 1,900-context audit and 1,202-context model-selection subset must remain distinct; selection on human labels is not a fresh blind test. Next use matched-question/target-count nested comparisons, publish eight-method audit scope, reranker output lengths and temporal edge filtering, and validate on independent endorsements.

Abstract/early text says roughly 140K test instances per tier, whereas Tables 4 and setup report 168613/167568/166180. Use explicit table cohort counts. Prose claims benchmark instances unchanged along the functional climb, but rhetorical scoring uses 5702/4483 nonempty instances and endorsement uses 257 or 402 pairs; broad denominators are approximately 167K instances. Table 10 reports 47.8% CiteNext unsolved by all at K=1000, implying union hit 52.2%, while Table 15 reports MC-SPECTER2 hit 67.6% on the full CiteNext set. Cohort/method inclusion differences must be reconciled before calling this a shared hardness ceiling. Broad CiteNew mean 13.8 targets uses the full release, while rhetorical density 0.0405 divides test positive edges by all broad test instances; this is not the mean target count in the scored 5702-instance rhetorical cohort. Reranker h@1000 is far below the unchanged MC top 1000 membership in rhetorical tables; if all candidates were retained, reranking alone would preserve coverage. Output filtering/truncation/validity behavior is not explained sufficiently. Endorsement appendix time origin refers to the focal paper while broad prose predicts its next paper; exact instance alignment needs release-code verification.
<!-- EVIDENCE:limitations:END -->
