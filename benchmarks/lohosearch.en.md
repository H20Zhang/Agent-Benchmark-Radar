# LoHoSearch: controlling search-space size and constraint-graph complexity instead of merely calling a query hard

[中文](lohosearch.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2606.12837) · [Data](https://huggingface.co/datasets/meituan-longcat/LoHoSearch)

## What it measures

LoHoSearch contains 544 human-verified questions across 11 domains, split into 282 tree-structured and 262 graph-structured tasks, derived from a knowledge graph with more than 7M Wikipedia entities. It explicitly controls candidate search-space size and structural constraint complexity and also measures calibration.

## Compared with what

Many deep-search benchmarks rely on annotator intuition for difficulty. LoHoSearch makes candidate-space size and constraint-graph structure observable variables, enabling more controlled study of long-horizon context management.

## Score boundary

Dual-judge accuracy and calibration support long-horizon constraint reasoning under the Wikipedia-derived space and named provider/tool. Synthetic question generation and live search infrastructure still limit external validity.

## Fair comparison conditions

Align tree/graph slice, provider, tool interface, context window, judge, and search budget, and report calibration separately.

## Next evaluation coordinate

The next step maps structural difficulty to natural user-query distributions and tests whether controlled complexity predicts real search cost and failure probability.
