# Ed-PhD-Copilot-Skills

面向教育技术领域、教育领导与管理专业、教育信息化治理方向的 AI Skills 项目。

本仓库以 `Supervisor-Skills` 的“Handbook + Skills”双轨组织方式为重要参照，但核心内容面向教育信息化治理、智能校园治理、教育数字化转型、教育领导力、组织变革与教育研究方法进行重写和本地化适配。

## 项目定位

`Ed-PhD-Copilot-Skills` 不是通用科研写作提示词集合，而是面向教育技术与教育治理交叉研究的结构化技能库。它帮助研究者在以下场景中获得更稳定的 AI 辅助：

- 教育信息化治理方向选题判断与问题诊断
- 教育数字化转型、智能校园、教育数据治理、AI 教育治理等议题的研究设计
- 教育领导与管理专业论文的结构规划、理论嵌入与方法论校准
- 混合研究、设计科学研究、案例研究、政策文本分析等方法的执行检查
- 教育技术类 CSSCI、SSCI、核心期刊论文的投稿前自查
- 技术系统、组织结构、政策制度与多主体协同关系的图示设计

## 改造依据

本仓库当前改造依据来自两个本地分析文档：

- [`docs/adaptation-diagnosis.md`](docs/adaptation-diagnosis.md)：诊断 `Supervisor-Skills` 与教育信息化治理方向在评价体系、论文叙事、图示逻辑和审稿机制上的不匹配。
- [`docs/paper-template-adaptation-plan.md`](docs/paper-template-adaptation-plan.md)：基于《电化教育研究》顶刊范式，重构教育技术学博士论文写作模板。

## 改造原则

1. 从技术性能导向转向教育治理问题导向。
2. 从算法改进叙事转向政策、组织、技术与人的协同叙事。
3. 从纯技术实验模板转向混合研究、设计科学研究和社科实证研究模板。
4. 从顶会审稿清单转向教育技术与教育管理期刊的理论、伦理、方法和政策合规清单。
5. 从神经网络图示逻辑转向多层治理架构、多主体协同与制度技术关系图示逻辑。

## 目录结构

```text
Ed-PhD-Copilot-Skills/
├── README.md
├── LICENSE
├── docs/
│   ├── adaptation-diagnosis.md
│   ├── paper-template-adaptation-plan.md
│   └── roadmap.md
├── handbook/
│   └── README.md
├── plugins/
│   └── ed-phd-copilot/
│       └── skills/
│           ├── README.md
│           ├── governance-idea-evaluator/
│           ├── edtech-intro-drafter/
│           ├── governance-paper-template/
│           ├── mixed-methods-evidence-template/
│           ├── governance-figure-designer/
│           ├── edtech-pre-submission-reviewer/
│           └── ai-assisted-edtech-research-workflow/
└── assets/
    └── README.md
```

## Skills 总览

| Skill | 用途 |
|---|---|
| `governance-idea-evaluator` | 评估教育信息化治理选题的政策价值、组织可行性、伦理风险和研究贡献 |
| `edtech-intro-drafter` | 生成教育技术/教育治理论文引言逻辑链，突出政策背景、技术赋能、现实异化与研究合法性 |
| `governance-paper-template` | 为智能校园架构、教育数据治理、AI 教育治理等系统/机制类论文搭建逻辑骨架 |
| `mixed-methods-evidence-template` | 设计指标体系、德尔菲论证、信效度检验、伴随式数据与访谈问卷的混合证据链 |
| `governance-figure-designer` | 设计多层治理架构、多主体协同、人智共融与制度技术关系图 |
| `edtech-pre-submission-reviewer` | 按教育技术与教育管理期刊标准进行投稿前审查 |
| `ai-assisted-edtech-research-workflow` | 规划负责任的 AI 辅助教育技术研究流程，保留研究者的学术判断权 |


## 当前成熟度

当前版本为 **V1.7 全链路压力测试增强版**：

