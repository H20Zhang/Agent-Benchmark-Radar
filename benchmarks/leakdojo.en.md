# LeakDojo: content leakage and defenses in controlled RAG configurations

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-04-07<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://aclanthology.org/2026.findings-acl.287/)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](leakdojo.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked selected results; no independent experiment reproduction.

Read all twenty-two pages of the proceedings paper, limitations and Appendices A–B, including interfaces/corpora, metric formulas, configuration matrices, budget/temperature/threshold analyses, costs and complete prompts; visually checked Tables 3 and 9. No attacks were executed.

[ACL Findings 2026 · 2026.findings-acl.287 · 5790–5811](https://aclanthology.org/2026.findings-acl.287.pdf)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

Experiments use isolated RAG systems over public SciFact, NFCorpus, FiQA and Enron corpora, treating each original document/email record as a non-overlapping retrieval unit. Evaluators know the corpus; the tested attacker sees only queries/final responses and at most domain knowledge. An illustrative defensive evaluation distinguishes repeated disclosure of one record from recovery of new records, then enables input-intent/output-content checks and measures protection plus benign-QA costs. Implementations adapt prior methods—for example generated PIDE queries and RAG-Thief through another code framework—so matching attack labels do not imply exact reproduction.

Editorial placement: prior work such as PoR and RAG-Thief studies particular extraction strategies. LeakDojo separates query generation, extraction instructions, retrieval and defenses under controlled budgets. Beyond QA accuracy or generic injection success, it measures distinct retrieval coverage, disclosure triggering and reconstruction quality—not production authorization or tenant isolation.

[Source](https://aclanthology.org/2026.findings-acl.287.pdf)
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

The default budget is N=200. Main cells average vanilla RAG, reranking, and reranking plus rewriting. Retrieval uses bge-large-en-v1.5 with Chroma/MMR, a forty-candidate pool and similarity threshold 0.75; bge-reranker-large reranks, while gpt-4.1-mini handles rewriting/summarization and several auxiliary generators. Decoding is greedy. CCL divides unique leaked units by ideal retrieval capacity kN; ARC divides unique retrieved units by kN. Neither is the fraction of the entire corpus recovered. SLT counts queries whose response exceeds 0.5 ROUGE-L recall against any retrieved unit. CRR averages, over successful queries only, the best unit’s coverage by contiguous matching blocks of at least fifty tokens. Output defense instead thresholds ROUGE-L F1, a different criterion.

[Source](https://aclanthology.org/2026.findings-acl.287.pdf)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Model-dependent strategy reversal on the same corpus

Public Enron 2015 corpus, two hundred queries, averaged over three RAG configurations. CCL/ARC use kN; SLT uses query count. CCL 88.3% does not mean recovery of 88.3% of the Enron corpus, and model token costs are not matched.

| Model/strategy | CCL (%) | SLT (%) | ARC (%) |
| --- | --- | --- | --- |
| Gemini-3-flash / PoR | 88.3 | 100 | 88.4 |
| DeepSeek-V3 / PoR | 6.8 | 12.0 | 75.4 |
| DeepSeek-V3 / RAG-Thief | 64.4 | 97.3 | 74.8 |

Source location: Table 2, proceedings p. 5795 (PDF p. 6); Appendix A.3 · [Source](https://aclanthology.org/2026.findings-acl.287.pdf)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Protection against the default configuration does not establish general safety

FiQA, DeepSeek-V3, T2 reranking+rewriting, two hundred queries. These are reported controlled-evaluation facts without attack prompts. CCL uses kN; rows changing both instructions and defenses are not a single-defense causal contrast.

| GEN-PIDE configuration | CCL (%) |
| --- | --- |
| Default / no defense | 57.5 |
| Default / input detector | 0.2 |
| CodeClaim / input detector | 59.6 |
| CodeClaim / input and output detectors | 26.5 |

Source location: Table 3, proceedings p. 5797 (PDF p. 8) · [Source](https://aclanthology.org/2026.findings-acl.287.pdf)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, limitations and next experiment

Attack rankings reverse across models, so one high score cannot summarize universal risk. CCL≈SLT×ARC is an empirical fit, not proof of statistical independence; instruction-following/leakage correlation is not causal. Summarization may reduce near-verbatim leakage while losing grounding, without establishing an inevitable trade-off between all useful QA and security. Blocking old instruction styles can overstate protection when other tested configurations still disclose content. English public corpora, unit lengths, query budgets and incompletely matched generation costs limit production extrapolation.

The abstract states fourteen models while Table 4 lists fifteen configurations; the main result uses six, and supplementary settings should not be silently combined. Table 9’s CCL falls from 56.5 at temperature zero to 39.4 at 0.8, qualifying the prose’s “small impact” claim. Near Table 3, the new GEN-PIDE value 59.6 is compared with 7.3, but that baseline belongs to TGTB; GEN-PIDE’s corresponding undefended value is 57.5. Retriever settings list top_k=10 and final top_n=5; reproduction must pin the actual final k rather than infer leaked counts from percentages.

Within authorized isolated corpora, pin final retrieval depth, token/query budgets and record lengths; repeat seeds and measure verbatim/semantic leakage plus benign-QA correctness. Report coverage relative both to kN and to corpus size. Separate defense selection from held-out stress tests and measure false blocking and residual exposure after content transformation.

[Source](https://aclanthology.org/2026.findings-acl.287.pdf)
<!-- EVIDENCE:limitations:END -->
