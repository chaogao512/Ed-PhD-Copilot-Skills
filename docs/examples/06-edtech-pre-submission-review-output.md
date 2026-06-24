# Example Output: edtech-pre-submission-reviewer

## Input Summary

基于多 Agent 的高校智能校园治理机制研究。

## Skill Invoked

`edtech-pre-submission-reviewer`

## References Used

- `review-rubric.md`
- `theory-policy-checklist.md`
- `method-evidence-checklist.md`
- `ethics-data-governance.md`
- `style-anti-patterns.md`

## Main Output

## Overall verdict

Major revision. 选题有价值，理论和架构方向清晰，但证据边界和伦理说明仍需加强。

## Review depth

`Strict`。该输出模拟投稿前审查，需要执行报告规范、证据边界、AI 风险生命周期和 72 小时修订计划。

## Findings ordered by severity

### CRITICAL

1. **Evidence overclaim**
   - Problem: 草稿用系统响应速度和预警准确率证明“治理能力提升”。
   - Why it matters: 技术指标不能直接支持组织治理效果。
   - Repair: 增加流程时长、协同记录、管理者访谈和教师反馈。
   - 72-hour feasible: yes, at least as revised design.

### MAJOR

2. **Theory-to-module mapping unclear**
   - Problem: 社会技术系统理论只在理论基础出现，未映射到架构层。
   - Repair: 增加“理论-设计原则-系统模块-证据”表。

3. **Ethics and data governance underdeveloped**
   - Problem: 学生数据脱敏、知情同意、申诉机制未说明。
   - Repair: 增加数据最小化、权限控制、人工复核、申诉流程。

4. **Human-in-the-loop too generic**
   - Problem: 只写“人类参与”，没有说明谁复核、何时复核、如何否决。
   - Repair: 明确教师、管理者、专家委员会的责任节点。

5. **Reporting-standard gate missing**
   - Problem: 混合研究部分未说明访谈报告、准实验/前后比较和系统日志如何整合。
   - Repair: 按 COREQ 报告访谈与编码，按 WWC/CONSORT 风格限制因果表达，并增加 joint display。

### MINOR

6. **Term inflation**
   - Problem: “赋能”“智能化”“高质量”重复出现但机制不足。
   - Repair: 用具体治理过程替换抽象赞美。

## V1.5 strict gates

| Gate | Status | Required action |
|---|---|---|
| PRISMA | Not applicable unless manuscript claims systematic review | 若写“系统梳理”，需补检索式、纳排标准和筛选流程 |
| COREQ | Missing | 补访谈抽样、研究者角色、访谈提纲、编码和引文 |
| WWC/CONSORT | Partly missing | 补基线、比较条件、实施一致性、流失和结果效度 |
| NIST-style AI risk lifecycle | Missing | 补风险识别、测量、管理、监测和责任主体 |

## 72-hour fix plan

1. 补理论-模块-证据矩阵。
2. 补数据治理与伦理小节。
3. 收缩结论，把“治理能力提升”改为“试点流程效率和协同感知改善”。
4. 重画架构图，突出人类监督责任链。
