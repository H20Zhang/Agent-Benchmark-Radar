# DSAEval: a data-science agent produces reasoning, code, results, and reports

[中文](dsaeval.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

## What it measures

DSAEval contains 641 problems over 285 real datasets spanning tabular, image, and text data, with GPU Jupyter execution and cumulative multi-query sessions. Evaluation inspects reasoning, code, execution results, and reports; the paper compares 13 agents.

## Compared with what

Code-only benchmarks miss analytical reasoning and communication. DSAEval jointly evaluates intermediate process and deliverables in multimodal data-science sessions where later queries can depend on prior notebook state.

## Score boundary

The multi-component score supports the full agent under the named GPU/Jupyter environment, datasets, and judge/rules. Component weights or judge changes can move aggregate rankings.

## Fair comparison conditions

Align dataset/version, GPU/runtime, session order, agent budget, component metrics, and report judge, and preserve the component breakdown.

## Next evaluation coordinate

The next step adds evolving data/objectives, artifact review, and business consequences, testing whether accumulated state ultimately helps or contaminates analysis.
