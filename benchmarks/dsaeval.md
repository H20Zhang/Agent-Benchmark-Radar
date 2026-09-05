# DSAEval：累积式、多模态 data-science project

**中文** | [English](dsaeval.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2601.13591) · [项目页](https://dsaeval.github.io/DSAEval/)

## 它到底测什么

DSAEval 评估 **真实 data-science project**：包含 multimodal environment perception、cumulative multi-query interaction，并分别评分 reasoning、code 与 result。共有 641 个问题、285 个 structured/unstructured dataset。

## 相比此前评测多测了什么

one-shot coding task 每题都会 reset；DSAEval 让后续 query 依赖此前分析，并把 observation 从 table 扩展到 image/text data，更接近连续的数据科学工作 session。

## 决定性证据

论文评估 11 种先进 agentic LLM：Claude-Sonnet-4.5 overall 最强，GPT-5.2 efficiency 最好，MiMo-V2-Flash cost-effectiveness 最好；multimodal perception 对 vision-related task 带来 2.04–11.30% 提升。structured/routine analysis 明显比 unstructured workload 容易。

## 这个分数能证明什么

benchmark 支持 cumulative project competence，并暴露 quality–efficiency–cost trade-off；但 model/scaffold 仍是一个组合系统，multi-dimensional grading 也可能包含 deterministic execution 之外的 evaluator assumption。

## 公平比较契约

应固定 dataset、query order、accumulated workspace state、tool environment、model、budget 与 evaluator，并精确保留 prior-query output；如果不同系统采用不同 reset/summary 策略，累计任务本身已经变了。

## 还没有测什么

真实项目会跨数周，有 stakeholder feedback、data update、version control 与 production deployment；这里的 cumulative interaction 仍是 bounded benchmark episode。

## 下一步最有判别力的验证

在早期分析里人为注入可控错误，测后续 recovery 与 error propagation，验证 agent 是否维护可信 analytical state，而不只是累积 conversation context。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究累积多问题项目中的多模态数据科学，而不只是独立单题。前面步骤产生的状态会影响后面回答；总分下降可能来自早期错误传播，而不是后续问题自身更难。

### 一个具体任务长什么样

示意任务：系统在同一项目中先探索表格、图像或文本数据，再根据连续请求建模和解释结果。若早期清洗或理解错误，后续笔记本可能继续沿用错误状态，直到最终报告才暴露问题。

### 最有判别力的实验

比较连续自主执行与每轮给定正确前序状态，分别评推理、代码和结果。固定 GPU、笔记本环境与评价器，按模态和问题位置拆分，识别跨轮状态管理是否真正改善了后续任务。

### 建议搭配

[dsagentbench](dsagentbench.md) · [agenticdatabench](agenticdatabench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`one-shot data analysis → cumulative multimodal project → persistent analytical state`

它把跨请求的 state continuity 变成 data-agent 的显式能力。