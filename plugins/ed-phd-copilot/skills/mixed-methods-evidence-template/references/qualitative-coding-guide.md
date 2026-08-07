# Qualitative Coding Guide for EdTech Governance Research

Use this guide when the study involves interviews, focus groups, open-ended survey items, classroom observations, policy documents or other textual data that must be coded into themes. It complements `qualitative-methods.md` (which defines minimum reporting) by specifying how coding should actually be performed and reported.

## 1. Coding approach selection

| Approach | Use when | Core logic |
|---|---|---|
| Deductive (theory-driven) coding | Testing a governance framework or mechanism derived from theory | Start from theory concepts; code text segments into pre-defined categories; track segments that do not fit |
| Inductive (data-driven) coding | Exploring a poorly understood governance phenomenon | Let categories emerge from the data; build up from open codes to themes |
| Hybrid (most common in EdTech governance) | Theory-anchored studies that must also capture unexpected patterns | Predefine theory categories, remain open to new codes, and report both |

## 2. Three-stage coding workflow (grounded-theory style, adaptable)

1. **Open coding**: label every meaningful segment with a short code close to the data (use the participant's language when possible, e.g., "数据责任边界模糊" rather than "governance ambiguity"). Keep a codebook with definition, example quote and decision rules.
2. **Axial coding**: group open codes into categories and specify relationships — conditions (when does this happen), actions/interactions (what actors do), consequences (what results). Example: "责任边界模糊" + "跨部门推诿" + "审批流程拖延" → category "数据共享的权责障碍".
3. **Selective coding**: integrate categories around a core category that answers the research question; test the integration against all transcripts and negative cases. Example: core category "权责制度化程度决定数据治理风险防控有效性".

## 3. Thematic analysis (Braun & Clarke six-phase, adapted)

1. Familiarization: read all transcripts; record analytic memos before coding.
2. Generating initial codes.
3. Searching for themes: collate codes into candidate themes with supporting segments.
4. Reviewing themes: check each theme against the coded extracts and the whole dataset; split, merge or discard.
5. Defining and naming themes: one-sentence definition + inclusion/exclusion criteria per theme.
6. Producing the report: each theme reported with representative quotes and analytic commentary; report the number of sources per theme.

## 4. Coding quality and inter-coder reliability

- **Double coding**: two coders independently code a subset (recommended 20–30% of material; minimum 2 transcripts or 2 documents).
- **Cohen's kappa (κ)** for inter-coder agreement on the double-coded subset:
  - κ ≥ 0.75: agreement acceptable; proceed with single coder and document it.
  - 0.40 ≤ κ < 0.75: discuss disagreements, refine codebook, re-code, re-check.
  - κ < 0.40: coding scheme is unstable; revise the codebook before continuing.
- **Codebook evolution log**: record every codebook change (date, code, reason, affected material) so the audit trail is complete.
- **Trustworthiness triangulation**: member checking, peer debriefing, audit trail, negative case analysis and thick description (see `qualitative-methods.md`).

## 5. Codebook template

| Code ID | Code name | Definition | Inclusion rule | Exclusion rule | Example quote | Stage (open/axial/selective) |
|---|---|---|---|---|---|---|
| C01 | 责任边界模糊 | 参与者报告数据权责不清 | 提及"谁负责/谁决定"不清 | 仅抱怨工作量 | "数据出了问题不知道找哪个部门" | Open |
| A01 | 权责障碍 | 责任边界模糊+流程推诿的类别 | 含 ≥2 个相关 open codes | 单一孤立片段 | — | Axial |
| T01 | 权责制度化 | 核心范畴：制度明确性与风险防控的关系 | 与 RQ 直接相关 | 与 RQ 无关 | — | Selective |

## 6. Reporting requirements (COREQ-aligned)

Report in the manuscript or appendix:

1. Coding approach (deductive/inductive/hybrid) and who coded (roles, training).
2. Stages performed and how the final theme structure was reached.
3. Double-coding proportion and κ value (or explicit statement if single-coded, with justification).
4. Codebook (as appendix or supplementary file).
5. Number of sources per theme, and representative quotes with participant IDs.
6. Negative cases: at least one quote or observation that contradicts the main theme, and how it was handled.

## 7. Software guidance (host-agnostic)

- Any qualitative analysis tool may be used (NVivo, MAXQDA, ATLAS.ti, Dedoose, or plain documents + spreadsheets); the host agent does not need the software.
- What matters for evidence quality: the audit trail (codes → categories → themes → quotes) must be reproducible from the raw material.
- If the host agent performs coding assistance, the human researcher must review and confirm every assigned code; AI-proposed codes are drafts, not analysis.
- Export a codebook and a coding matrix (source × code) as the machine-readable artifact of the coding process.
