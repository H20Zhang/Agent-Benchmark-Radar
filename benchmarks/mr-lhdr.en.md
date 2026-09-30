# Mr.LHDR

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-09-10<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2609.11318)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](mr-lhdr.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Sections 1–6, Node-Relation construction, metrics, main results, ablations and validity limits; appendices inspected: A–H, complete interfaces/workflow, statistics, model routes, judge prompt, all uncertainty/stratum tables, three full case studies and release statement. Not performed: No code rerun, hidden-DAG audit, human rejudgment or live-source verification

[arXiv v1, 2026-09-10](https://arxiv.org/pdf/2609.11318v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Compared with MM-BrowseComp’s shorter checklists and MC-Search’s local evidence paths, Mr.LHDR gates intermediate statements by prerequisites in open-web tasks. It measures dependency-consistent submitted conclusions; citation and trace evidence are still needed to verify the actual research process.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

Six graduate-level researchers construct entity–relation graphs, use AI to expand candidates and manually prune/audit them into 102 open-web short-answer tasks across eight categories with 1,231 intermediate conclusions. Each has ten to twenty-one conclusions, mean 12.1; the longest prerequisite path averages 10.4 nodes. Every item has annotated state-changing nontext evidence; 101 attach an image and one relies on nontext source URLs. Models see only questions and available images, not gold answers/checklists/sources/DAGs. OA scores final answers; SA additionally requires every checklist conclusion; CS averages within-question coverage. DACS credits a stated conclusion only when it and all transitive prerequisites are correctly stated, preserving independent-branch credit.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

Twenty-five systems run from 2026-04-30 through 05-05 via OpenRouter or DeerFlow, one request per item without an added system prompt or explicit sampling settings; browsing occurs inside services. Token/tool/latency budgets are unmatched. Groups comprise eleven image-plus-search configurations, seven image-only, four research endpoints and three DeerFlow backends. Research endpoints receive image URLs in text rather than inline image bytes, preventing interface equivalence. The main Qwen3-VL-235B-A22B-Instruct-FP8 judge sees question/reference/checklist/response without source verification. Missing/failed runs score zero with denominator 102. Ten thousand item bootstraps estimate uncertainty; twelve-model rejudging has no human-label calibration. DACS therefore measures dependency consistency of submitted statements, not actual browsing or latent reasoning.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Final answers versus dependency-consistent statements

Fixed 102 items, failed runs zero. CS/DACS first average within items then across items, not micro-average 1,231 nodes. Input/tool budgets differ. GPT-5.5 OA 95% interval is[33.3,52.9], SA[25.5,44.1]; nearby ranks need caution.

| System / route | OA percent | SA percent | CS percent | DACS percent |
|---|---|---|---|---|
| GPT-5.5 / search+image | 43.1 | 34.3 | 73.6 | 70.3 |
| Gemini3.1 Pro / image-only | 34.3 | 31.4 | 73.2 | 70.1 |
| o3 Deep Research / image URL | 32.4 | 19.6 | 56.1 | 49.8 |

Source: Tables 4 and 9 · [Paper](https://arxiv.org/pdf/2609.11318v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Paired image ablation and uncertainty

Qwen3-VL-235B directly answers the same 102 tasks, not the DeerFlow arm. Same questions/judge with 10,000 paired item bootstraps. All twelve judges give positive DACS gains but only seven positive SA gains; reference artifacts stay fixed.

| Metric | Image withheld percent | Image supplied percent | Gain pp | 95% paired CI pp |
|---|---|---|---|---|
| OA | 3.9 | 7.8 | 3.9 | [0.0,8.8] |
| SA | 2.0 | 4.9 | 2.9 | [0.0,6.9] |
| DACS | 21.6 | 34.2 | 12.6 | [6.9,18.9] |

Source: Figure 5; Appendix Table 12 · [Paper](https://arxiv.org/pdf/2609.11318v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

GPT-5.5 scores OA 43.1/SA 34.3 and o3 Research 32.4/19.6: final-answer success does not ensure every annotated conclusion is correctly stated, but these are not verified retrieval-chain completion rates. Tool-free Gemini3.1 Pro still obtains DACS 70.1, underscoring that visual/prior-knowledge statements can earn credit without provenance checks. The paired Qwen image probe raises DACS from 21.6 to 34.2, a 12.6-point gain with interval[6.9,18.9]. SA gains only 2.9 points and is positive under seven of twelve judges, so all four metrics are not uniformly robust or significant.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

Small samples, authored long chains, live-web drift and provider routes constrain generality. SA’s all-node product becomes mechanically stricter with more requirements; trends for three representative models are not universal causal length effects. The main judge is relatively lenient, and high model agreement is not truth; cross-model checks do not replace human calibration. Failure analysis uses Qwen3.5-Flash to define failures and Qwen3.6 Plus to classify them, micro-averaging failed steps rather than the main CS protocol. Next match image interfaces/resources, log execution and citations, human-verify key nodes, admit verified alternative proof paths, repeat runs and separate service failures.

SectionE.1 calls a 72.7% conditional answer-completeness penalty more than eight in ten; 72.7% is below eight in ten. Section 5 says hidden paths/full source chains are withheld, while Appendix H.1 promises release of checklists, source URLs and verified dependency graphs. Actual public availability requires repository inspection. Judge rescoring scope is described as 2065 responses, pooled reference as 2157, and balanced grid as 702 after 799 candidates; the first two cohort relationship is not fully reconciled. Illustrative success Table 20 grants all twelve checklist items despite some details, such as 1935 and Angus Hyland, not being explicitly stated in the displayed response; this needs human review under the stated complete-statement rule. Claimed multimodal necessity and irreducibility are annotation properties, not demonstrated impossibility of alternate routes; the model ablation establishes an average benefit, not necessity for every item.
<!-- EVIDENCE:limitations:END -->
