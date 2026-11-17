# SynthCorp

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-11-10<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2611.14765v1)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](synthcorp.md) · **English** · [Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope
Read the primary generation pipeline, data-context evaluation, result table and simulation-boundary discussion. Checked the arXiv release statement; no public official artifact was verified. No experiment reproduction or independent figure-pixel inspection.
[arXiv:2611.14765v1](https://arxiv.org/html/2611.14765v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Measured object and construction
SynthCorp is a benchmark-generation platform rather than a single fixed question set. It compiles reusable business-event definitions into simulation programs, schedules routine and disruptive events, and materializes relational data, documents and a catalog. An operation log preserves provenance for checking candidate reference programs. Seven generated estates yield 256 analytical tasks across five domains, reaching 1,000 operational tables. The key distinction is that a task can require historical business rules absent from a schema. The logged event history helps resolve conflicting candidate programs; it is not a formal proof that every generated question has a unique interpretation.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Protocol and fair comparison
Three reasoning-enabled models are evaluated with three runs per task. The four settings expose schema alone, schema plus one BM25-retrieved document, an agent with seven catalog/search/SQL tools, or files and a command line. Thus context and interface change together across parts of the comparison. The evaluator executes submitted queries and matches reference values to distinct output rows, allowing extra columns, reordering and float rounding. arXiv v1 says benchmark release is forthcoming. No unrelated repository sharing the name is treated as the official implementation.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Selected primary evidence
Table 7: Claude Opus 5.5, reasoning enabled, 256 tasks, three runs per task; reported execution accuracy (%) as mean ± standard error.

| Setting | Execution accuracy (%) |
|---|---|
| S1 | 54.6 ± 2.9 |
| S3 | 86.6 ± 1.9 |
| S4 | 88.8 ± 1.7 |

The selected result shows the value of richer access in this generated environment. It does not isolate a search policy: S1 lacks the documents containing relevant rules. S3 and S4 give a closer interface comparison, but their token costs differ. The reported numbers should remain attached to the original grader rather than replaced by a more permissive post-hoc audit.
[arXiv:2611.14765v1](https://arxiv.org/html/2611.14765v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next control
Output conventions are consequential: the paper’s failure audit identifies correct computations rejected for representation differences. That makes semantic equivalence a needed control, not permission to count every failed output as correct. Simulated values also differ from empirical business distributions. The generative pipeline and provenance audit make difficult examples inspectable, but independent validation is still necessary when the same system designs questions and gold programs. A useful release would pin simulation seeds, event definitions, task versions, model configurations and raw outputs. Before comparing agents, distinguish whether an error came from unavailable rules, failure to discover them, incorrect calculation or output normalization. This is an early signal about controllable enterprise evaluation, not evidence of general deployment readiness.
<!-- EVIDENCE:limitations:END -->

[arXiv:2611.14765v1](https://arxiv.org/html/2611.14765v1)
