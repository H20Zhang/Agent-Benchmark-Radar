# ClaimProbe：忠实度改善，需要同时看整体质量与写作成本

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2026-08-12<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://arxiv.org/abs/2608.28643)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](claimprobe.en.md) · [主入口](../README.md) · [基准资料库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已核对所述主论文版本的方法、设置、关键结果与局限；未独立复现实验。

v1主文第1—8节、局限与附录A—F，包括PDF中的评判／抽取提示；未独立执行系统或逐行核验发布代码的完整抽取器。

[arXiv:2608.28643v1](https://arxiv.org/html/2608.28643v1)

下列表格重新组织了有来源的选定事实。页首历史参考与正文采用的版本、切分和模型可能不同，不能跨表混合成绩。
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 测量对象、方法与比较

固定检索证据，只替换写作模块：先由问题生成提纲，再抽取、去重事实并分配章节，最后逐节写作和解析来源标记。审计双向检查报告主张及高相关源事实，使用top20候选；默认指标接受部分支持，严格指标不接受。

[原文](https://arxiv.org/html/2608.28643v1)
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 实验设置与分母

三个宿主为EDR、AI-Q、ODR，写作模型均为GPT-5.5，宿主内对照固定检索证据。主ClaimProbe审计用GPT-5.4-mini和100道题，嵌入为text-embedding-3-small，双向候选各取前20条；汇总是合并分子／分母的微平均。Hall分母为全部报告主张，Mis为带引用主张，Rec为高相关源事实，三者不能共用分母。RACE使用GPT-5.5，但表1写n=100、方法段写50道英文题，原文未解消这一冲突。

[设置来源](https://arxiv.org/html/2608.28643v1)
EDR是Enterprise Deep Research，AI-Q是NVIDIA AI-Q，ODR是OpenDeepResearch。Hall指没有检索来源支持的报告主张比例；Mis指引用的来源不支持、但其他已检索来源支持的错引比例；Rec指高相关源事实被报告覆盖的比例。默认指标可接受部分支持，严格指标要求完全支持。

<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 固定证据后，主张级指标确实改善

EDR宿主、GPT-5.5写作、GPT-5.4-mini评判，100题微平均；默认指标接受部分支持，严格版另算。

| 写作配置 | Hall（%，越低越好） | Mis（%，越低越好） | Rec（%，越高越好）  严格Hall（%，越低越好） | 严格Rec（%，越高越好） |
|---|---|---|--- --- | --- |
| 原写作模块 | 15.89 | 18.94 | 36.83  54.05 | 13.67 |
| ClaimWriter | 5.02 | 5.43 | 45.85  28.55 | 24.48 |

这支持固定来源条件下的写作侧忠实度收益，不表示检索覆盖变好，也不能直接推断现实部署中幻觉率。

事实来源：表2, 第4–5.2节 · [原文](https://arxiv.org/html/2608.28643v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 三个宿主的整体评分都小幅下降

RACE、GPT-5.5评判；原文题量50／100冲突未解决。每行只比较同一宿主的原写作模块和ClaimWriter。

| 宿主 | 原整体分（0–1） | ClaimWriter整体分（0–1） | 原可读性（0–1） | ClaimWriter可读性（0–1） |
|---|---|---|---|---|
| EDR | 0.544 | 0.536 | 0.510 | 0.470 |
| AI-Q | 0.553 | 0.535 | 0.528 | 0.473 |
| ODR | 0.540 | 0.530 | 0.523 | 0.485 |

应解释为忠实度提高，伴随小幅整体评分下降和可读性下降，不能再写成“RACE有所改善”。

事实来源：表1, 第5节.1 · [原文](https://arxiv.org/html/2608.28643v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## 首次写作并非等预算对照

EDR、GPT-5.5，每份报告的写作阶段平均；不含搜索、工具、查询或计划生成成本。

| 写作配置 | 输入词元／报告 | 输出词元／报告 |
|---|---|---|
| 原写作模块 | 1019276 | 92252 |
| ClaimWriter | 9697825 | 700626 |

复用事实结构可能降低后续更新成本，但首次写作成本显著增加。更新实验只有5题，不能从这里推定任意工作负载都能摊薄成本。

事实来源：表7,附录E · [原文](https://arxiv.org/html/2608.28643v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## 结论边界、缺口与下一步

评判仍依赖抽取器、相关性标签和前20条候选，漏检会影响结论。Hall的κ=0.484针对人类一致标签；对多数票只有0.299，不能省略这个范围。附录声称更新后所有指标在±1个百分点内，但表6的严格Hall有43.7→45.3，本文保留冲突。相比整篇报告评分，局部审计能揭示不同错误，却不自动消除评判偏差。下一步匹配写作预算，独立检查候选漏检和人类标签，并扩大更新任务。

[原始证据](https://arxiv.org/html/2608.28643v1)
<!-- EVIDENCE:limitations:END -->

<!-- RESEARCH-DECISION:START -->

上述方法、对照与局限一起决定何时适合使用这个基准；表格不构成跨协议排行榜，结构校验也不证明事实正确或完成复现。

相关测量与对照：[DeepResearch Bench](deepresearch-bench.md) · [LiveDRBench](livedrbench.md) · [Mr.LHDR](mr-lhdr.md)

<!-- RESEARCH-DECISION:END -->
