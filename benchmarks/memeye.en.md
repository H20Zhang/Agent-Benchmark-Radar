# MemEye: visual evidence that cannot be replaced by captions

[中文](memeye.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2605.15128) · [Code](https://github.com/MinghoKwok/MemEye)

## What it actually measures

MemEye evaluates multimodal memory along two axes: **visual evidence granularity** from scene-level to pixel-level details, and **memory reasoning depth** from single evidence to relational and evolutionary synthesis. It asks whether a memory system preserves the visual information that later reasoning actually requires.

## What changed relative to prior evaluation

Many multimodal-memory questions remain answerable from captions or textual traces, so a system can discard the image and still score well. MemEye uses ablation-driven validation gates for answerability, shortcut resistance, visual necessity, and reasoning structure, making “the image was genuinely needed” part of benchmark validity.

## Decisive evidence

The released benchmark contains 371 mirrored multiple-choice and open-ended questions across eight life-scenario tasks, with annotated clue rounds. Evaluation of 13 memory methods across four VLM backbones shows persistent difficulty preserving fine-grained visual detail and synthesizing state changes over time.

## What the score supports

MemEye provides evidence about multimodal **evidence preservation + routing + temporal reasoning**. It does not isolate storage from VLM perception: a system may store an image perfectly yet fail because the backbone cannot extract the decisive pixel-level feature.

## Fair comparison contract

Fix VLM backbone, image resolution/preprocessing, textual caption access, retrieval budget, and clue history. Report image-ablation and text-only controls together with main scores; otherwise a claimed multimodal-memory gain may only be better caption generation.

## What remains unmeasured

The tasks remain benchmarked life scenarios rather than open-world video streams. Continuous video compression, cross-device media, privacy, and storage/latency cost of retaining raw visual evidence are not fully represented.

## Next discriminating validation

Factor visual memory into store fidelity, retrieval recall, and downstream visual interpretation using oracle image retrieval. This would tell whether systems should invest in better multimodal indexing or better post-retrieval visual reasoning.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use MemEye to test whether memory retains genuinely necessary visual detail. For multimodal-memory claims, visual-necessity controls matter more than a higher average over mixed questions; textual shortcuts can make a system that discards image information appear effective.

### What a concrete task looks like

Illustrative task: repeated visual observations record changes to the same object, and a later query asks about a specific attribute and its evolution. Image order, fine-grained evidence, and provenance must survive; correctly recognizing one image is insufficient.

### Most discriminating experiment

With a fixed backbone, compare original images, coarse captions, detailed captions, and external visual memory. Report both multiple-choice and open-ended results. Remove visual input for matched samples to attribute differences to necessary visual information rather than answer format or evaluator changes.

### Pair with

[mem-gallery](mem-gallery.en.md) · [worldmemarena](worldmemarena.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`textualized multimodal memory → visually necessary evidence → fine-grained temporal visual memory`

MemEye prevents a common shortcut: calling a caption store “multimodal memory.”