# LifeSide: long-term user understanding is not the same as factual recall

[中文](lifeside.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

## What it measures

LifeSide scales personal-memory evaluation to 2,000 personas and roughly 111K tasks spanning memory tracking, user understanding, privacy control, and emotional companionship. The target is not only what a user said before, but whether a system forms an appropriate, bounded user model and uses it well over long interaction histories.

## Compared with what

LoCoMo and LongMemEval primarily emphasize conversational facts and reasoning. LifeSide adds persistent user understanding, privacy, and companionship, directly challenging the assumption that saturation on existing memory QA means personalized memory is solved.

## Decisive evidence and score boundary

The work reports that models which saturate prior memory benchmarks still fail substantially on long-horizon user understanding and companionship. This supports a benchmark-coverage gap, not a causal claim that one memory architecture is responsible; backbone capability, persona construction, and the judge all matter.

## Fair comparison conditions

Align persona/history generation, privacy policy, answerer, and judge, and inspect task families separately. Collapsing factual recall with emotional or privacy behavior into one number hides the capability structure.

## Next evaluation coordinate

The next step connects long-term user models to real permissions, deletion, tool-mediated actions, and externally observable consequences of incorrect personalization.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use LifeSide to study interactions among memory, user understanding, and privacy in persistent-companion tasks, not to rank a memory component in isolation. With simulated personas and environments, results first describe behavior under those simulation rules; real longitudinal relationships require separate validation.

### What a concrete task looks like

Illustrative task: a user's goals or emotional context change across sessions, and the assistant must use relevant history without revealing personal content in an inappropriate setting. Personal relevance and appropriate information use are separate outcomes to evaluate together.

### Most discriminating experiment

Vary memory and privacy policy independently over identical simulated-user trajectories. Report assistance quality and inappropriate disclosure rather than only a composite reward. Repeat with a simulator not used during development to test dependence on persona generation or evaluator preferences.

### Pair with

[dynamicmem](dynamicmem.en.md) · [gatemem](gatemem.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
