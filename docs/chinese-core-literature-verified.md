# Chinese Core Literature Verified Registry

> 目的：本文件用于登记已经完成题录核验的中文核心/CSSCI/教育技术权威期刊文献，以及可追溯的中文官方政策、标准与平台来源。  
> 当前状态：V1.4 阶段已先完成一批中文官方政策/标准来源核验；中文核心/CSSCI 论文仍需继续通过 CNKI、期刊官网或本地 PDF 核验。  
> 来源候选：`docs/chinese-core-literature-inventory.md`。

## Verification Rule

只有同时满足以下条件的文献才能进入本文件：

1. 题名、作者、期刊/来源、年份、卷期、页码等元数据已核验。
2. 至少有一种可追溯来源：CNKI 详情页、期刊官网、DOI 页面、本地 PDF 或学校数据库导出的题录。
3. 文献主题与教育信息化治理、教育数字化、教育数据治理、智能教育、教师数字素养、AI 教育治理、教育技术研究方法等方向直接相关。
4. 不得把搜索结果摘要、AI 生成题录或未经核验的候选条目作为正式文献。

## Metadata Fields

| Field | Requirement |
|---|---|
| ID | 连续编号 |
| Authors | 与原文一致 |
| Year | 与原文一致 |
| Title | 与原文一致 |
| Source | 期刊、会议、学位论文或官方出版物名称 |
| Volume/Issue/Pages | 尽可能完整 |
| DOI/CNKI URL | 如有则记录 |
| Verification source | CNKI、期刊官网、本地 PDF、DOI、学校数据库等 |
| Skill mapping | 该文献支撑哪些技能或 reference |
| Notes | 使用边界或待补信息 |

## Verified Entries

| ID | Authors | Year | Title | Source | Volume/Issue/Pages | DOI/CNKI URL | Verification source | Skill mapping | Notes |
|---:|---|---:|---|---|---|---|---|---|---|
| 1 | 教育部 | 2018 | 教育部关于印发《教育信息化2.0行动计划》的通知 | 中华人民共和国教育部政府门户网站 | 教技〔2018〕6号 | http://www.moe.gov.cn/srcsite/A16/s3342/201804/t20180425_334188.html | 教育部网页标题与正文关键词核验 | `edtech-intro-drafter`, `governance-paper-template`, `edtech-pre-submission-reviewer` | 用于政策背景、教育数字化治理要求；非期刊论文 |
| 2 | 教育部 | 2023 | 教育部关于发布《教师数字素养》教育行业标准的通知 | 中华人民共和国教育部政府门户网站 | 教师函〔2023〕2号 | http://www.moe.gov.cn/srcsite/A16/s3342/202302/t20230214_1044634.html | 教育部网页标题与正文关键词核验 | `governance-idea-evaluator`, `mixed-methods-evidence-template`, teacher digital competence cases | 用于教师数字胜任力/素养维度与证据边界；非期刊论文 |
| 3 | 中共中央、国务院 | 2025 | 教育强国建设规划纲要（2024－2035年） | 中国政府网 | 中央文件 | https://www.gov.cn/zhengce/202501/content_6999913.htm | 中国政府网页标题与正文关键词核验 | `edtech-intro-drafter`, `governance-paper-template`, policy framing | 用于教育强国与教育数字化战略背景；非期刊论文 |
| 4 | 国家智慧教育公共服务平台 | 2022 | 国家智慧教育公共服务平台 | 国家智慧教育公共服务平台 | Web platform | https://www.smartedu.cn/ | 页面标题核验 | `governance-paper-template`, `governance-figure-designer`, smart campus cases | 用于平台语境与案例背景；不作为学术论文引用 |

## Verified Chinese Policy and Standard Sources

| ID | Source type | Verified title | URL | How verified | Skill use |
|---:|---|---|---|---|---|
| P1 | 教育部政策文件 | 教育部关于印发《教育信息化2.0行动计划》的通知 | http://www.moe.gov.cn/srcsite/A16/s3342/201804/t20180425_334188.html | HTTP 200；页面标题和 H1 均匹配 | 政策背景、数字化治理需求、投稿前政策审查 |
| P2 | 教育行业标准发布通知 | 教育部关于发布《教师数字素养》教育行业标准的通知 | http://www.moe.gov.cn/srcsite/A16/s3342/202302/t20230214_1044634.html | HTTP 200；页面标题和 H1 均匹配 | 教师数字胜任力、教师发展证据、能力指标 |
| P3 | 中央政策文件 | 中共中央 国务院印发《教育强国建设规划纲要（2024－2035年）》 | https://www.gov.cn/zhengce/202501/content_6999913.htm | HTTP 200；页面标题和 H1 均匹配 | 教育强国、教育数字化、治理现代化背景 |
| P4 | 国家级平台 | 国家智慧教育公共服务平台 | https://www.smartedu.cn/ | HTTP 200；页面 title 匹配 | 智慧教育平台语境、平台建设与治理能力区分 |

## Migration Workflow

1. 从 `docs/chinese-core-literature-inventory.md` 选择一条候选文献。
2. 打开 CNKI、期刊官网、DOI 页面或本地 PDF 核验元数据。
3. 若元数据完整，复制到 `Verified Entries`。
4. 在 `docs/verified-source-registry.md` 中增加来源说明，或在 `docs/evidence-base.md` 中增加规则映射。
5. 若无法核验，保留在 inventory，不进入正式引用。

## Current Unverified Academic Targets

以下主题仍未进入 `Verified Entries` 的“学术论文”部分：

- 智慧教育 / 智能教育理论框架。
- 教育数字化转型与教育治理。
- 学习分析与教育数据伦理。
- 教育数据治理、数据安全、数据伦理 CSSCI 文献。
- 人机协同评价与课堂质量评价核心期刊文献。

这些主题需要 CNKI、期刊官网、DOI 页面或本地 PDF 的题录核验后才能作为正式学术引用使用。

## Public Web Verification Boundary

2026-06-24 已进行一轮公开网络检索尝试，见 `docs/chinese-literature-web-verification-log.md`。由于检索结果未稳定提供完整题录，本文件暂不新增中文核心/CSSCI 论文条目。

这不是文献缺失结论，而是核验边界结论：没有 CNKI、期刊官网、DOI、本地 PDF 或学校数据库导出题录，就不把候选条目登记为已核验文献。

## Use Boundary

本文件一旦填写正式条目，可用于：

- 补强 `references/` 中的中文学术语境。
- 支撑论文引言、文献综述、理论框架和投稿前审查。
- 连接教育技术中文期刊写作范式。

本文件不可用于：

- 伪造不存在的文献。
- 用未核验候选替代正式引用。
- 为了凑数量而加入主题不相关文献。
