# GISA：web search benchmark 也可以有 deterministic structured answers 和 human trajectories

**中文** | [English](gisa.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2602.08543) · [代码](https://github.com/RUC-NLPIR/GISA)

## 它在测什么

GISA 有 373 个 human-crafted queries，覆盖 10 个 topic groups，并用 item、set、list、table 四种 structured answer formats，同时区分 stable 与 live subsets。每个 query 都保留完整 human search trajectory，最终答案可用 deterministic exact-match 评价并定期刷新 live answers。

## 相比什么前进了

很多 deep-search benchmark 依赖短答案或 LLM judge。GISA 同时保留 human process trace 和结构化可验证答案，使 deep lookup 与 broad aggregation 都能在少依赖 judge 的条件下评价。

## 分数边界

structured exact match 支持在当前 answer refresh 与 web snapshot 下的最终信息获取；trajectory overlap 只能说明与 human path 的相似程度，并不代表那是唯一有效策略。live subset 随时间变化，所以 score date 是 evaluation contract 的一部分。

## 公平比较条件

锁定 stable/live split、answer refresh date、search provider、tool interface 与 output normalization。不同 refresh generations 必须分 snapshot。

## 下一步评测坐标

下一步可利用 human traces 评估 efficiency 与 repair：agent 是否用更少无效搜索达到同等 evidence coverage，而非仅模仿 human sequence。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究深查与广搜共同存在的信息获取，尤其是集合、列表和表格答案。结构化输出便于确定性评价，但内容正确与格式正确仍是两层问题；实时部分还必须绑定答案更新时间。

### 一个具体任务长什么样

示意任务：系统需要找出满足多个条件的一组对象，并按要求输出列表或表格，而不是只给一个代表例子。一个对象遗漏、字段不匹配或顺序错误，都可能改变任务是否被完整完成。

### 最有判别力的实验

把内容匹配错误与序列化错误分开诊断，在相同搜索后端下比较策略，并将稳定题与实时题分开。利用人工搜索轨迹检查遗漏发生在哪一步，但不把偏离人工路径自动判定为错误。

### 建议搭配

[sgr-bench](sgr-bench.md) · [wandr](wandr.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
