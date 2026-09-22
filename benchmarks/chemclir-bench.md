# ChemCLIR-Bench：把跨语言技术检索的失败拆到语言对和排名深度

**中文** | [English](chemclir-bench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2609.23231) · [代码](https://github.com/MohammadKhodadad/Multi-Lingual-QAC) · [数据](https://huggingface.co/datasets/MehdiAstaraki/multilingual_GP)

## 它在测什么

ChemCLIR-Bench 在 Google Patents 与 EPO 化学专利材料上比较同语言与跨语言检索。论文评测五种语言、八个 embedding 模型；检索脚本另提供按查询语言、原生或合成翻译来源、目标语言及语言对拆分的 Recall@10 / MRR@10 分析。[论文](https://arxiv.org/abs/2609.23231) · [官方实现](https://github.com/MohammadKhodadad/Multi-Lingual-QAC/blob/main/README.md)

## 相比什么前进了

相较 BEIR 的跨领域检索，这里的关键变量是专业领域中查询语言和证据语言不一致。更深的排名诊断可以区分“相关证据完全未找到”和“仍可找到但排得太低”，因此一个总体 Recall 不足以解释系统退化。它不是迭代式搜索或完整 RAG 问答评测。

## 实际怎样评测

公开流水线导出 MTEB 格式的 corpus、queries 和 qrels。当前生成路径先为文档产生英语问答，经过语言、忠实度与检索质量检查，再翻译到目标语言；运行记录保存数据规模、模型、Git 版本与逐题结果。仓库允许更多翻译语言，不能把当前配置直接等同于论文的五语言实验。

## 决定性证据与分数边界

论文摘要报告最佳模型的 Recall@10 从同语言 0.72 降至跨语言 0.53。这是该数据与配置下的结果，不是跨领域通用幅度，更不能直接推算下游答案损失。仓库还明确说明多语言正文和权利要求比标题、摘要稀疏，部分字段主要有英语；不同语言的可见内容必须检查。[结果来源](https://arxiv.org/abs/2609.23231) · [字段限制](https://github.com/MohammadKhodadad/Multi-Lingual-QAC/blob/main/README.md)

## 主要混杂与尚未覆盖的能力

最强替代解释是英语种子查询、翻译风格和各语言内容字段不等价，而不只是 embedding 对齐能力。还应检查专利家族重叠、相关性标签构造与样本过滤。公开数据的存在不代表这些混杂已经被完全排除。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合多语言企业知识库或技术检索中的语言对诊断，作为下游 RAG 实验的检索层检查。

### 一个具体任务长什么样

示意：中文查询描述一个化学工艺，相关专利只有德文摘要；只在中文结果中命中类似主题并不等于找到支持证据。

### 最有判别力的实验

固定文档字段、专利家族划分和 qrels，比较多语言 dense、查询翻译加 BM25 与 hybrid；逐语言对报告 Recall/MRR，并把原生问题和翻译问题分开，控制相同检索与重排预算。

### 建议搭配

[beir](beir.md) · [ontologybench](ontologybench.md) · [commercial-tax](commercial-tax.md)

<!-- RESEARCH-DECISION:END -->

---

证据核验：2026-09-23。本条依据论文元数据、官方协议及上述公开实现或数据说明；不把结构校验当作事实认证，也未独立复现实验。
