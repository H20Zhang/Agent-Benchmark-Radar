# FDABench: moving data agents from database queries to heterogeneous analytical workflows

[中文](fdabench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Project](https://fdabench.github.io/) · [Code](https://github.com/fdabench/FDAbench)

## What it measures

FDABench contains 2,007 analytical tasks across more than 50 domains, covering structured databases, documents, web content, images, video, and audio, with single-choice, multiple-choice, and report-generation tasks. The official framework supports planning, tool-use, reflection, and multi-agent patterns plus DAG-based traces, accuracy, report rubrics, latency, tokens, and cost.

## Compared with what

Spider and BIRD stay primarily inside databases, while DataSciBench expands data-science coding. FDABench makes source heterogeneity and report artifacts part of one suite, requiring tool selection, cross-source analysis, and deliverable generation.

## Score boundary

Choice or report scores support the full agent system under the named data/tool setup. Workflow pattern, model, tool availability, and budget all affect results, so an overall score cannot isolate planning or multi-agent mechanisms.

## Fair comparison conditions

Align Full/Lite release, source availability, workflow, model, maximum rounds, evaluator, and token/cost policy. Report and choice task types require separate tracks.

## Next evaluation coordinate

The next step strengthens business-semantic truth, artifact correctness, and repeated operational workflows so plausible-looking reports cannot substitute for actual business correctness.
