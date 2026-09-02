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

## 演化位置

`long-context multimodal QA ↔ external memory agents → hybrid selective visual retention`

它的价值在于把两种主流 memory 架构为什么失败讲清楚了。