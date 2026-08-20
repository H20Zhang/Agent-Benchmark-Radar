# Radar Family Architecture

Agent Benchmark Radar is the default entry point for a four-repository research system.

```text
                         Agent Benchmark Radar
                         entry + evaluation layer
                    /             |              \
                   /              |               \
        Agent Memory Radar   Agentic RAG Radar   Data Agent Radar
        memory systems       information access   end-to-end data work
```

## Why Benchmark Radar is the entry

A benchmark genealogy gives a newcomer a compact answer to three questions before they read methods: **what capability the field is trying to improve, what older evaluation target became insufficient, and what evidence currently counts as progress**. From there, the reader can continue into the corresponding domain radar for methods, systems, and research tensions.

The intended flow is:

`field question → evaluation target → benchmark genealogy → domain research line → methods/systems → back to evaluation`

## Division of responsibility

| Surface | Primary question | Continuation |
|---|---|---|
| **Agent Benchmark Radar** | What is measured, how did the target evolve, and what does a score support? | Route to the relevant domain radar. |
| **Agent-Memory-Radar** | How should agents write, organize, retrieve, reconstruct, update, forget, and govern memory? | Route evaluation questions back to the Memory benchmark map. |
| **Agentic-RAG-Radar** | How should agents plan information needs, access evidence, control retrieval, materialize context, preserve state, and stop? | Route evaluation questions back to the RAG/Search benchmark map. |
| **Data-Agent-Radar** | How should agents discover/ground data, plan analytic work, query/code/transform, inspect/verify, recover, and deliver artifacts? | Route evaluation questions back to the Data Agent benchmark map. |

Benchmark Radar should **route rather than duplicate** domain method surveys.

## Guardrail: benchmark coverage is not the field

Making Benchmark Radar the entrance creates a predictable failure mode: readers may infer that the best-measured problems are the most important problems.

The public entry must therefore keep **What Is Still Poorly Measured / 目前仍难以测量什么** as a first-class field-level section, placed near the area field maps rather than buried as archive metadata. It should name important capabilities, environments, lifecycle costs, validity threats, or long-horizon effects for which current benchmarks provide weak evidence.

A mature evaluation map should expose both:

`what the field can currently measure` **and** `what important research questions remain largely outside current measurement`.

This is especially important for persistent agents, real-user longitudinal effects, irreversible actions, lifecycle cost, privacy/authority, production reliability, and other properties that may be important before a clean benchmark exists.

## Cross-link contract

- Benchmark Radar first screen contains one compact `Research Radars` line linking to all three vertical radars.
- Each Benchmark Radar area map ends with exactly one canonical continuation link to its domain radar.
- Each domain radar exposes one evaluation continuation back to the corresponding Benchmark Radar section/genealogy.
- Deep benchmark or paper notes cross-link only when the adjacent research line materially helps interpretation; do not add repeated promotional links.
- Chinese and English Benchmark Radar surfaces must route to the same sibling repositories and research relationships.

The family should feel like one research map with four projections, not four repositories advertising one another.