# VAKRA: policy-constrained multi-hop reasoning over APIs and documents

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2608.12282)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](vakra.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked selected results; no independent experiment reproduction.

Read all substantive text across twenty-nine pages and Appendices A–J, including staged metrics, complete generation/judging prompts, model configurations, container and runner listings; visually checked Table 3 and Figure 6.

[arXiv 2608.12282v1 · 2026-08-12](https://arxiv.org/pdf/2608.12282v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

VAKRA turns BIRD databases into locally executable APIs and adds Wikidata5M/ClapNQ documents. SLOT composes nine generic operations; SEL offers twenty-six more specialized operations; Dashboard endpoints encapsulate computation, with domain-level rather than global tool exposure. Entity/parameter links generate API chains and API-to-document or document-to-API compositions. Mistral-Large-2411 generates questions, with Mixtral-8x22B assisting quality and cross-source answerability filtering. Policies can disable a needed source, making explicit inability to answer appropriate. Tuning and test sets do not share original BIRD queries, but capability settings can share source queries; columns are not matched component ablations.

Editorial placement: LiveAPIBench is the paper’s direct executable-API foundation; VAKRA adds entity transfer across documents/APIs, multi-hop chains and tool policies. Relative to CRAG-style answer evaluation, it also checks recovered information and prohibited calls. The extension concerns composition and policy constraints, not solved dynamic enterprise permissions.

[Source](https://arxiv.org/pdf/2608.12282v1)
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

Models use LangGraph ReAct with MCP access to domain SQLite APIs and ChromaDB retrieval embedded by granite-embedding-english-r2; raw databases and indexes are hidden. Live APIs mean actual local execution, not drifting production internet services. Predicted calls are re-executed, followed by information containment and GPT-OSS-120B semantic checks. Passing trajectories then receive final-answer groundedness and factual-consistency checks from the same temperature-zero judge. Disallowed-source calls are checked deterministically and fail even with a correct answer. Overall evaluation is therefore neither purely execution-based nor string matching. The paper describes fixed query timeouts and iteration caps without their main-experiment values; optional tool shortlisting is not clearly pinned.

[Source](https://arxiv.org/pdf/2608.12282v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Selected completion rates across distinct task settings

Table 2 test sizes are 549, 1,397, 1,597, 869 and 644, respectively, with 664 reported elsewhere for the last setting. Shared ReAct/local tools but different questions across columns; grading includes execution checks and GPT-OSS-120B judging. Multi-source scoring includes policy checks and internal weighting, preventing direct reconstruction of binary correct counts.

| Model | SEL (%) | SLOT (%) | Dashboard (%) | Multi-hop API (%) | Multi-source/policy (%) |
| --- | --- | --- | --- | --- | --- |
| GPT-5.5 | 51.0 | 50.04 | 70.4 | 52.4 | 26.0 |
| Qwen-3.5-397B | 42.3 | 47.8 | 46.7 | 30.0 | 16.6 |
| GPT-OSS-120B | 40.1 | 42.7 | 50.5 | 25.1 | 15.5 |

Source location: Tables 2–3, pp. 5–6; scoring Section 4, p. 5 · [Source](https://arxiv.org/pdf/2608.12282v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Success when policies change answerability

Three policy categories within the multi-hop/multi-source setting, not a randomized same-question policy intervention. Exact subclass counts are not clearly reported, and total counts conflict at 644/664; percentages are retained as reported.

| Model | Policy makes unanswerable (%) | Policy leaves answer unchanged (%) | No policy (%) |
| --- | --- | --- | --- |
| GPT-5.5 | 4.9 | 40.7 | 31.9 |
| GPT-OSS-120B | 17.1 | 24.7 | 16.8 |

Source location: Table 3 final three columns, p. 6; Section 5.2, p. 7 · [Source](https://arxiv.org/pdf/2608.12282v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, limitations and next experiment

Interface changes and longer chains correlate with different scores under the common controller, but samples, tool sets and grading differ; column differences cannot all be attributed to one added hop. Overall scoring aggregates settings and double-weights cross-source questions within the multi-source setting; this note retains component rates rather than inventing a uniform pass rate. GPT-OSS-120B is both evaluated and used as judge, motivating judge-sensitivity tests. Claude Opus 4.7 covers only a cost-limited subset. The three-reviewer audit samples sixty questions per setting rather than auditing the entire corpus. Synthetic links, source-exclusion filters and local determinism do not establish reliability under real enterprise permissions, changing state or recovery.

Table 2 and the quality study give 644 multi-source test samples, while the main text and Appendix C.2 give 664, split into 244 policy and 420 no-policy samples; the denominator conflict is unresolved. The headline exceeds 8,000 APIs whereas Appendix C.5 lists 7,087 Dashboard tools, a subset rather than an inventory simultaneously shown to every model. The human-study prose says five dimensions and 1,800 judgments, while the appendix lists four multi-hop and six multi-source dimensions; several κ values are near zero or negative, so raw agreement of 77%/90% is not a complete reliability guarantee.

Pin manifests and scoring code, reconcile 644 versus 664 samples and publish budgets. On identical underlying questions, vary interface abstraction, supply correct intermediate entities or replace retrieved evidence, measuring tool validity, information recovery, answer correctness and abstention separately, with independent judges and human spot checks.

[Source](https://arxiv.org/pdf/2608.12282v1)
<!-- EVIDENCE:limitations:END -->