- 7 个技能均已具备 `SKILL.md`、`agents/openai.yaml` 和 `references/` 支撑文件。
- 已建立外部依据清单：[`docs/evidence-base.md`](docs/evidence-base.md)。
- 已建立覆盖矩阵：[`docs/skill-coverage-matrix.md`](docs/skill-coverage-matrix.md)。
- 已建立贯穿案例：[`docs/case-multi-agent-smart-campus.md`](docs/case-multi-agent-smart-campus.md)。
- 已用贯穿案例生成 7 个技能样例输出，见 [`docs/examples/`](docs/examples/)。
- 已加入失败案例回测：[`docs/examples/failure-cases/`](docs/examples/failure-cases/)。
- 已加入文献地图：[`docs/literature-map-edtech-governance.md`](docs/literature-map-edtech-governance.md)。
- 已加入中文核心文献 inventory：[`docs/chinese-core-literature-inventory.md`](docs/chinese-core-literature-inventory.md)。
- 已建立中文核心文献正式核验登记模板：[`docs/chinese-core-literature-verified.md`](docs/chinese-core-literature-verified.md)。
- 已加入方法报告模板、设计科学研究报告模板和 filled examples。
- 已加入已核验来源登记表：[`docs/verified-source-registry.md`](docs/verified-source-registry.md)。
- 已完成安装前审计：[`docs/install-readiness-audit.md`](docs/install-readiness-audit.md)。
- 已加入 V1.2 多案例全技能链验证材料：[`docs/cases/`](docs/cases/) 与多场景 7 技能链输出。
- 已完成 V1.1 阶段评审：[`docs/review-2026-06-23-v1.1.md`](docs/review-2026-06-23-v1.1.md)。
- 已完成 V1.2 阶段评审：[`docs/review-2026-06-23-v1.2.md`](docs/review-2026-06-23-v1.2.md)。
- 已完成安装前向模拟测试：[`docs/install-forward-test.md`](docs/install-forward-test.md)。
- 已完成 V1.4 中文政策证据增强评审：[`docs/review-2026-06-23-v1.4.md`](docs/review-2026-06-23-v1.4.md)。
- 已加入 V1.5 方法透明度规则：PRISMA、COREQ、CONSORT/SPIRIT、MMAT 与 WWC 风格证据边界，用于系统综述、访谈/焦点小组、干预研究、混合方法和高风险教育 AI 审查。
- 已为混合方法证据设计与投稿前审查加入 `Light / Standard / Strict` 强度分层，兼顾早期选题探索、开题规划和投稿前严格审查。
- 已新增中文文献公开网络核验日志：[`docs/chinese-literature-web-verification-log.md`](docs/chinese-literature-web-verification-log.md)，明确搜索片段和 AI 生成题录不得升级为正式引用。
- 已补强 AI 辅助研究披露、作者责任和保密边界：AI 不能署名，实质性 AI 使用应按学校/期刊要求披露，敏感教育数据和未发表材料不得未经授权上传外部 AI。
- 已补强图示与引言的高风险 AI 边界：图示需显示模型/系统说明卡、数据说明卡、风险台账和责任泳道；引言需区分探索性文献扫描、系统综述和可支持的证据边界。
- 已完成 V1.5 阶段评审：[`docs/review-2026-06-24-v1.5.md`](docs/review-2026-06-24-v1.5.md)。
- 已加入真实博士选题压力测试：[`docs/examples/pressure-test-digital-governance-doctoral-topic/`](docs/examples/pressure-test-digital-governance-doctoral-topic/)，检验“选题评估 -> 论文模板 -> 证据设计 -> 投稿前审查”的核心链路是否保持同一治理对象和证据边界。
- 已加入可渲染图示与图示 QA：[`docs/examples/figure-rendering/`](docs/examples/figure-rendering/)，用于验证教育数据治理图示是否呈现责任、授权、申诉纠错、数据说明和审计机制。
- 已加入场景化 AI 使用披露模板：[`venue-disclosure-templates.md`](plugins/ed-phd-copilot/skills/ai-assisted-edtech-research-workflow/references/venue-disclosure-templates.md)，覆盖中文 CSSCI/核心期刊、博士开题/答辩、国际期刊和伦理审查场景。
- 已完成 V1.6 阶段评审：[`docs/review-2026-06-24-v1.6.md`](docs/review-2026-06-24-v1.6.md)。
- 已加入完整 7 技能博士选题压力测试：[`02-full-seven-skill-chain-output.md`](docs/examples/pressure-test-digital-governance-doctoral-topic/02-full-seven-skill-chain-output.md)，覆盖选题、论文、证据、引言、图示、审查和 AI 工作流。
- 已新增人机协同评价与教师数字胜任力治理的可渲染图示 artifact，并完成 V1.7 图示 QA。
- 已加入博士阶段模板：[`doctoral-stage-templates.md`](plugins/ed-phd-copilot/skills/governance-paper-template/references/doctoral-stage-templates.md)，覆盖开题报告、中期考核、预答辩和正式答辩。
- 已完成 V1.7 阶段评审：[`docs/review-2026-06-24-v1.7.md`](docs/review-2026-06-24-v1.7.md)。

下一阶段目标是 V1.8/V2.0：继续推进中文核心/CSSCI 期刊论文核验、安装后真实触发测试、博士开题报告级完整样稿和研究设计流程图。具体路线见 [`docs/skill-improvement-task-list.md`](docs/skill-improvement-task-list.md)。

## 推荐使用路径

1. 选题初筛：`governance-idea-evaluator`。
2. 论文骨架：`governance-paper-template`。
3. 证据设计：`mixed-methods-evidence-template`。
4. 引言生成：`edtech-intro-drafter`。
5. 图示设计：`governance-figure-designer`。
6. 投稿审查：`edtech-pre-submission-reviewer`。
7. 全程人机协作边界：`ai-assisted-edtech-research-workflow`。

## 与 Supervisor-Skills 的关系

本仓库借鉴 `HKUSTDial/Supervisor-Skills` 的组织理念和部分技能分工思路，并面向教育技术、教育领导与管理、教育信息化治理方向进行改写。原项目采用 CC BY-NC-SA 4.0 协议；本项目作为改编取向项目，同样采用 CC BY-NC-SA 4.0 协议发布。

使用或再改编本仓库时，请注明本项目来源，同时尊重 `Supervisor-Skills` 原项目的署名与许可证要求。

详细来源说明见 [`NOTICE.md`](NOTICE.md)。

## License

本项目采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 协议发布，仅供非商业用途分享与改编，并须署名及以相同协议共享。
