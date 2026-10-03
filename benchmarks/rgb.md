# RGB：分别检验噪声、拒答、信息整合与反事实

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2023-09<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://arxiv.org/abs/2309.01431)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](rgb.en.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已阅读下述主论文全文的方法、实验设置、结果与局限；未独立复现实验。

全部正文、构造、评测、错误分析和表1–7；此版本没有独立附录。

[v1,2023-09-04](https://arxiv.org/pdf/2309.01431v1)

补充核验首发评估代码: [d2293eec8c76467c1572b3ebedcaca4e9b4e82f4](https://github.com/chen700564/RGB/blob/d2293eec8c76467c1572b3ebedcaca4e9b4e82f4/evalue.py)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## 与相邻评测相比改变了什么

以下为基于所读协议的编辑比较，不表示论文宣称直接继承。

相较主要测检索排序的基准，RGB通过受控上下文替换直接诊断生成器怎样使用证据。它为后来的拒答、冲突与整合评测提供分解坐标，但没有测真实搜索过程。
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## 任务与证据如何构造

新闻问答经人工检查后检索Google前10页，切成最多300词元片段并稠密重排。以每题五文档为名义设置控制噪声比例、无答案、跨文档整合和人工反事实；这测生成器的证据使用，不是检索器排序。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 复现时必须保留的条件

基准问答每语言 300 题；信息整合与反事实各每语言 100 题。ChatGPT 指 gpt-3.5-turbo，精确日期版本未注明。答案准确率使用答案子串匹配，不能保证完整回答无矛盾。Rej 检查指定拒答字符串，Rej* 用 ChatGPT 判断语义拒答。反事实实验仅测试闭卷准确率超过 70% 的模型，并明确提示其警惕错误文档。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## ChatGPT证据使用诊断

ChatGPT百分比；声明题集规模为噪声/拒答每语言300题，整合/反事实每语言100题；实际计分分母未提供日志。噪声比例为名义设置；准确率为子串匹配，Rej为指定字符串，Rej*为语义判断。

| 指标／条件 | 英语 | 中文 |
|---|---|---|
| 噪声比例 0 的准确率 | 96.33 | 95.67 |
| 噪声比例 0.8 的准确率 | 76.0 | 70.67 |
| 信息整合，噪声比例 0 的准确率 | 55 | 63 |
| 信息整合，噪声比例 0.4 的准确率 | 34 | 47 |
| 纯噪声拒答率 Rej | 24.67 | 5.33 |
| 纯噪声语义拒答率 Rej* | 45 | 43.33 |
| 反事实测试的闭卷准确率 | 89 | 91 |
| 提供反事实文档时的准确率 | 9 | 17 |

事实来源：表 1,3,5,7 · [论文](https://arxiv.org/pdf/2309.01431v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:interpretation:START -->
## 这些比较支持什么结论

低拒答率既含证据判断失败，也含未按指定句式输出；应并列Rej与Rej*。反事实题筛选为模型已知知识，不能直接外推新知识场景。
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## 局限、来源冲突与下一步

提示明确警告错误，字符串命中仍可能夹带矛盾内容。下一步在真实检索轨迹中分别审核答案、弃答和证据纠错。

反事实纠错率的分母没有足够明确，本文不自行补数；所选表格数字未发现实质冲突。

[首发评估代码](https://github.com/chen700564/RGB/blob/d2293eec8c76467c1572b3ebedcaca4e9b4e82f4/evalue.py)会在候选不足时调整文档组成，并跳过异常；300是声明题集大小，实际运行排除日志未提供。噪声比例是名义设置。论文未明确解码参数；代码默认温度与示例命令不同，不能据任一默认值补齐实验条件。
<!-- EVIDENCE:limitations:END -->

相关基准：[ragtruth](ragtruth.md) · [lit-ragbench](lit-ragbench.md)
