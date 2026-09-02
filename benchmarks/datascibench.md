# DataSciBench：当 ground truth 不再是一个简单 unit test，Data Science 需要 IFC-style evaluator

**中文** | [English](datascibench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[项目页](https://datascibench.github.io/) · [代码](https://github.com/THUDM/DataSciBench)

## 它在测什么

DataSciBench 覆盖六类 data-science tasks、25 个 aggregate functions 与 519 个 test cases，问题来自更自然、复杂且 ground truth 不容易直接获得的分析需求。它用 Intention-Function-Code (IFC) framework 将意图、函数与 executable code outcomes 映射到 programmatic metrics；ACL 2026 版本评估了 26 个 models。

## 相比什么前进了

DS-1000 适合有明确 unit tests 的代码问题。DataSciBench 面对 uncertain GT 与多种可行 analysis outputs，尝试用半自动 GT generation + human verification + aggregate metrics 扩大可评价任务范围。

## 分数边界

IFC/completion metrics 支持在当前 GT pipeline 与 evaluator rules 下的 data-science competence；它仍可能偏向被预定义 aggregate functions 覆盖的分析形式，不能等同于完整 analyst artifact quality。

## 公平比较条件

锁定 benchmark version、GT generation/verification、IFC rules、runtime、agent scaffold 与 model budget。不同 evaluator generation 应分 track。

## 下一步评测坐标

下一步要把代码结果与 reasoning trace、visual artifact、source grounding 和 stakeholder-facing report 联合评价。
