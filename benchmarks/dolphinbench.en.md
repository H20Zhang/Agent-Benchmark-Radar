# DolphinBench: accuracy, cost and latency of history-dependent actions

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-09-21<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2609.24971)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](dolphinbench.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Read the complete six-section v2 paper, including both tables and construction/verification diagrams. Read complete README and CANONICAL_EVALUATION.md at pinned repository revision 81cb6f8405b40a9e76089cef650806a80af06ea2. No full raw-trace audit, code execution or independent reproduction.

[arXiv 2609.24971v2 (2026-09-22)](https://arxiv.org/html/2609.24971v2)

[Auxiliary material (checked 2026-09-30)](https://github.com/mem0ai/dolphinbench/blob/81cb6f8405b40a9e76089cef650806a80af06ea2/README.md)

[Auxiliary material (checked 2026-09-30)](https://github.com/mem0ai/dolphinbench/blob/81cb6f8405b40a9e76089cef650806a80af06ea2/docs/CANONICAL_EVALUATION.md)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

DolphinBench asks agents to complete simulated-app work using earlier user history rather than answer historical-fact questions. Three knowledge-work personas each have about 500,000 user-message tokens. Agents ingest dated messages and generate their own replies, then freeze completed memory while each test starts fresh conversation/app state. Requests omit required remembered recipients, dates, preferences or content. Tasks contain one to four separately graded actions and pass only if all checks pass.

Editorial placement: Relative to LoCoMo, it adds history-dependent app actions and ingestion-through-testing costs. Relative to MemoryArena’s dependent subtasks, it tests frozen-history utility without learning during the test sequence. This paper’s description of Mem2ActBench as complete simulated execution is too broad: that benchmark’s main setting supplies the correct tool and measures arguments.
Illustrative task: “Send the update to the person responsible for this project” omits the contact and preferred format stored in history. Success requires the correct recipient and content in the same simulated send action.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

The CEO, infrastructure engineer and product manager each have 200 tests, totaling 600. The 500,000-token measure covers user content only, excluding generated assistant replies. Certification requires GPT-5.6-Luna to pass twice with relevant original history and fail twice without it, followed by inspection for missing-information rather than tool defects. Grading combines deterministic call checks with GPT-5.6-Sol semantic checks; recipient/content requirements must hold in the same send call. Total USD cost includes ingestion, testing and memory processing; median task latency includes tools but not ingestion waiting. Table 2 reports 13 configurations without repeated-run intervals, fully uniform budgets or independent human judge validation.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Table 2, selected Hermes / GPT-5.6-Luna configurations

Hermes and GPT-5.6-Luna are fixed, but each memory configuration ingests independently. Values are paper-v2 reports, not current prices or a live board; totals are not recomputed from rounded components. Built-in zero memory cost means no separately billed memory component, not free ingestion.

600 tasks across three personas; total costs cover the reported ingestion/test run, not USD per task.

| Memory system | Task success (%) | Agent cost (USD) | Memory cost (USD) | Total cost (USD) | Median task latency (s) |
|---|---|---|---|---|---|
| Built-in memory | 65.67 | 61.48 | 0 | 61.48 | 44.35 |
| Mem0 | 70.67 | 61.54 | 34.68 | 96.21 | 37.69 |
| Hindsight | 69.5 | 57.99 | 26.66 | 84.65 | 55.31 |

Locator: Table 2, selected Hermes / GPT-5.6-Luna configurations · [Source](https://arxiv.org/html/2609.24971v2)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Table 2, selected Claude Code / Claude Sonnet 5 configurations

Claude Code and Claude Sonnet 5 are fixed. Keep this group separate from Hermes; backbone/harness differences are not backend effects. Honcho outscores Mem0 here, unlike the Luna group.

600 tasks per configuration; one reported aggregate without repeated-run intervals.

| Memory system | Task success (%) | Total cost (USD) | Median task latency (s) |
|---|---|---|---|
| Built-in memory | 26.33 | 1132.75 | 32.19 |
| Mem0 | 32.33 | 1830.57 | 42.3 |
| Honcho | 35.83 | 1565.82 | 37.92 |

Locator: Table 2, selected Claude Code / Claude Sonnet 5 configurations · [Source](https://arxiv.org/html/2609.24971v2)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Pinned README dataset table, user-message corpus sizes

Counts use o200k_base over user messages only. Generated replies and memory representations add processing; multi-year simulated dates are not years of real provider operation.

Three complete histories; 600 total tasks.

| Persona | User-message tokens | Tasks |
|---|---|---|
| Alex Valdez | 500109 | 200 |
| Morgan Chen | 500100 | 200 |
| Riley Tanaka | 500056 | 200 |

Locator: Pinned README dataset table, user-message corpus sizes · [Source](https://github.com/mem0ai/dolphinbench/blob/81cb6f8405b40a9e76089cef650806a80af06ea2/README.md)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

Certification is conditional on the selected Luna agent and two samples, not proof that every model must fail without history or a model-independent 100% ceiling. The certifier is also the strongest configuration’s backbone, creating possible selection affinity. Authors are affiliated with Mem0, which is evaluated; independent reproduction and run evidence remain important. Three synthetic personas, short action tasks and simulated apps do not establish cross-user transfer, live-service robustness or interleaved lifelong use. Common interfaces do not equalize context, internal models, cost or latency.

The pinned canonical guide says all three harness/model groups use five memory systems, whereas the paper and README show only three Claude Code systems; preserve the paper’s 13-row coverage. The guide also retains accepted Morgan-only 82/200, 138/200 and 126/200 results with 18 approved reruns; these are not the 600-task Table 2 results. Supermemory’s self-hosted compatibility patch is explicitly disclosed; it is not an unmodified hosted-product result. Hindsight client 0.6.1 in runtime versus 0.9.2 tooling illustrates why actual run provenance matters. Selected displayed cost components can differ by one cent from printed totals; preserve reported totals without inventing a reconciliation.



Next: Fix ingestion agent, executor, tools and grader across no-history, budget-matched retrieval and supplied relevant history, logging evidence arrival separately from action correctness. Report ingestion, maintenance, query cost and amortization, and repeat whole runs. Treat test-time updating as a separate online protocol.
<!-- EVIDENCE:limitations:END -->
