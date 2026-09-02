# RAGBench: benchmarking the evaluator, not only the RAG system

[中文](ragbench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2407.11005) · [Dataset](https://huggingface.co/datasets/rungalileo/ragbench)

## What it actually measures

RAGBench is a 100K-example benchmark across five industry-oriented domains for evaluating **RAG quality and RAG evaluators**. Its TRACe framework provides explainable/actionable labels rather than only one end-answer score.

## What changed relative to prior evaluation

A RAG pipeline can only be optimized if evaluation distinguishes retrieval/context defects from answer defects. RAGBench shifts part of the benchmark target from “which RAG system wins?” to “does the evaluator reliably identify the kind of failure that occurred?”

## Decisive evidence

The dataset spans multiple RAG task types and industry corpora such as user manuals. The paper finds that general LLM-based evaluation methods can struggle to match a finetuned RoBERTa model on the RAG-evaluation task, showing that evaluator sophistication and evaluator validity are different things.

## What the score supports

RAGBench supports claims about evaluator quality and labeled RAG failure dimensions under its annotation scheme. It is not evidence for adaptive retrieval policy, and any system ranking derived from an evaluator inherits that evaluator's biases.

## Fair comparison contract

Fix the labeled split, evaluator prompt/model/version, thresholding, and RAG outputs being judged. Report evaluator agreement/calibration before using it to rank new RAG systems. Human-label uncertainty should not disappear behind an aggregate metric.

## What remains unmeasured

Static labeled examples do not capture live-web drift, iterative tool use, budget allocation, or agent stopping. Explainable labels are useful only insofar as they predict interventions that improve end-to-end behavior.

## Next discriminating validation

Use each diagnostic label to trigger a targeted pipeline change, then measure whether the predicted failure class actually improves. This converts explainability from descriptive taxonomy into causal usefulness.

## Genealogy

`RAG output score → failure labels → evaluator validity and actionable diagnosis`

RAGBench matters because benchmark quality itself becomes part of the RAG systems problem.