# Install Forward Test

> 测试日期：2026-06-23  
> 测试类型：安装前向模拟测试。  
> 边界说明：本测试不把技能安装到当前 Codex 环境，也不覆盖用户已有技能目录；它基于仓库中的 `SKILL.md` frontmatter、reference 导航、样例输出和结构检查脚本进行触发与输出规范模拟。

## Test Purpose

验证 `Ed-PhD-Copilot-Skills` 在安装前是否具备可触发、可导航、可输出、可审查的技能链基础。测试重点不是生成新论文，而是检查每个技能是否满足：

1. 触发描述清楚。
2. 必要 reference 可被定位。
3. 输出格式明确。
4. 能处理教育信息化治理场景。
5. 能遵守证据边界和伦理边界。

## Test Method

1. 读取 7 个 `SKILL.md`。
2. 检查 frontmatter 中 `name` 与 `description` 是否可触发。
3. 检查 `Reference Navigation` 是否指向实际存在的 reference。
4. 使用主案例和三个新增案例的样例输出验证输出格式。
5. 使用失败案例验证红线和降级规则。
6. 运行 `python3 scripts/check_skill_structure.py`。

## Skill Trigger Tests

| Skill | Simulated user prompt | Expected trigger | Reference route | Result |
|---|---|---|---|---|
| `governance-idea-evaluator` | “帮我判断一个教育数据治理博士选题是否值得做” | 选题评估、风险判断、下一步路由 | `fatal-flaws.md`, `rubric.md`, `theory-anchors.md` | PASS |
| `governance-paper-template` | “把人机协同课堂评价研究整理成论文框架” | 论文类型、理论-机制-系统-证据矩阵 | `paper-types.md`, `theory-to-design.md`, `section-skeleton.md` | PASS |
| `mixed-methods-evidence-template` | “这个研究需要哪些问卷、访谈和日志证据” | 证据矩阵、方法设计、结论边界 | `claim-evidence-matrix.md`, `quantitative-methods.md`, `qualitative-methods.md`, `triangulation.md` | PASS |
| `edtech-intro-drafter` | “帮我写教育信息化治理论文引言逻辑” | 四重逻辑链、六段式引言 | `four-part-logic.md`, `paragraph-patterns.md`, `alienation-patterns.md` | PASS |
| `governance-figure-designer` | “画一个教育数据治理责任机制图” | 图示类型、布局、箭头规则、图注 | `figure-types.md`, `layout-patterns.md`, `quality-audit.md` | PASS |
| `edtech-pre-submission-reviewer` | “投稿前帮我审查这篇智能校园治理论文” | 严重性排序审查、72 小时修订计划 | `review-rubric.md`, `method-evidence-checklist.md`, `ethics-data-governance.md` | PASS |
| `ai-assisted-edtech-research-workflow` | “我想用 AI 辅助写开题报告，怎么分工合规” | 人机分工、红线、验证清单 | `human-ai-boundary.md`, `allowed-uses.md`, `red-lines.md`, `verification-checklist.md` | PASS |

## Progressive Disclosure Check

| Requirement | Evidence | Result |
|---|---|---|
| `SKILL.md` 保持主流程精炼 | 7 个技能均以 Overview、Reference Navigation、Core Procedure、Output Format 为主 | PASS |
| reference 文件按需读取 | 每个 `SKILL.md` 均显式列出 reference 读取条件 | PASS |
| reference 文件存在且不为空 | `scripts/check_skill_structure.py` 检查全部 required references | PASS |
| 输出格式可预测 | 所有技能均有 Output Format；案例样例统一加入协议字段 | PASS |

## Case Forward Test

| Case | Outputs checked | Result |
|---|---:|---|
| 基于多 Agent 的高校智能校园治理机制研究 | 7 | PASS |
| 区域教师数字胜任力提升的组织支持机制研究 | 7 | PASS |
| 高校教育数据治理能力建设与风险防控机制研究 | 7 | PASS |
| 人机协同支持的课堂教学评价改进机制研究 | 7 | PASS |

## Failure-Case Regression Test

| Failure type | Expected behavior | Result |
|---|---|---|
| 技术先行 | 不给高分，要求转向治理问题 | PASS |
| 证据错配 | 降级技术指标支持的结论 | PASS |
| 理论装饰化 | 要求理论生成设计原则 | PASS |
| 政策口号化 | 要求政策转化为治理矛盾 | PASS |
| 隐私盲区 | 触发 CRITICAL 伦理风险 | PASS |
| 因果越界 | 要求降级因果声明 | PASS |
| AI 伪造引用 | 拒绝伪造，改为核验流程 | PASS |
| 治理图示缺陷 | 要求补人类监督、责任和申诉 | PASS |

## Command Validation

```bash
python3 scripts/check_skill_structure.py
```

Expected result:

```text
OK: all Ed-PhD-Copilot skill structure checks passed
```

## Limitations

- 这是安装前模拟测试，不等同于已经安装到 `$CODEX_HOME/skills` 后的真实触发测试。
- 尚未验证 Codex 实际技能发现、加载和 UI 展示。
- 尚未使用真实博士选题材料进行现场前向测试。
- 中文核心/CSSCI 文献仍需继续核验。

## Recommendation

当前仓库已具备安装试运行条件。下一步可在用户确认后进行本地安装测试，并使用一个真实博士研究选题运行完整 7 技能链，记录实际触发、reference 读取和输出质量。

