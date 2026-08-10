# Handbook：教育技术专业博士科研系统指南

> 本手册改编自 [Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills)（CC BY-NC-SA 4.0，作者骆昱宇，香港科技大学广州），结合教育技术、教育领导与管理、教育信息化治理方向进行内容迁移与适配，服务博士研究训练。

本目录沉淀教育技术、教育领导与管理、教育信息化治理方向的系统指南：从论文质量判断、选题与 Idea 生成，到论文写作方法论、科研作图、AI 辅助科研（Vibe Research）实战，覆盖博士研究的完整科研流程。

## 目录结构

| 章节 | 主题 | 核心内容 |
|---|---|---|
| 01 宏观认识与评价 | 如何评价一篇论文的质量 | 从审稿视角理解论文标准（含理论根基维度），适配 EdTech 期刊评审文化 |
| 02 Idea 的诞生与升华 | 选题、创新与能力匹配 | EdTech 研究类型分类与生命周期、五维 Idea 框架（EdTech 版）、颠覆式创新 |
| 03 论文写作方法论 | 从骨架到细节 | Introduction 写作模型、教育技术类论文思考模板、写作细节与 Checklist（含 APA 7th / CSSCI 规范） |
| 04 科研作图指南 | 论文图表的设计与绘制 | 动机图、方案总览图、实验结果图的设计范式与 EdTech 示例、绘图 Checklist 与工具速查表 |
| 05 Vibe Research | AI 辅助科研实战 | Vibe Coding/Figure/Writing 方法论心法技法、工具经验与 AI 使用边界 |
| 06 论文写作案例 | EdTech 论文写作剖析 | [建设中] 将收录 EdTech 代表性论文（DBR/实证/系统评估/理论/量表）的逐段剖析 |

## 与 Skills 的关系

Handbook 提供**理论框架和方法论**，Skills（`plugins/ed-phd-copilot/skills/`）提供**可执行的 AI 工具**。两者配合使用：阅读 Handbook 建立判断力 → 在具体任务中调用对应 Skill 获得结构化输出。

| 迁移章节 | 对应技能（举例） |
|---|---|
| 01 论文质量评价 | `edtech-pre-submission-reviewer`（投稿前审查） |
| 02 Idea 与选题 | `governance-idea-evaluator`（选题评估） |
| 03 论文写作 | `edtech-intro-drafter`、`governance-paper-template`、`mixed-methods-evidence-template`、`governance-discussion-drafter`、`scale-development-template` |
| 04 科研作图 | `governance-figure-designer`（图示设计） |
| 05 Vibe Research | `ai-assisted-edtech-research-workflow`（AI 辅助研究流程） |
| 06 论文案例 | `literature-reader`（文献读取与系统综述） |

## 迁移说明

- 本手册由原 [Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) 手册迁移适配而来：方法论框架保留，CS 领域示例已替换为教育技术场景（学习分析、智能导学系统、自适应学习、教育信息化治理等）。
- 原手册中「Benchmark 与 Evaluation 类论文思考模板」（3.4）基于数据为中心的 AI 基准构建范式，是计算机科学特有论文类型，未迁移；教育技术领域的对应物（评估工具/量表开发论文范式）待后续补充。
- 原手册三篇 CS 案例剖析（Alpha-SQL / AFlow / LEAD）未迁移，第六章将收录教育技术代表性论文剖析案例（建设中）。
- 各章文件头部均标注来源与许可（CC BY-NC-SA 4.0）。

## 写作基调

Handbook 应服务于博士研究训练，而不是堆叠概念。每篇指南都应回答：

- 这个问题在教育技术研究中为什么重要？
- 需要调用哪些教育学、管理学或系统科学理论？
- 技术系统与人、组织、制度之间的关系如何被论证？
- 哪些证据可以支撑结论，哪些证据不能越界？（效应量与置信区间、样本与功效、信效度、伦理合规）
