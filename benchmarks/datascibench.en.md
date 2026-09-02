# DataSciBench: when ground truth is not a simple unit test, data science needs structured evaluators

[中文](datascibench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Project](https://datascibench.github.io/) · [Code](https://github.com/THUDM/DataSciBench)

## What it measures

DataSciBench covers six data-science task types, 25 aggregate functions, and 519 test cases with natural, complex prompts whose ground truth is not always directly available. Its Intention-Function-Code (IFC) framework maps intent, functions, and executable outcomes to programmatic metrics; the ACL 2026 version evaluates 26 models.

## Compared with what

DS-1000 works well when unit tests define correctness. DataSciBench addresses uncertain ground truth and multiple valid analytical outputs using semi-automated GT generation, human verification, and aggregate metrics.

## Score boundary

IFC and completion metrics support competence under the current GT pipeline and evaluator rules. They may still favor analyses expressible through the predefined aggregate functions and do not fully measure analyst-artifact quality.

## Fair comparison conditions

Align benchmark version, GT generation/verification, IFC rules, runtime, agent scaffold, and model budget. Different evaluator generations require separate tracks.

## Next evaluation coordinate

The next step jointly evaluates code outcomes, reasoning traces, visual artifacts, source grounding, and stakeholder-facing reports.
