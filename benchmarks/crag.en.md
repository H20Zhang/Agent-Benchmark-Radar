# CRAG: RAG under freshness, long-tail knowledge, and abstention pressure

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2024-06 · paper v1<br>
> **Copilot Pro — Human-eval Score_h (equal-weighted): 50.6**; **GPT-4 Turbo + Task-3 RAG — Auto-eval accuracy: 43.6%**<br>
> Best industry-system human score in Table 6 and best Task-3 baseline accuracy in Table 5; these scoring protocols and challenge scores differ. [Original source](https://arxiv.org/html/2406.04744v1)<br>
> Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.
<!-- RELEASE-REFERENCE:END -->

[中文](crag.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

main sections 1–6; Appendix A.1–A.4 including prompts, construction, judge validation, latency; Tables 1–11; Table 5/Figure 2 visually verified

[v1,2024-06-07](https://arxiv.org/pdf/2406.04744v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Compared with static, answerable-in-corpus tasks common in HotpotQA/KILT, CRAG adds freshness, long-tail entities, false premises and abstention with web and knowledge-graph evidence. Its contribution is an explicit answer-versus-error tradeoff rather than scale alone.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

KG templates and human web questions yield 4409 cases across five domains, eight types, freshness/popularity slices. Frozen pages and 38 mock APIs support Task 1(five pages), Task 2(+KG), Task 3(50 pages+KG). Correctness, hallucination and abstention remain separate.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

Main results use 1,335 public test questions. GPT-4 Turbo receives at most 4,000 web-context tokens and 2,000 KG tokens, with Llama3-8B-Instruct for entity extraction. Automatic scoring first checks exact match, then averages GPT-3.5-turbo and Llama3-70B-Instruct judgments. Scorea is accuracy minus hallucination. Human Scoreh assigns 1 to perfect, 0.5 to acceptable, 0 to missing and −1 to incorrect answers. Commercial systems use human evaluation and should not be ranked directly against frozen-web automatic baselines.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Accuracy gains need not improve risk-sensitive score

GPT-4 Turbo on 1,335 public test questions; the first three metrics are percentages and Scorea is accuracy minus hallucination in percentage points; web context is 4,000 tokens and KG context 2,000 tokens.

| GPT-4 Turbo condition | Accuracy | Hallucination | Missing | Scorea |
|---|---|---|---|---|
| LLM-only | 33.5 | 13.5 | 53.0 | 20.0 |
| Task 1 | 35.9 | 28.2 | 35.9 | 7.7 |
| Task 2 | 41.3 | 25.1 | 33.6 | 16.2 |
| Task 3 | 43.6 | 30.1 | 26.3 | 13.4 |

Source: Table 5, section 5.1 · [Paper](https://arxiv.org/pdf/2406.04744v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

Retrieval makes GPT-4 Turbo answer more questions but also increases hallucinations. Task 3’s risk-sensitive score of 13.4 remains below the closed-book score of 20.0. Commercial systems use a different protocol.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

Commercial tests omit original query_time/frozen retrieval; do not rank directly against baselines. Mock APIs omit live navigation. Next: match time/source access and retain error/abstention outcomes.

Table 5 reports Task 3 Scorea as 13.4, while the displayed accuracy minus hallucination, 43.6−30.1, equals 13.5. This is an unexplained display discrepancy; the reviewed source does not establish rounding as its cause. Preserve the reported value with attribution. Section 5.2 reverses former/latter wording in a sentence about automatic and human evaluation; Sections 4 and 5.1 and Appendix A.4 establish the actual settings.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [livebrowsecomp](livebrowsecomp.en.md) · [mtrag-un](mtrag-un.en.md)
