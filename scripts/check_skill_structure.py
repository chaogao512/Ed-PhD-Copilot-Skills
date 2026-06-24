#!/usr/bin/env python3
"""Check basic structure for Ed-PhD-Copilot skills."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "plugins" / "ed-phd-copilot" / "skills"

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

REQUIRED_V16_REFERENCE_HINTS = {
    "ai-assisted-edtech-research-workflow": ["venue-disclosure-templates.md"],
}

REQUIRED_V17_REFERENCE_HINTS = {
    "governance-paper-template": ["doctoral-stage-templates.md"],
}

REQUIRED_DOCS = [
    "docs/evidence-base.md",
    "docs/literature-map-edtech-governance.md",
    "docs/chinese-core-literature-inventory.md",
    "docs/chinese-core-literature-verified.md",
    "docs/chinese-literature-web-verification-log.md",
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
    "docs/review-2026-06-23-v1.4.md",
    "docs/review-2026-06-24-v1.5.md",
    "docs/review-2026-06-24-v1.6.md",
    "docs/review-2026-06-24-v1.7.md",
    "docs/install-readiness-audit.md",
    "docs/install-forward-test.md",
    "docs/examples/pressure-test-digital-governance-doctoral-topic/README.md",
    "docs/examples/pressure-test-digital-governance-doctoral-topic/01-core-chain-output.md",
    "docs/examples/pressure-test-digital-governance-doctoral-topic/02-full-seven-skill-chain-output.md",
    "docs/examples/figure-rendering/education-data-governance-mechanism.mmd",
    "docs/examples/figure-rendering/figure-qa-report.md",
    "docs/examples/figure-rendering/human-ai-assessment-governance-loop.mmd",
    "docs/examples/figure-rendering/teacher-digital-competence-governance.mmd",
    "docs/examples/figure-rendering/v17-figure-qa-report.md",
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
    "docs/examples/failure-cases/09-fake-systematic-review.md",
    "docs/examples/failure-cases/10-undisclosed-ai-and-sensitive-data.md",
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

V15_EXAMPLE_FILES = [
    "docs/examples/04-mixed-methods-evidence-output.md",
    "docs/examples/06-edtech-pre-submission-review-output.md",
    "docs/examples/case-teacher-digital-competence/03-mixed-methods-evidence-output.md",
    "docs/examples/case-teacher-digital-competence/06-edtech-pre-submission-review-output.md",
    "docs/examples/case-education-data-governance/03-mixed-methods-evidence-output.md",
    "docs/examples/case-education-data-governance/06-edtech-pre-submission-review-output.md",
    "docs/examples/case-human-ai-assessment/03-mixed-methods-evidence-output.md",
    "docs/examples/case-human-ai-assessment/06-edtech-pre-submission-review-output.md",
]

V15_REQUIRED_MARKERS = ["V1.5", "COREQ"]

AI_WORKFLOW_EXAMPLE_FILES = [
    "docs/examples/07-ai-assisted-workflow-output.md",
    "docs/examples/case-teacher-digital-competence/07-ai-assisted-workflow-output.md",
    "docs/examples/case-education-data-governance/07-ai-assisted-workflow-output.md",
    "docs/examples/case-human-ai-assessment/07-ai-assisted-workflow-output.md",
]

V15_INTRO_FIGURE_EXAMPLE_FILES = [
    "docs/examples/03-edtech-intro-drafter-output.md",
    "docs/examples/05-governance-figure-designer-output.md",
    "docs/examples/case-education-data-governance/04-edtech-intro-drafter-output.md",
    "docs/examples/case-education-data-governance/05-governance-figure-designer-output.md",
    "docs/examples/case-human-ai-assessment/04-edtech-intro-drafter-output.md",
    "docs/examples/case-human-ai-assessment/05-governance-figure-designer-output.md",
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
        if "V1.7" not in coverage_text:
            failures.append("coverage matrix does not reflect V1.7 status")

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
        for marker in [
            "NIST",
            "OECD",
            "DigCompEdu",
            "UNESCO",
            "Education Endowment Foundation",
            "What Works Clearinghouse",
            "PRISMA",
            "COREQ",
            "CONSORT",
            "MMAT",
            "ICMJE",
            "Nature",
            "Elsevier",
            "Model Cards",
            "Datasheets",
            "Wiley",
            "教育信息化2.0",
            "教师数字素养",
            "教育强国建设规划纲要",
            "国家智慧教育公共服务平台",
        ]:
            if marker not in registry_text:
                failures.append(f"verified source registry lacks required source marker: {marker}")

    verified_cn = ROOT / "docs" / "chinese-core-literature-verified.md"
    if verified_cn.exists():
        verified_text = verified_cn.read_text(encoding="utf-8")
        for marker in ["教育信息化2.0", "教师数字素养", "教育强国建设规划纲要", "国家智慧教育公共服务平台"]:
            if marker not in verified_text:
                failures.append(f"Chinese verified registry lacks source marker: {marker}")
        verified_rows = [
            line for line in verified_text.splitlines()
            if line.startswith("| ") and line.split("|")[1].strip().isdigit()
        ]
        if len(verified_rows) < 4:
            failures.append("Chinese verified registry has fewer than 4 verified source rows")

    cn_web_log = ROOT / "docs" / "chinese-literature-web-verification-log.md"
    if cn_web_log.exists():
        log_text = cn_web_log.read_text(encoding="utf-8")
        for marker in ["Non-Promotion Rule", "needs_cnki_verification", "CNKI", "local PDF"]:
            if marker not in log_text:
                failures.append(f"Chinese web verification log lacks marker: {marker}")

    ai_verify = SKILLS / "ai-assisted-edtech-research-workflow" / "references" / "verification-checklist.md"
    if ai_verify.exists():
        ai_verify_text = ai_verify.read_text(encoding="utf-8")
        for marker in ["Chinese Literature Verification Gate", "candidate", "CNKI", "AI Use Disclosure Checklist"]:
            if marker not in ai_verify_text:
                failures.append(f"AI workflow verification checklist lacks marker: {marker}")

    venue_templates = SKILLS / "ai-assisted-edtech-research-workflow" / "references" / "venue-disclosure-templates.md"
    if venue_templates.exists():
        venue_text = venue_templates.read_text(encoding="utf-8")
        for marker in ["Chinese CSSCI", "Doctoral Proposal", "International Journal", "Ethics Review"]:
            if marker not in venue_text:
                failures.append(f"venue disclosure templates lack marker: {marker}")
    else:
        failures.append("AI workflow lacks venue-disclosure-templates.md")

    ai_boundary = SKILLS / "ai-assisted-edtech-research-workflow" / "references" / "human-ai-boundary.md"
    if ai_boundary.exists():
        ai_boundary_text = ai_boundary.read_text(encoding="utf-8")
        for marker in ["Authorship", "Confidentiality", "AI tools must not be listed as authors"]:
            if marker not in ai_boundary_text:
                failures.append(f"AI workflow human-ai-boundary lacks marker: {marker}")

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

    for rel in V15_EXAMPLE_FILES:
        path = ROOT / rel
        if path.exists():
            text = path.read_text(encoding="utf-8")
            for marker in V15_REQUIRED_MARKERS:
                if marker not in text:
                    failures.append(f"{rel}: lacks V1.5 marker {marker}")
            if "mixed-methods" in rel or "/03-" in rel or "/04-" in rel:
                if "Audit Depth" not in text and "Audit depth" not in text:
                    failures.append(f"{rel}: lacks Audit Depth")
            if "pre-submission" in rel or "/06-" in rel:
                if "Review Depth" not in text and "Review depth" not in text:
                    failures.append(f"{rel}: lacks Review Depth")

    for rel in AI_WORKFLOW_EXAMPLE_FILES:
        path = ROOT / rel
        if path.exists():
            text = path.read_text(encoding="utf-8")
            for marker in ["AI Disclosure", "Confidentiality", "AI"]:
                if marker not in text:
                    failures.append(f"{rel}: lacks AI workflow marker {marker}")

    for rel in V15_INTRO_FIGURE_EXAMPLE_FILES:
        path = ROOT / rel
        if path.exists():
            text = path.read_text(encoding="utf-8")
            if "intro" in rel or "/04-" in rel:
                for marker in ["V1.5", "Evidence", "Risk Boundary"]:
                    if marker not in text:
                        failures.append(f"{rel}: lacks V1.5 intro marker {marker}")
            if "figure" in rel or "/05-" in rel:
                has_card = "Model/System Card" in text or "Dataset Datasheet" in text or "Model card" in text
                if not has_card:
                    failures.append(f"{rel}: lacks V1.5 figure card marker")

    failure_dir = ROOT / "docs" / "examples" / "failure-cases"
    if failure_dir.exists():
        failure_cases = sorted(path for path in failure_dir.glob("*.md") if path.name != "README.md")
        if len(failure_cases) < 10:
            failures.append("failure-case regression set has fewer than 10 cases")
        for path in failure_cases:
            text = path.read_text(encoding="utf-8")
            for required in ["## Weak input", "## Expected skill response", "## Expected diagnosis", "## Required repair"]:
                if required not in text:
                    failures.append(f"{path.relative_to(ROOT)} lacks required section: {required}")
        fake_review = failure_dir / "09-fake-systematic-review.md"
        if fake_review.exists():
            text = fake_review.read_text(encoding="utf-8")
            for marker in ["PRISMA", "Source verification", "systematic review"]:
                if marker not in text:
                    failures.append(f"{fake_review.relative_to(ROOT)} lacks marker: {marker}")
        undisclosed_ai = failure_dir / "10-undisclosed-ai-and-sensitive-data.md"
        if undisclosed_ai.exists():
            text = undisclosed_ai.read_text(encoding="utf-8")
            for marker in ["Disclosure", "Confidentiality", "AI"]:
                if marker not in text:
                    failures.append(f"{undisclosed_ai.relative_to(ROOT)} lacks marker: {marker}")

    pressure_test = ROOT / "docs" / "examples" / "pressure-test-digital-governance-doctoral-topic" / "01-core-chain-output.md"
    if pressure_test.exists():
        pressure_text = pressure_test.read_text(encoding="utf-8")
        for marker in [
            "Skill Chain Invoked",
            "Audit Depth",
            "Review Depth",
            "Claim downgrades",
            "Next Skill",
        ]:
            if marker not in pressure_text:
                failures.append(f"{pressure_test.relative_to(ROOT)} lacks marker: {marker}")

    figure_artifact = ROOT / "docs" / "examples" / "figure-rendering" / "education-data-governance-mechanism.mmd"
    if figure_artifact.exists():
        figure_text = figure_artifact.read_text(encoding="utf-8")
        for marker in ["flowchart", "Dataset Datasheet Panel", "Appeal and correction", "Data governance committee"]:
            if marker not in figure_text:
                failures.append(f"{figure_artifact.relative_to(ROOT)} lacks marker: {marker}")

    figure_qa = ROOT / "docs" / "examples" / "figure-rendering" / "figure-qa-report.md"
    if figure_qa.exists():
        qa_text = figure_qa.read_text(encoding="utf-8")
        for marker in ["Figure QA Report", "Journal-size readability", "Skill Feedback"]:
            if marker not in qa_text:
                failures.append(f"{figure_qa.relative_to(ROOT)} lacks marker: {marker}")

    full_chain = ROOT / "docs" / "examples" / "pressure-test-digital-governance-doctoral-topic" / "02-full-seven-skill-chain-output.md"
    if full_chain.exists():
        full_chain_text = full_chain.read_text(encoding="utf-8")
        for marker in [
            "Full Seven-Skill Pressure Test",
            "governance-idea-evaluator",
            "edtech-intro-drafter",
            "governance-figure-designer",
            "ai-assisted-edtech-research-workflow",
            "Quality Self-Check",
        ]:
            if marker not in full_chain_text:
                failures.append(f"{full_chain.relative_to(ROOT)} lacks marker: {marker}")

    v17_qa = ROOT / "docs" / "examples" / "figure-rendering" / "v17-figure-qa-report.md"
    if v17_qa.exists():
        v17_qa_text = v17_qa.read_text(encoding="utf-8")
        for marker in ["Human-AI Assessment QA", "Teacher Digital Competence QA", "Skill Feedback"]:
            if marker not in v17_qa_text:
                failures.append(f"{v17_qa.relative_to(ROOT)} lacks marker: {marker}")

    for rel, markers in {
        "docs/examples/figure-rendering/human-ai-assessment-governance-loop.mmd": ["Model/System Card Panel", "not final judgment", "appeal route"],
        "docs/examples/figure-rendering/teacher-digital-competence-governance.mmd": ["Evidence Panel", "Competence is not attendance", "feedback loop"],
    }.items():
        path = ROOT / rel
        if path.exists():
            text = path.read_text(encoding="utf-8")
            for marker in markers:
                if marker not in text:
                    failures.append(f"{rel} lacks marker: {marker}")

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

    for skill, refs in sorted(REQUIRED_V16_REFERENCE_HINTS.items()):
        folder = SKILLS / skill
        skill_md = folder / "SKILL.md"
        text = skill_md.read_text(encoding="utf-8") if skill_md.exists() else ""
        for ref in refs:
            path = folder / "references" / ref
            if not path.exists():
                failures.append(f"{skill}: missing V1.6 references/{ref}")
            else:
                ref_text = path.read_text(encoding="utf-8").strip()
                if len(ref_text.splitlines()) < 20:
                    failures.append(f"{skill}: V1.6 references/{ref} is too thin")
                if ref not in text:
                    failures.append(f"{skill}: V1.6 references/{ref} is not mentioned in SKILL.md")

    for skill, refs in sorted(REQUIRED_V17_REFERENCE_HINTS.items()):
        folder = SKILLS / skill
        skill_md = folder / "SKILL.md"
        text = skill_md.read_text(encoding="utf-8") if skill_md.exists() else ""
        for ref in refs:
            path = folder / "references" / ref
            if not path.exists():
                failures.append(f"{skill}: missing V1.7 references/{ref}")
            else:
                ref_text = path.read_text(encoding="utf-8").strip()
                if len(ref_text.splitlines()) < 20:
                    failures.append(f"{skill}: V1.7 references/{ref} is too thin")
                if ref not in text:
                    failures.append(f"{skill}: V1.7 references/{ref} is not mentioned in SKILL.md")

    if failures:
        for item in failures:
            print(item)
        return 1
    print("OK: all Ed-PhD-Copilot skill structure checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
