# MEMLENS：长上下文与 memory agent 的多模态正面对比

**中文** | [English](memlens.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2605.14906) · [代码](https://github.com/xrenaf/MEMLENS)

## 它到底测什么

MEMLENS 在受控 context length 下直接比较 **long-context VLM 与 memory-augmented agent** 的 multimodal multi-session memory，覆盖 information extraction、multi-session reasoning、temporal reasoning、knowledge update、answer refusal，并从 32K 扩展到 256K token。

## 相比此前评测多测了什么

它专门排除 text-only shortcut。image-ablation 验证大多数题确实需要 visual evidence，因此可以较干净地比较两种架构：保留 raw multimodal context，还是把历史压缩进 external memory representation。

## 决定性证据

MEMLENS 有 789 个问题、4 档 context length。对 evidence 包含图片的 80.4% 问题，去掉图像后两种 frontier LVLM accuracy 都跌到 2% 以下。对 27 个 LVLM 与 7 个 memory agent 的评估显示：long-context model 在短 context 更强，但历史增长后退化；memory agent 对长度更稳定，却因 storage-time compression 丢失 visual fidelity。multi-session reasoning 上多数系统仍低于 30%。

## 这个分数能证明什么

它揭示了真实架构 trade-off：**raw-context visual fidelity vs compressed-memory scalability**。结果不能推出某一范式普遍更好，因为不同系统的 backbone、compression format 与 context implementation 仍不完全匹配。

## 公平比较契约

尽量匹配 VLM backbone，统一 cross-modal token accounting、evidence image、context cutoff 与 query set，并报告 memory construction/storage cost。拿 256K raw-context 和 external-memory agent 比，却不计 ingestion 与 retained bytes，是不完整的比较。

## 还没有测什么

256K 仍远小于多年个人媒体；benchmark 也以 QA 为主，没有覆盖未来 multimodal action、持续视频 ingestion、update/delete operation。

## 下一步最有判别力的验证

构建 selective hybrid：只保留少量高价值 raw visual evidence，其余压缩，并同时画 accuracy–retained bytes–context length 曲线，直接验证 benchmark 暗示的架构方向。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合区分长上下文视觉模型的长度退化与外部记忆压缩造成的视觉损失。两类系统未必测试相同题集；比较前先对齐样本、视觉输入与预算，否则‘记忆胜过长上下文’容易成为混合条件的结论。

### 一个具体任务长什么样

示意任务：跨会话的图文历史逐步增长，后续问题要求恢复旧图中的信息或识别状态更新。原图仍可见时答错，与压缩阶段已丢掉关键像素，是不同的失败环节。

### 最有判别力的实验

只在共同问题子集上比较原始长上下文与外部记忆，分别给定原图和正确文字证据形成上界诊断。扫描历史长度时固定题目，并记录压缩、检索与回答阶段的成本，避免仅比较最终 token 数。

### 建议搭配

[memeye](memeye.md) · [mem-gallery](mem-gallery.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`long-context multimodal QA ↔ external memory agents → hybrid selective visual retention`

它的价值在于把两种主流 memory 架构为什么失败讲清楚了。