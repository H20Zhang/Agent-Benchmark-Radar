# GroupMemBench: speaker-conditioned QA over synthetic workplace groups

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2026-05-14 · paper v1<br>
> **Hindsight / GPT-5 — Micro-average QA accuracy: 46.01%**<br>
> Best among the compared systems in v1 Table 2. Appendix G defines a micro-average over the filtered union of Technology, Finance, Healthcare and Manufacturing, excluding unparseable judge outputs, not a six-category macro-average. Ingestion uses GPT-4o-mini; answering and judging use GPT-5. [Original source](https://arxiv.org/abs/2605.14498v1)<br>
> Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.
<!-- RELEASE-REFERENCE:END -->

[中文](groupmembench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Full substantive paper and appendix reading completed for the stated version; experiments were not independently reproduced.

Read all 24 pages of v1, main §§1–5 and Appendices A–L: graph schema, sampling equations, published prompts, generation knobs, domain results, cost accounting, judge protocol, all eight-system case traces and limitations. Visually checked Table 2 and the retrieval-failure figures. v2 dated 16 May exists but was not substituted into this v1 review.

[arXiv v1 / 2026-05-14](https://arxiv.org/pdf/2605.14498v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement

Graph traversal chooses a speaker, audience, project phase and reply parent; GPT-5 realizes messages with personas and occasional noise, disagreement or reversals. A solver–judge–refiner loop retains questions that defeat its retrieval solver. Every query includes an asker identity (§3).

In the worked Finance case, User_13 asks which teams must align on formatting. The gold is Finance and Data Engineering. BM25 retrieves the original request; Hindsight preserves that request with its speaker in a rewritten note. Other systems retrieve wrong speakers or merge extra teams (Appendix J). This distinguishes useful speaker-preserving compression from lossy rewriting; it does not prove all compression is harmful.

### Measurement genealogy

LoCoMo and LongMemEval supply long-history QA precedents. EverMemBench is the closer multi-party predecessor; GroupMemBench adds controlled reply structure, persona/audience wording and asker-conditioned questions. Those mechanisms operationalize social context, without establishing human-like Theory of Mind or enforcing access permissions.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

Four English workplace domains each contain 30,000 messages, with six query categories. GPT-4o-mini standardizes ingestion, GPT-5 answers and judges, and dense components use text-embedding-3-large where supported. Judge T=1, output cap 2,048, one verdict per answer; unclear parsed verdicts leave the denominator. Cross-domain scores are micro-averaged over filtered questions. Exact total/type counts, solver identity/refinement budget, answer decoding and matched retrieval-token caps are not fully tabulated. The worked dense retriever uses top-10, while several memory traces show three entries.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

Selected v1 facts. Overall is not the mean of the six displayed category percentages. Category maxima come from different methods, so the abstract’s three headline numbers are not one system profile.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| Hindsight / All categories | All categories; filtered union of four domains; N not explicitly tabulated | GPT-5-judged accuracy (%); unclear verdicts excluded | 46.01 | GPT-4o-mini ingestion where applicable; GPT-5 answerer; native retrieval budgets | Table 2, p.7 |
| BM25 / All categories | All categories; filtered union of four domains; N not explicitly tabulated | GPT-5-judged accuracy (%); unclear verdicts excluded | 43.22 | GPT-4o-mini ingestion where applicable; GPT-5 answerer; native retrieval budgets | Table 2, p.7 |
| HippoRAG / Knowledge Update | Knowledge Update; filtered union of four domains; N not explicitly tabulated | GPT-5-judged accuracy (%); unclear verdicts excluded | 27.10 | GPT-4o-mini ingestion where applicable; GPT-5 answerer; native retrieval budgets | Table 2, p.7 |
| Hindsight / Knowledge Update | Knowledge Update; filtered union of four domains; N not explicitly tabulated | GPT-5-judged accuracy (%); unclear verdicts excluded | 17.76 | GPT-4o-mini ingestion where applicable; GPT-5 answerer; native retrieval budgets | Table 2, p.7 |
| Hindsight / Term Ambiguity | Term Ambiguity; filtered union of four domains; N not explicitly tabulated | GPT-5-judged accuracy (%); unclear verdicts excluded | 37.74 | GPT-4o-mini ingestion where applicable; GPT-5 answerer; native retrieval budgets | Table 2, p.7 |

Source: [Table 2, p.7](https://arxiv.org/pdf/2605.14498v1)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

Table 2 identifies Hindsight as the v1 overall winner. The category leaders differ: 27.10 Update belongs to HippoRAG, while Hindsight scores 17.76. Adversarial selection measures a solver-conditioned hard distribution. Missing gold-message IDs can reflect rewritten alternative evidence, and conditional accuracy on retrieved cases is not an oracle intervention. One hundred manual checks with 99 agreements do not establish uniform judge bias or immutable rankings. Cost excludes querying and failed calls; allocated database sizes are not pure memory payload bytes. No privacy, membership-change or production-workflow safety is tested.
<!-- EVIDENCE:limitations:END -->

<!-- EVIDENCE:next:START -->
## Next experiment

Use the same answerer and token budget for raw, speaker-preserving compressed and speaker-shuffled stores. Independently replace retrieval with complete gold evidence, retaining a held-out non-adversarial query set. Measure answer quality, attribution, updates and access-policy compliance separately, and preserve exact verdict denominators plus ingestion/query costs.
<!-- EVIDENCE:next:END -->
