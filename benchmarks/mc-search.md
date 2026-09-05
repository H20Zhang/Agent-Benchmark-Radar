# MC-Search：multimodal agentic RAG 需要同时测 planning、modality choice 与每一 hop evidence

**中文** | [English](mc-search.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2603.00873) · [代码](https://github.com/YennNing/MC-Search)

## 它在测什么

MC-Search 包含 3,333 个 tasks、平均约 3.7 hops、五种 reasoning topologies，并为每一步标注 subquestion、retrieval modality、supporting evidence 与 intermediate answer。paper 描述的 KB 含约 389,750 张图片和 784,473 段文本；当前 released artifact 规模更小，因此 artifact version 本身需要记录。

## 相比什么前进了

普通 multimodal QA 只看最终答案；普通 agentic search 又常缺 gold trajectory。MC-Search 提供 hop-level retrieval、planning accuracy、gold-evidence answering 与 rollout deviation，使 over/under-retrieval、modality error 和 chain drift 可分开。

## 分数边界

高 planning/retrieval score 支持和 benchmark gold trajectory 的一致性，但 single-gold trajectory 可能惩罚其他有效路径。paper/released artifact 的 KB scale mismatch 也意味着结果必须绑定具体 version，不能混成一个 leaderboard。

## 公平比较条件

锁定 KB artifact、multimodal backbone、hop budget、judge 与 trajectory policy。gold-evidence 与 free-search conditions 应独立 track。

## 下一步评测坐标

下一步要允许 multiple valid trajectories，并将 modality choice 与真实 latency/cost 及 final evidence sufficiency 联合评价。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合诊断多模态搜索链中选错模态、缺少证据或规划偏离的环节。每跳标注提供可定位信号，但标准轨迹不是唯一可能路径；论文所述语料与公开子集的差异也会改变复现实验对象。

### 一个具体任务长什么样

示意任务：文字证据指出需要查看某幅图，视觉细节又决定下一轮应搜索哪个对象。系统必须在文字与图像之间切换；只使用文本检索或只评最终答案，会掩盖具体模态选择失误。

### 最有判别力的实验

固定公开语料版本，分别给定正确模态、正确中间证据和正确子问题，观察最终恢复。对可行的替代路径做证据检查，并分开报告论文规模与公开子集，避免将资源差异归因于策略。

### 建议搭配

[merrin](merrin.md) · [visdocagentbench](visdocagentbench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
