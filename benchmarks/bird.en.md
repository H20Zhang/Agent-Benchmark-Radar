# BIRD: text-to-SQL grounded in large, dirty database contents

<!-- RELEASE-REFERENCE:START -->
> **Historical paper result (not the initial version)** · 2023-11-15 · paper v3<br>
> **ChatGPT + CoT — Test execution accuracy with evidence: 40.08%**<br>
> V3 Table 2: ChatGPT + CoT with supplied knowledge evidence on the 1,789-question test split. This is neither plain ChatGPT nor the abstract’s GPT-4 54.89%; it is a selected later-version baseline, not an initial-release best claim. [Original source](https://arxiv.org/html/2305.03111v3)<br>
> Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.
<!-- RELEASE-REFERENCE:END -->

[中文](bird.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and versions

Full substantive paper and appendix reading completed for the stated primary version; experiments were not independently reproduced.

Read all substantive text of the 28-page v3 and Appendices A.1–A.7 and B.1–B.13, including prompts, execution/VES definitions and the human study.

[arXiv 2305.03111v3 · 2023-11-15](https://arxiv.org/pdf/2305.03111v3)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## What the method measures

BIRD evaluates SQL grounded in database values and optional expert-written evidence. EX compares result sets, discarding duplicates and order. VES averages correctness times the square root of reference/prediction runtime across all questions; incorrect outputs contribute zero.

<!-- EDITORIAL-METHOD:START -->
BIRD collects real databases from multiple domains, retaining non-normalized values and practical scale, and annotates questions, SQL and external-knowledge notes with review. An illustrative workflow asks for an aggregate using a business abbreviation: the model must map it to actual column values, choose filters/joins and produce executable SQLite SQL. Supplied evidence may provide that mapping or a calculation definition. The task therefore combines schema interpretation with content grounding. VES rewards efficient execution only when the result is correct, aggregated over every question; it is not a standalone runtime measure.

Editorial placement: Spider emphasizes SQL structure on unfamiliar schemas; BIRD adds value grounding, external knowledge and execution efficiency. Spider 2.0 later adds documentation, project code and interactive workflows. Larger databases alone do not establish cross-system discovery or production reliability.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

The v3 test split has 1,789 questions across 15 databases. GPT-4 uses a zero-shot programming prompt and temperature 0; ChatGPT+CoT adds one pseudo-demonstration. DIN-SQL adds retrieval/examples/self-correction, with no complete token/retry budget reported.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

V3 Table 2; SQLite test; EX is percent of all 1,789 questions. Only the first two rows isolate supplied evidence for the same named model.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| GPT-4 · no evidence | BIRD test; 1,789 questions / 15 databases | EX (%) | 34.88% | gpt-4-32k; T=0 | Table 2, p. 7 |
| GPT-4 · evidence | BIRD test; 1,789 questions / 15 databases | EX (%) | 54.89% | gpt-4-32k; T=0 | Table 2, p. 7 |
| ChatGPT + CoT | BIRD test; 1,789 questions / 15 databases | EX (%) | 40.08% | gpt-3.5-turbo; evidence; T=0 | Table 2, p. 7 |
| GPT-4 + DIN-SQL | BIRD test; 1,789 questions / 15 databases | EX (%) | 55.90% | Evidence; expanded scaffold | Table 2, p. 7 |

Fact source: [Table 2, p. 7](https://arxiv.org/pdf/2305.03111v3)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

The header retains a selected later-v3 result: ChatGPT+CoT with evidence scores 40.08%, not plain ChatGPT or the best result in that version. V3 is dated 2023-11-15, not the initial release. The human 92.96% reference uses trained annotators before expert correction without matched model budgets. EX can miss order-sensitive errors.

<!-- EDITORIAL-NEXT:START -->
Next, supply gold value mappings, business rules and both on identical questions, retaining the relatively clean GPT-4 evidence comparison. Add order/duplicate-aware validation and match DIN-SQL retry/token budgets; otherwise scaffold gains may reflect privileged guidance or additional compute.
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
