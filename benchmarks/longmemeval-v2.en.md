# LongMemEval-V2: workflows and file tools for action-history retrieval

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-05<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2605.12493)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](longmemeval-v2.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Substantive main 1–6 and Appendices A–E including annotation, evaluation rubrics, full listed controller/sandbox prompts, ablations, qualitative evidence and limitations. Printed numeric tables inspected; graphical curves and screenshot pixels not independently remeasured. No code/execution run.

[arXiv 2605.12493v1 (2026-05-12)](https://arxiv.org/html/2605.12493v1)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

Sequentially insert pre-collected web trajectories, retrieve compact multimodal evidence, then let a fixed reader answer 451 questions. Separate static state, dynamic changes, workflow, gotchas and false-premise awareness. R uses state/event/note pools; C searches files with manifests, workflow instructions and inspection helpers.

Editorial placement: LongMemEval-V2 continues long-term memory QA but centers user–agent tool-use histories and compares file/coding workflows with retrieval. It is not merely a longer original dataset; changed questions and controllers prevent direct subtraction of cross-version scores. This is an evaluation-coordinate comparison, not a claim of direct dataset inheritance.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

Small has separate domain-shared 100-trajectory haystacks, about 25M tokens; Medium uses roughly 500/question, about 115M. Qwen3.5-9B reader, 200K-token context cap; sampled temperature 0.6/top-p 0.95. R controller Qwen3.5-9B thinking with Qwen3-Embedding-8B; coding controller GPT-5.4-mini xhigh in Codex 0.117.0. Query concurrency capped 3. Structured answers use matching; GPT-5.2 medium judges gotchas/premise answers.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Main comparisons also change the controller

Answer accuracy and query latency; not lifecycle cost or browser task success. Shared reader and cap; controller models differ by family. C versus Codex is the closer matched controller comparison.

451 questions per tier; overall includes premise questions

| System | Small accuracy (%) | Small query latency (s) | Medium accuracy (%) | Medium query latency (s) |
|---|---|---|---|---|
| RAG: query→slice+notes | 51.0 | 0.2 | 45.9 | 0.3 |
| AgentRunbook-R | 58.6 | 26.9 | 57.0 | 25.8 |
| Codex | 69.9 | 177.2 | 68.7 | 185.8 |
| AgentRunbook-C | 74.9 | 108.3 | 70.1 | 139.9 |

Locator: Table 2, main methods · [Source](https://arxiv.org/html/2605.12493v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Helper functions do not improve every split

 Same coding controller; helpers improve Small but their removal slightly improves Medium, so no blanket accuracy benefit.

The subset and protocol are specified above; exact per-cell sample counts are not supplied.

| System | Small accuracy (%) | Medium accuracy (%) |
|---|---|---|
| AgentRunbook-C | 74.9 | 70.1 |
| AgentRunbook-C without workflow | 70.1 | 64.1 |
| AgentRunbook-C without helper functions | 71.4 | 71.8 |

Locator: Table 2, C ablations · [Source](https://arxiv.org/html/2605.12493v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Oracle evidence uses a different question subset

 Direct QA, not context-gathering; evidence selection and notes change inputs. Not a hard ceiling for main score.

Non-premise/ non-abstention subset, distinct from full 451-question main results; exact count not stated in this table

| System | Direct oracle trajectories (%) | Oracle slices+notes (%) |
|---|---|---|
| Qwen3.5-9B (thinking) | 59.6 | 82.5 |
| GPT-5.4-mini (medium) | 65.3 | 86.3 |

Locator: Figure 4/tabulated pilot, Appendix B · [Source](https://arxiv.org/html/2605.12493v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

File scaffolding improves the measured accuracy/latency tradeoff, yet no live task-execution or lifelong-update gain is tested. Questions are selected to defeat frontier no-history models, limiting natural-traffic prevalence claims. UNKNOWN scores 0; gotchas permit one correct noncontradictory insight, while premise rubric also accepts explicit inability to verify the live instance.

Table 1 says 100–498 sessions, prose targets 500; report approximately 500 rather than exact every-item size. Query-generation template includes question_type and original_goals metadata; audit parity with baseline inputs before causal interpretation.

Next: Compare R and C under the same controller and cost budget; separately measure insertion, query and reader costs. Preserve exact Small/Medium evidence seeds, test new environments, then add executable downstream tasks with and without history.
AgentRunbook-C preserves raw trajectories and gathers evidence rather than compressing the whole archive. It selects at most 20 states and returns at most 200K context tokens. Two-tier means 72.5/69.3/48.5 refer to C/Codex/slice+notes; 48.5 excludes AgentRunbook-R at 57.8.
<!-- EVIDENCE:limitations:END -->
