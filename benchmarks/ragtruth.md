# RAGTruth：定位检索增强回答中的局部幻觉

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2024-01<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://arxiv.org/abs/2401.00396)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](ragtruth.en.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已阅读下述主论文全文的方法、实验设置、结果与局限；未独立复现实验。

全文第1–7节及附录A–C的例子和生成/检测提示；表5–6经图像核对。

[arXiv v1；PDF 页眉为 2023-12-31](https://arxiv.org/pdf/2401.00396v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## 与相邻评测相比改变了什么

以下为基于所读协议的编辑比较，不表示论文宣称直接继承。

与RGB的受控压力测试相比，RAGTruth在人类标注的实际模型回答中定位局部无依据内容。变化是从整题正确率转向幻觉位置与检测器质量；回答筛选实验仍区别于主动检索修复。
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## 任务与证据如何构造

2973个输入生成六模型回答，得到17838条自然回答；人工按明显/隐晦矛盾及无依据引入四类标注局部幻觉。错误拒答另标，JSON空值误作false可独立纳入或排除。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 复现时必须保留的条件

测试为 450 个来源实例，每任务 150 个，每个实例有六个模型回答，不能称为只有 450 条回答。检测器为 Llama2-13B 的 LoRA，学习率 3e-4，训练三轮、使用四块 A100。回答级 F1 检测有无幻觉，跨度 F1 按字符重叠计算，不是词元或整段精确匹配。SelfCheck 对照使用另五个模型的回答，区别于同一模型的重复采样。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 检测与局部定位分开

450 个测试来源实例，每任务 150 个、每实例有多个模型回答；F1 单位百分数，回答级按是否有幻觉，跨度级按字符重叠计算。

| 方法 | 回答级 F1 | 字符跨度 F1 |
|---|---|---|
| GPT-4-turbo prompt | 68.3 | 32.7 |
| Finetuned Llama2-13B | 80.7 | 54.8 |

事实来源：表 5–6 · [论文](https://arxiv.org/pdf/2401.00396v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 筛选减少幻觉但可能损失覆盖

Llama 2-7B／Mistral 7B 的成对候选，450 个来源实例；返回数单位为条，幻觉率分母为该行实际返回回答数。

| 筛选规则 | 返回回答数 | 返回回答中的幻觉率 |
|---|---|---|
| 随机选择 | 450 | 55.1 |
| 选择检测到的幻觉跨度最少者 | 450 | 43.1 |
| 仅保留未检出幻觉者 | 326 | 23.9 |

事实来源：表 7, 节 6.3 · [论文](https://arxiv.org/pdf/2401.00396v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## 这些比较支持什么结论

论文已有候选回答筛选；这不是主动补搜或修订。无检测幻觉策略只返回326/450题，低幻觉率须与覆盖率一起看。
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## 局限、来源冲突与下一步

v1未给充分人工一致性量化；任务和六模型限定分布。下一步留出生成器/领域，并比较修复后的完整性而非只删内容。

微调检测器的字符跨度F1在表6为54.8，第6.2节写48.4，本文按表归属保留。表7另一组10.4→5.3被称下降41%，按展示舍入值约为49%，尚未解决。
<!-- EVIDENCE:limitations:END -->

相关基准：[ragbench](ragbench.md) · [claimprobe](claimprobe.md)
