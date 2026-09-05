# BEIR：把 retriever 的 zero-shot generalization 拉到异构领域

**中文** | [English](beir.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2104.08663) · [代码](https://github.com/beir-cellar/beir) · **领域：RAG / Retrieval**

BEIR 的历史价值是把一个长期被忽略的问题变成标准测试：**一个在熟悉数据上很强的 retriever，换到完全不同的领域后还能不能工作？** 它让 cross-domain zero-shot robustness 从附加实验变成 retrieval 的核心指标。

## 它到底测什么

BEIR 最初汇集 **18 个 retrieval datasets**，覆盖不同领域、任务类型、query 风格和 document 分布，并用统一 ranking protocol 比较 retriever。

它关心的不是某个模型在单一训练/测试分布上的极致分数，而是：

- 不针对目标 domain 重新训练时，ranking quality 是否还能保持；
- lexical、dense、sparse-dense hybrid 和 reranking 方法在不同 domain 上如何取舍；
- 一个方法的收益是不是只来自特定 dataset 的词汇、长度或训练数据重叠。

这使 BEIR 成为“retrieval method 是否真的泛化”的基础坐标。

## 相比此前评测多测了什么

早期 dense retrieval 进展大量围绕 MS MARCO 等少数 benchmark 报告。一个模型可以在训练分布附近显著领先，却未必在 biomedical、finance、argument retrieval 或 fact verification 等领域继续领先。

BEIR 的关键变化是 **heterogeneous suite**：不再问“这个模型能不能把一个 benchmark 做好”，而是问“这个 retrieval inductive bias 在不同信息需求下是否稳定”。

它也让 BM25 重新成为重要基线：dense retrieval 的提升如果不能稳定超过 lexical baseline，就很难声称是普遍的 retrieval 改进。

## 实际怎样评测

典型 BEIR evaluation 会对每个 dataset 单独构建或使用其 corpus / query / relevance judgments，计算 nDCG、Recall 等 ranking metrics，再按指定规则汇总多个 datasets。

解释 aggregate score 时必须知道：

- 实际用了哪些 BEIR datasets；
- corpus preprocessing 与 indexing 方式；
- 是否加入 reranker；
- retriever 是否在目标 benchmark 或相近数据上训练过；
- 最终 aggregate 是 macro average 还是其他汇总方式。

“BEIR 分数”不是一个天然唯一的数字；不同 subset、训练数据和 reranking setting 可能对应不同研究问题。

## 决定性证据与分数边界

BEIR 最重要的早期结论之一是：**在单一 benchmark 上强的 dense retriever，并不保证 zero-shot 跨域仍然占优；BM25 等 lexical baseline 在若干 domain 仍非常有竞争力。**

因此 BEIR 的主要证据价值是 cross-domain ranking robustness，而不是“dense 一定优于 sparse”或反过来。

现代 leaderboard 已经历大量更强 backbone、合成训练数据、instruction tuning 和 reranker 更新，所以今天的 aggregate nDCG 只能支持：在指定 dataset mixture、训练数据和 index protocol 下的 ranking quality。

它不能直接推出 end-to-end RAG answer quality，也不能证明 iterative / agentic search 更好。

## 最主要的混杂因素

第一是 **training-data overlap**。现代 retriever 的训练语料规模远大于 BEIR 时代，所谓 zero-shot 可能并不等于数据意义上的 unseen。

第二是 **subset selection**。只挑若干容易或适合自己方法的数据集，会显著改变平均分。

第三是 **reranking budget**。bi-encoder + expensive reranker 与单阶段 retriever 的最终 nDCG 可以接近，但 latency 和系统成本完全不同。

第四是 **query / corpus preprocessing**。document chunking、title 拼接、normalization、index 参数都可能改变结果。

## 公平比较条件

至少对齐：

- BEIR dataset subset 与版本；
- corpus / query preprocessing；
- retriever training data；
- index 和 search parameters；
- reranker 是否允许及候选深度；
- metric 与 aggregation rule；
- latency / hardware / cost 是否属于比较目标。

Partial-suite average 不应与 full-suite average 直接排在同一个榜单。

## 还没有覆盖什么

BEIR 本质上仍是 **static retriever-only benchmark**。它没有完整测量：

- agent 根据中间结果主动 reformulate query；
- multi-step evidence discovery；
- corpus 随时间变化；
- retrieval 结果是否真正被 downstream generator 正确使用；
- latency、token、index size 和 serving cost；
- 失败时 agent 是否知道需要继续搜索。

## 下一步最有判别力的验证

对现代 agentic retrieval 来说，最有价值的做法不是放弃 BEIR，而是把它当作 **retrieval floor**：先验证单步跨域 retrieval 没有退化，再在同一 domain 上增加 iterative search / reformulation / evidence-use 评测。

如果一个复杂 agent 在最终 QA 上变好，却在 BEIR-style first-hop retrieval 上更差，就需要解释增益来自哪里，而不是把所有提升归功于“更强搜索”。

## 演化位置

`single-domain retrieval → heterogeneous zero-shot retrieval → reasoning-intensive retrieval → iterative / agentic evidence search`

BEIR 是第二步的基础 benchmark：它定义了后来很多 retrieval 系统必须先回答的 baseline question——**你的方法离开训练分布后还成立吗？**
