# DABStep: complex data workflows need verifiable intermediate milestones

[中文](dabstep.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

## What it measures

The DABStep paper describes roughly 450 tasks from 95 workflows over more than 100K payment transactions, while the current public dataset has about 460 rows. Tasks expose verifiable intermediate steps and deterministic final answers with hidden tests or an online leaderboard, checking whether an agent actually executes the workflow.

## Compared with what

Open-ended analyst benchmarks are hard to attribute from final reports. DABStep introduces intermediate execution contracts so schema inspection, transformation, and aggregation failures can be localized before the final answer.

## Score boundary

Final and step success support execution reliability under the payment data and current workflow definitions. Differences between paper-scale and public artifacts require explicit release binding.

## Fair comparison conditions

Align dataset release, workflow version, runtime, hidden tests, tool budget, agent scaffold, and evaluator generation.

## Next evaluation coordinate

The next step combines step correctness with business invariants, recovery, and artifact provenance, separating executed steps from correct business state.
