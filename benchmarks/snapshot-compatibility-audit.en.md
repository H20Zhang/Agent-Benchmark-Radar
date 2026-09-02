# Snapshot Compatibility Audit

## What it actually measures

This audit does not ask only whether a larger corpus improves average accuracy. It asks whether **the same RAG agent changes answers to the same queries after a corpus-snapshot expansion by more than its own within-snapshot sampling variability**. Corpus version becomes an explicit deployment-regression variable: aggregate quality can stay nearly flat while many individual queries become behaviorally incompatible.

## What changed relative to predecessors

Stable-RAG and Con-RAG style evaluations usually perturb evidence under a fixed evaluation setup. This audit uses nested corpus snapshots to approximate an index/corpus upgrade and estimates within-snapshot disagreement as the agent's own stochastic baseline. Cross-snapshot churn is then interpreted relative to that baseline, producing **excess churn** instead of attributing every answer change to the corpus update.

## Decisive evidence

On NQ, reported excess churn is **6.438 percentage points exact** and **10.250 points semantic**, even though aggregate EM changes by only **−1.50 points**. **Forty stable flips account for 10.00 points of semantic churn.** The central result is therefore that similar aggregate benchmark scores do not imply behavioral compatibility between two corpus snapshots.

## What the score supports

The audit supports the existence of snapshot-compatibility failures beyond same-snapshot stochastic variation in the tested setup. It does not establish that every flip is harmful: some changes can be equivalent paraphrases, legitimate knowledge updates, or corrections from a wrong answer to a right one. Churn and harm must therefore be measured separately.

## Fair comparison contract

Generator, retriever, query set, sampling configuration, snapshot-nesting rule, and semantic evaluator should be held fixed. Temperature and top-p are particularly important because they alter the within-snapshot disagreement baseline itself. Shard ordering and document-entry order also affect what the snapshot-growth intervention actually means.

## How to use it in research

The metric is useful as a **compatibility regression test for production RAG**. When a corpus, embedding model, or index changes, aggregate accuracy alone can miss user-level breakage. A stronger release gate reports aggregate quality, within-snapshot variance, cross-snapshot excess churn, and the fraction of stable flips that are harmful versus beneficial.

## Next discriminating validation

The main gaps are live corpus refresh, multi-step agent trajectories, causal attribution to specific documents, and explicit harm measurement. The highest-leverage next step is to identify which newly added or re-ranked evidence causes stable flips and separate correct updates, harmless wording changes, and true regressions.

## Genealogy

The audit makes corpus version part of the RAG regression contract; `map_delta=reinforces`. It adds a **deployment-compatibility** coordinate that static answer-quality benchmarks usually miss rather than replacing conventional answer-quality evaluation.

Primary: https://arxiv.org/abs/2608.22856
