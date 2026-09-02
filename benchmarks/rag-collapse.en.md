# RAG Collapse

## What it actually measures

RAG Collapse is not a one-shot retrieval-relevance benchmark. It asks whether **independent sources are progressively displaced when a fixed model repeatedly retrieves model-authored sources inside a recursive corpus loop**. The measured object is therefore corpus provenance and retrieval-feedback dynamics, not degradation of the model weights themselves.

## What changed relative to the closest predecessor

The closest conceptual predecessor is recursive-training / model-collapse work, where models are repeatedly trained on synthetic generations. RAG Collapse keeps the model weights fixed and moves the recursion into the retrieval context. This isolates a different question: **can the information environment collapse even when the model is not retrained?**

## Decisive evidence

The paper reports an overall collapse rate of **79.6% across 1,528 simulations**. High collapse rates appear under Replace-All, Replace-One, and Search protocols. The important signal is not a single answer-quality number but the repeated displacement of independent sources across multiple corpus-update mechanisms.

## What the score supports

The result supports the claim that self-authored-source feedback can collapse source diversity in the paper's synthetic recursive-retrieval loops. It does **not** establish that the live web already exhibits the same failure at comparable scale, nor does it identify a particular retriever as the cause. The same model family writes and later reads sources, while collapse and quality are partly model-judged.

## Fair comparison contract

Comparisons should align model family, initial corpus, replacement/search policy, number of feedback rounds, generation budget, and collapse evaluator. If those differ, the comparison is system-level evidence. A particularly important alternative explanation is stylistic self-preference: source displacement should be separated from the possibility that the model simply prefers text written in its own style.

## How to use it in research

This benchmark is more useful as a **RAG validity and deployment-regression coordinate** than as a conventional answer-quality leaderboard. A system that claims to learn continuously from an evolving open corpus should report provenance diversity and independent-source survival together with task quality; average QA accuracy can otherwise hide a progressively narrowing evidence base.

## Next discriminating validation

The highest-value missing evidence is longitudinal live-web evaluation, cross-model authorship, style/content separation, and human provenance labels. The experiment most likely to change the conclusion is not another synthetic replacement rule, but evidence that excess collapse persists under realistic corpus refresh, heterogeneous authorship, and real search ranking beyond ordinary corpus drift.

## Genealogy

The benchmark makes corpus provenance and feedback dynamics a RAG-validity coordinate; `map_delta=reinforces`. It strengthens the argument that static benchmark scores are insufficient when the corpus itself changes through agent activity, rather than replacing standard retrieval-relevance evaluation.

Primary: https://arxiv.org/abs/2608.22118
