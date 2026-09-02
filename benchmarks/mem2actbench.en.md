# Mem2ActBench: measuring memory where it changes a tool call

[中文](mem2actbench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://aclanthology.org/2026.acl-long.370/) · [Code](https://github.com/Cantaloupe-M/Mem2ActBench)

## What it measures

Mem2ActBench contains 400 tool-use tasks derived from 2,029 sessions averaging about 12 user-assistant-tool turns; 91.3% of tasks were judged strongly memory-dependent. Systems must reuse preferences and task state to select tools and ground parameters correctly.

## Compared with what

Conversational QA only measures memory utility indirectly. Mem2ActBench scores tool-call correctness directly, exposing cases where a preference was remembered but not used for parameter grounding and separating action-level utilization from retrieval quality.

## Score boundary

Tool-call success supports correct use of memory under the named schema, backbone, and harness. It does not establish that the memory representation itself is better because synthetic generation, tool schema, and agent capability all affect the outcome.

## Fair comparison conditions

Align tool schemas, allowed calls, backbone, memory implementation, and task version. Different tool sets or parameter constraints require distinct tracks.

## Next evaluation coordinate

The stronger test lets tool calls modify persistent environment state and checks whether downstream errors caused by bad memory can be detected and repaired.
