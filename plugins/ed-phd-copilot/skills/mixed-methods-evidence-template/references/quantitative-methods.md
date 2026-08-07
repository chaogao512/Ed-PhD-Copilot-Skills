# Quantitative Methods Minimum Reporting

| Method | Use when | Must report | Common misuse |
|---|---|---|---|
| Questionnaire | Measuring perception, acceptance or competence | Construct source, sample, reliability, validity, items | Treating self-report as actual performance |
| Quasi-experiment | Comparing intervention effect without random assignment | Groups, baseline equivalence, intervention, outcome, threats | Strong causal claims without controls |
| Log analysis | Studying behavior or process | Data source, cleaning, metric definition, missing data | Equating activity volume with learning |
| EFA/CFA | Testing structure of scales | Sample size, extraction/fit indices, item removal logic | Running factor analysis on too few responses |
| Regression/SEM | Testing relationships | Model rationale, assumptions, covariates, limitations | Inferring causality from correlational data |
| AHP/entropy | Weighting indicators | Expert matrix or data basis, consistency, rationale | Hiding subjective assumptions behind numbers |
| Systematic review coding | Summarizing intervention or governance evidence | Search dates, databases, keywords, screening criteria, coding sheet, appraisal method | Treating selective literature reading as systematic evidence |
| AI risk measurement | Evaluating education AI systems | Intended use, affected groups, risk metrics, oversight logs, error/fairness monitoring | Reporting only accuracy while ignoring educational and rights risks |

## Education Intervention Evidence Boundaries

Use stronger causal language only when the design supports it.

| Evidence design | What it can support | What it cannot support |
|---|---|---|
| Descriptive survey | Current perceptions, needs, acceptance, self-reported practice | Intervention effectiveness or causal impact |
| One-group posttest | Participant response after an activity | Improvement, unless baseline or comparison is available |
| Pre-post without comparison | Change over time in one group | Strong attribution to the intervention |
| Quasi-experiment with baseline equivalence | Plausible intervention effect under stated limitations | Universal effectiveness across contexts |
| Randomized or strong matched comparison | Stronger causal inference if implementation is valid | Mechanism explanation without qualitative/process evidence |
| Longitudinal mixed evidence | Development trajectory and implementation process | Pure causal proof unless design controls threats |

## Design and Reporting Gates

| Gate | Minimum check | If absent |
|---|---|---|
| CONSORT/SPIRIT-style intervention transparency | State assignment/comparison design, participant flow, intervention components, outcomes and analysis plan | Downgrade to pilot or feasibility evidence |
| WWC-style education evidence boundary | Check baseline equivalence, attrition, outcome validity and implementation fidelity | Avoid causal or effectiveness claims |
| PRISMA-style evidence synthesis | Record search strategy, screening flow, inclusion/exclusion criteria and appraisal basis | Call it a narrative scan, not systematic review |
| NIST AI RMF-style risk measurement | Map context and affected groups, measure harms/benefits, manage safeguards and monitor lifecycle | Treat AI system as unvalidated risk-bearing prototype |

## Effect Size Reporting

Statistical significance alone is insufficient for education governance research. Report effect sizes with confidence intervals for every focal test.

| Effect size | Use when | Reporting rule | Rough interpretation guidance |
|---|---|---|---|
| Cohen's d | Group comparison (t-test, quasi-experiment) | d with 95% CI | 0.2 small, 0.5 medium, 0.8 large (context-dependent; interpret against field baselines) |
| η² / partial η² | ANOVA/ANCOVA | Report partial η² with CI when available | 0.01 small, 0.06 medium, 0.14 large |
| β with standardized/unstandardized coefficient | Regression/SEM | Report standardized β, SE and CI; compare practical vs statistical significance | Magnitude meaningfulness judged against outcome scale |
| OR / RR | Binary outcomes (logistic) | OR with 95% CI; state baseline rate | OR far from 1 with wide CI = weak evidence |
| r / Cramer's V | Correlations / chi-square associations | Report r or V with CI | V: 0.1 small, 0.3 medium, 0.5 large (df-adjusted) |
| R² / ΔR² | Model fit contribution | Report ΔR² when adding key predictors | Interpreted against discipline norms, not only p |

Rules: (1) effect size and CI for every primary hypothesis test; (2) do not interpret an effect size with a CI crossing zero as evidence of an effect; (3) discuss practical significance — a statistically significant but trivially small effect must be labeled as such.

## Robustness Checks

A robustness section strengthens claims when the main analysis could be sensitive to decisions. Report at least one check appropriate to the design:

| Design | Recommended robustness checks |
|---|---|
| Regression/SEM | Alternative model specifications (add/drop covariates), alternative estimators (e.g., robust SE, clustered SE), outlier sensitivity, multicollinearity diagnostics |
| Quasi-experiment | Alternative matching approaches, placebo outcome tests, sensitivity to attrition assumptions, subgroup analyses pre-specified |
| Questionnaire/scale | Alternative reliability estimates (α vs McDonald's ω), split-half, item deletion sensitivity |
| Log/data analysis | Alternative metric definitions, missing-data handling sensitivity (complete-case vs multiple imputation), time-window variation |
| Weighting (AHP/entropy) | Sensitivity of weights to expert input variation; rank stability |

Rules: (1) robustness checks are pre-registered or explicitly labeled exploratory; (2) report whether conclusions survive the checks — do not bury failures; (3) a robustness check that changes the conclusion triggers claim downgrade or reframing.

## Power Analysis Minimum Requirements

- Report the minimum detectable effect (MDE) or the achieved power for the primary hypothesis before collecting data (or justify its absence for secondary analyses).
- For education interventions, plan for effect sizes realistic in the field (often d ≈ 0.2–0.4 for school-based interventions) rather than textbook medium effects, unless prior evidence supports otherwise.
- For questionnaire studies, ensure sample size supports the planned analyses: e.g., EFA/CFA rules of thumb (item-to-response ratios, absolute minimums) and SEM complexity (cases per estimated parameter).
- For subgroup or moderation analyses, state explicitly that power is likely insufficient unless the study is designed for it; interpret null moderations cautiously.
- Report: software/method, parameters assumed, MDE achieved, and whether the design can detect the effect the study claims to investigate.

## Minimum Claim Language

- Use **associated with** for correlational models.
- Use **perceived improvement** for satisfaction and self-report evidence.
- Use **implementation feasibility** for pilot demonstrations.
- Use **preliminary effect** for weak comparison or short-term pre-post evidence.
- Use **causal effect** only with a design that addresses selection, baseline equivalence, attrition and measurement threats.
- Use **systematic review** only when search, screening and reporting procedures are reproducible.
- Use **safe or trustworthy AI** only when risk, oversight, transparency and monitoring evidence are reported.
