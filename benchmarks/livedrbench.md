# LiveDRBench：把广泛证据发现同报告写作拆开

**中文** | [English](livedrbench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2508.04183) · [代码](https://github.com/microsoft/LiveDRBench) · [数据](https://huggingface.co/datasets/microsoft/LiveDRBench)

## 它在测什么

LiveDRBench 把 deep research 定义为从大量来源中发现结构化主张与支持依据，而不是写得很长。官方 v1-full 含八类、100 个任务，数据采集于 2025 年 5—6 月；论文首发为 2025-08-06。此次是历史补录，不把名称里的 Live 或未来更新计划当成测试集持续更新的证据。[官方数据说明](https://github.com/microsoft/LiveDRBench/blob/main/README.md)

## 相比什么前进了

相较报告整体打分，它通过中间的结构化主张把证据覆盖与写作质量分开；相较单答案搜索题，它要求更广的发现集合。这个缺失的历史参照有助于理解后续 ClaimProbe 和 Mr.LHDR 的主张、引用及依赖清单评测，但不能只因补录一篇论文就宣布新的领域趋势。

## 实际怎样评测

任务给出查询与输出结构，参考主张用于 precision、recall 和 F1 评测；代码按类别分发评分器，默认 judge 为 GPT-4o。已核对的 evaluate.py 将缺失预测记为零，overall 对逐题指标平均，而不是把八个类别均值再等权平均。数据仅供测试，参考答案的加密措施不能被当成彻底防污染。[实际评分代码](https://github.com/microsoft/LiveDRBench/blob/main/src/evaluate.py)

## 决定性证据与分数边界

论文报告当时最强系统 overall F1 为 0.55，并显示子类别跨度很大。这是初始实验中的系统级结果，不是 2026 年当前最佳成绩。可复用增量在于把覆盖不全暴露出来，而不是证明更长报告或更多搜索调用一定有效。[论文](https://arxiv.org/abs/2508.04183)

## 主要混杂与尚未覆盖的能力

参考集合可能遗漏其他有效来源，网页会变化，judge 和输出解析也会影响分数。领域集中于部分科学主题与事件，不能代表所有研究工作；高 claim F1 也不等于报告结构、论证或表达优秀。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合评测广度搜索与证据覆盖，并给报告质量评测配一个相对独立的内容发现指标。

### 一个具体任务长什么样

示意：寻找同时满足若干实验条件的材料，需要发现一组候选和各自证据；只找到一个熟悉案例或写出流畅综述都不等于覆盖完整。

### 最有判别力的实验

固定模型、网页快照和搜索预算，比较单链搜索与多分支探索；保留未完成题并按逐题规则聚合，另外人工核验参考集合外的有效发现。随后单独评估报告，不让文风掩盖证据漏项。

### 建议搭配

[deepresearch-bench](deepresearch-bench.md) · [claimprobe](claimprobe.md) · [mr-lhdr](mr-lhdr.md)

<!-- RESEARCH-DECISION:END -->

---

证据核验：2026-09-23。本条依据论文元数据、官方协议及上述公开实现或数据说明；不把结构校验当作事实认证，也未独立复现实验。
