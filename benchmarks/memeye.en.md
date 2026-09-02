# MemEye: first proving that the question genuinely requires visual memory

[中文](memeye.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2605.15128) · [Code](https://github.com/MinghoKwok/MemEye)

## What it measures

MemEye releases 371 mirrored multiple-choice and open-ended questions across eight life-scenario tasks, organized by visual-evidence granularity and reasoning depth. A visual-necessity ablation checks whether a question actually depends on images rather than text or world knowledge.

## Compared with what

Many multimodal memory datasets can be solved through captions, textual shortcuts, or common sense. MemEye makes irreducible visual evidence a validation requirement, providing stronger tests of fine-grained visual retention, temporal state tracking, and evolutionary synthesis.

## Score boundary

MCQ and open-ended judge scores support use of necessary visual evidence in constructed scenarios. They do not establish long-horizon action utility in real multimodal agents, and judge choice, backbone, and scenario construction remain important variables.

## Fair comparison conditions

Align mirrored question set, visual-necessity filtering, backbone, image preprocessing, and judge, and keep MCQ and open-ended tracks separate.

## Next evaluation coordinate

The next step makes retained visual evidence affect later operations and tests cross-session visual-state updates and conflicts.
