# AutoResearchBench：定位目标论文并发现未知大小的论文集合

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（历史参考）** · 2026-04 · 论文 v1<br>
> **Claude-Opus-4.6 / ReAct — Deep Research accuracy: 9.39%**；**Gemini-3.1-Pro-Preview / ReAct — Wide Research IoU: 9.31%**<br>
> 表 2 受控 ReAct 比较中的分项最佳；不混入只跑 50 题的端到端系统测试，也不把 IoU 当准确率。 [原始来源](https://arxiv.org/html/2604.25256v1)<br>
> 仅供了解当时难度，不代表当前最佳；不同任务、版本和实验条件不能直接混比。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](autoresearchbench.en.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已阅读下述主论文全文的方法、实验设置、结果与局限；未独立复现实验。

28页正文第1–5节及附录A–G全部阅读，包含构造审核、运行/工具细节、完整提示与案例；实际运行分母和审核协议冲突仍未解。

[arXiv v1, 2026-04-28](https://arxiv.org/pdf/2604.25256v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## 与相邻评测相比改变了什么

以下为基于所读协议的编辑比较，不表示论文宣称直接继承。

与SAGE的目标论文/开放集合两分法相近，AutoResearchBench进一步用困难筛选、无答案及集合交并比强调精确约束和多报惩罚。它扩大学术检索压力，但摘要化工具接口与有效分母缺口仍限制解释。
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## 任务与证据如何构造

围绕DeepXiv超过300万篇arXiv论文，构造600道Deep和400道Wide题。Deep以全文细节、引用关系及弱化词面线索定位唯一论文，另改坏一个条件生成60道无答案题；筛除GPT-5.4改写搜索、Sonnet/Flash代理及10分钟人类检索轻易解决的题。Wide从主题候选提炼多重条件，扩展候选并逐篇全文审核，最终每题2–34篇，平均9.23篇。Deep指标为预测集合与金标集合完全相等；Wide为逐题集合交并比IoU后平均，罚漏检也罚多报。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 复现时必须保留的条件

主评测为单一search工具的ReAct循环：最多30轮，软上下文11万token，每轮最多4096新token，温度0.6，默认每次10篇；官方API或SGLang。关键接口限制是：DeepXiv虽存全文，给代理的search_evidence来自正文首个可用片段再经辅助LLM压缩，没有单独全文打开工具。工具错误、上下文/轮次上限都会触发终止。端到端产品另用随机50题，不与600题轨道等价。多次采样报告Deep pass@k与Wide oracle best@k，后者不是可部署的无金标选优。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 已报告主轨道成绩与成本

Deep标称600题、Wide400题；具体有效Deep分母未解，数字按原表报告。时间为每题平均秒数，IoU为逐题集合交并比均值×100；共享search-only ReAct但模型推理实现不同。

| 模型 | Deep准确率（%） | Deep秒数 | Wide IoU（%） | Wide秒数 |
|---|---|---|---|---|
| GPT-5.4 | 7.44 | 72.5 | 8.12 | 115.98 |
| Gemini-3.1-Pro-Preview | 7.93 | 1221.4 | 9.31 | 235.3 |

事实来源：表 2; 附录表 8–9 · [论文](https://arxiv.org/pdf/2604.25256v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 同框架的文献搜索后端替换

同ReAct与名义600/400题，Deep分母缺口同上；百分数与每题平均调用数。开放网搜为Jina且偏向arXiv，DeepXiv索引和摘要方式不同。

| Gemini-3.1-Pro 后端 | Deep准确率（%） | Wide IoU（%） | Wide调用数 |
|---|---|---|---|
| 开放网页搜索 | 6.82 | 7.37 | 2.92 |
| DeepXiv | 7.93 | 9.31 | 3.49 |

事实来源：表 3 · [论文](https://arxiv.org/pdf/2604.25256v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## 这些比较支持什么结论

应把结果限定为具体接口与样本：主ReAct轨道Opus的Deep为9.39%，Gemini-Pro的Wide IoU为9.31%，但端到端GPT Deep Research另在50題中答对11题，不能称全部系统都低于10%。Deep标称含10%无答案且按集合精确匹配，按公式总输出空集应得10%；原文未报告此朴素基线或解释主表有效分母，因此“最高仅9.39%”的解读必须保留这个核验缺口。全文细节型任务配摘要压缩接口，也使低分不能纯归因于科研推理能力。
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## 局限、来源冲突与下一步

模型/人类难度筛选使题集刻意对抗特定系统，不能代表所有真实文献检索。无答案和穷尽集合不能由有限搜索形式化证明；额外预测96%无效的人工审查没有明确样本量，不能等同金标完整性保证。辅助摘要模型、候选累计策略及语料时间界限会影响成绩。下一步先发布逐题评测分母、空集基线和准确的审核流程，再为代理增加同预算全文读取工具，并让人工复核未列入金标的有效论文。

Deep标称600题含60空集，9.39等主表百分数不符合单次600题二元均值步长；实际分母/排除/多次聚合不明，总空集基线按所述公式应为10%。Wide正文要求三模型全票及最终人工全面审查，附录却为多数票、50%抽样和75%精度阈值。补充池704题/4887篇与最终400题/3692篇转换细节不足。Sonnet Wide主表5.83与附表4.96、DeepSeek不同表7.70/5.96冲突。错误分析Opus4.5与主表4.6也不同；SAGE“无交互环境”的综述说法与SAGE原文MCP实验不符。
<!-- EVIDENCE:limitations:END -->

相关基准：[sage](sage.md) · [scholarquest](scholarquest.md)
