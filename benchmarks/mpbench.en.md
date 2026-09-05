# MPBench

## Measurement object

MPBench measures the **cross-session lifecycle of persistent-memory poisoning**. Six classes of malicious content enter persistent memory through four write channels; the benchmark then asks whether the content is actually stored and, in a later session with a relevant query, whether the poisoned record is retrieved and influences the output. The object is therefore the full `write → persist → retrieve → respond` chain rather than immediate prompt-injection success.

## What changed relative to predecessors

LoCoMo and LongMemEval mainly measure benign memory fidelity, while AgentDojo and InjecAgent emphasize same-session hijacking. MPBench separates the write event from the future trigger, so it can distinguish “malicious content entered memory” from “that content was later reactivated by retrieval.” This is why attack success and conditional retrieval success need to be interpreted together.

## Decisive evidence

For the evaluated systems, OpenClaw reports mean **ASR / conditional RSR of 34.25% / 17.40%**, while HERMES reports **66.67% / 64.70%**. PromptArmor reaches only **67.67% TPR at 1% FPR** in the reported setting. The important signal is that risk does not end at admission: in some stacks, a malicious record that persists still has a substantial chance of being surfaced again by a later relevant query.

## What the score supports

The headline numbers measure **system + harness exposure to persistent poisoning**. They do not isolate the base model or the retriever as the cause because the two agents use different write and retrieval policies, and some channels rely on statically labeled context.

## Fair comparison contract

A fair comparison should align backbone, write channel, memory-admission policy, retrieval top-k / ranking, trigger queries, attack budget, and evaluator. Security results should be paired with benign-memory utility: reducing retrieval success by rejecting large amounts of legitimate memory is not evidence of a better memory system.

## How to use it in research

If a memory method claims long-term security or resistance to prompt injection, MPBench is useful for testing the persistence surface, but it should be paired with a benign utility benchmark. Report write acceptance, retrieval exposure, conditional ASR, and end-to-end joint success separately so that the defense can be localized to a lifecycle stage rather than compressed into one number.

## Next discriminating validation

The main gaps are additional backbones, fully executable delivery channels, natural memory drift, and explicit security–utility curves. The experiment most likely to change the conclusion would compare multiple memory stores under the same backbone, attack set, and benign workload instead of comparing two packaged agents with different surrounding systems.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use MPBench for cross-session memory poisoning across write channels. Unlike same-session prompt injection, it requires evidence of persistence before later effects are measured. Differences in channels and write policies should not be interpreted directly as differences in model safety.

### What a concrete task looks like

Illustrative task: external context or tool feedback enters a write session, then a fresh query session performs a benign task. Reappearance there establishes a cross-session path; merely continuing the original context does not provide that control.

### Most discriminating experiment

Match content and budgets across channels and measure write admission, later retrieval, and final deviation, including a persistence-disabled control. Report benign utility with security metrics to distinguish safe writing from apparent safety achieved by not using memory.

### Pair with

[injecmem](injecmem.en.md) · [gatemem](gatemem.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

MPBench creates the key transition from benign memory fidelity to persistent poisoning; `map_delta=splits`. It adds a distinct safety coordinate to memory evaluation: **can memory be maliciously written, and can that state be reactivated later?**

Primary: https://arxiv.org/abs/2606.04329
