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
