# SAGE：学术检索要区分“找到指定论文”和“尽可能完整地找齐一组论文”

**中文** | [English](sage.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2602.05975) · [代码](https://github.com/HughieHu/Sage)

## 它在测什么

SAGE 提供 1,200 个 expert queries，覆盖 computer science、healthcare、humanities 与 natural science：600 个 short-form target-paper queries 和 600 个 open-ended discovery queries，基于约 200K papers 的 controlled corpus。前者看 exact paper retrieval，后者用 weighted recall 看是否找全高价值 evidence。

## 相比什么前进了

一般 literature search benchmark 常只测 title/known-item retrieval。SAGE 把 targeted lookup 与 open-ended evidence collection 分开，并做 agent-retriever ablation，因此可以观察同一个 search agent 换 backend 后能力如何变化。

## 分数边界

exact-paper/weighted-recall 支持在给定 corpus snapshot、index 与 retrieval budget 下的 scientific discovery quality；开放式 gold set 本身可能不完备，而且 released repo 并未 turnkey 提供完整 200K corpus/environment，因此 artifact packaging 是复现边界。

## 公平比较条件

锁定 corpus snapshot、indexing configuration、agent subquery generation、budget 与 gold-set version。short-form 与 open-ended 不能压成一个 SOTA 数字。

## 下一步评测坐标

下一步应接入 citation graph、full text 与动态 scholarly databases，同时明确 completeness ceiling 和 search cost。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合区分科学文献检索中的目标论文定位与开放式证据收集。两者对漏检的容忍度不同：找到一篇正确论文不能证明完成了领域覆盖；复现还取决于完整语料和搜索环境是否实际可得。

### 一个具体任务长什么样

示意任务：一类查询用若干线索找出特定论文，另一类要求搜集支持某个研究主题的多篇相关工作。相同检索器可能擅长精确定位，却在宽覆盖收集时反复返回同一研究簇。

### 最有判别力的实验

在同一论文语料上固定搜索接口与预算，分别比较目标命中和加权覆盖。记录论文去重、元数据与全文访问条件，并把完整环境缺失与算法失败区分，避免用不一致索引产生的差异评价检索策略。

### 建议搭配

[autoresearchbench](autoresearchbench.md) · [scholarquest](scholarquest.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
