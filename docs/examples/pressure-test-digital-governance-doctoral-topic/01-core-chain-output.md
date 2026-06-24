# Pressure Test Output: County Education Data Governance Doctoral Topic

## Input Summary

研究主题：县域义务教育数字化转型中的教育数据治理能力建设研究。

研究场景：县级教育行政部门推动区域智慧教育平台、作业/评价数据、教师发展数据和学校质量监测数据整合，但学校之间数据基础、教师数字能力、数据质量、隐私保护和治理责任存在差异。

## Skill Chain Invoked

1. `governance-idea-evaluator`
2. `governance-paper-template`
3. `mixed-methods-evidence-template`
4. `edtech-pre-submission-reviewer`

## References Used

- `governance-idea-evaluator/references/rubric.md`
- `governance-idea-evaluator/references/fatal-flaws.md`
- `governance-paper-template/references/paper-types.md`
- `governance-paper-template/references/theory-to-design.md`
- `mixed-methods-evidence-template/references/claim-evidence-matrix.md`
- `mixed-methods-evidence-template/references/triangulation.md`
- `mixed-methods-evidence-template/references/method-reporting-templates.md`
- `edtech-pre-submission-reviewer/references/method-evidence-checklist.md`
- `edtech-pre-submission-reviewer/references/ethics-data-governance.md`

## Main Output

### 1. Governance Idea Evaluation

| Dimension | Judgment | Reason |
|---|---|---|
| Policy relevance | High | The topic connects education digitalization, county governance and education-quality improvement. |
| Education value | High | It studies how data use changes teaching support, school improvement and administrative coordination. |
| Governance specificity | High after narrowing | The object must be "data governance capacity", not "digital platform construction". |
| Method feasibility | Medium-high | County bureau documents, school cases, interviews, teacher survey and platform logs can form a mixed evidence chain. |
| Ethics controllability | Medium | Student and teacher data require minimization, desensitization, approval, access control and appeal/correction routes. |
| Theoretical contribution | Medium-high | The topic can connect organizational capacity, data governance and education leadership. |

**Maturity level:**可开题选题，可向博士论文拓展。

**Fatal-flaw check:** no immediate `CRITICAL` flaw if the study removes identifiable student-level data from AI tools and avoids unsupported causal language.

**Required narrowing:**

- Replace "数字化转型效果研究" with "数据治理能力建设机制研究".
- Define the county-level governance unit: education bureau, school leadership, data steward, teacher and student/data subject.
- Distinguish platform availability, data quality, organizational routines and educational improvement.

**Next Skill:** `governance-paper-template`.

### 2. Paper Template

**Recommended paper type:**治理机制型 + 案例研究型, with a doctoral expansion path.

| Layer | Core question | Output |
|---|---|---|
| Theory | What explains county data-governance capacity? | Organizational capacity, data governance, distributed leadership and socio-technical governance. |
| Mechanism | How is capacity built? | Responsibility allocation, standard setting, data-quality routines, school-level use, feedback and accountability. |
| System | What infrastructure supports it? | Data catalogue, authorization workflow, data-quality dashboard, issue log, training and review process. |
| Evidence | How will claims be supported? | Documents, interviews, teacher survey, platform trace data, school case comparison and governance artifacts. |
| Contribution | What does the study add? | A county education data governance capacity framework and evidence-bound implementation path. |

**Section skeleton:**

1. Policy and problem background: from digital infrastructure to governance capacity.
2. Literature and theoretical framing: education digitalization, data governance, organizational capacity and education leadership.
3. Analytical framework: capacity dimensions, actor responsibilities and risk controls.
4. Case and method: county selection, school sampling, documents, interviews, survey and data traces.
5. Findings: responsibility structure, data-quality routines, school-use differences and risk-control gaps.
6. Mechanism model: how county-level rules become school-level data-use routines.
7. Discussion: governance modernization, teacher workload, student data rights and scalability.
8. Conclusion: contribution, limitations and future verification.

