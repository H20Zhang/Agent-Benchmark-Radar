# ICM-Bench

## Measurement object

Tests person-linked recall, cross-episode identity retrieval and long-term profile inference over a synthetic multimodal life album.

## What changed compared with predecessors

Beyond general multimodal recall, isolates recurring-person linkage and profile evidence across an extended timeline.

## Protocol and comparison controls

Recall/Retrieval consume clips only through before_clip; Profile uses the full timeline. Video settings receive a calibration clip. Gold character IDs, evidence and speaker-labeled transcripts are evaluator-only. The shared judge compares answer meaning.

## Decisive evidence and score ceiling

The official release includes video generation and M3-Agent, Vgent and HippoRAG2 integrations, but explicitly excludes the direct caption-memory baseline implementation. This limits reproduction of that important comparison.

## Strongest confounders and limitations

Video sampling, transcription, captioning and answerer configurations differ across systems. Their aggregate gap is not an isolated memory-architecture effect. A small separate generation pilot is not a second evaluated test domain.

## Coverage gap and next experiment

A single synthetic cast does not establish robustness to diverse real people, long-term appearance changes, or downstream action.

Freeze perception and the answering model, then compare full caption history with explicit person-event relations. Test identity swaps and evidence removal without exposing gold labels.

## Genealogy and use

[MemEye](memeye.en.md) · [Mem-Gallery](mem-gallery.en.md) · [LifeSide](lifeside.en.md)

This entry is an `early_signal`: acceptance of a useful evaluation object does not promote one paper into a durable field-map claim.

## Primary sources and version

[Paper](https://arxiv.org/abs/2609.04438) · [Reviewed full text](https://arxiv.org/html/2609.04438v2)

[code](https://github.com/Shidu-Ren/ICM-Bench)

[data](https://huggingface.co/datasets/ryanren0330/ICM-Bench)

First public event: **2026-09-03**. Reviewed: **2026-09-17**. Source release and Radar acceptance are separate events.

[中文](icm-bench.md) · [Complete index](../library/README.en.md)
