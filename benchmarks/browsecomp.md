# BrowseComp：持续搜索难以定位的事实

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（历史参考）** · 2025-04-10 · 官方首发<br>
> **OpenAI deep research — Accuracy: 51.5%**<br>
> 首发官方文章的最佳模型成绩；原始 1,266 题。作者说明 deep research 的训练专门覆盖此类任务。 [原始来源](https://openai.com/index/browsecomp/)<br>
> 仅供了解当时难度，不代表当前最佳；不同任务、版本和实验条件不能直接混比。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](browsecomp.en.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已阅读下述主论文全文的方法、实验设置、结果与局限；未独立复现实验。

全文第1–5节及附录A–B的预测/评分提示，全部表1–3和图1–5。

[arXiv v1 (2025-04-16)，与 2025-04-10 发布文章分开](https://arxiv.org/pdf/2504.12516v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## 与相邻评测相比改变了什么

以下为基于所读协议的编辑比较，不表示论文宣称直接继承。

相较HotpotQA的固定百科证据，BrowseComp把困难主要放在开放网页事实定位与持续搜索。最终短答案简化判分，却没有提供固定候选语料或逐步证据使用的可归因性；BrowseComp-Plus随后针对这一界面缺口冻结语料。
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## 任务与证据如何构造

人工先选稳定事实，再逆向构造多约束难题；通过模型、五次简单搜索和部分人类尝试筛难。评分器判断最终短答案与参考的语义等价，不检查搜索证据链。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 复现时必须保留的条件

共 1266 道题。表中 GPT-4o 为 2024-08-06，搜索版为 gpt-4o-search-preview-2025-03-11，o1 为 2024-12-17 的 medium 设置。Deep Research 训练过相似任务，论文没有给出可对齐的绝对工具/token 预算；最终裁判的精确模型也未清楚注明。并行实验每题最多采样 64 次，按置信度选择 best-of-N，不能当作 oracle pass@N。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 历史系统结果

1266 道题的参考答案等价准确率，单位百分数；模型版本见条件表，Deep Research 的绝对工具／token 预算未公开。

| 系统 | 准确率 |
|---|---|
| GPT-4o | 0.6 |
| GPT-4o browsing | 1.9 |
| o1 medium | 9.9 |
| Deep Research | 51.5 |

事实来源：表 3 · [论文](https://arxiv.org/pdf/2504.12516v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 人类尝试的不同分母

计数表；367/1255 为自报解出，317/367 为已解出子集的参考答案一致，不能把 29.2% 当作参考答案准确率。

| 结果 | 分子 | 分母 |
|---|---|---|
| 自报解出 | 367 | 1255 |
| 已解出子集内参考答案一致 | 317 | 367 |
| 尝试至少 2 小时后放弃 | 888 | 1255 |

事实来源：表 2 · [论文](https://arxiv.org/pdf/2504.12516v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## 这些比较支持什么结论

29.2%是人类自报解出比例，并非参考答案通过率；模型版本与训练、工具同时不同，也不能从表3隔离浏览工具的因果贡献。
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## 局限、来源冲突与下一步

唯一答案未穷举证明；筛题本身依赖被测模型。并行投票大幅增加资源，不等于单次能力。下一步固定版本/预算并核实完整证据。

第4.5节称14%题目零成功，后文又出现删21题前的1287题中118题零成功，样本版本/分母未对齐。精确校准误差定义和绝对浏览预算未充分给出。
<!-- EVIDENCE:limitations:END -->

相关基准：[browsecomp-plus](browsecomp-plus.md) · [livebrowsecomp](livebrowsecomp.md)
