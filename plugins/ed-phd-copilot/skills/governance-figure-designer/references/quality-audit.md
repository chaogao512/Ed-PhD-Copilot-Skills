# Figure Quality Audit

Check every proposed figure:

- One main claim is visible within 10 seconds.
- Human actors are visible, not hidden as “users”.
- AI/system actors are bounded by responsibility and oversight.
- Data flow, decision flow, feedback flow and accountability flow are visually distinct.
- Ethics/privacy/fairness boundary appears where data and decisions are high risk.
- The caption states the argument of the figure.
- Labels use education governance language.
- The diagram can be read in grayscale and at journal column size.
- AI systems have visible intended-use, limitation and human-oversight notes.
- Data sources have visible consent, minimization, quality, retention and deletion notes.
- High-risk uses have visible risk owner, monitoring evidence, appeal/correction and incident response.

## Severity

- CRITICAL: no human oversight in a high-stakes AI education diagram.
- CRITICAL: high-risk AI diagram shows automatic decision, ranking or profiling without appeal and accountable owner.
- MAJOR: actor roles or accountability are unclear.
- MAJOR: dataset or model is shown as a black box without source, limitation or non-use boundary.
- MINOR: labels are too technical or caption is descriptive only.

## Scenario-Specific Figure Checks

### Teacher Digital Competence

- Show region, school,教研 group and teacher as different actors.
- Separate training input, classroom transfer, peer feedback and continuous improvement.
- Avoid showing teachers as passive recipients of technology.

### Education Data Governance

- Show data owner, data steward, data user, data subject and oversight body.
- Distinguish data flow from authorization flow and accountability flow.
- Include risk review, audit trail, retention/deletion and appeal/correction routes.

### Human-AI Assessment

- Show AI suggestion as intermediate evidence, not final judgment.
- Include teacher interpretation, student explanation, appeal and instructional improvement.
- Distinguish feedback for learning from accountability or ranking uses.

## Model Card / Dataset Datasheet Audit

For AI or data-intensive figures, check whether the figure or caption answers:

| Card item | Minimum visible answer |
|---|---|
| Intended use | Which educational decision or support process the system serves |
| Non-use boundary | What the system must not decide |
| Data source | What data are collected and from whom |
| Data rights | Consent, authorization, access and correction route |
| Quality and bias | Missing data, subgroup risk and error cases |
| Oversight | Who reviews, overrides and is accountable |
| Monitoring | Logs, incident reporting, fairness/drift checks and update cycle |

If these cannot fit inside the main diagram, add a side panel or table.
