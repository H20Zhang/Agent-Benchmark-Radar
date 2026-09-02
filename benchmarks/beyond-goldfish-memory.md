# Beyond Goldfish Memory：multi-session conversation 的早期长期记忆坐标

**中文** | [English](beyond-goldfish-memory.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://aclanthology.org/2022.acl-long.356/)

## 它在测什么

该工作用跨多次 human-human chat sessions 的开放域对话，检查对话系统能否记住过去互动并保持 persona、事实和交流连续性。它早于今天的 memory-agent 体系，核心对象是 cross-session recall 与 conversation consistency。

## 相比什么前进了

传统 dialogue benchmark 通常把一次 session 当成独立样本。这里第一次系统性要求模型在下一次聊天中继续承接过去，使“跨 session 的长期状态”成为独立评测维度，并为 LoCoMo 等后续长时对话 benchmark 提供前驱坐标。

## 分数边界

生成质量或人评可以说明系统在给定 dialogue model 与 retrieval/summarization 方法下保持连续性的能力，但不能区分 write、retrieval 与 generation 的贡献，也没有测试 knowledge update、tool use 或未来 action。

## 公平比较条件

应锁定 dialogue model、历史可见方式、retrieval/summarization strategy 和 human-evaluation protocol。现代更强模型直接使用更长 context 的结果不能与早期 external-memory setup 简单横比。

## 下一步评测坐标

后续 benchmark 需要从“还记得之前聊过什么”推进到更新、冲突、忘记、行动与成本，验证记忆是否真正改变未来行为。
