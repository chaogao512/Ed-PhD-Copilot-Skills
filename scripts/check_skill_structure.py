#!/usr/bin/env python3
"""Check basic structure for Ed-PdD-Copilot skills."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "plugins" / "ed-pdd-copilot" / "skills"

REQUIRED_REFERENCE_HINTS = {
    "governance-idea-evaluator": ["rubric.md", "fatal-flaws.md", "theory-anchors.md", "worked-examples.md"],
    "edtech-intro-drafter": ["four-part-logic.md", "paragraph-patterns.md", "alienation-patterns.md", "worked-examples.md"],
    "governance-paper-template": ["paper-types.md", "theory-to-design.md", "dual-topology.md", "section-skeleton.md", "worked-examples.md"],
    "mixed-methods-evidence-template": [
        "claim-evidence-matrix.md",
        "indicator-system.md",
        "quantitative-methods.md",
        "qualitative-methods.md",
        "triangulation.md",
        "method-reporting-templates.md",
        "design-science-reporting.md",
        "worked-examples.md",
    ],
    "governance-figure-designer": ["figure-types.md", "layout-patterns.md", "label-language.md", "quality-audit.md"],
    "edtech-pre-submission-reviewer": ["review-rubric.md", "theory-policy-checklist.md", "method-evidence-checklist.md", "ethics-data-governance.md", "style-anti-patterns.md"],
    "ai-assisted-edtech-research-workflow": ["human-ai-boundary.md", "allowed-uses.md", "red-lines.md", "verification-checklist.md"],
}

REQUIRED_DOCS = [
    "docs/evidence-base.md",
    "docs/literature-map-edtech-governance.md",
    "docs/chinese-core-literature-inventory.md",
    "docs/chinese-core-literature-verified.md",
    "docs/verified-source-registry.md",
    "docs/skill-coverage-matrix.md",
    "docs/case-multi-agent-smart-campus.md",
    "docs/cases/case-teacher-digital-competence-governance.md",
    "docs/cases/case-education-data-governance.md",
    "docs/cases/case-human-ai-assessment-governance.md",
    "docs/review-2026-06-23-v0.4.md",
    "docs/review-2026-06-23-v1.0.md",
    "docs/review-2026-06-23-v1.1.md",
    "docs/review-2026-06-23-v1.2.md",
    "docs/review-2026-06-23-v1.3.md",
    "docs/install-readiness-audit.md",
    "docs/install-forward-test.md",
    "CHANGELOG.md",
]

REQUIRED_EXAMPLES = [
    "docs/examples/01-governance-idea-evaluator-output.md",
    "docs/examples/02-governance-paper-template-output.md",
    "docs/examples/03-edtech-intro-drafter-output.md",
    "docs/examples/04-mixed-methods-evidence-output.md",
    "docs/examples/05-governance-figure-designer-output.md",
    "docs/examples/06-edtech-pre-submission-review-output.md",
    "docs/examples/07-ai-assisted-workflow-output.md",
    "docs/examples/README.md",
    "docs/examples/case-teacher-digital-competence/01-governance-idea-evaluator-output.md",
    "docs/examples/case-teacher-digital-competence/02-governance-paper-template-output.md",
    "docs/examples/case-teacher-digital-competence/03-mixed-methods-evidence-output.md",
    "docs/examples/case-education-data-governance/01-governance-idea-evaluator-output.md",
    "docs/examples/case-education-data-governance/02-governance-paper-template-output.md",
    "docs/examples/case-education-data-governance/03-mixed-methods-evidence-output.md",
    "docs/examples/case-human-ai-assessment/01-governance-idea-evaluator-output.md",
    "docs/examples/case-human-ai-assessment/02-governance-paper-template-output.md",
    "docs/examples/case-human-ai-assessment/03-mixed-methods-evidence-output.md",
    "docs/examples/failure-cases/01-technology-first-idea.md",
    "docs/examples/failure-cases/02-evidence-mismatch.md",
    "docs/examples/failure-cases/03-decorative-theory.md",
    "docs/examples/failure-cases/04-policy-sloganization.md",
    "docs/examples/failure-cases/05-privacy-blindness.md",
    "docs/examples/failure-cases/06-overclaimed-causality.md",
    "docs/examples/failure-cases/07-ai-fabricated-citation.md",
    "docs/examples/failure-cases/08-incoherent-governance-figure.md",
    "docs/examples/failure-cases/README.md",
]

CASE_EXAMPLE_DIRS = [
    "docs/examples/case-teacher-digital-competence",
    "docs/examples/case-education-data-governance",
    "docs/examples/case-human-ai-assessment",
]

CASE_REQUIRED_SUFFIXES = [
    "01-governance-idea-evaluator-output.md",
    "02-governance-paper-template-output.md",
    "03-mixed-methods-evidence-output.md",
    "04-edtech-intro-drafter-output.md",
    "05-governance-figure-designer-output.md",
    "06-edtech-pre-submission-review-output.md",
    "07-ai-assisted-workflow-output.md",
]

MAIN_EXAMPLE_FILES = [
    "docs/examples/01-governance-idea-evaluator-output.md",
    "docs/examples/02-governance-paper-template-output.md",
    "docs/examples/03-edtech-intro-drafter-output.md",
    "docs/examples/04-mixed-methods-evidence-output.md",
    "docs/examples/05-governance-figure-designer-output.md",
    "docs/examples/06-edtech-pre-submission-review-output.md",
    "docs/examples/07-ai-assisted-workflow-output.md",
]


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)


def main() -> int:
    if not SKILLS.exists():
        fail(f"Missing skills directory: {SKILLS}")

    failures = []
    for rel in REQUIRED_DOCS + REQUIRED_EXAMPLES:
        path = ROOT / rel
        if not path.exists():
            failures.append(f"missing required project artifact: {rel}")
        elif len(path.read_text(encoding="utf-8").strip().splitlines()) < 5:
            failures.append(f"project artifact too short: {rel}")

    coverage = ROOT / "docs" / "skill-coverage-matrix.md"
    if coverage.exists():
        coverage_text = coverage.read_text(encoding="utf-8")
        if "pending" in coverage_text.lower():
            failures.append("coverage matrix still contains pending items")
        if "V1.3" not in coverage_text:
            failures.append("coverage matrix does not reflect V1.3 status")

    inventory = ROOT / "docs" / "chinese-core-literature-inventory.md"
    if inventory.exists():
        inventory_text = inventory.read_text(encoding="utf-8")
        # Count table rows with numbered entries.
        rows = [line for line in inventory_text.splitlines() if line.startswith("| ") and len(line.split("|")) > 5]
        numbered_rows = [line for line in rows if line.split("|")[1].strip().isdigit()]
        if len(numbered_rows) < 20:
            failures.append("Chinese literature inventory has fewer than 20 numbered entries")
        if "needs_cnki_verification" not in inventory_text:
            failures.append("Chinese literature inventory lacks verification-status labeling")

    registry = ROOT / "docs" / "verified-source-registry.md"
    if registry.exists():
        registry_text = registry.read_text(encoding="utf-8")
        for marker in ["NIST", "OECD", "DigCompEdu", "UNESCO", "Education Endowment Foundation", "What Works Clearinghouse"]:
            if marker not in registry_text:
                failures.append(f"verified source registry lacks V1.1 source marker: {marker}")

    for case_dir in CASE_EXAMPLE_DIRS:
        folder = ROOT / case_dir
        if not folder.exists():
            failures.append(f"missing multi-case example directory: {case_dir}")
            continue
        for filename in CASE_REQUIRED_SUFFIXES:
            path = folder / filename
            if not path.exists():
                failures.append(f"{case_dir}: missing seven-skill output {filename}")
            else:
                text = path.read_text(encoding="utf-8")
                if len(text.strip().splitlines()) < 10:
                    failures.append(f"{case_dir}: output too short {filename}")
                for required in ["## Input Summary", "## Skill Invoked", "## References Used", "## Main Output"]:
                    if required not in text:
                        failures.append(f"{case_dir}/{filename}: lacks example protocol section {required}")

    for rel in MAIN_EXAMPLE_FILES:
        path = ROOT / rel
        if path.exists():
            text = path.read_text(encoding="utf-8")
            for required in ["## Input Summary", "## Skill Invoked", "## References Used", "## Main Output"]:
                if required not in text:
                    failures.append(f"{rel}: lacks example protocol section {required}")

    failure_dir = ROOT / "docs" / "examples" / "failure-cases"
    if failure_dir.exists():
        failure_cases = sorted(path for path in failure_dir.glob("*.md") if path.name != "README.md")
        if len(failure_cases) < 8:
            failures.append("failure-case regression set has fewer than 8 cases")
        for path in failure_cases:
            text = path.read_text(encoding="utf-8")
            for required in ["## Weak input", "## Expected skill response", "## Expected diagnosis", "## Required repair"]:
                if required not in text:
                    failures.append(f"{path.relative_to(ROOT)} lacks required section: {required}")

    for skill, refs in sorted(REQUIRED_REFERENCE_HINTS.items()):
        folder = SKILLS / skill
        skill_md = folder / "SKILL.md"
        agents = folder / "agents" / "openai.yaml"
        ref_dir = folder / "references"
        if not folder.exists():
            failures.append(f"{skill}: missing folder")
            continue
        if not skill_md.exists():
            failures.append(f"{skill}: missing SKILL.md")
            text = ""
        else:
            text = skill_md.read_text(encoding="utf-8")
            if not text.startswith("---\n") or f"name: {skill}" not in text or "description:" not in text:
                failures.append(f"{skill}: invalid frontmatter")
            if "TODO" in text or "placeholder" in text.lower():
                failures.append(f"{skill}: contains TODO/placeholder")
        if not agents.exists():
            failures.append(f"{skill}: missing agents/openai.yaml")
        if not ref_dir.exists():
            failures.append(f"{skill}: missing references directory")
        else:
            for ref in refs:
                path = ref_dir / ref
                if not path.exists():
                    failures.append(f"{skill}: missing references/{ref}")
                else:
                    ref_text = path.read_text(encoding="utf-8").strip()
                    if not ref_text:
                        failures.append(f"{skill}: empty references/{ref}")
                    if len(ref_text.splitlines()) < 8:
                        failures.append(f"{skill}: references/{ref} is too thin")
                    if ref not in text:
                        failures.append(f"{skill}: references/{ref} is not mentioned in SKILL.md")

    if failures:
        for item in failures:
            print(item)
        return 1
    print("OK: all Ed-PdD-Copilot skill structure checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
