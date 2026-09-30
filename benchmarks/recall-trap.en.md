# Recall Trap: file coverage versus repair success under fixed context slots

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08-10<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2608.14838)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](recall-trap.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked selected results; no independent experiment reproduction.

Read all twenty-four pages, statistics and validity discussion, and Appendices A–D covering artifact handles, registration chronology, incompatible models and the fifteen-entry hypothesis registry; visually checked the result tables on pages 10 and 12. The archive was not executed and commit chronology was not independently audited.

[arXiv 2608.14838v1 · 2026-08-14](https://arxiv.org/pdf/2608.14838v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

SWE-bench Verified issues and retrieved code occupy twelve fixed chunk slots. A model emits SEARCH/REPLACE edits once; edits are applied to isolated pristine repositories and graded by the official Docker tests. For an illustrative boundary-condition fix, ON keeps only the highest-ranked chunk per file, covering about twelve files; OFF retains the raw ranking, giving several chunks from about five files. ON may find the correct filename while OFF exposes the function body needed to edit it. This estimates the total packing-policy effect. A shared candidate pool and ranker do not imply identical served ranks, content or token counts.

Editorial placement: the closest methodological predecessors include Levy et al.’s fixed-length multi-document study and eRAG’s task-based retrieval evaluation; the paper credits RGFL for the right-file/wrong-lines failure mode. The added coordinate is a within-service file-deduplication intervention scored by executable repair tests, rather than a new universal recall paradox. It complements ContextBench’s cross-system correlations, while jointly changing file count, depth, positions and distractors rather than identifying one exclusive mediator.

[Source](https://arxiv.org/pdf/2608.14838v1)
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

The main retriever fuses Qwen3-Embedding-8B, lexical and graph signals. Chunking, embeddings, ranking weights and slot count are held fixed. Generation is single-shot, tool-free, temperature 0.2, with 6000 output tokens for non-reasoning arms; repaired DeepSeek runs use 16000 with a requested 2000-token reasoning cap. Qwen’s 32000 amendment and reporting ambiguity are discussed below. Empty patches and retained harness errors count as failures; never-generated instances are excluded pairwise, giving model-specific n. Resolve rate is test-passing tasks divided by paired n, with paired McNemar tests and repository-cluster intervals. Mean ON/OFF inputs are 1451/1525 tokens: slots, not tokens, are fixed. Anchor dose uses gold pre-image patch lines and is a retrospective diagnostic, not an answer-free deployment signal.

[Source](https://arxiv.org/pdf/2608.14838v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Effect size and evidence boundaries for the same packing switch

SWE-bench Verified, twelve slots, one tool-free completion, official executable tests; empty patches remain failures. Absolute cross-model scores are not a capability ranking. DENSE-1’s interval includes zero. Denominators are paired n, not submitted patches only.

| Model/retriever | Paired n | ON resolved (%) | OFF resolved (%) | OFF−ON (pp) | Repository-cluster 95% CI (pp) |
| --- | --- | --- | --- | --- | --- |
| gpt-5.6-sol / fusion | 500 | 39.2 | 46.8 | +7.6 | [+0.8, +13.1] |
| Qwen3.6-27B / fusion | 499 | 9.2 | 12.8 | +3.6 | [+0.9, +4.9] |
| gpt-5.6-sol / DENSE-1 | 494 | 41.5 | 47.2 | +5.7 | [−0.9, +8.6] |

Source location: Section 5.1 and Figure 2, PDF pp. 10–11 · [Source](https://arxiv.org/pdf/2608.14838v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Retriever and tool boundaries constrain generalization

BM25 remains twelve-slot single-shot, with clustered CI [−5.8, −0.3]. Read-enabled execution permits ten turns and further file reads; McNemar p=0.45, 80%-power MDE 4.5 pp. Models and harnesses differ, so absolute rates are not comparable and nonsignificance is not exact equivalence.

| Condition | Paired n | ON resolved (%) | OFF resolved (%) | OFF−ON (pp) |
| --- | --- | --- | --- | --- |
| gpt-5.6-sol / BM25 / single-shot | 500 | 37.2 | 34.0 | −3.2 |
| sonnet-5 / fusion / Read-enabled | 499 | 65.9 | 64.5 | −1.4 |

Source location: Sections 5.3, 5.5 and 6.2, PDF pp. 12,14,18 · [Source](https://arxiv.org/pdf/2608.14838v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, limitations and next experiment

The central gpt and Qwen contrasts remain positive under repository clustering and both-nonempty conditioning. DeepSeek’s conditional p=0.49 shows material patch-producibility involvement; DENSE-1’s clustered interval crosses zero. The BM25 reversal rules out a universal fewer-files law. Read-enabled agents do not show the same effect, but models also change, preventing a tool-only causal attribution. Gold-line coverage, distractor removal and chunk contiguity remain entangled. Random per-file chunk selection is worse, rejecting a bad-argmax explanation without separating file-set membership from depth. SWE-PolyBench gives only +2.59 pp over 617 model–instance pairs, p=0.056; gold validity also misses the preregistered 95% floor, so this is not confirmed multilingual generality.

Index-evaluation recall 0.666→0.817 is distinct from gold-file presence in served packs: ON=0.878 and OFF=0.806. Original gpt responses were not logged; its apply-stage funnel comes from a separately preregistered replication, whose +6.4 pp must not replace the original +7.6 pp. Figure 2 broadly labels confirmation preregistered, but Appendix B qualifies original gpt/DeepSeek timing as same-day design commits supported by logs; DENSE-1 was designed after observing the primary effect. Section 4.3 says both Qwen arms were regenerated at 32K, while Section 5.9 describes K=12 as a lower-budget/high-empty regime. We therefore do not join K=4,12,40 into one matched curve.

Hold file sets, token count and positions fixed while manipulating within-file depth, contiguity and gold-line exposure separately; add budget-matched parent expansion and larger-chunk controls. Use a same-model single-shot/Read-enabled factorial and post-cutoff, cross-file repairs. Report task success, empty-patch rates, actual input costs, repository-cluster intervals and per-instance exclusion reasons together.

[Source](https://arxiv.org/pdf/2608.14838v1)
<!-- EVIDENCE:limitations:END -->
