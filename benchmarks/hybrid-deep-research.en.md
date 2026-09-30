# HybridDeepResearch: carrying constraints between SQL and search

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-06<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2609.09410)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](hybrid-deep-research.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked the selected results; no independent experiment reproduction.

Read the complete 20-page text and Appendices A–H, including construction, review, tool interfaces, model settings, supplementary results and trajectory cases; visually checked Tables 1–5.

[arXiv 2609.09410v1 · 2026-09-08](https://arxiv.org/pdf/2609.09410v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

HybridDeepResearch separates database–text handoffs into SQL followed by search (SQL2S, 203 tasks), search followed by SQL (S2SQL, 58), and intersection of independently retrieved candidates (Parallel, 119). The 380 tasks use nine LiveSQLBench-Base-Lite databases. Entity anchors and SQL patterns drive generation, followed by execution checks, single-tool exclusion tests and human review. The hard subset contains forty tasks of each type, totaling 120. smolagents uses a single shared-context agent; MiroFlow uses a main agent and workers. Both receive equivalent tool categories while retaining native prompting and context organization.

[Source](https://arxiv.org/pdf/2609.09410v1)

<!-- EDITORIAL-METHOD:START -->
Editorial placement: BrowseComp-style search and BIRD-style database tasks are usually evaluated separately; HybridDeepResearch joins them through SQL-to-search, search-to-SQL and candidate intersection. The added coordinate is cross-tool entity/constraint transfer. Retrieval, execution and orchestration all affect results, preventing exclusive attribution to a shared-context design.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

Read-only SQLite queries return at most 500 rows, with schema discovery left to the agent. Real Web uses live search and page retrieval; Corpus Search uses fixed Wikipedia and FineWeb10BT indexes. Each task has a cap of 300 tool-calling turns and 3,600 seconds, with eight independent main-experiment trials. Pass@8 is the fraction of tasks solved at least once; Avg@8 averages success over eight attempts per task, with N tasks and 8N attempts respectively. S2SQL compares executed results after column alignment; the other types use Qwen3-30B-A3B-Instruct-2507 as an answer judge. Qwen thinking is enabled; proprietary models use medium reasoning effort, with other sampling and quantization settings differing.

[Source](https://arxiv.org/pdf/2609.09410v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Fixed backbone and index: at-least-once versus average success

All 380 tasks, eight trials each; Qwen3.5-397B-A17B-FP8 with Corpus Search; 300-turn/3,600-second task caps, without matched realized cost.

| Scaffold | Pass@8 (%) | Avg@8 (%) |
| --- | --- | --- |
| smolagents | 56.58 | 32.43 |
| MiroFlow | 63.42 | 32.76 |

Source location: Table 1, p. 7; Sections 6.1–6.2 · [Source](https://arxiv.org/pdf/2609.09410v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Selected hard-subset model results

Hard subset of 120 tasks, forty per type and eight trials per task; smolagents + Corpus Search throughout; GLM uses maximum reasoning and proprietary models medium effort, not matched reasoning budgets.

| Model | Pass@8 (%) | Avg@8 (%) |
| --- | --- | --- |
| GLM-5.2-FP4 | 50.83 | 25.00 |
| Claude-Sonnet-4.6 | 52.50 | 28.12 |
| GPT-5 | 54.17 | 27.40 |

Source location: Table 3, p. 8; Appendix E · [Source](https://arxiv.org/pdf/2609.09410v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Scaffold cost: completed-trajectory means and all-attempt timeouts

Hard-120 only, eight trials per task, totaling 960 attempts per scaffold; Qwen3.5-397B-A17B with Corpus Search. Calls and tokens average only trajectories completed within one hour; timeout rates use all 960 attempts. These are not cost statistics for the full-380 comparison above.

| Scaffold | Completed/attempts | Timeout (%) | Mean model calls | Mean tool calls | Mean input tokens (M) | Mean output tokens (K) |
| --- | --- | --- | --- | --- | --- | --- |
| smolagents | 800/960 | 16.7 | 52.5 | 78.1 | 2.78 | 34.9 |
| MiroFlow | 564/960 | 41.3 | 120.1 | 210.0 | 2.06 | 46.1 |

Source location: Appendix G.1, Table 5 and adjacent completion counts, p. 18 · [Source](https://arxiv.org/pdf/2609.09410v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, source limitations and next experiment

Holding the Qwen backbone and retrieval backend fixed, MiroFlow improves Pass@8 but changes Avg@8 only slightly: the gain is in solving a task at least once, not a large improvement in single-attempt reliability. The hard-set leaders differ between Pass@8 and Avg@8. Trajectory statistics show additional calls and timeouts; shorter worker contexts reduce input tokens without establishing lower overall cost. Heterogeneous model and native-scaffold configurations, plus absent uncertainty intervals, limit causal attribution.

The hard subset is selected using both task complexity and pilot-agent failures, not unbiased random sampling. Single-tool ablations establish necessity only for tested configurations; the four PhD reviewers are authors. Supplementary full-set proprietary results use only two trials and cannot be ranked directly alongside main Pass@8 results.

Freeze a test set independently of the evaluated models’ failures and match total token, time and tool budgets. Report average success, at-least-once success, timeouts and cost together. Audit entity-anchor preservation, SQL constraint translation and candidate intersection to test whether shared intermediate evidence improves single-attempt success rather than merely adding retries.

[Source](https://arxiv.org/pdf/2609.09410v1)
<!-- EVIDENCE:limitations:END -->
