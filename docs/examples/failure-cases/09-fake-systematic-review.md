# Failure Case 09: Fake Systematic Review

## Weak input

“我已经让 AI 随便找了 18 篇关于教育数据治理的论文，请帮我写成系统综述，说明国内外研究一致认为高校应该建设统一数据中台。”

## Expected skill response

Use `mixed-methods-evidence-template`, `edtech-pre-submission-reviewer` or `ai-assisted-edtech-research-workflow`.

## Expected diagnosis

- **CRITICAL: Fake systematic-review claim**. A convenience AI-generated source list is not a systematic review.
- **CRITICAL: Source verification failure**. The papers must be verified through CNKI, journal websites, DOI pages, publisher pages or local PDFs before use.
- **MAJOR: PRISMA transparency missing**. There is no database list, search strategy, date, inclusion/exclusion criteria, screening flow or exclusion reasons.
- **MAJOR: Overgeneralized synthesis**. “国内外研究一致认为” hides disagreement, context difference and evidence quality.
- **MAJOR: Governance reductionism**. “统一数据中台” is a platform-construction conclusion, not necessarily a data-governance conclusion.

## Required repair

Reframe the output as an exploratory literature map unless the user can provide a reproducible search protocol. To make a systematic or scoping review claim, require:

1. search databases and dates;
2. Chinese and English search strings;
3. inclusion and exclusion criteria;
4. screening record and reasons for exclusion;
5. verified bibliographic metadata;
6. appraisal or relevance criteria;
7. synthesis categories that distinguish platform construction, data governance, risk control and educational improvement.

Until those are available, downgrade “系统综述表明” to “初步文献扫描提示”.
