# RetailBridge

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-10-18<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2610.25096v1)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](retailbridge.md) · **English** · [Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope
Read the primary construction method, evaluation, baseline setup and judge-audit sections; checked the official repository README and artifact inventory. No benchmark reproduction or independent figure-pixel inspection.
[arXiv:2610.25096v1](https://arxiv.org/html/2610.25096v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Measured object and construction
RetailBridge asks an agent to connect evidence rather than answer from one document. Persona-driven retail simulations produce five tables and three text collections. Atomic questions are combined through shared entities or intermediate answers. For example, finding a buyer’s largest purchase can select the review whose explanation is needed next. Construction records retain SQL or retrieval chains behind the reference answer. The benchmark has 1,680 questions, balanced across three generation models, with separate depth, source and modality labels. RetailRAG is the associated method, not the benchmark name: schema briefing precedes source-routed planning and local repair.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Protocol and fair comparison
The main harness comparison fixes GPT-oss-120B, Qwen3-Embedding-8B and Qwen3.6-Plus as backbone, embedder and semantic judge. SQLite serves tables; a dense index serves text, with shared top-10 retrieval. Accuracy is string containment, while the judge assesses semantic equivalence. These are different metrics, not interchangeable estimates of exact correctness. Baseline-specific control flows and settings remain different. The official repository exposes benchmark data, RetailRAG, scripts and evaluate.py; availability is not a claim that this review ran them.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Selected primary evidence
Table 2: shared GPT-oss-120B backbone, all 1,680 questions; average string-containment accuracy, semantic-judge accuracy and API calls per query.

| Setting | Containment accuracy | Judge accuracy | API calls/query |
|---|---|---|---|
| RetailRAG | 0.298 | 0.429 | 7.45 |
| HetaRAG | 0.149 | 0.293 | 25.21 |

This selected comparison supports better outcomes for the tested integrated framework, not a universal ranking of retrieval policies. Its higher judge score cannot be silently substituted for containment accuracy. Fewer API calls also do not establish proportional savings: calls can differ substantially in prompt size, generated tokens, caching and service latency.
[arXiv:2610.25096v1](https://arxiv.org/html/2610.25096v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next control
The simulated population and compositional construction define a controlled test distribution, not observed production demand. Because the authors also design RetailRAG, benchmark and method choices should be tested separately. The paper audits judge agreement, but scoring an answer is not independently proving that its cited evidence supports every claim. A useful next comparison would hold tools, schema exposure and total resources fixed, retain both answer metrics, and test human-authored questions on new schemas. Construction chains help audit provenance; they should not become information inadvertently supplied to the evaluated agent. Treat this as an early measurement signal for heterogeneous evidence orchestration, rather than proof that scaling alone cannot solve enterprise retrieval.
<!-- EVIDENCE:limitations:END -->

[arXiv:2610.25096v1](https://arxiv.org/html/2610.25096v1) · [Official repository](https://github.com/DISL-Lab/RetailBridge)
