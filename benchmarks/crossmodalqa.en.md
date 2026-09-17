# CrossModalQA

## Measurement object

Tests text-question answering that requires multi-hop transitions between textual and visual evidence, with retrieval and answer metrics.

## What changed compared with predecessors

Adds explicit cross-modal evidence paths rather than treating the presence of an image as proof of multimodal reasoning.

## Protocol and comparison controls

All questions are text inputs: visual/text path labels describe evidence transitions. Retrieval and generation are scored separately; gold text, images and combined evidence provide oracle controls. Some comparison methods require adaptations to accept text queries.

## Decisive evidence and score ceiling

The oracle-evidence comparisons expose a difference between evidence availability and answer construction. They provide a diagnostic bound under a selected answerer, not an attainable retrieval score.

## Strongest confounders and limitations

Constructed paths, question-generation checks and a small fixed corpus can favor the intended traversal. The paper protocol was verified; a standalone public dataset endpoint was not independently confirmed.

## Coverage gap and next experiment

Gold-document hit does not establish recovery of the complete evidence chain; the benchmark is not an open-web interactive agent test.

Pair complete-chain recall with answer accuracy under fixed evidence length. Test wrong-bridge negatives and modality removal against an equally strong text-only control.

## Genealogy and use

[MultiHop-RAG](multihop-rag.en.md) · [MuDABench](mudabench.en.md) · [VisDocAgentBench](visdocagentbench.en.md)

This entry is an `early_signal`: acceptance of a useful evaluation object does not promote one paper into a durable field-map claim.

## Primary sources and version

[Paper](https://arxiv.org/abs/2609.05518) · [Reviewed full text](https://arxiv.org/html/2609.05518v1)

First public event: **2026-08-31**. Reviewed: **2026-09-17**. Source release and Radar acceptance are separate events.

[中文](crossmodalqa.md) · [Complete index](../library/README.en.md)
