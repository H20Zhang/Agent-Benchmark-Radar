# Spider 2.0: interactive enterprise-database workflows

<!-- RELEASE-REFERENCE:START -->
> **Release result (historical reference; not a best claim)** · 2024-11-12 · paper v1<br>
> **o1-preview + paper code-agent framework — Task success: 17.0%**<br>
> Code-agent result in the initial abstract on the original task collection; not later Lite, Snow, or revised sets. [Original source](https://arxiv.org/abs/2411.07763v1)<br>
> Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.
<!-- RELEASE-REFERENCE:END -->

[中文](spider-2.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and versions

Full substantive paper and appendix reading completed for the stated primary version; experiments were not independently reproduced.

Read the complete 45-page v1, including evaluation, annotation, databases, documentation, harnesses, costs, cases and prompts in Appendices A, B.1–B.8 and C.1–C.6.

[arXiv 2411.07763v1 · 2024-11-12](https://arxiv.org/pdf/2411.07763v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## What the method measures

Spider 2.0 evaluates database workflows using code, documentation and execution feedback. Lite is a different SQL-output track. Focused judges check task-designated outputs rather than universal whole-table equality.

<!-- EDITORIAL-METHOD:START -->
Tasks place natural-language requests inside workspaces containing databases, documentation and project files. An agent discovers schemas and dialect conventions, inspects values, edits SQL or project code, runs it and responds to errors before submitting the required artifact; Lite asks only for SQL. An illustrative workflow reads a metric definition, locates join keys, fixes a dialect error and produces the result file. Reference workflows distinguish generating one query from discovering the context needed to finish a task, while focused output checks can leave side effects or extraneous content unexamined.

Editorial placement: this extends Spider/BIRD’s static question-plus-schema setting toward document use, project navigation and execution feedback. Different tracks and older benchmarks do not form a matched model-difficulty curve; the change in workflow requirements is the stronger comparison.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

The original agent track reports 632 tasks; Lite has 547. The agent receives a heuristic 30-step request and stops after three repeated results or an action exceeding 120 seconds. Lite uses temperature 0 and 128K context; BigQuery value linking is omitted.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

V1; within-track comparisons only. SR is focused-output task success; Lite EX is focused execution agreement. Reference plans are privileged inputs.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| Spider-Agent + o1-preview | Original track; 632 reported tasks | SR (%; inconsistent count denominator) | 17.01% | Code/docs/tools; temperature conflict | Table 4, p. 7; C.1, p. 35 |
| Spider-Agent + GPT-4o | Original track; 632 reported tasks | SR (%) | 10.13% | Same named scaffold | Table 4, p. 7 |
| DAIL-SQL + GPT-4o | Spider2.0-lite; 547 tasks | EX (%) | 5.68% | T=0; sampled values/docs; no reference plan | Tables 5/10, pp. 7/9 |
| DAIL-SQL + GPT-4o + reference plan | Spider2.0-lite; 547 tasks | EX (%) | 8.78% | T=0; human reference plan | Table 10, p. 9 |

Fact source: [Table 4, p. 7; C.1, p. 35; Table 4, p. 7; Tables 5/10, pp. 7/9; Table 10, p. 9](https://arxiv.org/pdf/2411.07763v1)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

The 91.2/73.0/17.0 comparison combines earlier GPT-4 methods with Spider-Agent+o1-preview; it is not matched transfer. Table 4’s 17.01% conflicts with the conclusion’s 18.8% and cannot yield a consistent integer numerator over 632. Main-text temperature 0 conflicts with agent Appendix C.1’s 1.0/top-p 0.9. Preserve these unresolved discrepancies.

<!-- EDITORIAL-NEXT:START -->
Next, fix model and budget within the agent track, separately supply the correct files, relevant documentation or reference plan, and classify discovery, execution and artifact failures. A plan’s benefit may come from privileged decomposition rather than transferable planning ability.
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
