<div align="center">

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Version](https://img.shields.io/badge/version-1.9-blue.svg)]()
[![Platform](https://img.shields.io/badge/platform-agnostic-green.svg)]()
[![GitHub stars](https://img.shields.io/github/stars/chaogao512/Ed-PhD-Copilot-Skills?style=social)](https://github.com/chaogao512/Ed-PhD-Copilot-Skills)

</div>

# Ed-PhD-Copilot-Skills

🇺🇸 English | [🇨🇳 中文](./README.zh-CN.md)

A structured AI skill library for education technology, educational leadership and education informatization governance research. Platform-agnostic: any agent platform that triggers skills from `SKILL.md` (Reasonix, ChatGPT Custom GPT, Claude Project, Cursor Rules) can use it directly.

The organization follows the "Handbook + Skills" two-track model of `Supervisor-Skills`, but the content was rewritten for education informatization governance, smart campuses, digital transformation, educational leadership and education research methods.

## What this project does

It is not a collection of generic writing prompts. It makes the judgment calls in education technology research explicit:

- **Topic screening** — policy value, organizational feasibility, ethics risk and theoretical contribution in one pass
- **Paper structure** — separate skeletons for mechanism, empirical and indicator studies
- **Evidence design** — minimum requirements for mixed methods, scale development, qualitative coding and statistics reporting
- **Introduction and discussion writing** — paragraph logic instead of word stacks
- **Pre-submission review** — theory, method, ethics and format checks against journal standards
- **AI use boundaries** — division of labor, red lines, disclosure templates and verification checklists

## Skills overview

| Skill | What it does |
|---|---|
| `governance-idea-evaluator` | Screens research topics: fatal-flaw gates, seven-dimension scoring, proceed or pivot |
| `edtech-intro-drafter` | Introduction outline: policy demand — technology affordance — governance alienation — research legitimacy |
| `governance-paper-template` | Paper skeleton: paper types, theory-to-design mapping, technology-organization dual topology, doctoral-stage templates |
| `mixed-methods-evidence-template` | Mixed evidence chains: claim-evidence matrix, triangulation, reporting-standard gates |
| `governance-figure-designer` | Figure design: mechanism, flow and evidence-chain diagrams with quality audit |
| `edtech-pre-submission-reviewer` | Pre-submission review: CRITICAL/MAJOR/MINOR findings, APA 7th / CSSCI format gates |
| `ai-assisted-edtech-research-workflow` | AI use boundaries: human-AI division, red lines, disclosure templates, verification checklist |
| `literature-reader` | Literature intake: Zotero or local folder input, literature cards plus systematic review workflow |
| `governance-discussion-drafter` | Discussion writing: theory dialogue, literature comparison, limitation taxonomy, bounded implications |
| `scale-development-template` | Scale development: construct definition, item pool, expert review, EFA/CFA, reliability and validity, norms |

## Directory layout

```text
Ed-PhD-Copilot-Skills/
├── README.md / README.zh-CN.md
├── LICENSE
├── docs/            reviews, cases, examples, literature evidence
├── handbook/        system guide: 6 chapters, 13 methodology docs (evaluation / ideas / writing / plotting / AI-assisted research / cases)
├── plugins/
│   └── ed-phd-copilot/skills/   10 skills, each with SKILL.md + agents/openai.yaml + references/
├── scripts/         check_skill_structure.py structure checks
└── assets/          external reference assets
```

Every skill has three layers: `SKILL.md` (frontmatter plus execution flow), `agents/openai.yaml` (platform metadata) and `references/` (rubrics, checklists, templates loaded on demand).

## Handbook: the knowledge layer

The handbook holds the theory and methodology — how to judge a paper, how to pick a topic, how to write and how to draw. Skills execute; the handbook explains why. Read the matching chapter before calling a skill.

| Chapter | Topic | What it covers |
|---|---|---|
| 01 Preliminary | Evaluating a paper | Reviewer perspective, EdTech journal culture, theory grounding |
| 02 Idea Generation | Topics and innovation | Research-type lifecycle, five-dimension idea framework, disruptive innovation |
| 03 Paper Writing | From skeleton to detail | Introduction flowchart, full-paper template, writing checklist (APA 7th / CSSCI) |
| 04 Scientific Plotting | Figures | Motivation, solution-overview and results figures, tools cheat-sheet |
| 05 Vibe Research | AI-assisted research | Vibe Coding / Figure / Writing, tool experience, AI use boundaries |
| 06 Case Studies | EdTech paper walkthroughs | Under construction — planned types listed |

## Suggested workflow

1. Screen the topic: `governance-idea-evaluator`
2. Build the skeleton: `governance-paper-template`
3. Design evidence: `mixed-methods-evidence-template` (use `scale-development-template` when the deliverable is an instrument)
4. Draft the introduction: `edtech-intro-drafter`
5. Design figures: `governance-figure-designer`
6. Write the discussion: `governance-discussion-drafter`
7. Review before submission: `edtech-pre-submission-reviewer`
8. Literature and AI boundaries run throughout: `literature-reader`, `ai-assisted-edtech-research-workflow`

## Current status

Version **V1.9** (2026-08-10).

**Skills and support material**

- 10 skills, each with `SKILL.md`, `agents/openai.yaml` and `references/`
- Method standards in place: PRISMA/COREQ/CONSORT/WWC/MMAT reporting gates, three-stage qualitative coding with Cohen's κ, effect sizes and power analysis, systematic review workflow, APA 7th and CSSCI format gates
- Theory anchors on both tracks: collaborative governance, data governance, institutional theory, plus CoI, cognitive load, self-determination, UTAUT and others

**Evidence and cases**

- 4 cross-cutting cases run through the 7-skill chain: smart campus governance, teacher digital competence, education data governance, human-AI classroom assessment, learning-analytics early warning
- 9 main-case skill outputs plus 11 failure-case regressions
- Literature evidence: `docs/evidence-base.md`, `docs/verified-source-registry.md`, verified Chinese core-journal registry

**Reviews**

- Each version has a review record in `docs/review-YYYY-MM-DD-vX.Y.md`; the latest is [`docs/review-2026-08-10-v1.9.md`](docs/review-2026-08-10-v1.9.md)

**Validation**

- `make check` runs the full structure check (equivalent to `python3 scripts/check_skill_structure.py`)

Next steps: verify Chinese CSSCI/core-journal records one by one, run installed-skill trigger tests, and produce a proposal sample plus a research-design flow diagram once the actual research direction is known. The roadmap lives in [`docs/roadmap.md`](docs/roadmap.md).

## Relation to Supervisor-Skills

This repository adapts the organizational model of `HKUSTDial/Supervisor-Skills` and rewrites the content for education technology, educational leadership and education informatization governance. Both the original project and this one are CC BY-NC-SA 4.0. When re-adapting, credit this repository and respect the original attribution requirements. Source notes are in [`NOTICE.md`](NOTICE.md).

## License

[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/): non-commercial use, attribution required, share alike.
