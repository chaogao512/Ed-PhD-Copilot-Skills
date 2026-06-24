# Install Readiness Audit

## Scope

This audit checks whether `Ed-PhD-Copilot-Skills` is ready to be used as a local skill repository before installation.

## Evidence

| Requirement | Evidence | Status |
|---|---|---|
| Seven skills exist | `plugins/ed-phd-copilot/skills/*/SKILL.md` | PASS |
| Each skill has UI metadata | `agents/openai.yaml` under each skill | PASS |
| Each skill has references | `references/` under each skill | PASS |
| Core skills have rubrics or method templates | `rubric.md`, `claim-evidence-matrix.md`, `method-reporting-templates.md`, `design-science-reporting.md` | PASS |
| Examples exist | `docs/examples/01-...` through `07-...` | PASS |
| Failure tests exist | `docs/examples/failure-cases/` | PASS |
| Evidence base exists | `docs/evidence-base.md`, `docs/verified-source-registry.md` | PASS |
| Chinese literature inventory exists | `docs/chinese-core-literature-inventory.md` | PASS |
| License compatible with adaptation source | `LICENSE` is CC BY-NC-SA 4.0 and `NOTICE.md` attributes Supervisor-Skills | PASS |
| Structure checker passes | `python3 scripts/check_skill_structure.py` | PASS |

## Boundary

The repository is install-ready as a skill set. It is not a substitute for a verified bibliography. Chinese core-journal candidates remain clearly marked until CNKI, journal websites, or local source PDFs verify full citation metadata.

## Recommendation

Proceed to local installation or installation rehearsal. After installation, run the seven-skill chain on a real doctoral topic and record outputs as future regression examples.
