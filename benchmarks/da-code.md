# DA-Code：把 data analysis decomposition 变成 executable coding benchmark

**中文** | [English](da-code.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

## 它在测什么

DA-Code 包含 500 个 executable Python/SQL tasks，覆盖 data wrangling、machine learning 与 exploratory analysis，并用 task accuracy/completion 检查 agent 是否能把自然语言分析需求分解成可运行的数据处理步骤。

## 相比什么前进了

DS-1000 多是局部 library coding；DA-Code 更接近分析任务，把 SQL/Python 与多步骤 data operations 结合，使 task decomposition 与 execution chain 进入同一评测。

## 分数边界

execution success 支持在当前 sandbox、data assets 与 task specification 下完成分析操作；它仍没有覆盖自主问题发现、业务语义或最终 report quality。

## 公平比较条件

锁定 Python/SQL runtime、package versions、task data、allowed tools、step/retry budget 与 completion criterion。

## 下一步评测坐标

后续需要把 executable analysis 与不确定 ground truth、visualization、reporting 和跨系统 data access 结合起来。
