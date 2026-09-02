# T²-RAGBench：text-table financial QA 在拿掉 oracle context 后才真正变成 RAG

**中文** | [English](t2-ragbench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://aclanthology.org/2026.eacl-long.8/) · [代码](https://github.com/uhh-hcds/g4kmu-paper)

## 它在测什么

当前 T²-RAGBench release 含 23,088 个 question-context-answer triples，覆盖 7,318 份 financial reports，来源于 FinQA、ConvFinQA first turn 与 TAT-DQA；最初 paper 报告 32,908，后续移除 VQAonBD。benchmark 同时测 text/table retrieval MRR@3 与 numerical answer，并提供 oracle-context upper bound。

## 相比什么前进了

原 financial QA dataset 通常直接给出正确 context，无法评价 retrieval。T²-RAGBench 去掉 oracle evidence，把 end-to-end text-table retrieval 与 numerical reasoning 接起来，并保留 oracle baseline 来定位 retrieval loss。

## 分数边界

retrieval MRR 与 numerical accuracy 支持当前 dataset/version、serialization 与 reader 下的表现；release 已发生样本组成变化，因此 paper 初版与 current artifact 不是同一 track。

## 公平比较条件

锁定 dataset version、document serialization、chunk/index pipeline、reader 与 corpus-size setting，并显式区分 oracle-context 与 retrieved-context。

## 下一步评测坐标

下一步应覆盖更长 financial collections、cross-report aggregation 与 provenance，评价数字答案是否由完整证据链支持。
