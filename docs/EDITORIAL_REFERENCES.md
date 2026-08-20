# Editorial References

This file records the external writing/research conventions that informed the Radar family editorial contract. They are **design references**, not runtime dependencies.

## Google Technical Writing

References:

- https://developers.google.com/tech-writing/two/large-docs
- https://developers.google.com/tech-writing/one/documents
- https://developers.google.com/tech-writing/one/audience

Adopted principles:

- put key points and scope near the start;
- organize large information collections with progressive disclosure;
- write for a specified audience and provide a path from introductory to deeper material;
- use concrete language and structure documents around what the reader is trying to accomplish.

Radar consequence: README supports `scan → expand → deep note → topic library → temporal synthesis` rather than forcing one depth on every reader.

## Clear and concise technical prose

Reference implementation studied:

- https://github.com/softaworks/agent-toolkit/tree/main/skills/writing-clearly-and-concisely

Useful principles adopted:

- active voice when it makes the actor clear;
- concrete nouns and verbs;
- omit needless words;
- avoid promotional/puffy adjectives and generic AI vocabulary;
- reduce excessive formatting and repeated template phrasing.

Radar consequence: the local `EDITORIAL_STANDARD.md` checks specificity and repeated sentence skeletons. It does **not** import or depend on this external skill.

## Research claim discipline

The Radar family also follows the general research-review norm that claims should stay within the evidence actually provided: comparison baselines, experimental assumptions, limitations, and negative results should be visible near the interpretation they constrain.

Radar consequence:

`Research delta → Problem → Mechanism → Closest comparison → Decisive evidence → What remains unproven → Field-map consequence`

For benchmarks, replace mechanism-centric attribution with:

`Measurement delta → Predecessor → Capability × Environment × Protocol → What the score supports → Confounder → What remains unmeasured → Genealogy consequence`

## What we deliberately reject

We do **not** use a generic “humanizer” that adds colloquial fragments, artificial irregularity, emotional language, or stylistic randomness merely to hide model authorship. Those techniques can reduce technical precision.

The target is narrower: remove generic, repetitive, machine-like prose while preserving research density, explicit uncertainty, and causal boundaries.

Likewise, the editorial linter is not a word blacklist. A single phrase such as `important`, `robust`, `值得注意的是`, or an em dash is not evidence of bad writing. The warning condition is **pattern density without corresponding analytical value**.
