# DSGym：先过滤“不看数据也能做”的 data-science benchmark

**中文** | [English](dsgym.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2601.16344) · [代码](https://github.com/fannie1208/DSGym)

## 它到底测什么

DSGym 同时是标准化 **execution framework** 和经过筛选的 task suite，用 self-contained environment 评估/训练 data-science agent 的分析、prediction 与 domain-specialized workflow。

## 相比此前评测多测了什么

作者发现现有 data-science benchmark 有相当一部分任务即使不使用给定数据也能答。DSGym 显式过滤 shortcut-solvable problem，并标准化 environment interface，把 data grounding 与 cross-benchmark comparability 放到中心。

## 决定性证据

DSGym 清洗既有任务，并新增 DSBio 与 DSPredict，覆盖 bioinformatics 和更难的 prediction；它还支持 execution-verified trajectory synthesis。作为 training case，2,000 个生成样本训练出的 4B model 在标准化 analysis benchmark 上超过 GPT-4o。

## 这个分数能证明什么

它对“agent 是否真的会在受控 environment 中 plan、implement、validate analysis”证据较强。4B training result 说明 framework 可用于训练，但不能推出小模型在 benchmark 外普遍优于更强模型。

## 公平比较契约

应固定 Docker/environment image、tool、dataset、metric implementation、agent scaffold、model 与 execution budget，保留 shortcut filter，并把 pass@k 与 average trajectory score 分开报告。

## 还没有测什么

标准化也牺牲了一部分生产 messy reality：enterprise semantics、permission、evolving repository、collaboration 与 deployment 不是核心对象。

## 下一步最有判别力的验证

对每个 benchmark source 公布 shortcut filtering 前后的 performance delta，直接量化过去看似的 data-agent progress 有多少其实来自 benchmark leakage 或“不用数据也能答”。

## 演化位置

`fragmented data-science benchmarks → grounded standardized gym → execution-verified agent training/evaluation`

它把 benchmark validity 与 environment reproducibility 本身当成研究贡献。