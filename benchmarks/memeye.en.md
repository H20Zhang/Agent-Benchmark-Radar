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

## Genealogy

`textualized multimodal memory → visually necessary evidence → fine-grained temporal visual memory`

MemEye prevents a common shortcut: calling a caption store “multimodal memory.”