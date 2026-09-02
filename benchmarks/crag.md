# CRAG：把 freshness、long tail 与 abstention 带进 RAG

**中文** | [English](crag.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2406.04744) · [代码](https://github.com/facebookresearch/CRAG)

## 它在测什么

CRAG 含 4,409 个 QA pairs，覆盖五个 domain、八类问题，并通过 mock web API 与 knowledge-graph API 测动态事实、长尾实体、检索与 abstention。答案 grading 对 hallucination 敏感，因此“没有可靠证据时不答”也是能力的一部分。

## 相比什么前进了

静态 RAG benchmarks 容易把 corpus 当成永恒真相。CRAG 把 popularity、freshness 与 dynamic facts 纳入 evaluation，并作为 KDD Cup 2024 challenge 推动系统比较，说明 knowledge cutoff 与 retrieval source 本身是 benchmark variables。

## 决定性证据与分数边界

CRAG 的价值在于让 static-parametric knowledge 与 dynamic external evidence 的边界变得可测。一个高分支持系统在该 mock API / KG snapshot 与 grading rule 下处理事实查询；它不能证明 live-web agent 普遍更强，因为真实网页 interface、provider ranking 和 drift 被模拟层控制了。

## 公平比较条件

锁定 mock API/KG version、knowledge cutoff、answer grader、allowed tools 与 retrieval budget。不同 external model cutoff 或真实搜索接口应分 track。

## 下一步评测坐标

下一步应把 freshness 保留下来，同时用可重放网页 snapshot 或 recorded tool traces 控制 drift，从而区分 retrieval policy、source quality 与 model knowledge。
