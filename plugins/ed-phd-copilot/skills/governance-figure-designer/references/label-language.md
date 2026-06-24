# Label Language Guide

| Engineering label to avoid | Education governance label to prefer |
|---|---|
| Input | 情境感知 / 伴随式数据采集 |
| Processor | 多主体协同决策 / 智能分析与解释 |
| Output | 治理反馈 / 发展性支持 / 干预建议 |
| User | 教师主体 / 学校管理者 / 学习者 / 专家共同体 |
| Model | 智能体 / 评价模型 / 决策支持机制 |
| Control | 价值对齐 / 人工复核 / 责任追踪 / 风险规约 |
| Database | 教育数据资源池 / 数据治理中台 |
| API | 数据互操作接口 / 权限受控服务 |
| All data | 最小必要教育数据 / 经授权的数据范围 |
| Student profile | 需人工解释的学习支持线索 |
| Automatic decision | AI 辅助建议 / 人工复核后决策 |
| Prediction result | 风险提示 / 待核验证据线索 |
| Model card | 模型用途与限制说明 |
| Dataset card | 数据来源、授权与质量说明 |
| Risk module | 风险台账与监测机制 |

## Rule

Labels should name educational function and governance responsibility, not only technical component.

## High-Risk Label Rules

- Replace “自动评价” with “AI 辅助证据整理 + 教师复核”.
- Replace “领导驾驶舱” with “治理决策支持与问责看板”.
- Replace “学生画像” with “学习支持线索”, unless the manuscript explicitly justifies profiling, consent, appeal and safeguards.
- Replace “模型输出” with “可解释建议 / 待复核线索”.
- Add “不适用场景” when the AI system must not be used for ranking, punishment, admissions, awards or teacher appraisal.
