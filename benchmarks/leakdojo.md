# LeakDojo：RAG benchmark 还需要问“数据库内容能被攻击者抽出来多少”

**中文** | [English](leakdojo.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://aclanthology.org/2026.findings-acl.287/) · [代码](https://github.com/yeasen-z/LeakDojo)

## 它在测什么

LeakDojo 是 configurable RAG leakage diagnostic。paper 比较 6 种既有 leakage attacks、14 个 LLMs 与 FIQA、SciFact、NFCorpus、Enron 四个 datasets；当前代码实现 7 种 attack methods。指标包含 query-budget scaling、ROUGE-L recall 与 unique chunk recovery，并支持 defense ablation。

## 相比什么前进了

以往 leakage 工作常只在一个 model/pipeline 上展示一个攻击。LeakDojo 把 attack、model、retriever、corpus 与 defense 配置统一成可比较实验矩阵，使 database extraction risk 成为可重复的 RAG evaluation object。

## 分数边界

recovered text/chunks 支持在指定 attack budget、chunking、query generator 与 RAG pipeline 下的 extraction risk；它不覆盖 permissions、API secrets、cross-tenant access 或真实 incident impact。

## 公平比较条件

锁定 corpus/chunking、attack implementation、query budget、generator、model、retriever 与 leakage threshold。不同 budget 必须画 curve，而不是只报一个 maximum。

## 下一步评测坐标

下一步应把 content extraction 与 authorization boundary、sensitive-field severity 和 production consequence 联合评价，而非所有 chunk 等权。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合在受控 RAG 配置下比较知识库内容泄露风险与防御。恢复多少文本取决于查询预算和切块方式；它不能替代跨租户权限或真实生产事故评估，也不能只看一次攻击的最高泄露率。

### 一个具体任务长什么样

示意任务：攻击者通过有限查询试图恢复本不应公开的检索库内容，防御则限制暴露同时保留正常问答。相同内容被重复吐出与不断恢复新的片段，代表不同的累积泄露风险。

### 最有判别力的实验

固定语料、切块、检索器和查询预算，同时报告唯一片段恢复与正常问答质量。按不同攻击与模型交叉比较，检验防御是否只是抑制某种输出样式，而非真正减少不当证据暴露。

### 建议搭配

[gatemem](gatemem.md) · [injecmem](injecmem.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
