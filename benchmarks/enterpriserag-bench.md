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
