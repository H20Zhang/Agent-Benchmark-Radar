# The Compaction Cliff

## What it actually measures

The Compaction Cliff measures **survival of safety constraints under bounded-context management**. When an agent repeatedly compacts, decomposes, or retrieves state, can explicit rules remain intact and continue to constrain later behavior? The benchmark asks a stricter question than generic memory retention: do different information types need different retention contracts, especially constraints that cannot safely be approximated away?

## What changed relative to predecessors

Work such as MaRS introduces typed memory but often evaluates it through aggregate utility, while LLMLingua-2 and production compactors focus on compression quality or length without treating constraint preservation as a hard metric. This work evaluates exact constraint preservation across compact, decompose, and retrieve operators, making failure modes of different context-management strategies directly comparable.

## Decisive evidence

Sonnet `/compact` constraint retention drops from **0.53 to 0.10 after five rounds**, while TypeCompact remains at **0.96**. TypeDecompose reports **0% locality violation**, and TypeRetrieve reaches **100% recall@50**. The important signal is that a generic semantic compactor can preserve something that looks globally similar while systematically losing non-negotiable constraints, whereas typed operators substantially improve retention in the tested protocols.

## What the score supports

The results support the claim that typed retention better preserves safety constraints in the evaluated setting. They do not establish that every long-running agent becomes safer: behavioral experiments are not strictly token-matched, TypeCompact can retain more context, and the safety guarantee inherits false negatives from the classifier that decides which information is a constraint.

## Fair comparison contract

Initial context, constraint set, number of compaction rounds, token budget, model, classifier, retrieval k, and downstream behavior task should be aligned. If one method keeps substantially more tokens, report **constraint retention versus retained-token budget** rather than only retention rate. Typed methods should also expose classifier false negatives because unrecognized constraints never enter the protected path.

## How to use it in research

The benchmark is useful for studying **information-type-aware policies for agent memory and context compression**. A method claiming safe long-horizon state compression should measure factual recall, preference retention, procedural state, and hard constraints separately; average semantic similarity can hide rare but high-impact rule loss.

## Next discriminating validation

The main gaps are online constraint identification, realistic enterprise/interaction distributions, shared memory across agents, and strictly token-matched behavior. The highest-value test is to compare TypeCompact with generic compactors under the same token budget, unseen constraint types, and real downstream actions and verify that higher retention actually reduces behavioral violations.

## Genealogy

Together with MPBench, InjecMEM, and Utility Under Attack, the benchmark decomposes memory safety across write, retrieval, and compaction lifecycle stages; `map_delta=reinforces`. Its key added coordinate is that **retention policy may need to depend on information type**, not merely whether QA remains answerable after compression.

Primary: https://arxiv.org/abs/2608.22752
