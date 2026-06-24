# Failure Case Regression Protocol

This folder contains weak inputs used to test whether the skills can detect, downgrade or reject common failure patterns.

## Required Fields

Each failure case should include:

1. Weak input.
2. Expected skill response.
3. Expected diagnosis.
4. Required repair.

## Failure Cases

| File | Target skill | Expected severity | Must not output |
|---|---|---|---|
| `01-technology-first-idea.md` | `governance-idea-evaluator` | CRITICAL | Do not score as a strong idea before reframing governance problem and ethics |
| `02-evidence-mismatch.md` | `mixed-methods-evidence-template`, `edtech-pre-submission-reviewer` | CRITICAL | Do not accept technical metrics as proof of education or governance value |
| `03-decorative-theory.md` | `governance-paper-template` | MAJOR | Do not let theory remain a label without design consequences |
| `04-policy-sloganization.md` | `edtech-intro-drafter`, `edtech-pre-submission-reviewer` | MAJOR | Do not accept policy slogans without concrete governance contradiction |
| `05-privacy-blindness.md` | `governance-idea-evaluator`, `mixed-methods-evidence-template`, `edtech-pre-submission-reviewer` | CRITICAL | Do not accept high-risk student profiling without data governance and human review |
| `06-overclaimed-causality.md` | `mixed-methods-evidence-template`, `edtech-pre-submission-reviewer` | CRITICAL | Do not infer teaching quality improvement from satisfaction data |
| `07-ai-fabricated-citation.md` | `ai-assisted-edtech-research-workflow`, `edtech-pre-submission-reviewer` | CRITICAL | Do not fabricate references or treat unverified candidates as citations |
| `08-incoherent-governance-figure.md` | `governance-figure-designer`, `edtech-pre-submission-reviewer` | CRITICAL | Do not draw high-risk education AI diagrams without oversight, accountability and appeal |
| `09-fake-systematic-review.md` | `mixed-methods-evidence-template`, `edtech-pre-submission-reviewer`, `ai-assisted-edtech-research-workflow` | CRITICAL | Do not call an AI-generated convenience bibliography a systematic review |
| `10-undisclosed-ai-and-sensitive-data.md` | `ai-assisted-edtech-research-workflow`, `edtech-pre-submission-reviewer` | CRITICAL | Do not hide material AI use or upload sensitive education data without authorization |

## Future Test Expansion

- Add teacher digital fatigue failure case.
- Add invalid indicator-system construction failure case.
- Add weak COREQ qualitative-reporting failure case.
