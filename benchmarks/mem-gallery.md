# Mem-Gallery：多模态 memory 不只是把图片 caption 化

**中文** | [English](mem-gallery.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://aclanthology.org/2026.acl-long.1892/) · [代码](https://github.com/YuanchenBei/Mem-Gallery)

## 它在测什么

Mem-Gallery 用 multi-session visual-text conversations，在统一框架下比较 12 个 memory systems，覆盖 memory extraction、test-time adaptation、reasoning、knowledge management 与 multimodal retention，并同时观察效率。

## 相比什么前进了

文本 memory benchmark 可以把图像压成 captions 后继续工作。Mem-Gallery 把 visual retention 和跨模态 reasoning 设为一等能力，使视觉细节在写入或压缩阶段丢失的代价能被观察。

## 分数边界

统一框架支持跨 memory system 的相对比较，但最终 QA/efficiency 仍受到 multimodal backbone、memory harness 与 judge 影响。高分说明 package 在该视觉对话 contract 下更好，不能直接证明某个 compression 或 retrieval component 因果更优。

## 公平比较条件

锁定 multimodal backbone、image encoding/compression、memory budget、answerer 与 judge，并分别报告 capability slices 和 efficiency。

## 下一步评测坐标

下一步应把 visual memory 接到真实环境 action，并验证细粒度 visual evidence 是否改变后续 tool choice 或 state update。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究视觉信息在长期对话中的保留与知识管理。必须先验证视觉确实参与解题：如果文本转述已包含答案，更高分可能来自语言推理，而非多模态记忆保存得更好。

### 一个具体任务长什么样

示意任务：早期会话展示一张图片，后续只用语言询问其中的细节或与另一张图的差异。系统应能追溯原始视觉证据；仅保留笼统图像描述可能丢掉决定答案的细粒度属性。

### 最有判别力的实验

固定视觉语言骨干，比较原图可访问、仅描述文本与压缩视觉记忆，并分开统计确实依赖图像的问题。记录写入后的信息损失和检索失败，避免把视觉编码能力与记忆机制的收益混为一谈。

### 建议搭配

[memeye](memeye.md) · [memlens](memlens.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
