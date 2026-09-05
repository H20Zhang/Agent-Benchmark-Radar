# MemEye：不能被 caption 替代的视觉 memory

**中文** | [English](memeye.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2605.15128) · [代码](https://github.com/MinghoKwok/MemEye)

## 它到底测什么

MemEye 沿两个轴评估 multimodal memory：**visual evidence granularity** 从 scene-level 到 pixel-level，**memory reasoning depth** 从单条 evidence 到 relational / evolutionary synthesis。它真正问的是：memory system 有没有保存之后推理所必需的视觉信息。

## 相比此前评测多测了什么

不少所谓 multimodal-memory question 只靠 caption 或文本 trace 也能回答，系统把图片扔掉仍能拿高分。MemEye 用 answerability、shortcut resistance、visual necessity、reasoning structure 等 ablation gate 验证题目，把“图片是否真的必要”变成 benchmark validity 的一部分。

## 决定性证据

公开 benchmark 有 371 个 mirrored MCQ + open-ended question，覆盖 8 类生活 scenario，并标注 clue round。论文评估 4 个 VLM backbone 上的 13 种 memory method，发现当前系统仍难以保存细粒度视觉 detail，也难以综合随时间变化的 visual state。

## 这个分数能证明什么

MemEye 提供的是 multimodal **evidence preservation + routing + temporal reasoning** 的整体证据，不能把结果直接归因给 storage：系统可能完整保存了图片，却因为 VLM backbone 看不出决定性的 pixel-level feature 而失败。

## 公平比较契约

应固定 VLM backbone、image resolution/preprocessing、caption access、retrieval budget 与 clue history，并把 image-ablation / text-only control 与主结果一起报告，否则所谓 multimodal-memory gain 可能只是 caption generation 更好。

## 还没有测什么

场景仍是 benchmark 化的 life scenario，不是开放世界连续视频；continuous video compression、跨设备媒体、privacy，以及保留 raw visual evidence 的 storage/latency cost 都没有被完整覆盖。

## 下一步最有判别力的验证

用 oracle image retrieval 把 visual memory 拆成 store fidelity、retrieval recall、downstream visual interpretation，判断系统应该投资更好的 multimodal index，还是更强的 post-retrieval visual reasoning。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合检验长期记忆是否保住真正必要的视觉细节。对多模态记忆论文，视觉必要性对照比单纯提高混合题集均分更关键；否则文本捷径会让丢失图像信息的系统也显得有效。

### 一个具体任务长什么样

示意任务：几次视觉观察记录同一物体的细节变化，之后要求判断具体属性和时间演化。图片的顺序、细粒度信息和证据来源都需要被保留，单张图识别正确还不足以完成整条任务。

### 最有判别力的实验

固定骨干后，对原图、粗描述、细描述及外部视觉记忆分别做测试，联合报告选择题和开放题。针对相同样本去掉视觉输入，确认性能差异确实来自必要图像信息，而不是回答格式或评分器变化。

### 建议搭配

[mem-gallery](mem-gallery.md) · [worldmemarena](worldmemarena.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`textualized multimodal memory → visually necessary evidence → fine-grained temporal visual memory`

它堵住了一个常见 shortcut：不能再把 caption store 直接叫作“multimodal memory”。