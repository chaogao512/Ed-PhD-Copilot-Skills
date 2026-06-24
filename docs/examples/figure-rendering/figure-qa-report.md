# Figure QA Report: Education Data Governance Mechanism

> Version: V1.6
> Artifact: `docs/examples/figure-rendering/education-data-governance-mechanism.mmd`

## Figure Purpose

The figure tests whether `governance-figure-designer` can move from a text-only layout recommendation to an actual renderable diagram artifact for an education data governance case.

## QA Checklist

| Check | Result | Evidence |
|---|---|---|
| Main claim visible | Pass | The central layer is "Governance Capacity Layer", keeping the figure focused on governance capacity rather than raw platform flow. |
| Human actors visible | Pass | Students and teachers appear as data subjects with notice, consent and correction relationships. |
| Organizational responsibility visible | Pass | Data steward, data governance committee, ethics review and audit are separate nodes. |
| Data flow and accountability flow separated | Pass | Solid arrows show data/use flow; dotted arrows show authorization, human review and documentation relationships. |
| Dataset documentation present | Pass | A dedicated `Dataset Datasheet Panel` records sources, use, non-use, risks and controls. |
| High-risk boundary visible | Pass | The figure states that data must not be used for automatic punishment or ranking. |
| Appeal/correction route visible | Pass | `Appeal and correction` loops back to the data steward and connects with educational-use nodes. |
| Journal-size readability | Conditional pass | Mermaid text is readable in a full-width manuscript figure. For single-column journal layout, split the datasheet panel into a caption table. |
| Caption quality | Pass | Recommended caption below states the argument rather than only naming boxes. |

## Recommended Caption

Figure X. County education data governance capacity mechanism. The mechanism links data subjects, platform data sources, governance routines, educational use and accountability bodies, emphasizing that education data use must be bounded by authorization, quality audit, human review, appeal/correction and lifecycle management.

## Required Revisions Before Publication

1. Replace generic system names with the actual county and school data-source categories after fieldwork.
2. Add approval number or ethics-review record in the manuscript method section, not inside the figure.
3. If an AI model is added to the diagram later, add a separate `Model/System Card Panel` with intended use, non-use boundary, limitations, oversight and monitoring.

## Skill Feedback

This rendering test confirms that V1.5 figure rules are usable, but V1.6 should require at least one actual diagram artifact for each high-risk AI/data governance case when the figure skill is used for a submission-oriented manuscript.
