# Learning Analytics Governance Case: Idea Evaluation

## Input Summary

基于学习分析的大学生学业预警与精准支持机制研究；对象为某省属高校本科学生与辅导员；核心技术为学业风险预测模型与预警推送；治理焦点为解释性、公平性、学生知情权与支持转化。

## Skill Invoked

`governance-idea-evaluator`

## References Used

- `fatal-flaws.md`
- `rubric.md`
- `theory-anchors.md`

## Main Output

## Fatal-Flaws Audit

未触发 CRITICAL 短路，但存在三个必须处理的 MAJOR 风险：

- 若只做"预警准确率提升"的算法研究，教育治理贡献不足（技术先行风险）。
- 若预警直接关联处分、劝诫或评优，将触发学生权益红线（伦理不可控）。
- 若用登录次数等行为代理指标定义学业风险且不说明理由，证据效度不足。

## Scoring

| Dimension | Score | Rationale |
|---|---:|---|
| Policy relevance | 5 | 对接教育数字化转型与学生学业帮扶政策 |
| Educational value | 5 | 直接服务于学业支持与教育公平 |
| Organizational feasibility | 3 | 需要教务、学工、信息化与院系协同授权 |
| Methodological evidencability | 4 | 日志+问卷+访谈可形成混合证据链 |
| Ethical controllability | 3 | 学生数据敏感、标签化风险高，须设人工复核与申诉 |
| Theoretical contribution | 4 | 学习分析伦理与组织支持机制结合有理论空间 |

## Verdict

`Proceed with safeguards`。研究定位应为"预警机制的治理化改造与支持转化"，而非"预测模型优化"。下一步进入 `governance-paper-template`，同时必须先行设计伦理与数据治理方案。

## Remaining Gaps

需明确：样本院校授权、预警特征清单及理由、高风险决策边界（禁止直接处分）、学生知情与申诉流程、支持资源供给方与责任归属。
