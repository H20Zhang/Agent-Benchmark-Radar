# ChemCLIR-Bench: diagnosing language-pair and ranking-depth failures in patent retrieval

[中文](chemclir-bench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2609.23231) · [Code](https://github.com/MohammadKhodadad/Multi-Lingual-QAC) · [Data](https://huggingface.co/datasets/MehdiAstaraki/multilingual_GP)

## What it measures

ChemCLIR-Bench compares same-language and cross-language retrieval over chemical-patent material from Google Patents and EPO. The paper evaluates five languages and eight embedding models. The released pipeline additionally reports Recall@10 and MRR@10 by query language, original versus synthetic-translation origin, target language, and language pair. [Paper](https://arxiv.org/abs/2609.23231) · [Official implementation](https://github.com/MohammadKhodadad/Multi-Lingual-QAC/blob/main/README.md)

## Compared with what

Compared with BEIR's cross-domain retrieval, the controlled contrast is a mismatch between query and evidence language inside technical subject matter. Ranking-depth diagnostics help distinguish missing evidence from evidence that remains recoverable but is ranked too low. One aggregate recall cannot explain that distinction. This is not an iterative-search or end-to-end RAG answer benchmark.

## Evaluation protocol

The pipeline exports corpus, queries, and qrels in MTEB retrieval format. Its current generation path creates English QAs, checks language, faithfulness, and retrieval quality, and translates them into target languages. Run metadata records dataset sizes, models, Git revision, and per-query results. The configurable repository supports additional translation languages and is not automatically the same as the five-language paper experiment.

## Decisive evidence and score boundary

The abstract reports a best-model Recall@10 drop from 0.72 in the monolingual setting to 0.53 cross-lingually. That is a source-reported result for its dataset and configuration, not a universal cross-domain effect or a direct estimate of answer degradation. The repository also warns that multilingual descriptions and claims are much sparser than titles and abstracts, with some fields mainly available in English; visible content must therefore be checked per language. [Result source](https://arxiv.org/abs/2609.23231) · [Field limitations](https://github.com/MohammadKhodadad/Multi-Lingual-QAC/blob/main/README.md)

## Confounders and remaining coverage gaps

The strongest alternative explanation involves English-seeded queries, translation style, and unequal content fields, not only embedding alignment. Patent-family overlap, qrel construction, and filtering also need auditing. Public data availability does not mean these confounders have been eliminated.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use it for language-pair diagnostics in technical or enterprise retrieval, as a retrieval-layer check before downstream RAG experiments.

### What a concrete task looks like

Illustrative task: a Chinese query describes a chemical process whose supporting patent has a German abstract; finding topically similar Chinese text is not equivalent to locating the evidence.

### Most discriminating experiment

Fix document fields, patent-family splits, and qrels; compare multilingual dense retrieval, query translation plus BM25, and hybrid retrieval. Report Recall/MRR per language pair, separate original and translated queries, and match retrieval and reranking budgets.

### Pair with

[beir](beir.en.md) · [ontologybench](ontologybench.en.md) · [commercial-tax](commercial-tax.en.md)

<!-- RESEARCH-DECISION:END -->

---

Evidence checked: 2026-09-23. This note uses paper metadata and the official protocols, implementations, or dataset descriptions identified above. Structural validation is not factual certification, and experiments were not independently reproduced.
