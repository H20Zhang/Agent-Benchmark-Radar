# MPBench: separating persistent writes from conditional behavioral influence

<!-- RELEASE-REFERENCE:START -->
> **Release diagnostic (historical reference)** · 2026-06-03 · paper v1 snapshot<br>
> **OpenClaw — Attack success rate: 34.25%** (Persistent-memory poisoning ASR); **HERMES — Attack success rate: 66.67%** (Persistent-memory poisoning ASR)<br>
> Attack-success rates: higher indicates a stronger attack, not a better defender. [Original source](https://arxiv.org/abs/2606.04329)<br>
> From a previously curated original-paper record, for historical reference; not rerun in this update and not current SOTA.
<!-- RELEASE-REFERENCE:END -->

[中文](mpbench.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Read Sections 1–6 and Appendices A–D, all seven tables, taxonomy, threat model and generation templates. Checked PDF metric formulas and image-only JSON schema. Read the official data repository README at the fixed commit. No attack execution, independent judge audit or reproduction. Parsed all released JSON objects for counts and schema labels without executing their content.

[arXiv 2606.04329v2 (2026-06-18)](https://arxiv.org/html/2606.04329v2)

[Auxiliary material (checked 2026-09-30)](https://github.com/Digital-Trust-Lab/mp-bench/blob/6886880a7c29625e0109e0ad91d0e095029f1577/README.md)

[Auxiliary material (checked 2026-09-30)](https://github.com/Digital-Trust-Lab/mp-bench/blob/6886880a7c29625e0109e0ad91d0e095029f1577/adversarial_data.jsonl.jsonl)

[Auxiliary material (checked 2026-09-30)](https://github.com/Digital-Trust-Lab/mp-bench/blob/6886880a7c29625e0109e0ad91d0e095029f1577/benign_data.jsonl.jsonl)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

MPBench separates cross-session poisoning into two stages. After untrusted external content enters a normal task, it checks whether persistent memory contains the targeted behavioral directive. Only successfully written cases receive a related task in a fresh session to test subsequent influence. Attackers cannot directly edit memory/system prompts or impersonate users. Four write paths cover explicit instructions, system retention policies, compaction and experience-to-skill synthesis; six classes span explicit and apparently ordinary factual inputs.

Genealogy: Relative to AgentDojo/InjecAgent current-task injection, it adds persistent writes and later activation. Relative to LoCoMo/LongMemEval benign fidelity, it adds source trust and write authority as safety coordinates. This is a protocol comparison, not claimed data inheritance. A representative task is an agent reading external operational material and later reusing an unauthorized suggestion; this note analyzes measurement without executable payloads.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

The paper reports 3240 attack examples: five classes of 600 and 240 skill cases, plus 2997 benign examples. Meta-Llama-3.1-70B-Instruct generates queries, external context, expected writes and follow-up queries, followed by schema checks and spot checks. Both agents use GPT-OSS-120B with default prompts/memory configurations. OpenClaw lacks skill writing, so inapplicability is not zero performance. Some files are retrieved through tools; email, Slack and web inputs include statically labeled external context rather than complete connector pipelines. ASR is successful writing; RSR is subsequent behavioral influence conditional on successful writing, not simple retrieval recall. An LLM judges semantic matches, but its identity and the human audit sample/agreement are unspecified.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Table 2, reported agent-level macro averages

Equal averages over applicable classes, not pooled sample rates, with different class coverage. Multiplying these macro averages does not yield end-to-end success; RSR is not a fraction of all attack attempts.

Attack pool 3240; OpenClaw excludes the 240 skill cases. Exact evaluated and write-positive counts per row are not printed.

| Agent | ASR write % | Conditional RSR influence % | Applicable classes |
|---|---|---|---|
| OpenClaw | 34.25 | 17.4 | 5 |
| HERMES | 66.67 | 64.7 | 6 |

Locator: Table 2, reported agent-level macro averages · [Source](https://arxiv.org/html/2606.04329v2)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Table 2, selected matched-class contrasts

Shared backbone but different write policies, automatic loading and tool retrieval. HERMES injects a memory snapshot at session start; OpenClaw requires memory_search. This system comparison does not separately manipulate retrieval or write aggressiveness.

Each selected class has a reported pool of 600, but exact completed evaluation counts and write-positive RSR denominators are not supplied.

| Class | OpenClaw ASR % | OpenClaw conditional RSR % | HERMES ASR % | HERMES conditional RSR % |
|---|---|---|---|---|
| Explicit Command Insertion | 18.25 | 44.23 | 42.67 | 86.33 |
| Salience-Driven Compaction | 45.1 | 11.31 | 85.17 | 69.86 |
| Policy-Conformant Fact Injection | 8.33 | 5.93 | 64.5 | 42.12 |

Locator: Table 2, selected matched-class contrasts · [Source](https://arxiv.org/html/2606.04329v2)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Table 3, selected detector adaptation results

Input-detector classification, not end-to-end defense after deployment in an agent. CommandSans adaptation sharply reduces false positives while PromptArmor worsens; adaptation is not uniformly ineffective.

Attack/benign pools 3240/2997; detector test sizes, adaptation train/test split and exact counts are not specified.

| Detector / condition | TPR % | FPR % |
|---|---|---|
| PIGuard original | 38.33 | 0.33 |
| PIGuard adapted | 47.67 | 5.33 |
| CommandSans original | 52.33 | 45.0 |
| CommandSans adapted | 61 | 8.67 |
| PromptArmor original | 67.67 | 1 |
| PromptArmor adapted | 61.6 | 2.67 |

Locator: Table 3, selected detector adaptation results · [Source](https://arxiv.org/html/2606.04329v2)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:result-4:START -->
## Table 4, selected detector signal-strength contrasts

Adapted PIGuard narrows the strong/weak gap while lowering strong-signal detection. Weak signal is a constructed taxonomy class, not all theoretically undetectable attacks.

Exact strong/weak evaluation denominators are not supplied; do not infer them from the full corpus class counts.

| Detector / condition | Strong-signal detection % | Weak-signal detection % |
|---|---|---|
| PIGuard original | 51.67 | 18.34 |
| PIGuard adapted | 48.33 | 46.66 |
| PromptArmor original | 84.44 | 42.5 |

Locator: Table 4, selected detector signal-strength contrasts · [Source](https://arxiv.org/html/2606.04329v2)
<!-- EVIDENCE:result-4:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

Later-session effects establish persistent risk, but there is no long-run decay curve, persistence-disabled control or common benign-task utility measurement. Thus stronger memory is not proven inherently less safe. Differences between packaged agents are not single-variable causal evidence about writing policy. One backbone, static delivery, automatic memory loading and asymmetric class coverage limit transfer; results do not establish current product safety rankings. Four imperfect input detectors do not prove all input defenses impossible. Provenance-aware writing is a proposed direction, not a validated defense here.

The introductory 50.46% ASR and 41.05% RSR are averages of the two agent macro averages, not pooled lifecycle probabilities. Appendix schema prose allows strong/moderate/weak signals, while its pictured schema allows strong/weak and Tables 2/7 classify compaction as strong; exact stratification needs data-level verification. Defense adaptation procedures, disjoint training/testing, temperature, output caps, retries and judge prompts are insufficiently specified for full reproduction. The official repository exposes data and README rather than a complete execution/judging harness at the inspected entry point; reading the paper does not certify reproduction. At fixed commit 6886880a7c29625e0109e0ad91d0e095029f1577, sequential JSON decoding finds 3241 adversarial and 2999 benign objects, not paper counts 3240/2997. Some objects are concatenated on one line, breaking standard JSONL parsing. Attack labels differ from the six paper classes, with no explicit skill-procedure label; signals include moderate and subtle. No undocumented class mapping or deletion was applied. All parsed IDs and objects are unique. The 240 skill-bearing objects do exist but use other attack labels and omit retrieval_query; two further adversarial objects lack expected_memory and retrieval_query. Absence of an explicit skill class label does not mean the skill data are absent.



Next: Pair with AuthMem-Bench and MemSecBench. Under one backbone, delivery channel, task set and memory budget, independently toggle write validation, provenance labels and automatic loading. Report successful writes, retrieval exposure, conditional behavioral deviation and per-example joint success. Add persistence-disabled and legitimate-memory controls, with source/task-cluster intervals, to distinguish protection from simply avoiding memory.
<!-- EVIDENCE:limitations:END -->
