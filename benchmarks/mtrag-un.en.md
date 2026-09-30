# MTRAG-UN: multi-turn RAG should not assume every turn is answerable, complete, or standalone

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-02-26<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://aclanthology.org/2026.findings-acl.503/)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](mtrag-un.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Full seven-page paper, Sections 1–5 and limitations; appendices inspected: A–B, task distribution, judge validation and underspecified-turn stitching; visual checks: Figures 2–6 and Table 4 rendered pages 2, 4 and 6; supporting source: Original MTRAG https://aclanthology.org/2025.tacl-1.36.pdf, targeted reading of Sections 6.3–8 for inherited metrics; not a full reread of this supporting paper. Not performed: No rerun or implementation audit; inherited settings beyond cited metric definitions not independently reconstructed

[ACL 2026 Findings — ACL 2026 Findings, pp. 10363–10369](https://aclanthology.org/2026.findings-acl.503.pdf) · [TACL 2025 — TACL 2025, Section 6.3–8 targeted metric reading](https://aclanthology.org/2025.tacl-1.36.pdf)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

MTRAG-UN directly extends MTRAG’s multi-turn enterprise QA with unanswerable and underspecified requests. It distinguishes missing facts requiring abstention from missing constraints requiring clarification, beyond generic answer similarity.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

Each of 666 conversations contributes one selected evaluation turn with its preceding history, emphasizing unanswerable, underspecified, context-dependent and clarification cases rather than treating every turn as a task. Six domains combine four inherited corpora with banking and telecommunications pages. Some underspecified tasks stitch human questions onto existing conversations, 75% on similar topics and 25% across topics, followed by validation that ambiguity remains. Retrieval compares the last user turn with GPT-OSS-20B rewriting on 468 answerable or partially answerable tasks. Generation contrasts up to ten gold passages with the top five Elser rewrite-retrieved passages, requesting responses under 150 words and explicit requests for missing information when underspecified.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

Retrieval uses only 468 answerable/partial tasks with a six-domain macro-average; non-standalone/standalone subsets contain 214/254. RBalg harmonically averages BERT reference recall, BERT knowledge precision against evidence and ROUGE-L. RBllm judges faithfulness, appropriateness and completeness against reference and evidence; RLF is reference-less RAGAS faithfulness. Answerability/IDK conditioning gives one to correct abstention on an unanswerable task and zero to abstention on an answerable task. Underspecified tasks use a separate explicit-information-request judge, validated at 96.2% on eighty sampled responses. GPT-OSS-120B replaces the specified GPT-4o-mini judge, with other inherited judges unchanged.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Last turn versus conversational rewrite

R@5 is on a 0–1 scale; all 468 answerable/partial tasks use a six-domain macro-average, while non-standalone and standalone subsets contain 214 and 254 tasks. Rewriting uses GPT-OSS-20B.

| Elser subset | Last-turn R@5 | Rewrite R@5 |
|---|---|---|
| All answerable/partial | 0.4 | 0.49 |
| Non-standalone | 0.39 | 0.52 |
| Standalone | 0.4 | 0.46 |

Source: Tables 2–3 · [Paper](https://aclanthology.org/2026.findings-acl.503.pdf)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Generation scores and evidence conditions

All metrics are on a 0–1 scale and conditioned on answerability/IDK. Underspecified tasks use a separate judge and exact metric denominators are not explicitly reported. Reference evidence has up to ten passages versus five retrieved passages.

| GPT-OSS-120B evidence | RLF | RBllm | RBalg |
|---|---|---|---|
| Reference up to 10 | 0.65 | 0.76 | 0.46 |
| Elser rewrite top 5 | 0.59 | 0.65 | 0.37 |

Source: Table 4; metric definitions inherited from original MTRAG Section 6.3 · [Paper](https://aclanthology.org/2026.findings-acl.503.pdf)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

Rewriting yields matched retrieval gains: Elser R@5 rises from 0.40 to 0.49, with a larger change for non-standalone questions, 0.39 to 0.52, than standalone questions, 0.40 to 0.46. Generation differs between reference and retrieved evidence, but passage counts also change, so the entire gap is not a causal estimate of retrieval noise. Unanswerable and underspecified questions need different behavior: abstention can be correct for the former, while the latter judge requires an explicit request for missing information. Merely saying information is missing does not count as successful clarification.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

Corpus-relative unanswerability means annotators found no relevant passage, not that the world has no answer. Collection relies on Elser and initial Mixtral 8×7B responses, potentially favoring that retrieval pipeline. The clarification judge mainly detects requests for information rather than their usefulness or eventual task resolution. GPT-OSS-120B appears as both judge and evaluated model, motivating independent judging. Next, match reference/retrieved passage counts, audit clarification usefulness with humans, and evaluate task completion after the user supplies the missing information.

Figure 3 is captioned RBalg throughout, although Section 3.1 says underspecified examples use a distinct clarification judge and are not scored with the other metrics; distinguish the red underspecified bars from RBalg. The abstract says over 2,800 turns while Section 2 describes 666 conversations averaging eight turns; the paper does not clearly reconcile turn units or full-versus-prefix counts. Keep 666 selected tasks and avoid treating either count as exact. Table 4 does not supply the precise denominators/aggregation for every generation metric after separating underspecified examples; do not label all entries as a uniform 666-task average. The text broadly calls GPT-OSS-120B best, but RAG RBalg is 0.37 versus 0.38 for Granite-4-small and Llama-3.3-70B; rankings depend on the metric.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [rgb](rgb.en.md) · [longmemeval](longmemeval.en.md)
