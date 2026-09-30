# SearchAuditBench: separating failure diagnosis from repair-guided recovery

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2026-08 · paper v1<br>
> **SearchAuditor / GPT-5.5 — Full Pass Score (FPS): 32.26%**; **SearchAuditor / GPT-5.5 — CS-Strict: 44.89%**<br>
> Best trajectory-auditing configuration in Table 2; FPS grades a complete audit and CS-Strict the critical step, not search-answer success. [Original source](https://arxiv.org/html/2608.05212v1)<br>
> Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.
<!-- RELEASE-REFERENCE:END -->

[中文](searchauditbench.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked selected results; no independent experiment reproduction.

Read Sections 1–6 and Appendices A–G across thirty-three pages, including exclusions, annotation rules, cost, blinded grader validation, both full cases and five auditing prompts; visually checked Tables 2–4.

[arXiv 2608.05212v1 · 2026-08-05](https://arxiv.org/pdf/2608.05212v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

Eight open-weight search models run a shared Search/Visit scaffold on five benchmarks. From 3,500 raw traces, gradable incorrect runs are retained after excluding bad references, corrupted traces, offline-unidentifiable environmental failures and cases lacking a single critical cause, leaving 1,243. Four author annotators split the cases, one labeler per case, with Claude Opus 4.6 proposing candidate error regions. Auditors know the final answer failed but receive no gold answer or web access. SearchAuditor combines holistic, backward-constraint and forward-timeline branches, adjudicates with trace windows and writes a repair. One case recognizes a perfect-cube requirement but substitutes a familiar sum-of-cubes puzzle and outputs 1729; repair must restore the mathematical constraint rather than reveal the target answer.

Editorial placement: AgentRx is the closest diagnostic-framework comparison, while underlying tasks such as BrowseComp primarily supply final-answer correctness. SearchAuditBench adds critical-step, root-cause and process-repair supervision, then separately links repairs to actual resumption. This is not yet early online detection when failure is unknown.

[Source](https://arxiv.org/pdf/2608.05212v1)
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

GPT-5.5, Gemini-3.1-Pro and Claude-Opus-4.8 are evaluated with high effort and the same backbone across auditing stages. CS-Strict requires the exact critical assistant message; CS-Loose permits its annotated span. Diag requires loose localization and the correct cause. DeepSeek-V4-Flash checks three to five expert repair criteria per case. Rep@Diag uses only correctly diagnosed cases, whereas FPS uses all cases. A blinded validation of two hundred diagnosis-passing outputs obtains 82.5% case-level agreement, not end-to-end annotation agreement. Main total budgets and repeated-run uncertainty are incompletely specified; the cost study permits model and transport retries, so five nominal stages need not mean exactly five calls.

[Source](https://arxiv.org/pdf/2608.05212v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Offline auditing with GPT-5.5 fixed

All 1,243 auditable failures; Rep@Diag alone uses each method’s correctly diagnosed subset, while other columns use all cases. FPS requires both sound diagnosis and every repair criterion. This table does not rerun the original search tasks.

| Audit method | CS-Strict (%) | Diag (%) | Rep@Diag (%) | FPS (%) |
| --- | --- | --- | --- | --- |
| All-at-Once | 38.29 | 32.90 | 80.68 | 26.55 |
| SearchAuditor | 44.89 | 38.05 | 84.78 | 32.26 |

Source location: Table 2 and Section 5.1, pp. 5–6 · [Source](https://arxiv.org/pdf/2608.05212v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Actual resumption: failure repair and overall accuracy

335 LiveBrowseComp questions; generating agents Kimi-K2.6 and Quest-35B, auditor GPT-5.5. Fix-rate denominators are 213/300 gradable failures; both overall denominators are 335, with original accuracy 34.03%/8.96%. Generic hints use SearchAuditor’s predicted location. Retries start fresh while repairs retain prefixes, differing in compute and context.

| Intervention | Kimi fix rate (%) | Kimi overall accuracy (%) | Quest fix rate (%) | Quest overall accuracy (%) |
| --- | --- | --- | --- | --- |
| Unguided retry | 9.39 | 40.00 | 5.00 | 13.43 |
| Generic hint | 5.63 | 37.61 | 4.67 | 13.13 |
| SearchAuditor repair | 17.37 | 45.07 | 10.33 | 18.21 |

Source location: Section 5.4 and Table 4, pp. 6–7 · [Source](https://arxiv.org/pdf/2608.05212v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Audit-perspective control under the stated matched compute

Random three-hundred-case subset with GPT-5.5 and the same three-stage pipeline. The paper defines three holistic copies as matched compute; these scores differ from the full-1,243 result. This more directly tests audit perspective than cross-backbone/call-budget comparisons, but repeat intervals are absent.

| Configuration | CS-Strict (%) | FPS (%) |
| --- | --- | --- |
| Full H+B+F | 49.00 | 31.67 |
| Three holistic audits | 46.00 | 27.33 |

Source location: Table 3 and Section 5.3, p. 6 · [Source](https://arxiv.org/pdf/2608.05212v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, limitations and next experiment

Selecting only failures with one offline-identifiable cause excludes some environmental and multi-cause cases. Evidence-use-versus-retrieval proportions characterize this corpus, not all search failures. Actual recovery is tested separately: 213 Kimi and 300 Quest gradable failures on another benchmark resume from predicted critical steps with repairs; non-gradable runs still count as incorrect in overall accuracy. SearchAuditor beats retries and a generic hint at the same location, but added auditing compute is not fully matched against larger retry budgets, and failure is known. On one hundred cases, GPT-5.5 auditing averages 214.1 seconds/275.6K input tokens versus 38.5 seconds/68.9K for All-at-Once, a genuine quality-cost trade-off.

The original note treated actual rerun utility as future work, but Section 5.4 already performs repair-guided resumption on LiveBrowseComp. FPS remains offline diagnosis/repair-rubric success and is distinct from recovery. Appendix E measures cost on one hundred cases while Table 9 copies FPS from all 1,243, not the same cost-quality sample. A shared grader does not automatically eliminate differential error across output styles.

Test online triggering on unfiltered successful, failed and environmentally blocked traces, reporting false alarms, harmful corrections and final success. Match total tokens/time including auditing against multiple fresh retries and diagnosis-free rollback. Independently double-annotate critical steps/causes and quantify reference/grader uncertainty.

[Source](https://arxiv.org/pdf/2608.05212v1)
<!-- EVIDENCE:limitations:END -->
