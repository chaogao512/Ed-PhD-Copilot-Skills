# Systematic Review Workflow for EdTech Governance Research

Use this reference when the user wants a systematic review, evidence map, scoping review or reproducible literature synthesis rather than a reading list. It upgrades `literature-reader` output (literature cards) into a review pipeline that can be reported transparently.

## 1. Review type decision

| Type | Use when | Minimum transparency requirements |
|---|---|---|
| Scoping review | Mapping concepts, definitions, methods in a broad area | Search sources and dates, inclusion criteria, charting form |
| Systematic review | Answering a focused question with quality appraisal and synthesis | Full PRISMA-style flow: search, screening, eligibility, appraisal, synthesis |
| Evidence map / gap map | Showing what evidence exists and where gaps are | Search protocol, coding sheet, gap table |
| Narrative review | Selective scholarly interpretation (not systematic) | Must be labeled narrative; never claim systematic status |

## 2. Protocol stage (before searching)

1. Formulate the review question; make it specific enough to be answerable. For intervention questions use PICO-style elements: Population (e.g., 中小学教师/高校学生), Intervention or phenomenon (e.g., 学业预警系统/数据治理机制), Comparison (if any), Outcomes (e.g., 学业表现、伦理风险、采纳).
2. Draft the search strategy: databases (e.g., Web of Science, Scopus, ERIC, CNKI, Wanfang), search terms in Chinese and English, Boolean combinations, date range, language limits.
3. Define inclusion and exclusion criteria in advance: study design, population, context (country/region), publication type (journal article, conference, grey literature), time window.
4. Pre-register or record the protocol with a date so the review is reproducible. If the protocol changes during the review, document the deviation.

## 3. Search and record stage

- Record per database: search date, exact query, number of hits, number imported.
- Deduplicate (e.g., by DOI/title) and record the count before and after deduplication.
- Export the full hit list as an artifact (CSV/BibTeX) so screening can be audited.
- For Chinese literature, note the database-specific constraints (CNKI export limits, non-promotion rules) and state what could not be exported.

## 4. Screening stage (PRISMA-style flow)

1. Title/abstract screening against inclusion criteria; record decisions and reasons for exclusion in batches.
2. Full-text retrieval; record how many full texts could not be obtained.
3. Full-text eligibility assessment; record one exclusion reason per excluded study (do not stack reasons).
4. Produce the PRISMA flow numbers: identified → after deduplication → screened → excluded at title/abstract → full-text assessed → excluded with reasons → included.

## 5. Quality appraisal

| Synthesis type | Appraisal tool | Minimum use |
|---|---|---|
| Mixed methods studies | MMAT (Mixed Methods Appraisal Tool) | Rate each included study's screening questions and quality criteria |
| RCT/quasi-experimental education studies | WWC-style standards or Cochrane risk-of-bias | State which studies meet standards with/without reservations |
| Qualitative studies | COREQ-based appraisal or CASP qualitative checklist | Report appraisal results per study |
| Systematic reviews of interventions | AMSTAR-2 | Only when synthesizing existing reviews |

- Report appraisal results in a table (study × criteria) and state how appraisal affects synthesis conclusions (e.g., sensitivity analysis excluding low-quality studies).

## 6. Coding, synthesis and gap identification

- Code included studies using the same coding sheet (population, intervention/phenomenon, design, outcomes, context, quality rating). Reuse `references/literature-card-template.md` fields where possible.
- Synthesis options: narrative synthesis (thematic grouping with an explicit logic), vote counting (with caveats), meta-analysis (only with sufficiently homogeneous quantitative studies and appropriate methods — do not meta-analyze heterogeneous education governance studies without justification).
- Gap identification: build a matrix of population × intervention × outcome × design and mark cells with evidence (strong/weak/none). Name gaps as (a) empty cells, (b) weak-evidence cells, (c) design-imbalanced cells (e.g., all surveys, no quasi-experiments).

## 7. Reporting gate

Before calling the output a systematic review, verify all of the following:

- [ ] Review question and eligibility criteria stated.
- [ ] Search strategy reproducible (databases, dates, full queries).
- [ ] PRISMA-style flow numbers reported.
- [ ] Quality appraisal performed and reported.
- [ ] Synthesis method explicit; meta-analysis only when appropriate.
- [ ] Gap analysis connects to future research questions.
- [ ] All included records verified as CITE-READY via `references/verification-gate.md`; unverified records are excluded or explicitly listed as candidates.

If any check fails, label the output as a narrative scan or scoping exercise and tell the user what is missing.
