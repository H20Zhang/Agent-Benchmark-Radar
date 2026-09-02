# DAComp: data agents need both executable checks and open-ended analytical artifacts

[中文](dacomp.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

## What it measures

DAComp contains 210 tasks across data engineering and open-ended analysis, combining executable transformation/query checks with judge-based analytical rubrics instead of reducing all data work to one SQL string or one natural-language grade.

## Compared with what

DABStep emphasizes deterministic workflow execution, while InsightBench emphasizes open insights. DAComp puts hard execution checks and softer analytical-quality evaluation in one suite, exposing cases where code is correct but analysis is weak or prose is convincing while data processing is wrong.

## Score boundary

Execution plus rubric scores support the full system under the current datasets, runtime, and judge. Open-ended judging remains style-sensitive and does not equal real stakeholder value.

## Fair comparison conditions

Align task release, runtime, data-engineering validators, analysis judge/rubric, agent tools, and budget, and report executable and open-ended slices separately.

## Next evaluation coordinate

The next step adds business invariants and artifact-level reproducibility so every important report claim can be traced back to executed results.
