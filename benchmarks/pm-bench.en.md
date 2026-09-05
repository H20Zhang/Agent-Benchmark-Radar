# PM-Bench: Agent memory must remember what to do later, not only what happened before

[中文](pm-bench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2607.12385)

## What it measures

PM-Bench measures **prospective memory**: maintaining a delayed user intention while continuing other activities, then executing it when the correct future time, cue, or environment state occurs without another reminder. It uses a text-based simulated seven-day Virtual Week inspired by cognitive-science paradigms.

## What changed relative to prior evaluation

Benchmarks such as LoCoMo and LongMemEval primarily ask what happened in the past or what state is current. PM-Bench reverses the temporal direction: maintain an intention, monitor for its trigger, and act at the right future moment.

## Decisive evidence

The paper evaluates eight LLMs under eight agent configurations. The best reported GPT-5.4 agent reaches only 65.1% F1, and no prospective-memory strategy dominates consistently across models.

## What the score supports

It supports claims about delayed-intention maintenance and cue-triggered execution in the controlled simulation. It does not establish long-horizon reliability with real calendars, asynchronous notifications, tool failures, or safety-critical actions.

## Fair comparison contract

Match backbone, agent configuration, time representation, cue visibility, ongoing-task policy, and scoring. Explicit scheduler/notification tools should be reported as a separate condition from context-only memory.

## What remains unmeasured

Real days-to-months horizons, external notification systems, conflicts and cancellations among future intentions, and the safety cost of erroneous execution.

## Next discriminating validation

Pair time-based, event-based, updated, cancelled, and conflicting variants of the same intention. Compare context-only, persistent memory, and explicit scheduling while separating correct first trigger, misses, and false triggers.

<!-- RESEARCH-DECISION:START -->
## Research decision card
### When to use it
Use PM-Bench when the memory claim is that an agent will do the right thing later when needed, rather than merely restate an old fact on demand.
### What a concrete task looks like
Illustrative task: on Monday a user asks for X when a particular cue appears on Thursday. The agent handles unrelated activity until then, must trigger on the first correct cue, and must not act early.
### Most discriminating experiment
Pair time cues, event cues, updates, cancellations, and conflicts for the same intention, comparing context-only, persistent-memory, and scheduler conditions.
### Pair with
[LongMemEval](longmemeval.en.md) · [MemoryArena](memoryarena.en.md) · [Mem2ActBench](mem2actbench.en.md)
> **Score-reading rule:** prospective-memory F1 is not end-to-end safety reliability for real automation.
<!-- RESEARCH-DECISION:END -->

## Evolution position
`past-event recall → current-state tracking → future-intention execution`
