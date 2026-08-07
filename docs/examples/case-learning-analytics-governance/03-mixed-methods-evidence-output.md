# Learning Analytics Governance Case: Mixed-Methods Evidence

## Input Summary

学业预警治理化机制的混合证据设计；证据目标：预警机制的解释性、公平性、学生知情权与支持有效性（分边界）。

## Skill Invoked

`mixed-methods-evidence-template`

## References Used

- `claim-evidence-matrix.md`
- `quantitative-methods.md`
- `qualitative-methods.md`
- `qualitative-coding-guide.md`
- `triangulation.md`
- `method-reporting-templates.md`

## Main Output

## Audit Depth

`Standard`（后续投稿前审查升级为 `Strict`）。

## Claim-Evidence Alignment（关键行）

| 声称 | 最低证据 | 边界与降级规则 |
|---|---|---|
| 学生知情度提升 | 知情度问卷（前后测）+ 知情材料核验 | 自报数据只能声称"感知提升" |
| 辅导员复核改善判断 | 辅导员访谈 + 复核/否决日志 | 无对照时降级为机制可行性证据 |
| 预警支持转化为行动 | 支持工单完成率 + 求助意愿问卷 | 不能声称学业成绩提升，除非有对照设计 |
| 预警公平性 | 分群体性能指标（性别/专业/生源地）+ 公平性监测 | 单校数据不得推广为普适结论 |
| 机制解释性 | 特征说明材料 + 访谈确认辅导员能理解 | 解释性不等于模型可解释性论文 |

## Quantitative Design

- 问卷：学生感知公平性、知情度、求助意愿量表（路由至 `scale-development-template` 完成信效度）。
- 日志：预警触发率、复核率、否决率、申诉率、支持完成率；明确行为代理指标边界（登录次数≠学习投入）。
- 报告要求（V1.5）：效应量（d/η²）+ 置信区间；功效分析说明；稳健性检验（替代特征集、子群体敏感性）。统计符号与格式遵循 APA 7th（`edtech-pre-submission-reviewer/references/format-gates.md`）。

## Qualitative Design

- 访谈：辅导员（预警使用体验、判断依据）与学生（被预警经历、公平性感知）。
- 编码：混合式（理论驱动 + 开放编码），双编码 30% 材料，报告 Cohen's κ；遵循 `qualitative-coding-guide.md` 的三阶段流程与编码簿模板。
- 报告：COREQ 对齐（研究者角色、抽样、访谈协议、编码过程、引文支持）。

## Triangulation Matrix

| 研究问题 | 量化证据 | 质性证据 | 整合逻辑 |
|---|---|---|---|
| 支持是否转化 | 工单完成率 | 辅导员访谈（资源障碍） | 完成率低时用访谈解释原因 |
| 公平性感知 | 分群体问卷得分 | 学生访谈（标签担忧） | 量化差异用质性解释机制 |
| 复核有效性 | 否决率与日志 | 辅导员判断依据访谈 | 验证人工复核是否实质而非形式 |

## Ethics and Data Governance Checklist

- 预警结果不得用于处分/劝退；高影响决策人工复核并留痕。
- 学生知情同意、数据来源告知、申诉纠错通道。
- 标签访问控制、留存期限、最小化原则。
- 公平性与准确率分别报告（`claim-evidence-matrix.md` 红线）。

## Claims That Must Be Weakened

"预警系统提升学业成绩"——本设计无随机对照，只能声称"机制可行性与支持转化过程证据"；成绩影响需后续准实验设计。
