# Learning Analytics Governance Case: Figure Design

## Input Summary

为学业预警治理化机制论文设计两张承重图：治理化预警机制闭环图 + 证据链图。

## Skill Invoked

`governance-figure-designer`

## References Used

- `figure-types.md`
- `layout-patterns.md`
- `label-language.md`
- `quality-audit.md`

## Main Output

## Figure 1: 治理化预警机制闭环图（flowchart）

布局：泳道式闭环（学生 / 辅导员 / 教务学工 / 数据部门 / 治理委员会）。

- 数据流：LMS 与校园数据 → 特征构建（明示代理指标与理由）→ 风险模型（仅产生建议）。
- 决策流：预警建议 → 辅导员人工复核（可否决）→ 分层支持工单 → 支持行动 → 效果反馈。
- 纠错流：学生申诉 → 委员会复核 → 标签修正与日志留存。
- 强制面板：`Model/System Card Panel`（特征清单、公平性监测、人工复核规则）+ `Appeal and correction`（申诉通道）+ `Not final judgment`（预警仅是建议，非处分依据）。

## Figure 2: 证据链图（研究设计）

- 量化支线：问卷（公平性/知情度/求助意愿，量表信效度）+ 日志指标（触发/复核/否决/申诉/完成率）。
- 质性支线：辅导员与学生访谈（编码 → 主题）。
- 整合节点：三角互证矩阵；结论按边界分级标注（可行性 / 过程证据 / 效果证据）。

## Label Language

- 不用"输入-处理-输出"工程话语；改用"数据采集—风险识别—人工复核—支持行动—申诉纠错"治理话语。
- 学生不标为"风险对象"，标为"支持对象"；预警标为"风险提示"而非"问题学生"。

## Quality Audit

- 图题自包含，坐标轴诚实（准确率与公平性分开展示）。
- 色盲安全配色；矢量格式；无 chartjunk。
- 治理要素齐全：责任主体、授权边界、申诉纠错、数据说明、审计日志。
- 可渲染性：本输出为文本草图；后续生成 Mermaid artifact 并附 QA 报告（参照 `docs/examples/figure-rendering/` 流程）。
