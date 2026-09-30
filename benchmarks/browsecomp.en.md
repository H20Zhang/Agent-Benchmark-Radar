# BrowseComp: persistent search for hard-to-find web evidence

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2025-04-10 · official launch<br>
> **OpenAI deep research — Accuracy: 51.5%**<br>
> Best model in the official launch article, on the original 1,266 questions. The authors state that deep research was trained specifically for this task type. [Original source](https://openai.com/index/browsecomp/)<br>
> Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.
<!-- RELEASE-REFERENCE:END -->

[中文](browsecomp.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

main sections 1–5; Appendices A–B prediction/grading prompts; Tables 1–3 and Figures 1–5; Table 3/Figure 4 visually verified

[arXiv v1 (2025-04-16) — v1,2025-04-16; separate from 2025-04-10 launch article](https://arxiv.org/pdf/2504.12516v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Compared with HotpotQA’s fixed encyclopedic evidence, BrowseComp emphasizes locating obscure facts through sustained web search. Short answers simplify grading but leave corpus and evidence-use attribution uncontrolled; BrowseComp-Plus subsequently freezes that interface.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

Humans invert stable facts into difficult multi-constraint questions, screened with models, simple searches and some human attempts. A grader checks short-answer equivalence, not evidence trajectories.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

There are 1,266 questions. Table models are GPT-4o-2024-08-06, gpt-4o-search-preview-2025-03-11 and o1-2024-12-17 at medium effort. Deep Research is trained on similar tasks; the paper does not give a comparable absolute tool/token budget or a clear exact final-grader model. Parallel experiments sample up to 64 runs per question and select by confidence; this best-of-N is not oracle pass@N.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Historical system outcomes

Reference-answer equivalence accuracy in percent on 1,266 questions; dated model versions appear in the conditions, while the absolute tool and token budget for Deep Research is undisclosed.

| System | Accuracy |
|---|---|
| GPT-4o | 0.6 |
| GPT-4o browsing | 1.9 |
| o1 medium | 9.9 |
| Deep Research | 51.5 |

Source: Table 3 · [Paper](https://arxiv.org/pdf/2504.12516v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Human-attempt denominators

Counts; 367/1,255 is self-reported completion, whereas 317/367 is reference agreement among completed attempts; 29.2% is not reference-answer accuracy.

| Outcome | Numerator | Denominator |
|---|---|---|
| Reported solved | 367 | 1255 |
| Reference agreement among solved | 317 | 367 |
| Gave up after≥2h | 888 | 1255 |

Source: Table 2 · [Paper](https://arxiv.org/pdf/2504.12516v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

Human 29.2% is reported solved, not reference-graded accuracy. Models differ in training/version/tools, preventing a pure browsing-tool causal claim.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

Answer uniqueness is not exhaustive; screening is model-dependent. Parallel voting spends more resources. Next: fixed versions/budgets and complete evidence verification.

§4.5 states 14% zero-success tasks but later mentions 118 of 1287 zero-pass tasks before 21 removals; denominators/versions are not reconciled. Exact calibration-error definition and absolute browsing-compute budget absent; do not invent them.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [browsecomp-plus](browsecomp-plus.en.md) · [livebrowsecomp](livebrowsecomp.en.md)
