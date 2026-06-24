# Example Output Protocol

本目录保存 `Ed-PhD-Copilot-Skills` 的正向样例、贯穿案例输出和失败案例回归材料。样例不是最终论文文本，而是用于检验技能是否稳定执行其流程、引用合适 reference，并保持教育信息化治理方向的理论、方法和伦理边界。

## Standard Fields

每个样例输出建议包含：

1. Input summary：输入主题、研究对象、场景边界。
2. Skill invoked：调用的技能名称。
3. References used：本次输出应读取或依据的 reference。
4. Main output：技能的核心输出。
5. Quality self-check：对政策、理论、方法、证据、伦理和路由的自查。
6. Remaining gaps：仍需人工补充的材料或下一步任务。

## Current Example Sets

| Folder/File | Purpose |
|---|---|
| `01-...` to `07-...` | 主贯穿案例“多 Agent 高校智能校园治理机制研究”的 7 个技能输出 |
| `case-teacher-digital-competence/` | 教师数字胜任力治理案例的 7 技能链输出 |
| `case-education-data-governance/` | 高校教育数据治理案例的 7 技能链输出 |
| `case-human-ai-assessment/` | 人机协同课堂评价案例的 7 技能链输出 |
| `pressure-test-digital-governance-doctoral-topic/` | 县域教育数据治理博士选题的核心技能链压力测试 |
| `figure-rendering/` | 教育数据治理图示的 Mermaid artifact 与图示 QA 报告 |
| `failure-cases/` | 用于测试技能是否识别低质量输入和研究设计风险 |

## Review Rule

新增样例后，应同步检查：

- 是否有明确治理问题，而不是只描述技术工具。
- 是否包含理论锚点，并能影响设计或证据。
- 是否有方法与结论边界。
- 是否包含隐私、公平、人类监督和问责机制。
- 是否能路由到下一步技能。

## V1.5 Example Requirements

混合方法和投稿前审查样例必须体现：

- `Audit Depth` 或 `Review Depth`，区分 `Light / Standard / Strict`。
- 至少一个 V1.5 报告门槛，如 PRISMA、COREQ、CONSORT/WWC、MMAT 或 NIST-style AI risk lifecycle。
- 明确哪些结论需要降级，不能用满意度、平台日志、模型准确率或便利文献清单支撑强结论。

结构检查脚本会检查主案例和三个迁移案例中的混合方法/投稿前审查样例是否包含这些标记。

## Seven-Skill Chain

每个贯穿案例的完整输出应包含：

1. `01-governance-idea-evaluator-output.md`
2. `02-governance-paper-template-output.md`
3. `03-mixed-methods-evidence-output.md`
4. `04-edtech-intro-drafter-output.md`
5. `05-governance-figure-designer-output.md`
6. `06-edtech-pre-submission-review-output.md`
7. `07-ai-assisted-workflow-output.md`

## V1.6 Pressure-Test Requirements

真实博士课题压力测试必须体现：

- 同一研究对象在选题评估、论文模板、证据设计和投稿前审查之间保持一致。
- 技能链主动降级证据不足的强因果、强效果或强推广结论。
- 数据治理、AI 使用或高风险教育决策必须出现责任主体、权利边界、人工复核、申诉纠错和监测机制。
- 图示类输出至少保留一个可渲染 artifact 或明确说明为什么当前阶段只能给出文本草图。
