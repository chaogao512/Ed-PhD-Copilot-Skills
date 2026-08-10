<div align="center">

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Version](https://img.shields.io/badge/version-1.9-blue.svg)]()
[![Platform](https://img.shields.io/badge/platform-agnostic-green.svg)]()
[![GitHub stars](https://img.shields.io/github/stars/chaogao512/Ed-PhD-Copilot-Skills?style=social)](https://github.com/chaogao512/Ed-PhD-Copilot-Skills)

</div>

# Ed-PhD-Copilot-Skills

[🇺🇸 English](./README.md) | 🇨🇳 中文

面向教育技术、教育领导与管理、教育信息化治理方向的结构化 AI 技能库。平台无关：任何能按 `SKILL.md` 触发技能的智能体平台（Reasonix、ChatGPT Custom GPT、Claude Project、Cursor Rules）都可以直接使用。

它参考了 `Supervisor-Skills` 的 "Handbook + Skills" 双轨组织方式，但内容按教育信息化治理、智能校园、教育数字化转型、教育领导力与教育研究方法重写。

## 这个项目解决什么问题

它不是通用写作提示词集合，而是把教育技术研究中容易走偏的判断显性化：

- 选题值不值得做——政策价值、组织可行性、伦理风险、理论贡献一次评估完
- 论文骨架怎么搭——机制类、实证类、指标类各有结构模板
- 证据怎么设计——混合方法、量表开发、质性编码、统计报告都有最低要求
- 引言和讨论怎么写——有段落逻辑，不靠堆砌
- 投稿前怎么自查——按期刊标准查理论、方法、伦理、格式
- AI 用到哪里为止——人机分工、披露、验证一条条写清楚

## Skills 总览

| Skill | 做什么 |
|---|---|
| `governance-idea-evaluator` | 评估选题：致命缺陷闸门、七维评分、推进或转向建议 |
| `edtech-intro-drafter` | 引言大纲：政策背景—技术可能—治理异化—研究合法性 |
| `governance-paper-template` | 论文骨架：论文类型、理论架桥、技术-组织双层结构、博士各阶段模板 |
| `mixed-methods-evidence-template` | 混合证据链：声称-证据矩阵、三角互证、报告规范门槛 |
| `governance-figure-designer` | 图示设计：机制图、流程图、证据链图，附质量审计 |
| `edtech-pre-submission-reviewer` | 投稿前审查：CRITICAL/MAJOR/MINOR 分级，含 APA 7th / CSSCI 格式门 |
| `ai-assisted-edtech-research-workflow` | AI 使用边界：人机分工、红线、披露模板、验证清单 |
| `literature-reader` | 读文献：Zotero/本地目录输入，文献卡 + 系统综述流程 |
| `governance-discussion-drafter` | 讨论写作：理论对话、文献对比、局限分类、有边界的启示 |
| `scale-development-template` | 量表开发：构念定义、题目池、专家评审、EFA/CFA、信效度、常模 |

## 目录结构

```text
Ed-PhD-Copilot-Skills/
├── README.md / README.zh-CN.md
├── LICENSE
├── docs/            评审、案例、示例、文献依据
├── handbook/        系统指南：6 章 13 篇方法论文档（论文评价/选题/写作/作图/Vibe Research/案例）
├── plugins/
│   └── ed-phd-copilot/skills/   10 个技能，各含 SKILL.md + agents/openai.yaml + references/
├── scripts/         check_skill_structure.py 结构检查
└── assets/          外部参考资产
```

每个技能三层：`SKILL.md`（frontmatter + 英文执行流程）、`agents/openai.yaml`（平台元数据）、`references/`（评分表、检查清单、模板，按需读取）。

## Handbook：知识层

Handbook 装的是理论和方法论：怎么判断一篇论文、怎么选题、怎么写、怎么作图。Skills 负责执行，Handbook 负责解释为什么这样做。调用技能之前，先读对应的 Handbook 章节。

| 章节 | 主题 | 核心内容 |
|---|---|---|
| 01 宏观认识与评价 | 如何评价一篇论文的质量 | 审稿视角、EdTech 期刊评审文化、理论根基 |
| 02 Idea 的诞生与升华 | 选题、创新与能力匹配 | 研究类型生命周期、五维 Idea 框架、颠覆式创新 |
| 03 论文写作方法论 | 从骨架到细节 | Introduction Flowchart、Full Paper 模板、写作 Checklist（APA 7th / CSSCI） |
| 04 科研作图指南 | 论文图表的设计与绘制 | 动机图、方案总览图、实验结果图范式、工具速查表 |
| 05 Vibe Research | AI 辅助科研实战 | Vibe Coding / Figure / Writing 心法技法、工具经验、AI 使用边界 |
| 06 论文写作案例 | EdTech 论文写作剖析 | 建设中——拟收录类型已列出 |

## 推荐使用路径

1. 选题初筛：`governance-idea-evaluator`
2. 论文骨架：`governance-paper-template`
3. 证据设计：`mixed-methods-evidence-template`（量表为核心时走 `scale-development-template`）
4. 引言：`edtech-intro-drafter`
5. 图示：`governance-figure-designer`
6. 讨论与启示：`governance-discussion-drafter`
7. 投稿审查：`edtech-pre-submission-reviewer`
8. 文献与 AI 边界贯穿全程：`literature-reader`、`ai-assisted-edtech-research-workflow`

## 当前状态

版本 **V1.9**（2026-08-10）。

**技能与支撑**

- 10 个技能，每个都有 `SKILL.md`、`agents/openai.yaml` 和 `references/`
- 方法规范齐全：PRISMA/COREQ/CONSORT/WWC/MMAT 报告门槛、质性三级编码与 Cohen's κ、效应量与功效分析、系统综述流程、APA 7th 与 CSSCI 格式门
- 理论锚点覆盖治理与教学双线：协同治理、数据治理、制度理论，以及 CoI、认知负荷、自我决定、UTAUT 等

**证据与案例**

- 5 个案例文档跑通技能链：智能校园治理（主案例，输出 01–09）与 4 个迁移案例（教师数字胜任力、教育数据治理、人机协同课堂评价、学习分析学业预警，各含 7 技能链输出）
- 9 个主案例技能输出 + 11 个失败案例回归
- 文献依据：`docs/evidence-base.md`、`docs/verified-source-registry.md`、中文核心文献核验登记

**评审记录**

- 每版评审存档于 `docs/review-YYYY-MM-DD-vX.Y.md`，最新为 [`docs/review-2026-08-10-v1.9.md`](docs/review-2026-08-10-v1.9.md)

**验证**

- `make check` 跑通全仓库结构检查（等价于 `python3 scripts/check_skill_structure.py`）

下一步方向：中文核心/CSSCI 文献逐条核验、安装后真实触发测试、按实际研究方向出开题报告样稿与研究设计流程图。路线见 [`docs/roadmap.md`](docs/roadmap.md)。

## 与 Supervisor-Skills 的关系

本仓库借鉴 `HKUSTDial/Supervisor-Skills` 的组织理念，内容按教育技术、教育领导与管理、教育信息化治理方向改写。原项目与本项目均采用 CC BY-NC-SA 4.0。再改编时请注明本项目来源，并遵守原项目署名要求。来源说明见 [`NOTICE.md`](NOTICE.md)。

## License

[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)：非商业用途，须署名并以相同协议共享。
