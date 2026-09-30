# WANDR: large-scale discovery, enrichment and record-level evidence verification

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-07-14<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2608.14747)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](wandr.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked selected results; no independent experiment reproduction.

Read all forty-five pages and Appendices A–J, including task creation/admission, identity resolution, scoring pseudocode and worked trees, costs, detailed failures, delivery ablations and RL caveats; visually checked Tables 3–4 and the page-41 scoring tree. No live research runs or refetching of benchmark evidence.

[arXiv 2608.14747v1 · 2026-08-14](https://arxiv.org/pdf/2608.14747v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

Five hundred tasks abstract reusable shapes from de-identified product requests, then pass author/critic loops, executability/difficulty checks, a near-quota feasibility witness merged from ten to twelve runs, sampled judge audits and optional human sign-off. The witness is not an answer key. Leaf records contain identifying keys, URL, excerpts and a structured claim. For example, seventy companies need appointment evidence plus a listing-status source for each same company, requiring at least 140 leaves rather than any 140 rows. Canonicalization and semantic identity deduplication align branches; subtask scores multiply at shared keys, so a missing branch can zero an entity. Median quotas are one hundred core members and 245 records. Tasks are curated stress cases, not random deployment requests.

Editorial placement: close collection predecessors are WideSearch and DeepWideSearch, using cell/table evaluation and human gold sets. WANDR makes entity/subtask requirements recursive and replaces exhaustive answer enumeration with live-source verification. The added coordinate is repeated investigation and evidence completion per entity. It complements DRACO’s report evaluation, but its recall is quality-adjusted quota completion, not recall over every qualifying real-world entity.

[Source](https://arxiv.org/pdf/2608.14747v1)
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

Evaluation uses GPT-5.4: low effort for fetch triage/canonicalization, medium for judgment and high for deduplication, with browser retries for problematic pages. Full leaf success requires a usable page, clear claim, faithful excerpts, valid identity, every requirement satisfied by the page and every requirement supported by excerpts alone. Retrieval-only checks page-level satisfaction. Only leaves at ordinal confidence levels 2 or 3 are used; lower-confidence leaves are missing: omitted from precision but potentially reducing quota recall. Soft precision averages supplied children. Recall takes the worst duplicate-identity score, retains the best required number of distinct members and zero-pads shortfalls. Hard recursively thresholds incomplete scores; subtask multiplication and dispatch averaging remain. F1 is computed per task and then equally averaged, not reconstructed from headline mean precision/recall. Six production systems each run once with unmatched models, interfaces, tools, delivery channels and budgets; terminal errors after retries remain zero in the five-hundred-task denominator.

[Source](https://arxiv.org/pdf/2608.14747v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Substantial losses remain in evidence quality and quota completion

One run per five hundred tasks, full verdict, zero-filled terminal errors and equal task weighting. Matching model names do not match system stacks. Costs are historical solver charges, latency excludes verification, and neither is current pricing or budget matching. Perplexity uses file sharing; the other two use sandbox files.

| System / main configuration | Completed / 500 | Soft F1 (0–1) | Hard F1 (0–1) | Solve cost (USD/task) | Median solve latency (min) |
| --- | --- | --- | --- | --- | --- |
| Perplexity / GPT-5.5 high / Search as Code | 500 | 0.363 | 0.133 | 5.20 | 14.9 |
| Anthropic / Opus 4.8 high / Managed Agents | 500 | 0.249 | 0.072 | 46.43 | 73.7 |
| OpenAI / GPT-5.5 high / Responses API | 499 | 0.121 | 0.035 | 0.50 | 8.6 |

Source location: Tables 3–5, PDF pp. 15–16 · [Source](https://arxiv.org/pdf/2608.14747v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Higher effort does not uniformly help on the same forty-five tasks

Same forty-five scheduled tasks with each system’s selected delivery route. Perplexity xhigh completes 44/45; others 45/45, while scores/costs retain denominator forty-five. No repeat-run variance; identically named effort is not a common compute budget.

| System/effort | Soft F1 (0–1) | Hard F1 (0–1) | Solve cost (USD/task) |
| --- | --- | --- | --- |
| Perplexity / high | 0.397 | 0.156 | 4.75 |
| Perplexity / xhigh | 0.447 | 0.224 | 7.32 |
| OpenAI / high | 0.153 | 0.073 | 0.49 |
| OpenAI / xhigh | 0.127 | 0.060 | 0.74 |

Source location: Tables 6–7, PDF p. 18 · [Source](https://arxiv.org/pdf/2608.14747v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, limitations and next experiment

Perplexity’s profile is consistent with programmable fan-out, persistent candidate state and quota backfilling, but does not causally isolate these mechanisms. Its solver shares the grader’s first fetch backend, creating possible accessibility alignment. Live-page drift, missing dynamic content and LLM identity/evidence judgments affect scores. Best hard F1=0.133 is not a 13.3% whole-task pass rate; it averages member-based task scores. Structural depth/volume covary with content difficulty. The forty-five-task delivery ablation uses independent stochastic runs rather than deterministic pairs, so file-output advantages also include rollout variation. The RL section proposes a training substrate without measuring training gains.

The prose loosely describes hard precision as complete-member credit, but Appendix G applies quota zero-padding only to recall. In Appendix H, Delhi submits one of two required heritage sites yet has hard/soft precision 1/1 and recall 0/0.5. Quota completeness therefore requires hard recall, not hard precision alone. Headline scores zero-fill all five hundred scheduled tasks; diagnostics use different available-detail subsets, including only 350 Parallel tasks, and are not an unbiased complete decomposition. The manuscript is dated July 16 while arXiv v1 is August 14; the registry’s July 14 is not automatically arXiv publication.

Match model, search/fetch backend, total cost and token budget while randomizing code orchestration, parallel search, explicit quota state and backfilling; repeat paired runs. Freeze evidence snapshots and audit with independent fetchers/humans, separating unassessable leaves and missing diagnostics. Report quota completion, all-condition support, faithful/complete excerpts and estimated real-set coverage separately; test over-submission, alias padding and cache artifacts.

[Source](https://arxiv.org/pdf/2608.14747v1)
<!-- EVIDENCE:limitations:END -->
