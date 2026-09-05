# Beyond Goldfish Memory: an early coordinate for multi-session conversational memory

[中文](beyond-goldfish-memory.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://aclanthology.org/2022.acl-long.356/) · **Area: Agent Memory**

Beyond Goldfish Memory is important mainly for its historical position. Before today's Agent Memory terminology and system stacks matured, it already made **persistent memory across sessions** an explicit evaluation problem.

## What it actually measures

The work uses open-domain conversations resumed across multiple human-human chat sessions and asks a system to keep using prior interactions in later conversations, preserving personal facts, remembered content, and conversational continuity.

The core object is therefore:

- whether information from earlier sessions can be correctly reused later;
- whether remembering history improves continuity and personalization of future responses.

Unlike current memory-agent evaluations centered on write, retrieve, update, and act, this benchmark lives primarily at the **cross-session recall + conversational continuity** layer.

## Compared with what

Traditional dialogue benchmarks often treat each conversation session as an independent example. A model may maintain context within one session without carrying anything into a later one.

The key change here is simple but consequential: **a session boundary no longer implies a memory reset**.

That establishes a foundational assumption for later long-term memory benchmarks. Long-term memory is not just a longer prompt; prior interactions must continue to influence future episodes.

## How the evaluation works

An interpretable multi-session memory result needs the dialogue model, history-access method, retrieval or summarization strategy, and response-evaluation protocol to be fixed.

If a system sees only retrieved history, final quality bundles retrieval and generation. If it sees the complete history, it operates under a different evidence contract.

Modern long-context models that directly ingest all prior text therefore cannot be compared naively with early external-memory setups.

## What a score supports

Automatic generation metrics or human ratings can support a claim that, under the current history-access mechanism and dialogue model, the system better preserves cross-session consistency, relevance, or personalization.

A higher final-response score does not isolate whether the gain comes from:

- better memory writing;
- better retrieval;
- more faithful summarization;
- stronger generation conditioned on memory.

The components are bundled in the final response, so this is mainly a **system-level memory-effect** benchmark rather than a fine-grained component-attribution benchmark.

## Main confounders

The first is the **base dialogue model**. Stronger generation can improve continuity even if the memory mechanism itself changes little.

The second is the **history-access budget**. How much prior evidence is visible, and in what form, strongly determines what the system can exploit.

The third is **human-evaluation sensitivity** when subjective dialogue quality is the primary endpoint.

## Fair comparison contract

At minimum, align:

- dialogue model;
- session segmentation and history length;
- history-access or retrieval contract;
- summarization and memory capacity;
- generation decoding;
- human and automatic evaluation protocol.

A system with full-history access and one restricted to a fixed number of retrieved memories should be treated as different tracks.

## What is still missing

This early coordinate does not systematically test:

- updates and staleness when new information supersedes old facts;
- conflicting memories and source reliability;
- deletion and forgetting;
- permissions and privacy;
- whether memory improves tool use or future actions;
- token, latency, and storage cost of maintaining memory over time.

These later became major branches of Agent Memory evaluation.

## Most discriminating next test

The highest-value extension from this historical baseline is not simply longer dialogue, but **state change**: update a user preference, fact, or constraint in a later session and test whether the system applies the newest state instead of mechanically repeating old memory.

That moves evaluation from long-term storage to long-term maintenance.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use Beyond Goldfish Memory as a historical anchor for cross-session dialogue continuity. It motivates the need for memory but does not replace mechanism-level evaluation of writing, conflict updates, deletion, or action effects. Make that foundational role explicit in a modern suite.

### What a concrete task looks like

Illustrative task: two participants resume a conversation after a gap and must naturally continue earlier topics and relationships. Evaluation concerns not only fact repetition but consistency and coherence of the generated continuation.

### Most discriminating experiment

Compare no history, full history, and summary memory for the same continuation, scoring historical consistency separately from general fluency. Blind evaluators to conditions so longer or more polite replies are not mistaken for better memory. Add structured update tasks for mechanism-level claims.

### Pair with

[locomo](locomo.en.md) · [longmemeval](longmemeval.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Evolution position

`single-session dialogue → cross-session conversational memory → updateable persistent memory → memory-guided action`

Beyond Goldfish Memory occupies the second step and is an important precursor to LoCoMo, LongMemEval, and the broader Agent Memory benchmark lineage.
