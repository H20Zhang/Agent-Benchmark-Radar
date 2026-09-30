# ICM-Bench: organizing cross-time evidence around recurring people

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-09-03<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2609.04438)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](icm-bench.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Read main Sections 1–5 and Appendices A–I, including all result tables, generation/curation records, human and judge protocols, full caption/answer/judge prompts and detailed failure traces. PDF prompt text checked. Official README inspected; no implementation audit, video playback audit or reproduction.

[arXiv 2609.04438v2 (2026-09-08)](https://arxiv.org/html/2609.04438v2)

[Auxiliary material (checked 2026-09-30)](https://github.com/Shidu-Ren/ICM-Bench/blob/beeb816a21085e23b8d0c38097576c0f4c0aad7d/README.md)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

ICM-Bench follows six recurring synthetic adults through a year-long life album, asking about person-linked events, cross-clip associations and accumulated habits or relationships. Planning specifies identities and evidence before rendering and voice synthesis; two authors then verify each question against permitted video. The 839 clips include a shared face–voice calibration clip without names and 838 dated memory clips. Recall/Retrieval use question-specific prefixes; Profile uses the full timeline. Gold IDs, answers, evidence annotations and named transcripts are withheld.

Editorial placement: Broad M3-Bench QA changes little when face processing or face–voice links are removed. ICM-Bench instead makes recurring people central to cross-time evidence selection. This changes the required evidence organization rather than directly extending M3-Bench data; aggregate QA still does not prove identity mechanisms are necessary for every item.
Illustrative task: a recurring person participates in activities across dated clips. A later question requires linking the clips to the right person before inferring a habit; recognizing activities while mixing up people still gives the wrong answer.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

The sequence spans 141 minutes, with 140.6 minutes of main memory. There are 1217 open-ended questions: 400 Recall, 500 Retrieval and 317 Profile. Gemini direct baselines caption complete clips; Qwen direct baselines use 12 uniform frames plus speakerless ASR. Vgent builds at 1 fps, retrieves five nodes and supplies 12 frames per selected clip. M3-Agent uses 2 fps for memorization and 5 fps for faces; HippoRAG2 indexes clip captions and filters records beyond the cutoff. Answer instructions match, but perception, retrieval and call budgets differ. Gemini 3 Flash judges whether answers entail the reference meaning at temperature 0.000001; complete output/context budgets for all systems are not reported.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Table 4, selected Qwen3.5-9B comparisons

Same answerer and questions, with unequal perception/memory procedures. Both frameworks improve overall/event retrieval scores while lowering Profile accuracy; gains do not extend to every memory capability.

1217 overall; category denominators 400/500/317. Overall weights questions, not three equally weighted categories.

| System | Overall accuracy (%) | Recall (%) | Retrieval (%) | Profile (%) |
|---|---|---|---|---|
| Caption-memory / Qwen3.5-9B | 47.9 | 53.5 | 45.8 | 44.2 |
| Vgent / Qwen3.5-9B | 52.3 | 66.0 | 54.6 | 31.2 |
| HippoRAG2 / Qwen3.5-9B | 49.6 | 61.3 | 54.4 | 27.4 |

Locator: Table 4, selected Qwen3.5-9B comparisons · [Source](https://arxiv.org/html/2609.04438v2)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Table 4, visual-evidence and strong-reader references

ASR controls remove frames, visual captions and face cues, demonstrating value beyond transcripts without isolating face identity as the sole cause. Human scores average two untimed independent evaluators, not matched compute or a hard ceiling.

1217 questions overall and 317 Profile; human row averages two full answer sets.

| Configuration | Overall accuracy (%) | Profile (%) |
|---|---|---|
| Caption-memory / Gemini 3.5 Flash | 73.4 | 50.8 |
| ASR-only / Gemini 3.5 Flash | 38.7 | 31.9 |
| Caption-memory / Gemini 3.1 Pro | 74.0 | 60.3 |
| Human | 93.8 | 89.6 |

Locator: Table 4, visual-evidence and strong-reader references · [Source](https://arxiv.org/html/2609.04438v2)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Tables 1 and 4, identity-component diagnostic

Corresponding M3-Agent component removals; ICM uses the original Qwen2.5-Omni-7B SFT configuration. Compare directions within each benchmark, not absolute cross-benchmark scores. Removing links lowers ICM overall but raises Profile; no repeated-run intervals are supplied.

M3-Bench Web: all 575 questions from 100 randomly sampled videos. ICM: 1217 overall/317 Profile.

| Configuration | M3-Bench Web accuracy (%) | ICM overall (%) | ICM Profile (%) |
|---|---|---|---|
| M3-Agent full | 52.5 | 45.4 | 24.3 |
| M3-Agent no face | 55.3 | 41.0 | 24.3 |
| M3-Agent no equiv | 53.0 | 42.9 | 27.1 |

Locator: Tables 1 and 4, identity-component diagnostic · [Source](https://arxiv.org/html/2609.04438v2)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:result-4:START -->
## Appendix F, judge–human agreement on two audited answer runs

Each judge is compared with two independent human label sets and agreement is averaged. This validates correctness labels for two runs, not answer accuracy or all systems. Human evaluators completed answerability first, then verified model outputs.

1217 responses per audited run, 2434 total; two human label sets per run.

| Audited answer source | Gemini 3 Flash agreement (%) | GPT-5.4-mini agreement (%) |
|---|---|---|
| M3-Agent / Qwen2.5-Omni-7B SFT | 96.6 | 95.7 |
| Caption-memory / Gemini 3.1 Pro | 96.1 | 95.3 |

Locator: Appendix F, judge–human agreement on two audited answer runs · [Source](https://arxiv.org/html/2609.04438v2)
<!-- EVIDENCE:result-4:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

This is a single synthetic-cast diagnostic; the separate 30-clip theater theme tests construction only. Generation and the strongest direct answerer share the Gemini family; human curation does not replace independent-generation replication. The answer prompt explicitly forbids Unknown and permits reasonable guessing, so abstention rates describe calibration under that instruction. The primary metric scores answers, not identity links or evidence coverage directly; aggregate ablations are not universal component-necessity proofs. Real video, long-term appearance changes and downstream action utility remain unverified.

The inspected official README explicitly omits the direct caption-memory implementation, limiting reproduction of the strongest comparison. Most questions name the person, while evidence must connect the name to multimodal events; this is not uniformly an unnamed-face identification task. Calibration links faces and voices without names. Profile access to the full timeline differs from prefix-limited Recall/Retrieval. The 95.3–96.6% judge agreement range covers two audited runs only.



Next: Fix perception, answerer and total budget across complete captions, retrieved snippets and person–event structures. Retain face/link ablations and add paired identity swaps, evidence removal and oracle evidence. Score answers, identity links and retrieval coverage separately, then validate on consented real video and independent synthetic casts.
<!-- EVIDENCE:limitations:END -->
