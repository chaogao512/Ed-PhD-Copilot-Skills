# Failure Case 11: Learning-Analytics Labeling without Support and Consent

## Weak input

"我们开发了基于深度学习的学业预警系统，AUC 达到 0.91。系统自动将学生分为高风险/中风险/低风险三档并直接推送给学生所在院系，院系据此约谈学生并纳入评优负面清单。研究结论：智能预警系统能有效提升学业管理水平。"

## Expected skill response

`governance-idea-evaluator` 应触发伦理 MAJOR→CRITICAL 升级：预警结果直接进入评优负面清单属于高影响决策且无人工复核；未说明学生知情同意、数据来源与申诉通道；AUC 高不代表教育治理价值（代理指标与真实学业风险混用）。

## Expected diagnosis

1. **伦理不可控（CRITICAL）**：预警标签直接影响评优等学生权益决策，且系统自动推送无人工复核、无申诉机制，违反学习分析伦理红线（知情、解释、纠错、人工复核）。
2. **证据错配（MAJOR）**：用模型 AUC 声称"提升学业管理水平"，未测量支持行动、学生公平性感知或任何学业结果。
3. **标签固化风险（MAJOR）**：高风险标签直接约谈学生而无支持路径，可能强化自我实现预言，属于治理异化而非精准支持。
4. **技术先行（MAJOR）**：研究贡献定位为模型性能，无治理机制设计。

## Required repair

1. 将系统定位改为"预警建议"：模型输出仅作为辅导员复核的参考信息，任何高影响决策由人工执行并留痕（对应 `theory-anchors.md` Learning analytics ethics frameworks 锚点）。
2. 补充学生知情、数据来源说明、申诉纠错通道与标签访问控制设计。
3. 增加支持转化证据：预警触发后支持行动完成率、学生求助意愿与公平性感知（量表+访谈，编码遵循 `qualitative-coding-guide.md`）。
4. 结论降级：删除"提升学业管理水平"的因果表述，改为"机制可行性 + 支持转化过程证据"；成绩影响需对照设计。
5. 路由：`governance-idea-evaluator` → `mixed-methods-evidence-template` → `scale-development-template`（公平性感知量表）→ `governance-discussion-drafter`（局限与伦理讨论）。
