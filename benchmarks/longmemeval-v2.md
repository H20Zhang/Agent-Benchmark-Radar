# LongMemEval-V2：工作流和文件工具怎样帮助找回行动历史

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2026-05<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://arxiv.org/abs/2605.12493)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](longmemeval-v2.en.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已核对所述论文版本的方法、实验设置、关键结果与局限；未独立复现实验。

已阅读正文第1—6节与附录A—E，包括标注、评分细则、全部列出的控制器/沙箱提示、消融、案例和局限。表格已核对，未独立测量截图像素或曲线，也未运行代码。

[arXiv 2605.12493v1 (2026-05-12)](https://arxiv.org/html/2605.12493v1)

页首历史参考原样保留；正文的新版本结果不能代替原始发布成绩。
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 任务怎样产生记忆需求

依次写入预收集网页轨迹，搜集紧凑多模态证据，再让固定读取器回答451道题。分别测试静态状态、动态变化、工作流、陷阱与错误前提识别。R使用状态/事件/笔记池；C通过清单、流程指引和检查脚本搜索文件。

定位比较：LongMemEval-V2延续长期记忆问答方向，但将核心证据扩展到用户—智能体工具调用历史，并比较文件、编码工具与检索式工作流。它不是简单把原版历史加长；新问题和控制器设置使跨版本分数不能直接相减。 这里是评测坐标比较，不表示直接继承了前者的数据。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 实验设置与评分对象

Small为各域共享100轨迹、约25Mtokens；Medium每题约500轨迹、115M。读取器Qwen3.5-9B，上限200Ktokens，采样温度0.6/top-p0.95。R控制器为开启思考的Qwen3.5-9B，嵌入Qwen3-Embedding-8B；coding控制器为Codex0.117.0中的GPT-5.4-mini xhigh。查询并发上限3。结构化答案用匹配，陷阱/错误前提题由GPT-5.2 medium评判。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 主表比较同时包含控制器差异

共用回答器与上下文上限，但控制器模型随方案变化；C对Codex是更接近匹配的控制器比较。延迟仅为查询阶段，不是全生命周期成本。

每档451题，主结果包含前提错误题。

| 系统 | Small准确率（%） | Small查询延迟（秒） | Medium准确率（%） | Medium查询延迟（秒） |
|---|---|---|---|---|
| RAG: query→slice+notes | 51.0 | 0.2 | 45.9 | 0.3 |
| AgentRunbook-R | 58.6 | 26.9 | 57.0 | 25.8 |
| Codex | 69.9 | 177.2 | 68.7 | 185.8 |
| AgentRunbook-C | 74.9 | 108.3 | 70.1 | 139.9 |

定位：表2：主要方法 · [原文](https://arxiv.org/html/2605.12493v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 辅助函数的收益并非所有切分都一致

同一编码控制器；去掉辅助函数降低Small成绩，却略提高Medium，不能声称全面有益。

同一编码控制器与各档451题。

| 配置 | Small准确率（%） | Medium准确率（%） |
|---|---|---|
| AgentRunbook-C | 74.9 | 70.1 |
| AgentRunbook-C without workflow | 70.1 | 64.1 |
| AgentRunbook-C without helper functions | 71.4 | 71.8 |

定位：表2：编码控制器消融 · [原文](https://arxiv.org/html/2605.12493v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## 理想证据试验采用不同题集和回答方式

直接QA，不是主实验的上下文收集任务；同时改变证据选择与笔记，不能作为主分数的硬上限。

排除前提/弃答题的先导子集；表中未报告精确题数，不能视为完整451题主结果。

| 模型 | 直接理想轨迹（%） | 理想片段加笔记（%） |
|---|---|---|
| Qwen3.5-9B (thinking) | 59.6 | 82.5 |
| GPT-5.4-mini (medium) | 65.3 | 86.3 |

定位：图4的先导实验、附录B · [原文](https://arxiv.org/html/2605.12493v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## 结论边界与下一步验证

文件辅助设计改善了所测准确率/延迟取舍，但未测试实时任务执行或终身更新收益。题目经筛选使强模型无历史时出错，不能外推自然请求中的发生率。UNKNOWN记0；陷阱题只需一个正确且无矛盾见解，前提题规则也接受明确说明无法核验实时实例。

每题历史规模的表1上限为498会话，正文以约500会话描述，不应写成所有题恰有500会话。查询模板还包含question_type和original_goals元数据；在归因前需要核验各基线的输入权限是否完全一致。

下一步：在同一控制器和成本预算下比较R与C，分别计量写入、查询和读取成本。保持Small/Medium证据种子一致，测试新环境，再加入有/无历史的可执行后续任务。
AgentRunbook-C保留原始轨迹；它是证据搜集策略，不是把整个档案压缩成摘要。最多选择20个状态、返回200K词元上下文。两档均值72.5/69.3/48.5分别属于C、Codex、slice+notes；48.5不是全部RAG方案最高值，AgentRunbook-R为57.8。
<!-- EVIDENCE:limitations:END -->
