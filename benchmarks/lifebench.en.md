# LifeBench: long-term memory over simulated multi-source life records

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2026-03 · paper v1<br>
> **MemOS / GPT-5.1-Mini — Overall accuracy: 55.22%**<br>
> Best overall accuracy in v1 Section 4.3; GPT-5.1-Mini for memory, answers, and judging on the original 2,003 questions. [Original source](https://arxiv.org/html/2603.03781v1)<br>
> Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.
<!-- RELEASE-REFERENCE:END -->

[中文](lifebench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Full substantive paper and appendix reading completed for the stated version; experiments were not independently reproduced.

Read all 28 pages: §§1–5 and Appendices A–H, including synthesis algorithms, quality rubrics, error cases, ethical limits and complete provided schemas/monthly-report examples. Visually checked Figures 7 and 9.

[arXiv v1 / 2026-03-04](https://arxiv.org/pdf/2603.03781v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement

DeepSeek-R1 expands survey-informed personas into yearly plots, nested events, daily activities and phone traces. A second agent checks time, location and travel feasibility; the benchmark then asks questions grounded in those records. Questions test extraction, multi-hop reasoning, temporal updates, inferred habits/preferences and abstention. Evidence gaps are filled by generating additional phone records after question creation (§3.2.5). This is controlled synthetic QA, not demonstrated real-user personalization.

A source example asks about a person’s first time caring for a neighbor’s cat: the reference distinguishes initial nervousness and awkwardness from later confidence. Retrieving the event alone can miss the state that the question asks about (Table 4).

### Measurement genealogy

LoCoMo and LongMemEval center on conversational histories; Mem-Pal adds application logs. LifeBench moves the observable evidence to dense, heterogeneous life records, making cross-source aggregation and inferred habits explicit. Its next coordinate is time-correct, revisable personalization on less scripted records, rather than a larger synthetic history alone.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

Ten synthetic users, one year each; 2,003 questions: 517 multiple-choice and 1,486 short-answer. GPT-5.1-Mini handles memory, answering and grading; text-embedding-3-small supplies embeddings. Structured records become textual summaries in LoCoMo-compatible inputs; monthly ground-truth summaries are excluded. Retrieval caps, temperatures, repeats and exact ingestion cutoffs are unspecified (§4.2; Appendix H.5).
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

Selected Figure 7 values; accuracy is the percentage of questions judged correct, using GPT-5.1-Mini and the LoCoMo grading prompt. Denominators come from Table 2; all systems use the same named base model and textualized records.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| MemOS / GPT-5.1-Mini / overall | LifeBench v1; 2,003 questions | Judged accuracy (%) | 55.22 | text-embedding-3-small; same-model judge | Figure 7, p.8; Table 2, p.6 |
| Hindsight / GPT-5.1-Mini / overall | LifeBench v1; 2,003 questions | Judged accuracy (%) | 40.99 | Same named model, embeddings and judge | Figure 7, p.8; Table 2, p.6 |
| Hindsight / GPT-5.1-Mini / ND | LifeBench v1 non-declarative slice; 429 questions | Judged accuracy (%) | 50.35 | Habits, skills, emotions and preferences; same judge | Figure 7, p.8; Table 2, p.6 |
| MemOS / GPT-5.1-Mini / ND | LifeBench v1 non-declarative slice; 429 questions | Judged accuracy (%) | 47.32 | Same non-declarative slice and judge | Figure 7, p.8; Table 2, p.6 |

Source: [Figure 7, p.8; Table 2, p.6](https://arxiv.org/pdf/2603.03781v1)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

Overall ranking hides the non-declarative reversal in the preceding table. Shared answering/judging models and summary preprocessing constrain attribution; the synthetic-history generator is a different model. Chinese-adult personas limit coverage; synthetic health traces are explicitly non-clinical. Figure 9 provides coarse per-user costs, not standardized latency. Architectural explanations in §4.3 lack matched component ablations.
<!-- EVIDENCE:limitations:END -->

<!-- EVIDENCE:next:START -->
## Next experiment

Enforce and publish timestamp cutoffs. Compare raw records, supplied summaries and source-shuffled summaries with fixed retrieval tokens; add an independent blinded judge and user-clustered intervals. Test whether inferred habits remain useful after explicit corrections.
<!-- EVIDENCE:next:END -->
