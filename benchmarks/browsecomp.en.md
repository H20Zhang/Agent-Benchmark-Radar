# BrowseComp: stress-testing persistence and creativity in web search

[中文](browsecomp.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Official description](https://openai.com/index/browsecomp/) · [Code](https://github.com/openai/simple-evals)

## What it measures

BrowseComp contains 1,266 short-answer, verifiable but deliberately hard-to-find web questions. Success often requires persistent browsing, query reformulation, cross-page tracking, and discovering non-obvious sources, making information-seeking persistence the central difficulty.

## Compared with what

Benchmarks such as HotpotQA fix the corpus and supporting evidence. BrowseComp moves the environment to the live web, so deciding where and how to keep searching becomes part of the task. Search provider, web drift, and tool interface consequently become part of the evaluation contract too.

## Decisive evidence and current results

OpenAI's original evaluation reports Deep Research at 51.5%, o1 without browsing at 9.9%, GPT-4o with browsing at 1.9%, and lower no-browsing baselines. Radar preserves this as a dated 2025-04-10 official snapshot rather than merging it with later providers or derived benchmarks. The launch also notes that Deep Research had been trained on BrowseComp-style data, making benchmark familiarity/leakage a real interpretation variable.

## Fair comparison conditions

Align question version, search provider, browser/tool interface, tool-call budget, knowledge cutoff, and evaluator. Because the web changes, score date is part of the result.

## Next evaluation coordinate

Short answers do not measure citation quality, evidence portfolios, or long-form synthesis. BrowseComp-Plus and related fixed-corpus variants trade live-web realism for stronger attribution and reproducibility.
