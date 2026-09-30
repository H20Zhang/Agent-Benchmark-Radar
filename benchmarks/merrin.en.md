# MERRIN: infer the needed modality before retrieving evidence from the noisy web

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-04-15<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2604.13418)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](merrin.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Sections 1–6, all three search settings, gold-evidence interventions and human analysis; appendices inspected: A–E, limitations, annotation, setup, judge/human prompts and video-tool ablation. Not performed: No rerun, implementation audit or reconstruction of human/URL aggregation denominators

[arXiv v1, 2026-04-15](https://arxiv.org/pdf/2604.13418v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Compared with BrowseComp’s web-text clues, MERRIN asks systems to discover the need for image, video or audio evidence. It adds modality discovery to open search, while shared multimodal tools complicate backbone attribution.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

The 162 human-reviewed questions use natural language without directly specifying an attached modality, require non-text evidence for at least one step, and have a unique short answer. One hundred twenty are newly authored, thirty-seven extend SealQA and five ChartMuseum. Independent reviewers attempt text-only Google search and then up to twenty adversarial searches with known answers to screen out shortcuts; browsing-enabled ChatGPT also screens difficulty. Sources include text, images, video/audio and tables, and 119 questions combine multi-hop reasoning with cross-modal conflict.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

Settings are no search, model-native search and a smolagents multimodal agent. The latter uses Serper search and Gemini-3-Flash-powered visit_webpage/watch_video tools to interpret pages and YouTube video/audio, so text-only Qwen agents also receive mediated multimodal information. Final grading uses a BrowseComp-style answer-equivalence prompt; the exact judge model is not explicit in the reviewed setup, while a fifty-example human check finds all judgments correct. Main scores are means±standard deviations over three runs on 162 questions, not confidence intervals. Native tool coverage, context limits and platform timeouts differ, preventing matched-budget or single-retriever attribution.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Video tools and full agent orchestration

162 questions and three runs; mean accuracy is in percent and across-run SD in percentage points, not a confidence interval. Tools and search orchestration differ.

| Gemini-3.1-Pro setting | Accuracy mean percent | Run SD |
|---|---|---|
| Native Search | 29.0 | 1.1 |
| Native Search + Video | 37.5 | 2.0 |
| Agentic Multimodal Search | 40.1 | 2.8 |

Source: Table 7 · [Paper](https://arxiv.org/pdf/2604.13418v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Gold-evidence interventions retain substantial error

162 questions over three runs, in percent/percentage points. Injection retains live distractors, gold-only retains processing tools, and direct prompting switches to one native multimodal pass. Retrieval recall is not the sole variable.

| Gemini-3.1-Pro intervention | Accuracy mean percent | Run SD |
|---|---|---|
| Gold URL injection | 43.4 | 3.8 |
| Gold URLs only | 45.5 | 2.3 |
| Direct gold-source prompting | 47.7 | 2.0 |

Source: Table 4; Section 4.3 · [Paper](https://arxiv.org/pdf/2604.13418v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

Gemini-3.1-Pro scores 29.0% with native search, 37.5% after adding video processing and 40.1% with the full multimodal agent, making tool availability a material condition. Gold URLs yield 45.5%, and direct gold multimodal inputs 47.7%, leaving substantial errors. However, the 40.1→47.7 contrast changes sources, distractors, tool execution and reasoning format together; its 7.6-point difference is not a mathematical upper bound on search error. Human time gains and over-exploration patterns are observational rather than proof that stronger models intrinsically waste compute.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

Twenty searches cannot exhaustively rule out text shortcuts, and web drift/Google rankings affect reproducibility. Added Gemini tools supply video/audio interpretation absent from native search, mixing external-model capability into gains; platform timeouts also affect product scores. Annotated URLs are not exhaustive, so low overlap does not automatically imply useless or incorrect sources. Next, fix time snapshots, task subsets, tool interpreters and budgets, intervene separately on source selection and understanding, and report timeout/failure handling and visited-URL scope explicitly.

Human evaluation is described as fifty questions, yet 71.4% and 59.2% are not integer fractions of fifty; exclusions, per-rater averaging or another effective denominator are not explained. Table 3 agent accuracy is 40.1, matching the full-set headline, and native accuracy 30.9 differs from Table 2’s 29.0. The exact common question set for the human/agent comparison is not explicit. URL-overlap prose/caption says visited URLs, while discussion attributes low precision to all URLs encountered; with 63.6 encountered versus 3.5 visited per question, this scope difference is material. The text calls gold-prompting gain an upper bound on search limitations, but the intervention also removes agent orchestration and changes multimodal presentation. Text is called the dominant dataset modality in one sentence despite listed image share 35.9% exceeding text 31.4%.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [mc-search](mc-search.en.md) · [browsecomp](browsecomp.en.md)
