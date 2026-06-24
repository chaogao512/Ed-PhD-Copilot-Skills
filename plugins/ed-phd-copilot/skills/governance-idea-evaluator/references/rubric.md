# Governance Idea Evaluation Rubric

Use this rubric after the fatal-flaws audit. Score each dimension from 1 to 5. Require evidence from the user's idea; do not infer a high score from good intentions.

## Scoring anchors

| Dimension | 1 point | 3 points | 5 points |
|---|---|---|---|
| Policy relevance | Mentions digital education policy only as background slogan | Connects to one policy demand but lacks institutional translation | Names a policy demand and converts it into concrete governance requirements |
| Educational value | Tool demonstration with unclear benefit to teaching, learning or management | Plausible benefit but actor and mechanism are not specific | Clear benefit for learning, teaching, evaluation, leadership, equity or organizational improvement |
| Organizational feasibility | Ignores school hierarchy, workload, data access or budget | Identifies stakeholders but implementation path is vague | Maps responsibilities, data rights, workload, capacity and adoption risks |
| Human-AI collaboration | Replaces human judgment with automated output | Keeps humans in review role but authority is unclear | Specifies human oversight, interpretation, override, accountability and feedback loop |
| Methodological evidencability | Claims cannot be tested with available data | Evidence route exists but misses one key data source | Mixed evidence can directly support the core claims |
| Ethics and legal controllability | Requires sensitive data without safeguards or consent | Mentions privacy but lacks operational safeguards | Includes consent, minimization, anonymization, fairness, transparency and human review |
| Theoretical contribution | No theory or only decorative theory | Uses a theory to name variables or stages | Theory generates design principles, mechanisms, indicators or interpretation logic |

## Verdict thresholds

- **Proceed**: no CRITICAL flaw, average score >= 4.0, and no dimension below 3.
- **Proceed with guardrails**: no CRITICAL flaw, average score >= 3.0, but at least one dimension below 3.
- **Pivot**: any CRITICAL flaw, or average score below 3.0, or the idea remains technology-first after clarification.

## Maturity levels

| Level | Definition | Required next step |
|---|---|---|
| Germinal idea | Topic exists but scenario, actors or evidence are unclear | Clarify problem, stakeholder and data source |
| Proposal-ready idea | Has problem, theory and feasible evidence route | Move to `governance-paper-template` |
| Manuscript-ready idea | Has section logic, contribution and validation design | Move to `edtech-intro-drafter` or review |
| Dissertation-expandable idea | Can support multiple studies or design iterations | Create chapter map and staged evidence plan |
