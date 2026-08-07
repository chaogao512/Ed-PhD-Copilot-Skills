# Worked Examples for Scale Development

## Example 1: 高校教育数据治理能力量表

**Goal**: develop a scale measuring 高校教育数据治理能力 (organizational level) for a doctoral chapter.

**Construct definition (from `construct-definition.md`)**:

- Construct: 教育数据治理能力 = 高校在数据全生命周期中通过制度、流程与技术手段实现数据可用、可信、可控的组织能力。
- Anchor: 数据治理理论 (data governance theory) + 教育信息化治理文献。
- Level: organization (informant = 信息化管理/数据管理部门负责人及骨干).
- Dimensions (4): D1 数据权责清晰度; D2 数据质量审查; D3 数据安全与隐私保护; D4 数据共享与协同利用.

**Item development (from `item-development.md`)**:

- Initial pool: 4 dimensions × 5 items = 20 items; 5-point Likert (1 = 完全不符合, 5 = 完全符合).
- Expert panel: 7 experts (2 教育技术, 2 数据治理, 1 高校信息化处长, 2 测量); I-CVI per item 0.71–1.00; 3 items revised, 2 deleted (relevance < 0.78); final 18 items.
- Pilot: 45 高校信息化人员; item-total correlations 0.31–0.68; 2 items revised for clarity; no deletions.

**Validation plan (from `validity-reliability-protocol.md`)**:

- EFA sample: 280 informants from 80 高校 (convenience + snowball, response rate 61%); parallel analysis → 4 factors; oblique rotation; 2 items deleted (cross-loading); 16 items retained; loadings 0.45–0.82.
- CFA sample: 315 informants (independent); CFI = 0.94, TLI = 0.93, RMSEA = 0.058 [0.049, 0.067], SRMR = 0.052; loadings 0.52–0.79.
- Reliability: ω = 0.91 total, per-dimension ω 0.78–0.89; test-retest (n = 38, 3 weeks) ICC = 0.84.
- Validity: convergent — r = 0.62 with 数据治理成熟度评估 (adapted CMM-style instrument); discriminant — r = 0.31 with 信息化经费规模 (single item); criterion — 量表得分与近一年数据安全事件数负相关 (r = −0.35, p < .01).
- Norms: 暂不提供常模; 明确说明切分点需代表性样本 + ROC 证据后方可设定 (used for research, not certification).

**Honest reporting**: sampling is convenience-based; invariance across 本科/高职 not tested — stated as a limitation and next step.

## Example 2: 教师人机协同教学评价采纳量表 (adaptation + new dimensions)

**Goal**: adapt an existing human-AI collaboration scale to Chinese classroom assessment context and add a new dimension (评价标准解释权).

**Construct definition**: 采纳 = 教师在课堂评价中持续、有理解地使用 AI 辅助评价结果; anchor = 技术接受与使用统一理论 (UTAUT) + 形成性评价理论; new dimension D5 解释权感知 = 教师对评价标准解释与最终裁定保留权的感知.

**Item development**: 12 items translated/adapted from source scale (back-translation + cultural adaptation evidence), 5 new items for D5; expert review 8 experts; I-CVI ≥ 0.78 for all kept items; pilot n = 60 teachers.

**Validation**: EFA n = 320 teachers (5 factors, parallel analysis), CFA n = 340 (fit: CFI = 0.95, RMSEA = 0.052); α/ω per dimension 0.80–0.90; discriminant evidence: D5 vs "对 AI 的信任" r = 0.38 (HTMT = 0.44, below 0.85); invariance across 城市/乡镇 teachers: ΔCFI = 0.008 (configural → metric).

**Reporting rule demonstrated**: adaptation of an existing scale still requires full relevance judgment for the new population — documented in the expert review round.

## What these examples demonstrate

- Construct definitions are explicit with boundaries and levels.
- Every deletion/revision at every stage is logged with a reason.
- EFA and CFA use separate samples with pre-specified criteria.
- Reliability uses ω alongside α; validity evidence is multi-type.
- Norms/cut-offs are withheld when evidence is insufficient.
- Limitations of sampling and invariance are stated rather than hidden.
