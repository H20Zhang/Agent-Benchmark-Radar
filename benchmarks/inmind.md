# InMind：真正相关的 memory 可能和 query 一点也不像

**中文** | [English](inmind.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2607.24368) · [项目页](https://keep-it-inmind.github.io/) · [代码](https://github.com/imlrz/InMind)

## 它到底测什么

InMind 针对一个 **implicit-association retrieval blind spot**：真正影响当前 query 的个人 memory，表面语义可能和 query 很远；只有把个人事实与外部 world knowledge 结合起来，才知道它其实相关。benchmark 因而明确拆开“模型看到 memory 后会不会用”与“memory system 能不能意识到应该把它找出来”。

## 相比此前评测多测了什么

多数 memory retrieval 依赖 lexical/embedding similarity，多数 benchmark 也奖励 direct fact recall。InMind 对同一个个人事实构造 direct / indirect paired control；indirect query 的 relevance 必须经过外部知识桥接，而不是靠表面相似度。

## 决定性证据

套件包含 10 个 domain 的 125 个专家验证任务，其中 113 个由公开来源 grounding。当 decisive memory 直接放入 context 时，backbone 对 indirect question 的正确率达到 84.0%；但要求 memory system 自己 retrieve 后，6 类 vector / graph / agentic memory 方法最高只有 14.4%，而 direct recall 可以达到 100%。让 memory 始终可见的 diagnostic probe 能恢复大部分差距。

## 这个分数能证明什么

这是很强的证据：瓶颈可能位于 **query-to-memory interface**，而不是 storage capacity 或 answer reasoning。它也不能推出 similarity retrieval 应该被淘汰，因为 benchmark 本身就是有意选择“相似度不够”的 case。

## 公平比较契约

应固定 background memory trace、backbone、world-knowledge access、retrieval budget 与 direct/indirect paired task，并一起报告 oracle-in-context、target recall、end-answer accuracy。没有 oracle 条件时，retrieval failure 和 answerer failure 会再次混在一起。

## 还没有测什么

数据规模不大，而且专门针对 similarity 的弱点；真实 personal-agent workload 中这种 indirect relevance 的占比还未知。主动 world-knowledge search 还可能引入明显成本与 hallucination risk。

## 下一步最有判别力的验证

先在真实个人 agent log 中测 indirect relevance 的发生率，再在 equal-cost 下比较 query expansion、world-knowledge-conditioned retrieval 与 agentic search。系统层真正的问题是：能不能用一个便宜 trigger 判断什么时候普通 similarity retrieval 已经不可信。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究相关性必须借助常识才能成立的记忆检索。它尤其能挑战‘向量相似就足够’的前提；但间接问题失败也可能因为骨干缺少连接知识，不能未经对照就判定检索器有问题。

### 一个具体任务长什么样

示意任务：历史保存了一条个人事实，新问题使用完全不同的概念，只有理解二者的常识联系才知道应调出该事实。直接问原事实可以成功，却不能说明系统会在需要时主动检索它。

### 最有判别力的实验

对同一事实配对直接和间接查询，并补充事实已放在上下文中的条件。先检查骨干能否在证据给定时完成连接，再比较检索路由；另加不相关但词面相似的干扰，检验方法是否只是扩大召回。

### 建议搭配

[locomo-plus](locomo-plus.md) · [came-bench](came-bench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`semantic recall → query-conditioned retrieval → knowledge-mediated relevance discovery`

它挑战的是一个很基础的假设：当前 query 并不总是一个足够好的 retrieval key。