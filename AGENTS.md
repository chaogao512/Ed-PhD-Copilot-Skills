# Ed-PhD-Copilot-Skills

面向教育技术、教育领导与管理、教育信息化治理方向的 AI Skills 项目（平台无关的通用智能体技能库），V1.8。

## Project

- **定位**: 结构化 AI 技能库，服务教育信息化治理博士研究（选题、论文骨架、证据设计、引言、图示、投稿审查、AI 使用边界）。
- **平台**: 平台无关——可在 Reasonix、ChatGPT Custom GPT、Claude Project、Cursor Rules 等任何支持按 `SKILL.md` 触发技能的智能体平台使用。
- **入口**: 技能由宿主智能体平台按 SKILL.md 中的 `name` + `description` 触发匹配，无传统 main/entry point。
- **许可证**: CC BY-NC-SA 4.0。

## Commands

- **结构检查**: `python3 scripts/check_skill_structure.py` — 验证 10 个技能的 SKILL.md、agents/openai.yaml、references/ 完整性，docs/ 关键文件与协议段落、示例协议段落、verified-source-registry 标记等。本地开发可加 `make check` 快捷方式（Makefile 为本地维护文件，不随仓库分发）。

（本项目无 build/test/lint/run 命令；它是纯内容仓库。）

## Architecture

```
Ed-PhD-Copilot-Skills/
├── plugins/ed-phd-copilot/skills/   ← 核心：10 个可执行技能
│   ├── governance-idea-evaluator/           选题评估
│   ├── edtech-intro-drafter/                引言起草
│   ├── governance-paper-template/           论文模板
│   ├── mixed-methods-evidence-template/     混合方法证据设计
│   ├── governance-figure-designer/          图示设计
│   ├── edtech-pre-submission-reviewer/      投稿前审查
│   ├── ai-assisted-edtech-research-workflow/ AI 辅助研究流程
│   ├── literature-reader/                   文献读取与系统综述
│   ├── governance-discussion-drafter/       Discussion 写作
│   └── scale-development-template/          量表开发与验证
├── handbook/                        系统指南（6 章 13 篇方法论文档：论文评价/选题/写作/作图/Vibe Research/案例）
├── docs/                            诊断、审查、案例、示例、文献依据
├── scripts/                         check_skill_structure.py 结构完整性检查
└── assets/                          外部参考资产
```

每个技能三层结构：
- `SKILL.md` — YAML frontmatter（name, description）+ 英文执行流程 + Reference 导航
- `agents/openai.yaml` — display_name, short_description, default_prompt
- `references/` — 按需加载的评分表、检查清单、模板、样例等

## Conventions

- **技能语言**: SKILL.md 正文用英文（面向 AI agent 执行）；docs/ 和 README 用中文。
- **技能 frontmatter**: 必须包含 `name` 和 `description`（YAML），description 用于触发匹配。
- **渐进披露**: 技能主流程在 SKILL.md，细节在 references/ 中按需读取。
- **版本命名**: V1.x 语义化版本；评审文档 `docs/review-YYYY-MM-DD-vX.Y.md`。
- **新增技能**: 必须提供 SKILL.md + agents/openai.yaml + references/ 至少一个文件，并在 `scripts/check_skill_structure.py` 的 `REQUIRED_REFERENCE_HINTS`（及相应版本增量表）中注册；如有文档/案例/示例要求，同步在 `REQUIRED_DOCS`、示例协议检查处登记。
- **引用外部来源**: 所有外部文献、政策、标准必须在 `docs/verified-source-registry.md` 登记，AI 生成的题录不得作为正式引用。
- **AI 使用边界**: 技能是辅助判断工具，不可替代研究者的选题、理论、证据和学术责任判断。

## Notes

（待后续补充）
