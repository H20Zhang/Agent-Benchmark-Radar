# BRIGHT：当 relevance 本身需要 reasoning

**中文** | [English](bright.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2407.12883) · [官方榜单](https://brightbenchmark.github.io/) · **领域：RAG / Retrieval**

BRIGHT 的核心问题不是“retriever 能否理解 query 语义”，而是更难的一层：**相关性本身是否需要先推理才能被识别？** 如果 query 与正确文档之间没有直接词汇或 embedding 相似度，只靠一次向量匹配就可能系统性漏掉答案。

## 它到底测什么

BRIGHT 包含 **1,384 个真实 queries**，覆盖 economics、psychology、mathematics、coding 等多个领域。

与传统 retrieval benchmark 不同，很多相关文档只有在先理解问题、推导隐含条件或构造 reasoning steps 后，才会显得相关。因此 nDCG@10 不只测 representation similarity，也间接暴露：

- query 是否被正确分解；
- 隐含 constraint 是否被识别；
- retrieval query 是否需要 reasoning expansion；
- reranker 是否能识别“表面不相似但逻辑上相关”的证据。

## 相比此前评测多测了什么

BEIR 的重点是 **跨领域 zero-shot generalization**：换 domain 后 retriever 是否还能泛化。

BRIGHT 增加的是另一维：即使 domain 已知，**relevance judgment 本身也可能需要 reasoning**。

这两个 benchmark 不应被当成替代关系：

- BEIR 更像 robustness test；
- BRIGHT 更像 reasoning-aware relevance test。

一个方法可能在 BEIR 上稳定，却在 BRIGHT 上因为无法做 query reasoning 而明显退化。

## 实际怎样评测

BRIGHT 的核心输出仍是 ranking metric，例如 nDCG@10。也就是说，它最终评价的是“正确文档排得够不够前”。

但产生这个 ranking 的方法可以非常不同：

- 原始 query 直接 dense retrieval；
- LLM 先生成 reasoning / query expansion；
- multi-query retrieval；
- retrieve-then-rerank；
- 针对不同 dataset 使用额外 preprocessing。

因此解释一个 BRIGHT 分数时，必须把 **reasoning budget、reranking stage 和 index setting** 与分数一起报告。

## 决定性证据与当前成绩

原始论文最重要的发现不是某个绝对数字，而是：当相关性需要 reasoning 时，当时的强 retrievers 相比传统 retrieval benchmark 出现明显下降。这说明 BRIGHT 确实暴露了传统相似度检索的盲区。

官方 leaderboard 后续持续更新。本 Radar 当前单独追踪 short-document 12-dataset mean nDCG@10；任何“当前最佳”都只应该解释为 **该 leaderboard track、该时间点、该协议下的最高已核验分数**，不能外推到 long-document、不同 subset 或 agentic search。

## 分数能说明什么

更高的 BRIGHT nDCG 支持的是：在指定 dataset mixture、document setting 和 retrieval pipeline 下，系统更能找到 reasoning-dependent relevant documents。

它不能单独证明：

- agent 的 multi-step search 更强；
- 最终 QA answer 更正确；
- reasoning 本身是因果来源；
- 系统成本更优。

例如，一个非常昂贵的 query-expansion + reranking pipeline 可能显著提高 nDCG，但并不意味着它是更好的 production retriever。

## 最主要的混杂因素

第一是 **reasoning expansion budget**。用一个强 LLM 生成大量候选 query，本身就可能带来显著收益。

第二是 **reranking**。如果一个方法做单阶段 retrieval，另一个方法在 top-k 上再跑昂贵 cross-encoder 或 LLM judge，两者并不是同一个系统成本级别。

第三是 **dataset aggregation**。不同子数据集难度和规模不同，macro average 会隐藏某些 domain 的失败。

第四是 **short vs. long document setting**。document granularity 改变后，retrieval difficulty 和 index cost 都会变化。

## 公平比较条件

至少需要对齐：

- short / long document setting；
- dataset subset；
- index preprocessing 与 chunking；
- 是否允许 reasoning expansion / multi-query；
- reranker 类型与 candidate depth；
- LLM、token 与调用预算；
- metric 与 aggregation rule。

如果这些条件不同，应该分别报告 track，而不是混成一个统一排名。

## 还没有覆盖什么

BRIGHT 本质上仍是 **static ranking benchmark**。它没有完整测量：

- 根据第一次 retrieval 失败后主动改写 query；
- 多步搜索中的 evidence chaining；
- live corpus 与新信息；
- search trajectory 的错误定位；
- latency、token、tool-call 与 index serving cost；
- retrieved evidence 是否最终被 generator 正确使用。

## 下一步最有判别力的验证

下一步最值得做的是把 BRIGHT 从“一次 ranking”扩展成 **reasoning-controlled retrieval trajectory**：给 agent 相同 query，允许有限次 search / reformulation，并同时记录每一步新找到的有效证据与成本。

这样可以比较：一个系统是因为 first-hop retriever 更强，还是因为它更会发现自己第一次没搜对并进行修正。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合检验相关性本身需要推理的检索任务。它比普通语义相似检索更能区分查询理解能力，但查询改写、长推理与重排都增加计算；只有在相同资源约束下比较，才能判断方案是否更有效率。

### 一个具体任务长什么样

示意任务：查询描述一个现象，真正有用的文档解释背后的原理，却没有重复查询词语。系统需要推断信息需求；检索到许多主题相同但不能解释现象的文档，并不构成有效证据。

### 最有判别力的实验

固定语料与相关性标注，对比原查询、模型改写查询、重排与混合检索，并分别计入改写和重排成本。再按领域与推理类型分析，区分更好表示、更多计算和参数知识提供的收益。

### 建议搭配

[beir](beir.md) · [bright-pro](bright-pro.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`semantic similarity retrieval → reasoning-aware relevance → iterative reasoning-controlled evidence search`

BRIGHT 位于中间一步：它把“相关性需要推理”正式变成 benchmark，但还没有把完整 search process 作为评测对象。
