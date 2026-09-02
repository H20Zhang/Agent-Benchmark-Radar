# DDR-Bench: in open data research, choosing what is worth analyzing may be the central capability

[中文](ddr-bench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

## What it measures

DDR-Bench covers 291 entities—100 MIMIC, 91 GLOBEM, and 100 10-K—over more than 203M records, 40 tables, 6,372 fields, and 2,058 checklist items. With a minimal prompt, agents must set goals, explore data, and produce insights autonomously.

## Compared with what

Most benchmarks tell the agent exactly what query to answer. DDR-Bench leaves the research objective more open and tests whether the agent selects valuable analyses in large databases rather than only executing a specification.

## Score boundary

Checklist and insight scores support autonomous exploration under the three data families and benchmark-defined research criteria. They do not equal real scientific or business value because checklist construction determines what counts as worth discovering.

## Fair comparison conditions

Align dataset snapshot, minimal prompt, tool access, exploration budget, checklist/judge, and entity split, and report domain slices.

## Next evaluation coordinate

The next step needs stronger novelty and decision-value evaluation plus calibrated stopping when evidence is insufficient for an insight.
