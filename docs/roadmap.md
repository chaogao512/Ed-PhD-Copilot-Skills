# Roadmap

当前版本：**V1.9**（2026-08-10）→ 目标 **V2.0**。

状态标记：`[x]` 已完成、`[ ]` 待办、`⏳` 等待外部条件（用户提供研究方向、批准安装等）。

---

## 已落地（V1.7 → V1.8，本轮不再追踪）

| 条目 | 交付内容 |
|---|---|
| 技能扩展 | 新增 `governance-discussion-drafter`（Discussion 写作）、`scale-development-template`（量表开发），技能总数 10 |
| 方法规范深化 | 质性三级编码指南、统计报告规范（效应量/稳健性/功效分析）、APA 7th / CSSCI 格式门、系统综述工作流 |
| 理论锚点扩展 | `theory-anchors.md` 新增 CoI、认知负荷、自我决定、UTAUT、制度理论、学习分析伦理等 |
| 案例与回归 | 第 4 个贯穿案例（学习分析学业预警）7 技能链 + failure case 11，失败案例库达 11 个 |
| 文献读取 | `literature-reader` 技能（Zotero JSON/SQLite/本地目录三模式）+ 系统综述流程 |
| Handbook 知识层 | 13 篇方法论文档 + 16 图纳入版本控制；10 个 SKILL.md 添加 Handbook Guidance 双向链接；修复 3.2 死引用、补 3.4 缺失说明；README 增加 Handbook 章节表 |
| 平台无关与发布 | AGENTS/README 去平台绑定；双语 README（英文默认 + 中文切换 + 徽章）；结构检查克隆自洽性修复；CHANGELOG 改为本地维护文件 |

---

## 路径 A：技能质量深化

| 条目 | 状态 | 说明与产出物 |
|---|---|---|
| A1. 开题报告级完整样稿 | ⏳ | 基于 `doctoral-stage-templates.md` 产出一份完整样稿，主题需用户提供实际研究方向。产出：`docs/examples/doctoral-proposal-sample.md` |
| A2. 研究设计流程图 artifact | [ ] | 制作论文证据流与混合方法整合路径图（Mermaid/SVG），覆盖 DBR / RCT / 混合方法三类，附 QA 报告 |
| A3. Handbook 第六章案例填充 | [ ] | 从 `docs/cases/` 选 1 篇已跑通 7 技能链的案例，按 3.2 Flowchart 框架逐段剖析，写入 `handbook/06_Case_Studies/` |
| A4. 多案例与失败案例回归 | [ ] | 每轮版本迭代对 4 个贯穿案例与 11 个失败案例重新回归；持续补充真实失败模式 |

## 路径 B：文献与证据体系

| 条目 | 状态 | 说明与产出物 |
|---|---|---|
| B1. 中文核心/CSSCI 题录核验 | [ ] | 将 `docs/chinese-core-literature-inventory.md` 中 `needs_cnki_verification` 条目逐条经 CNKI / 期刊官网 / DOI / 本地 PDF 核验，登记至 `docs/chinese-core-literature-verified.md` |
| B2. 方法学证据转化 | [ ] | B1 核验通过的文献转化为具体技能规则，登记于 `docs/evidence-base.md` |
| B3. 文献地图对齐 | [ ] | `docs/literature-map-edtech-governance.md` 按用户研究方向完善主题/理论/方法分节 |

## 路径 C：通用化与平台无关

| 条目 | 状态 | 说明与产出物 |
|---|---|---|
| C1. 跨平台部署说明 | [ ] | 产出 `handbook/deployment-guide.md`：各平台注册 SKILL.md 的方法、差异与 PDF 解析降级策略 |
| C2. 非 Reasonix 平台触发测试 | [ ] | 在至少一个非 Reasonix 平台实测 SKILL.md 触发效果，记录差异并回写 C1 |

## 路径 D：博士研究实战支撑（用户方向待确认）

| 条目 | 状态 | 说明与产出物 |
|---|---|---|
| D1. 开题报告样稿 | ⏳ | 同 A1，按用户实际研究方向定制（优先级最高） |
| D2. 安装后真实触发测试 | ⏳ | 用户批准安装后，用真实提示词触发技能并记录 references 加载行为 |
| D3. 用户方向贯穿案例 | ⏳ | 用户描述方向后评估现有 4 案例是否覆盖；不覆盖则新建并跑通技能链 |

## 路径 E：仓库级质量保障

| 条目 | 状态 | 说明与产出物 |
|---|---|---|
| E1. 结构检查持续注册 | [ ] | `scripts/check_skill_structure.py` 随版本增量注册新技能、新 docs、新检查（V1.9 已注册 review 文件） |
| E2. 覆盖矩阵持续更新 | [ ] | `docs/skill-coverage-matrix.md` 每轮更新，保持无 pending 且含当前版本号 |
| E3. 版本发布流程 | [x] | 本轮执行：版本号统一 V1.9、roadmap 重写、CHANGELOG 新增条目、创建 V1.9 评审文档 |

---

## 每轮迭代固定收尾动作

1. 更新 `docs/skill-coverage-matrix.md`
2. 运行 `make check`（等价于 `python3 scripts/check_skill_structure.py`）
3. 更新 `CHANGELOG.md`（本地维护文件）、创建 `docs/review-YYYY-MM-DD-vX.Y.md`、更新 README 成熟度段落

## 本轮已完成（V1.9）

- [x] 全项目当前版本号统一至 V1.9（AGENTS.md、README ×2、覆盖矩阵基线、roadmap）
- [x] 重写本 roadmap：清理 V1.7→V1.8 已交付条目，重组 V1.9→V2.0 待办
- [x] 新增 CHANGELOG V1.9 条目、创建 `docs/review-2026-08-10-v1.9.md` 并在结构检查脚本注册

## 下一步最小行动

1. [ ] 用户描述研究方向 → 填充 A1 / D1 / D3 主题
2. [ ] 起草开题报告级完整样稿（A1 / D1）
3. [ ] 制作研究设计流程图 artifact（A2）
4. [ ] 中文核心/CSSCI 题录逐条核验（B1）
