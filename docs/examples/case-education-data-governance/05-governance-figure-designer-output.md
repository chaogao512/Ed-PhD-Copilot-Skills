# Education Data Governance Case: Figure Design

## Input Summary

为高校教育数据治理能力与风险防控机制设计核心图示。

## Skill Invoked

`governance-figure-designer`

## References Used

- `figure-types.md`
- `layout-patterns.md`
- `quality-audit.md`

## Main Output

## Figure Type

Data governance responsibility map.

## Recommended Paradigm

责任地图 + 多流程箭头：区分数据流、授权流、决策流、反馈流和问责流。

## Layout Sketch

```text
数据主体：学生 / 教师
        ↓ 授权、知情、纠错
数据来源：教务 / 学工 / 教学平台 / 质量保障
        ↓ 标准化、脱敏、质量检查
数据治理层：数据目录、权责、标准、质量、安全、生命周期
        ↓ 授权访问
业务使用层：教学改进、学生支持、质量监测、管理决策
        ↔ 人工解释、申诉纠错、伦理审查
监督问责层：数据治理委员会 / 伦理委员会 / 审计机制
```

侧边增加 `Dataset Datasheet Panel`：

| Item | Content |
|---|---|
| 数据来源 | 教务、学工、教学平台、质量保障系统 |
| 授权边界 | 研究/改进用途，禁止未审查的绩效或惩戒使用 |
| 质量风险 | 缺失、重复、部门口径不一致、历史偏差 |
| 保留删除 | 保留期限、删除责任、纠错渠道 |

下方增加 `Risk Register`：

| Risk | Owner | Safeguard |
|---|---|---|
| 学生画像误用 | 数据治理委员会 | 用途限定、人工解释、申诉纠错 |
| 数据质量导致误判 | 数据管理员 | 数据质量审计和异常记录 |
| 跨部门越权访问 | 信息化部门/审计部门 | 角色权限、访问日志、定期审计 |

## Arrow Rules

- 实线：数据流。
- 虚线：授权与审批。
- 双向箭头：反馈、纠错和申诉。
- 粗线：问责链。

## Caption Draft

图 X 高校教育数据治理责任与风险防控机制。该机制将数据主体、数据来源、治理规则、业务使用和监督问责连接起来，强调教育数据使用必须经过授权、质量控制、风险审查和人工解释。

## Quality Self-Check

- 图中出现数据主体、数据使用者和监督者。
- 区分数据流与责任流。
- 包含申诉、纠错、审计和删除。
- 包含数据说明卡和风险台账，避免把数据中台画成中性技术输入。

## Remaining Gaps

可继续补一张能力指标体系图，用于专家咨询和 Delphi 论证。
