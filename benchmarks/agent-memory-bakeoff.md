# Agent Memory Bakeoff：写入扩展能否弥补查询词汇变化

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2026-08-21<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://github.com/JaysonRawlins/agent-memory-bakeoff)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](agent-memory-bakeoff.en.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已阅读固定版本的官方协议、设置、结果记录与局限；未独立复现实验。

完整阅读固定提交的README、语料和查询生成器、主题种子、检索与评分脚本；解析已发布数据计数并检查一个完整场景及同场景文档。未独立运行检索，提交树没有完整原始检索矩阵。

[固定版本 57585be8bcf7](https://github.com/JaysonRawlins/agent-memory-bakeoff/blob/57585be8bcf735ef783fc0b8134e809b943d9695/README.md)

[辅助材料（2026-09-30查阅）](https://github.com/JaysonRawlins/agent-memory-bakeoff/blob/57585be8bcf735ef783fc0b8134e809b943d9695/gen/generate_corpus.py)

[辅助材料（2026-09-30查阅）](https://github.com/JaysonRawlins/agent-memory-bakeoff/blob/57585be8bcf735ef783fc0b8134e809b943d9695/gen/generate_queries.py)

[辅助材料（2026-09-30查阅）](https://github.com/JaysonRawlins/agent-memory-bakeoff/blob/57585be8bcf735ef783fc0b8134e809b943d9695/runners/retrieve.py)

[辅助材料（2026-09-30查阅）](https://github.com/JaysonRawlins/agent-memory-bakeoff/blob/57585be8bcf735ef783fc0b8134e809b943d9695/eval/score.py)

[辅助材料（2026-09-30查阅）](https://github.com/JaysonRawlins/agent-memory-bakeoff/blob/57585be8bcf735ef783fc0b8134e809b943d9695/data/queries/queries.jsonl)

页首历史参考原样保留；正文的新版本结果不能代替原始发布成绩。
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 任务怎样产生记忆需求

Agent Memory Bakeoff是检索组件实验。每个虚构运维场景生成1—3篇不同角度的记忆，再分别建立原文索引和扩展索引；扩展只增加2—3条未来搜索表达与一条症状描述。BM25、向量及分数融合使用相同文档和查询。它直接改变写入表示，没有回答模型，因此可以观察可访问性，但不能判断答案或行动是否更好。

谱系：这是围绕作者私有记忆系统经验构造的公开合成复核，不是LoCoMo或LongMemEval的数据派生。与这些下游QA基准相比，改变的是停止点：找到同场景任一文档就计成功。私有系统的盲评和低延迟叙述没有公开轨迹，不能当作该公开实验已验证的结果。
理解查询桶的示意：文档用一个内部缓存模块名记录故障，之后查询只描述“更新后仍显示旧值”。扩展索引把症状表达补进写入文本；评分只查是否找回同场景文档，不验证故障是否修好。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 实验设置与评分对象

固定提交实数为225场景、497文档、390查询；查询只来自130场景，每场景标识符、概念和症状各一条。文档、扩展与查询都由claude-haiku-4-5生成，查询看隐藏场景、不看文档或搜索短语；这减少直接照抄，但同源模型与情境仍产生相关性。BM25用bm25s默认设置和英文停用词，向量用本地nomic-embed-text余弦；混合分数先逐查询min-max归一化，再以α加权BM25、1−α加权向量。α遍历0.1到0.9，无独立调参集。MRR取前10中首个同场景文档的倒数名次；Recall@1/@5实际是查询级任一金文档命中率，不是全部金文档覆盖率。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 写入扩展在两种检索器上分别比较

同文档内容、查询与金集合，扩展增加索引文本，未匹配存储或写入计算预算。MRR为0—1，其余为百分比。

总390查询，三桶各130；每三条共享一个场景。

| 系统 | MRR@10 | Recall@1% | Recall@5% | 症状Recall@5% |
|---|---|---|---|---|
| bm25-plain | 0.678 | 58.7 | 79.7 | 60 |
| bm25-enriched | 0.783 | 70.3 | 89.7 | 83.8 |
| vector-plain | 0.565 | 46.7 | 69.7 | 39.2 |
| vector-enriched | 0.625 | 52.1 | 76.7 | 63.1 |

定位：固定版README：写入表示对照 · [原文](https://github.com/JaysonRawlins/agent-memory-bakeoff/blob/57585be8bcf735ef783fc0b8134e809b943d9695/README.md)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 调融合系数要保留留出边界

最佳α在同一查询集上挑选；0.806比0.783高0.023，但Recall@5未提高，概念桶反而下降。不能把该最优值当成留出泛化增益。

390查询，标识符与概念各130；无重复运行或按场景区间。

| 系统 | MRR@10 | Recall@5% | 标识符Recall@5% | 概念Recall@5% |
|---|---|---|---|---|
| bm25-enriched | 0.783 | 89.7 | 99.2 | 86.2 |
| hybrid α=0.5 enriched | 0.801 | 90.5 | 99.2 | 86.9 |
| hybrid α=0.6 enriched | 0.806 | 89.7 | 99.2 | 84.6 |

定位：固定版README：扩展与融合对照 · [原文](https://github.com/JaysonRawlins/agent-memory-bakeoff/blob/57585be8bcf735ef783fc0b8134e809b943d9695/README.md)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## 结论边界与下一步验证

它支持该合成语料上写入扩展对BM25的收益，不能推出嵌入普遍无用。扩展与查询都刻意采用症状词汇，且所有同场景文档都是金答案，未人工验证每篇都能解决每个查询。数据发布是固定的，LLM重新生成不是确定的。未报告稳定模型摘要、全矩阵原始检索输出、置信区间或公开延迟表；不能把README的私有成本优势当作这里的量化结论。

README称增益全部集中于症状，但概念命中也从79.2%升至86.2%，标识符从100%降至99.2%。盲查只是不看文档，不能声称查询统计独立。向量缓存只按文件名和行数校验，编辑内容但行数不变时需要清缓存，避免旧向量污染。



下一步：与LongMemEval或InMind配对，在自然、场景留出的查询上比较相同额外词元预算的写入扩展、查询扩展与重排，再测答案效用和错误扩展。按场景而非单查询自助抽样，调α使用独立开发集，保存模型摘要与完整排名。
<!-- EVIDENCE:limitations:END -->
