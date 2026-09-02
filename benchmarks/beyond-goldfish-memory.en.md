# Beyond Goldfish Memory: an early coordinate for multi-session conversational memory

[中文](beyond-goldfish-memory.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://aclanthology.org/2022.acl-long.356/)

## What it measures

The work uses open-domain conversations resumed across multiple human-human chat sessions and asks whether a dialogue system remembers prior interaction while preserving persona, facts, and conversational continuity. It predates modern memory-agent stacks and targets cross-session recall and consistency.

## Compared with what

Conventional dialogue benchmarks usually treat each session as independent. This setting explicitly requires later conversations to depend on earlier ones, making persistent cross-session state an evaluation coordinate and a precursor to benchmarks such as LoCoMo.

## Score boundary

Generation metrics or human ratings support continuity under the named dialogue model and retrieval/summarization method. They do not isolate writing, retrieval, or generation, and they do not test updating, tool use, or future action.

## Fair comparison conditions

Align the dialogue model, history access method, retrieval/summarization strategy, and human-evaluation protocol. Modern long-context systems operate under a different evidence contract from early external-memory setups.

## Next evaluation coordinate

Successors need to move from remembering prior conversation toward updates, conflicts, forgetting, action, and maintenance cost, directly testing whether memory changes future behavior.