**Evidence Design Needed:** method must distinguish descriptive capacity mapping from causal impact claims.

### 3. Mixed-Methods Evidence Design

**Audit Depth:** Strict.

| Research question | Evidence source | Analysis | Supportable conclusion |
|---|---|---|---|
| What dimensions constitute county education data governance capacity? | Policy documents, bureau rules, school data-use procedures, expert consultation | Policy text analysis, Delphi-style expert review if feasible | A preliminary capacity framework, not a nationally validated standard. |
| How are responsibilities distributed across bureau and schools? | Interviews with bureau staff, principals, data stewards and teachers | COREQ-style interview reporting, thematic coding, role-responsibility matrix | Mechanism explanation grounded in selected county cases. |
| How do schools differ in data-quality routines and data use? | Teacher survey, data-quality logs, school case documents | Descriptive statistics, cross-case comparison | Association and pattern comparison, not causal effect. |
| What risks emerge in data use? | Ethics review records, access logs, interview accounts, incident/complaint records if available | Risk register, process tracing, contradiction analysis | Risk profile and safeguard needs. |
| Does governance capacity improve education outcomes? | Longitudinal student/teacher outcome data and comparison design would be needed | Quasi-experimental or longitudinal design | Not supportable in the basic design; state as future validation. |

**V1.5 reporting gates:**

- **COREQ:** interview claims require sampling logic, interviewer role, interview protocol, coding procedure and quote evidence.
- **MMAT:** mixed-methods integration must show how qualitative and quantitative findings explain each other.
- **WWC-style boundary:** no strong causal claim without comparison, baseline, attrition handling, valid outcomes and implementation fidelity.
- **AI/data risk gate:** data minimization, authorization, access logs, appeal/correction and retention/deletion must be documented.

**Claim downgrades required:**

- "县域数字化治理显著提升教育质量" -> "揭示县域数据治理能力建设与学校改进机制之间的关联路径".
- "平台数据证明学生发展改善" -> "平台数据可作为学校治理过程变化的辅助证据".
- "AI 能自动发现薄弱学校" -> "数据分析可为人工研判提供线索，不得替代问责或资源配置决策".

### 4. Pre-Submission Review

**Review Depth:** Strict.

| Severity | Finding | Repair |
|---|---|---|
| CRITICAL if present | Using student platform data without approval, minimization or desensitization | Add ethics approval path, data access table, de-identification plan and non-upload rule for external AI tools. |
| MAJOR | Treating a county case as proof of national generalizability | Reframe as analytical generalization and state transfer conditions. |
| MAJOR | Claiming digitalization outcomes from governance-process evidence | Separate governance-capacity findings from outcome-impact claims. |
| MAJOR | Missing school-level actor roles | Add bureau-school-teacher-student responsibility matrix. |
| MINOR | Policy language remains slogan-like | Translate policy into measurable governance requirements such as standards, authorization, quality audit and feedback routines. |

**72-hour repair plan:**

1. Rewrite title and RQs around data governance capacity.
2. Add actor-responsibility matrix and data-rights table.
3. Convert all effectiveness claims into mechanism or process claims unless stronger outcome evidence exists.
4. Add COREQ-style interview reporting fields.
5. Add a dataset datasheet and risk register appendix.

## Quality Self-Check

- The topic stayed inside education informatization governance rather than drifting into system construction.
- The core chain preserved the same research object across all four skills.
- Method rules lowered claims that the proposed evidence cannot support.
- Ethics and data governance were treated as design conditions, not an afterthought.

## Remaining Gaps

- This pressure test does not verify Chinese CSSCI article metadata; it only uses already verified policy and method anchors.
- A real dissertation proposal would still need local access to CNKI, school database exports or verified PDFs.
- If the user wants to study effects on student learning, a separate longitudinal or quasi-experimental design is required.
