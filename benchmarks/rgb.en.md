# RGB: decomposing how a generator uses retrieved context into four failure modes

[中文](rgb.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2309.01431)

## What it measures

RGB uses four English/Chinese diagnostic testbeds for noise robustness, negative rejection, information integration, and counterfactual robustness. Rather than measuring retriever ranking, it controls the supplied context and asks whether a generator uses, rejects, or combines that evidence correctly.

## Compared with what

Many RAG evaluations collapse retrieval and generation into one final-answer score. RGB isolates context use so failures such as finding evidence but misusing it, answering without evidence, or failing to integrate multiple pieces become separately observable.

## Decisive evidence and score boundary

The paper shows that mainstream LLMs behave unreliably when context is noisy, missing, or counterfactual. This supports the need for context-use diagnostics; it says nothing directly about which retriever is better because retrieval is controlled. Score differences across generators or prompts cannot be credited to retrieval.

## Fair comparison conditions

Align the generator, prompt, constructed negatives/counterfactuals, and diagnostic split. Do not compress the four abilities into an opaque current-best number that hides asymmetric failure modes.

## Next evaluation coordinate

The stronger successor connects these diagnostics back to a retrieval loop: can an agent notice conflict, search again, and recover within a tool budget rather than passively consume fixed context?

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use RGB to isolate how a generator uses supplied evidence under noise, counterfactuals, and unanswerability. It is not a retriever benchmark. Improvements from supplying better context do not establish a better search policy.

### What a concrete task looks like

Illustrative task: a question is paired with correct, noisy, answer-free, or counterfactual context, testing evidence-grounded answering. The system must select usable material and recognize when an answer is unsupported.

### Most discriminating experiment

Vary context conditions for the same generator and report each of the four competencies. Keep supplied-context diagnosis separate from end-to-end retrieval tests. Check both over-trust and neglect of retrieved text rather than optimizing robustness in only one direction.

### Pair with

[ragtruth](ragtruth.en.md) · [lit-ragbench](lit-ragbench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
