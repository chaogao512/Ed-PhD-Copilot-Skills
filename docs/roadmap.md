# Roadmap

当前版本：**V1.7**（2026-06-24）→ 目标 **V1.8/V2.0**。

本路线图按路径组织，每条路径下列出具体条目、状态与产出物。状态标记：`[x]` 已完成、`[ ]` 待办、`⏳` 等待外部条件（如用户提供研究方向、批准安装）。

---

## 路径 A：技能质量深化（核心路径）

| 条目 | 状态 | 说明与产出物 |
|---|---|---|
| A1. 开题报告级完整样稿 | ⏳ | V1.7 评审 P1 项。目前仅有模板 `governance-paper-template/references/doctoral-stage-templates.md`，缺一份完整样稿。主题 = 用户实际研究方向（等待用户描述）。产出：`docs/examples/doctoral-proposal-sample.md` |
| A2. 研究设计流程图 artifact | [ ] | V1.7 评审 P2 项。现有图示仅覆盖机制图（`docs/examples/figure-rendering/`），缺论文证据流与混合方法整合路径图。产出：Mermaid/SVG artifact + QA 报告 |
| A3. 多案例回归测试 | [ ] | 现有 3 个贯穿案例（教师数字胜任力 / 教育数据治理 / 人机协同课堂评价）已跑通 7 技能链；每轮版本迭代需重新回归。若用户方向不在现有案例覆盖内，新建第 4 个案例目录 `docs/cases/` |
| A4. 失败案例库扩展 | [ ] | 现有 10 个 failure cases（`docs/examples/failure-cases/`）；持续补充真实失败模式并回测 |

## 路径 B：文献与证据体系

| 条目 | 状态 | 说明与产出物 |
|---|---|---|
| B1. 中文核心/CSSCI 题录核验 | [ ] | V1.7 评审 P3 项。将 `docs/chinese-core-literature-inventory.md` 中 `needs_cnki_verification` 条目逐条经 CNKI/期刊官网/DOI/本地 PDF 核验，升级登记到 `docs/chinese-core-literature-verified.md` |
| B2. 文献地图完善 | [ ] | `docs/literature-map-edtech-governance.md` 按主题/理论/方法分节完善，并与用户研究方向对齐 |
| B3. 方法学证据登记 | [ ] | 将已核验中文文献转化为具体技能规则（`mixed-methods-evidence-template`、`edtech-intro-drafter` 等），登记于 `docs/evidence-base.md` |
| B4. 文献读取链路接入 | [x] | 本轮新增 `literature-reader` 技能（Zotero Better BibTeX JSON / 本地目录 PDF+MD / Zotero SQLite），输出文献卡片并衔接 `docs/verified-source-registry.md` 验证门。后续：用用户真实 Zotero 库做一次端到端验证 |

## 路径 C：通用化与平台无关

| 条目 | 状态 | 说明与产出物 |
|---|---|---|
| C1. 去除平台绑定 | [x] | 本轮完成：`AGENTS.md` 与 `README.md` 定位改为"平台无关的通用智能体技能库"（Reasonix / ChatGPT Custom GPT / Claude Project / Cursor Rules 等均可部署） |
| C2. 文献读取能力 | [x] | 本轮完成：`literature-reader` 技能已在 `scripts/check_skill_structure.py` 注册 |
| C3. 跨平台部署说明 | [ ] | 产出 `handbook/deployment-guide.md`：各平台如何注册 SKILL.md（Reasonix 插件目录、Custom GPT Actions、Claude Project 导入等），及 PDF 解析能力差异与降级策略 |
| C4. 非 Reasonix 平台触发测试 | [ ] | 在至少一个非 Reasonix 平台实测 SKILL.md 触发效果，记录差异并回写 C3 文档 |

## 路径 D：博士研究实战支撑（用户方向待确认）

| 条目 | 状态 | 说明与产出物 |
|---|---|---|
| D1. 开题报告样稿 | ⏳ | 同 A1。主题、文献地图、研究问题与方法须按用户实际研究方向定制（用户将在后续消息中描述研究方向）。博士进展：选题/开题阶段，本条目优先级最高 |
| D2. 研究设计流程图 | [ ] | 同 A2。与开题报告配套 |
| D3. 安装后真实触发测试 | ⏳ | V1.7 评审 P4 项。需用户批准安装后，用 7 个真实提示词触发技能并记录 references 加载行为（此前因用户要求适配前不安装而搁置） |
| D4. 用户方向贯穿案例 | ⏳ | 用户描述研究方向后，评估现有 3 案例是否覆盖；不覆盖则新建案例并跑通 7 技能链 |

## 路径 E：仓库级质量保障

| 条目 | 状态 | 说明与产出物 |
|---|---|---|
| E1. 结构检查脚本增强 | [ ] | `scripts/check_skill_structure.py` 随每版本增量注册新检查（如 V1.6/V1.7 增量表模式）；新技能、新 docs 必须同步登记 |
| E2. 覆盖矩阵持续更新 | [ ] | `docs/skill-coverage-matrix.md` 每轮迭代更新技能覆盖行与 Next Coverage Targets；保持无 pending 且含当前版本号 |
| E3. 版本发布流程 | [ ] | 每次迭代固定收尾：更新覆盖矩阵 → 运行结构检查 → 更新 `CHANGELOG.md` + `docs/review-YYYY-MM-DD-vX.Y.md` + README 成熟度段落 |

---

## 每轮迭代固定收尾动作

1. 更新 `docs/skill-coverage-matrix.md`
2. 运行 `python3 scripts/check_skill_structure.py`
3. 更新 `CHANGELOG.md`、`docs/review-YYYY-MM-DD-vX.Y.md`、README 成熟度段落

## 本轮已完成

- [x] `AGENTS.md` / `README.md` 去除 Reasonix 绑定，改为通用智能体定位（路径 C1）
- [x] 新建 `literature-reader` 技能（Zotero + 本地文献读取）并在结构检查脚本注册（路径 C2 / B4）
- [x] 重写本 roadmap（分路径分条目）

## 下一步最小行动

1. [ ] 用户描述研究方向 → 填充路径 A1/D1/D4 主题，更新 V1.7 评审 P1 样稿主题
2. [ ] 起草开题报告级完整样稿（`docs/examples/doctoral-proposal-sample.md`）
3. [ ] 制作研究设计流程图 artifact（A2/D2）
4. [ ] 中文核心/CSSCI 题录逐条核验（B1）
