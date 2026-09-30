# SP-Mem: What to remember and when to restore private values

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08-17<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2608.16551)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](sp-mem.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

The full primary paper was read for methods, setup, results and limitations; experiments were not independently reproduced.

Read Sections 1–6 and Appendices A–F, including profile/dialogue generation, all four sanitization strategies, storage and restoration algorithms, domain results, ablations and judge prompts. This is the August 17, 2026 first version. Code was not executed, and synthetic profiles are not treated as real participants.

[Full primary paper](https://arxiv.org/pdf/2608.16551v1) · 2608.16551v1
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## Relation to neighboring evaluations

The paper connects utility-oriented memory systems such as Mem0, Zep and MemOS with query-aware protection in PII-Bench and contextual privacy norms in PrivacyLens. Its added coordinate is the persistent-memory lifecycle: isolate exact values at writing time, check task necessity and consent at query time, and assess both usefulness and disclosure. Correctly recalling a private fact is therefore insufficient: using generalized context without access, or requesting permission when needed, can be the desired behavior. This is a comparison of measurement goals, not a claim that the dataset inherits those benchmarks.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

The pool contains 1,000 synthetic profiles, equally divided across finance, medical, education and mental-support domains. There are 37 privacy fields in eight categories, plus 14 general preference dimensions and four additional dimensions per domain. Rules generate structured fields, Gemma-3-12B-IT enriches open fields, and an external disease dataset seeds medical attributes; consistency checks reject direct contradictions. The 376 subtasks comprise 185 preference-only, 51 privacy-only and 140 mixed tasks. Each user receives 12 coverage tasks and nine random tasks. Llama-3.1-8B-Instruct plays the user and Gemma-3-12B-IT the assistant, progressively disclosing required entities until coverage is complete. The full pool contains 21,000 histories and 54,000 query instances derived from 270 query variants. Histories average 8,530.70 tokens per user under cl100k_base, excluding chat-template overhead.

SP-Mem extracts natural-language facts and relation triples. Searchable vector and graph stores hold non-private information and sanitized representations; separate protected storage holds exact values, linked by mapping keys. Sanitization uses aliases, last-four-digit masking, numerical buckets and model-based generalization. The query analyzer selects a minimal required entity set from a whitelist. Exact values are restored only when needed and consented to; otherwise generation uses sanitized context. An illustrative dinner recommendation needs food preferences rather than an exact home address, while an address-dependent form requires permission first. The paper does not establish cryptographic security for the separate store.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup and scoring

Evaluation uniformly samples 100 users across the four domains, using 2,100 histories and 5,400 queries. Conditions are preference-only, privacy-only with consent allowed/denied, and mixed with consent allowed/denied. All memory systems use GPT-5.2-Chat for construction; response backbones are GPT-5.2-Chat, Llama-3.1-8B-Instruct, DeepSeek-V3.2 and Qwen3-14B. Appendix E states that memory baselines share query analysis, consent handling and generation while changing storage/retrieval backends. A separate full-context baseline receives the complete history. Stores are Qdrant and Neo4j; local open models use A40 GPUs. Retrieval counts, sampling temperatures, token caps and exact baseline versions are not fully specified.

GPT-4.1 compares anonymized response pairs. Task completion P-TC applies to every condition; personalization P-PQ applies only to preference-bearing tasks. Every pair is judged in both orders: a decisive winner is retained only if both orders agree, and other cases become ties. Reported quality is (wins + ties)/comparisons, not the strict win rate; separate win/tie/loss counts are absent. PAR checks permission requests against whether exact private information is required. UPU exact-matches responses against the profile inventory for unnecessary or unauthorized values; masked and generalized values do not count. The total query count is not the denominator of every cell because conditions, metric applicability and effective comparison counts differ.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Quality: non-loss is not strict win rate

Each row compares SP-Mem with the named baseline using the same response backbone. Allowed includes preference-only and both consented privacy-bearing conditions; denied includes the two refused conditions. Units are percentage (wins + ties)/valid pairs in the applicable group; P-PQ excludes privacy-only tasks. GPT-4.1 judges both orders and disagreement becomes a tie. Exact cell denominators are not listed.

| Comparison condition | P-TC (%) | P-PQ (%) |
|---|---|---|
| GPT-5.2-Chat / allowed / Full-context | 65.35 | 79.13 |
| GPT-5.2-Chat / allowed / Mem0 | 90.87 | 94.24 |
| GPT-5.2-Chat / denied / Full-context | 91.45 | 90.86 |
| Qwen3-14B / allowed / Full-context | 45.09 | 71.70 |
| Qwen3-14B / allowed / Mem0 | 80.63 | 89.54 |
| Qwen3-14B / denied / Full-context | 86.65 | 88.88 |

Source: Tables 3–4 · [Paper](https://arxiv.org/pdf/2608.16551v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Direct exposure remains nonzero

UPU is responses exposing unnecessary or unauthorized exact private values divided by valid responses in the condition; lower is better. These are narrative aggregates; backbone aggregation weights and per-condition denominators are not specified. Masked/generalized values do not count as exact exposure.

| System and condition | UPU (%) |
|---|---|
| SP-Mem / Preference-only | 0.33 |
| Full-context / Preference-only | 16.00 |
| SP-Mem / Privacy-only-denied | 1.12 |
| SP-Mem / Mixed-denied | 1.21 |

Source: Section 4.4; Figure 4 · [Paper](https://arxiv.org/pdf/2608.16551v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Permission detection and token trade-offs

PAR covers all five conditions: recall is divided by tasks requiring exact private information, precision by tasks requesting authorization; both are 0–1 proportions. Token ratios normalize the same-backbone full-context total to 1.00. They are not dollar costs and do not establish amortized construction cost.

| Response backbone | PAR recall | PAR precision | SP-Mem token ratio | Mem0 token ratio |
|---|---|---|---|---|
| GPT-5.2-Chat | 0.84 | 1.00 | 0.31 | 0.25 |
| Llama-3.1-8B-Instruct | 0.92 | 1.00 | 0.30 | 0.23 |
| Qwen3-14B | 0.91 | 1.00 | 0.26 | 0.21 |

Source: Tables 5–6 · [Paper](https://arxiv.org/pdf/2608.16551v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:interpretation:START -->
## What the evidence supports

Low exact-value exposure can coexist with high non-loss rates, but the results do not establish privacy at zero utility cost or universal superiority over full context. Qwen3-14B has only 45.09% task-completion non-loss against full context in the allowed group, implying decisive losses on more than half of comparisons. Higher rates elsewhere may contain many ties. Strong denied-group non-loss suggests sanitized information can support useful service without exact values. Hybrid vector-plus-graph memory exceeds 80% overall non-loss against either single branch, but this still does not identify strict win rates. SP-Mem uses fewer tokens than full history and more than existing memory baselines.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source gaps and next test

Synthetic profiles, fixed entity vocabularies and explicit consent labels simplify real ambiguity; profile-conditioned preferences may also encode particular associations. UPU excludes inference, paraphrased disclosure, re-identification, multi-turn attacks and compromise of protected storage. Last-four-digit masks and city-level generalizations can still be sensitive. Human-judge agreement, confidence intervals and repeated-run variability are not reported. Although latency is mentioned in the introduction, the principal cost table reports relative tokens, not end-to-end latency or monetary cost. A useful next test holds users/tasks fixed while switching consent, publishes win/tie/loss counts and valid denominators, adds semantic disclosure and multi-turn attacks, and audits that restoration logs contain only authorized fields.

Scope reconciliation: 14 general plus four domain-specific preferences describes each user; the appendix’s 16 domain-specific dimensions cover all four domains. The scenario table has seven tested general scenarios plus profile completion used only for histories, so not all eight general entries enter testing. Figure 4’s narrative provides aggregate exposure rates without clearly specifying backbone weights or effective denominators by condition; the table above labels them as reported aggregates rather than assigning them to one model. Retrieval configurations and implementation-level protection of the exact-value store still require code inspection.
<!-- EVIDENCE:limitations:END -->
