# EnterpriseRAG-Bench：企业 RAG 的难点是跨源冲突、约束与“找不到”

**中文** | [English](enterpriserag-bench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2605.05253) · [代码](https://github.com/onyx-dot-app/EnterpriseRAG-Bench)

## 它在测什么

EnterpriseRAG-Bench 构造约 500K coherent synthetic documents，覆盖 9 类 enterprise source types，并设计 500 个 questions、10 个 diagnostic categories。它同时测 document recall、answer alignment/completeness、source constraints、conflict resolution 与 not-found behavior。

## 相比什么前进了

通用 RAG benchmark 往往是一问一证据。企业场景中同一事实可能在 email、ticket、wiki、document 中重复、冲突或缺失；EnterpriseRAG-Bench 把这种 coherent cross-source workspace 设为统一 ontology，使 conflict 和 absence 进入 contract。

## 分数边界

combined score 支持在 synthetic company ontology、chunking/indexing 与 judge 下的 enterprise-style RAG；它不证明真实企业 deployment，因为 permissions、organizational drift 与 proprietary distributions 都没有被复现。

## 公平比较条件

锁定 generated corpus version、chunking/index、reader、judge、source constraints 与 question category。不同 corpus generator/version 应单独 snapshot。

## 下一步评测坐标

下一步应加入真实 authorization、versioned artifacts 与 write operations，验证冲突解决后系统是否会更新或污染共享知识状态。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合在统一企业式语料中研究噪声、重复、冲突和缺失信息。连贯的合成公司比互不关联文档更利于交叉推理，但组织权限与真实业务语义仍不是自动获得的；高分不能直接解释为企业部署可靠性。

### 一个具体任务长什么样

示意任务：项目决定分散在文档、消息与其他企业来源中，其中有重复版本和相互冲突的描述。系统需要识别有效证据并回答完整范围；找出一个支持片段并不代表已经处理了冲突。

### 最有判别力的实验

固定语料快照与切块方式，分别测来源受限、冲突、完整性和无答案问题。加入正确文档集合给定条件，再按语料规模扩展，检验收益来自跨来源推理、索引覆盖还是对合成公司的适配。

### 建议搭配

[gatemem](gatemem.md) · [mudabench](mudabench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
