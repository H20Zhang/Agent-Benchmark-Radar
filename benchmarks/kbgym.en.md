# KBGym / Training a Knowledge Base

## What it actually measures

KBGym turns a knowledge base from a pre-built static index into a **persistent state that can be trained from supervised experience, frozen, and then evaluated independently**. A curator sees supervised questions and gold answers and edits the store; after freezing, an independent reader answers both trained and unseen questions at different supervision-coverage levels. The object is therefore whether training-time edits to knowledge representation transfer to future queries.

## What changed relative to predecessors

Systems such as HippoRAG generally build structured retrieval state from the full corpus without question-answer supervision. KBGym explicitly treats `(question, answer)` pairs as training signals and stratifies evaluation by whether future questions share answer keys with the supervised set. This separates memorization of trained questions, transfer through shared keys, and generalization beyond the covered structure.

## Decisive evidence

The corrected v2 results report roughly **25% action saving and +0.294 F1** on trained questions. For unseen questions, the gain falls with answer-key coverage: **+0.176 F1 for both-key, +0.059 for one-key, and no gain for neither-key**. Only **27.6% of the corpus** is covered by training. The important result is therefore the strong coverage dependence, not a blanket claim that editing the KB improves all queries.

## What the score supports

The benchmark supports the claim that supervised QA can train persistent knowledge state in the tested synthetic atomic-document setting, with benefits tightly linked to overlap between training keys and future queries. It does not establish general KB improvement: low corpus coverage, a single seed, and same-family curator/reader models limit the inference.

## Fair comparison contract

A fair comparison should align curator and reader models, allowed edit actions, number of training questions, freeze point, reader action budget, document construction, and the coverage split. Trained, both-key, one-key, and neither-key results should be reported separately so an average score cannot hide dependence on supervision coverage.

## How to use it in research

KBGym is particularly useful for **self-improving representations and learned retrieval state**, because it makes “how should an agent change its knowledge store after seeing historical QA?” directly measurable. For new methods, the most informative result is a benefit-versus-supervision-coverage curve and a comparison against simpler cache or exemplar accumulation to test whether structural edits generalize beyond shared keys.

## Next discriminating validation

The main gaps are cross-model transfer, multiple seeds, natural corpora, and online/prequential evaluation. The highest-leverage question is whether trained knowledge structures still improve the **neither-key** region when curator and reader come from different model families, documents are natural rather than synthetic atomic facts, and the query distribution evolves over time.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use KBGym to study where gains arise when optimization targets an editable knowledge store rather than model weights. Overall improvement is less informative than performance on unseen questions, uncovered keys, and new structures. Writeback of training answers requires explicit leakage controls.

### What a concrete task looks like

Illustrative task: a curator edits a persistent document store using training questions and feedback, then the store is frozen for a fixed reader. New representations may improve access or merely cache training answers; different controls distinguish these mechanisms.

### Most discriminating experiment

Hold out questions, entity keys, and relation structures separately. Compare the original store, answer caching, budget-matched structural edits, and random edits with a frozen reader. Charge curation cost and test reader transfer; out-of-coverage gains are needed for claims beyond caching.

### Pair with

[structmemeval](structmemeval.en.md) · [snapshot-compatibility-audit](snapshot-compatibility-audit.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

KBGym makes the corpus a trainable and auditable frozen state object; `map_delta=early_signal`. It is closer to a benchmark for representations that learn from query history than to a conventional RAG retrieval leaderboard.

Primary: https://arxiv.org/abs/2608.21829
