# StatFormBench：代码执行之前，先检验分析问题有没有定义对

**中文** | [English](statformbench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2609.01982) · [代码](https://github.com/THU-CongLab/StatFormBench) · [数据](https://huggingface.co/datasets/THU-CongLab/StatFormBench)

## 它在测什么

StatFormBench 把统计分析的上游步骤拆为问题分类与变量识别、角色分配。它来自五本统计教材和数据科学案例库，含 1,013 个样本、20 个粗粒度和 85 个细粒度类别。目标是分析该怎样定义，而不是一个已经指定好的程序是否输出正确结果。[论文](https://arxiv.org/abs/2609.01982)

## 相比什么前进了

相较 DS-1000 的代码实现和 Spider 的查询生成，它减少了“用户已经给出正确分析目标”这个默认前提。与完整 DataScienceBench 互补：当最后结果出错时，可以先检查方法类别、变量集合和角色是否在执行之前就选错。

## 实际怎样评测

官方运行器把样本和 prompt 发给指定模型，评测脚本读取输出并与参考答案匹配，报告粗细分类准确率、变量集合 Jaccard、precision、recall 和角色一致性。已核对的 variable_metrics.py 使用集合交并比计算 Jaccard；这类变量指标不是运行代码后的功能正确率。[运行与评分说明](https://github.com/THU-CongLab/StatFormBench/blob/main/readme.md) · [变量指标](https://github.com/THU-CongLab/StatFormBench/blob/main/src/evaluation/variable_metrics.py)

## 决定性证据与分数边界

论文在 14 个模型上报告最佳零样本细分类准确率 72.0、变量集合重合度 63.2，且两个子任务没有始终占优的同一模型。这些是各指标上的论文报告，不应拼成某一模型的单条成绩，也不表示分析执行有同样的成功率。[结果来源](https://arxiv.org/abs/2609.01982)

## 主要混杂与尚未覆盖的能力

教材可能进入训练语料；固定 taxonomy 也可能把多种合理分析压成唯一标签。变量别名、输出解析与角色 rubric 都影响测量。这个基准仍不验证实际数据中的统计假设、数值实现或业务目标含糊时的澄清行为。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合给数据智能体增加执行前诊断，判断瓶颈在任务理解还是程序实现。

### 一个具体任务长什么样

示意：用户问“这次改版有没有改善留存”，模型先判断比较对象、结果变量与可能混杂，再决定分析；直接写出可运行的均值查询仍可能回答错问题。

### 最有判别力的实验

固定执行引擎，把模型自行制定的分析与专家提供的 formulation 交给同一执行器；分别报告 formulation 分数和最终数值正确性，再对多解案例进行盲审。若专家 formulation 消除大部分失败，优先修任务定义，而非堆执行工具。

### 建议搭配

[ds-1000](ds-1000.md) · [datascibench](datascibench.md) · [data-agent-benchmark](data-agent-benchmark.md)

<!-- RESEARCH-DECISION:END -->

---

证据核验：2026-09-23。本条依据论文元数据、官方协议及上述公开实现或数据说明；不把结构校验当作事实认证，也未独立复现实验。
