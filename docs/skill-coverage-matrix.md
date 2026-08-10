# Skill Coverage Matrix

覆盖矩阵基线 V1.8 → 本轮更新 V1.9（版本号统一 + roadmap 重写 + Handbook 知识层双向链接）。

| Skill | Rubric | Checklist | Anti-patterns | Worked example | Method detail | Ethics check | Routing rule | Failure cases | Status |
|---|---|---|---|---|---|---|---|---|---|
| `governance-idea-evaluator` | `rubric.md` | `fatal-flaws.md` | `fatal-flaws.md` | `worked-examples.md`, main example, `docs/examples/case-*/01-...` | `theory-anchors.md` (V1.8: CoI/CLT/SDT/UTAUT/制度理论/学习分析伦理) | `fatal-flaws.md` | `SKILL.md` | `01`, `05`, `11` | V1.8 |
| `edtech-intro-drafter` | `paragraph-patterns.md` | `four-part-logic.md`, V1.5 evidence/risk boundary | `alienation-patterns.md`, `docs/examples/case-*/04-...` | main example, V1.5 examples, `worked-examples.md` | `paragraph-patterns.md`, Chinese policy anchors, PRISMA boundary language | `four-part-logic.md` | `SKILL.md` | `04`, `09` | V1.5 |
| `governance-paper-template` | `paper-types.md` | `section-skeleton.md`, `doctoral-stage-templates.md` | `theory-to-design.md` | main example, `worked-examples.md`, `docs/examples/case-*/02-...`, V1.7 full-chain pressure test | `dual-topology.md`, platform-governance boundary, doctoral-stage mapping | `dual-topology.md`, doctoral ethics/data gates | `SKILL.md` | `03` | V1.7 |
| `mixed-methods-evidence-template` | `claim-evidence-matrix.md` | `triangulation.md`, PRISMA/COREQ/CONSORT-WWC/MMAT gates, Light/Standard/Strict depth | `claim-evidence-matrix.md` | main example, V1.5 examples, `worked-examples.md`, `docs/examples/case-*/03-...` | `indicator-system.md`, `quantitative-methods.md` (V1.8: 效应量/稳健性/功效分析), `qualitative-methods.md`, `qualitative-coding-guide.md` (V1.8: 三级编码/主题分析/Cohen's κ/编码簿), `method-reporting-templates.md`, `design-science-reporting.md` | `claim-evidence-matrix.md`, AI risk reporting gate | `SKILL.md` (V1.8: 路由至 `scale-development-template`) | `02`, `06`, `09`, `11` | V1.8 |
| `governance-figure-designer` | `quality-audit.md` | `quality-audit.md`, model-card/dataset-card/risk-register gates, renderable figure QA | `label-language.md` | main example, V1.5 examples, `docs/examples/case-*/05-...`, `docs/examples/figure-rendering/` | `figure-types.md`, `layout-patterns.md`, Model Cards, Datasheets, V1.7 rendered artifacts | `quality-audit.md` | `SKILL.md` | `08`, `10` | V1.7 |
| `edtech-pre-submission-reviewer` | `review-rubric.md` | `theory-policy-checklist.md`, `method-evidence-checklist.md`, reporting-standard audit, Light/Standard/Strict depth, V1.8 `format-gates.md` (APA 7th / GB-T 7714 / CSSCI 体例) | `style-anti-patterns.md` | main example, V1.5 examples, `docs/examples/case-*/06-...` | `method-evidence-checklist.md` | `ethics-data-governance.md`, lifecycle risk-governance audit | `SKILL.md` | `02`, `04`, `05`, `06`, `07`, `09`, `11` | V1.8 |
| `ai-assisted-edtech-research-workflow` | `verification-checklist.md` | `verification-checklist.md`, `venue-disclosure-templates.md`, AI disclosure and Chinese citation gates | `red-lines.md` | main example, `docs/examples/case-*/07-...` | `allowed-uses.md`, ICMJE/Nature/Elsevier/Wiley AI policy mapping | `human-ai-boundary.md`, `red-lines.md`, confidentiality rules | `SKILL.md` | `07`, `09`, `10` | V1.6 |
| `literature-reader` | `verification-gate.md` | `literature-card-template.md`, V1.8 `systematic-review-workflow.md` (PRISMA 流程/质量评估/空白识别) | `verification-gate.md` | main example, 08/09 输出可消费的文献卡 | `source-ingestion.md`, Zotero JSON/SQLite/本地目录三模式 | `verification-gate.md` | `SKILL.md` | `07`, `09` | V1.8 |
| `governance-discussion-drafter` (V1.8 新增) | `discussion-patterns.md` | `limitation-taxonomy.md` | `discussion-patterns.md` anti-patterns checklist | main example `08-...`, `worked-examples.md` | `implication-mapping.md` (证据边界→启示类型) | `limitation-taxonomy.md`, 伦理讨论规则 | `SKILL.md` (承接 paper-template / evidence 输出) | `06` (结论越界) | V1.8 |
| `scale-development-template` (V1.8 新增) | `validity-reliability-protocol.md` | `validity-reliability-protocol.md` reporting gates | `item-development.md` anti-patterns | main example `09-...`, `worked-examples.md` | `construct-definition.md`, `item-development.md`, EFA/CFA/信效度/常模协议 | 高利害测评公平性与不变性检查 | `SKILL.md` + `mixed-methods-evidence-template` 路由 | `02` (证据错配) | V1.8 |

## Next Coverage Targets

- Continue verifying Chinese CSSCI/core-journal article records in `docs/chinese-core-literature-inventory.md` and move verified entries into `docs/chinese-core-literature-verified.md`.
- Run real installed-skill forward tests after user approves installation.
- Add a doctoral proposal research-design flow diagram (path A2/D2 in `docs/roadmap.md`).
- Draft a full 开题报告 sample once the user provides their actual research direction (path A1/D1).
- Continue converting verified Chinese journal literature into concrete skill rules after metadata verification.
- Extend the learning-analytics case with a rendered Mermaid artifact and figure QA report when the user needs the design-flow diagram.
