# Validity and Reliability Protocol for EdTech Governance Scales

## 1. Validation sampling

- State the target population and sampling frame; report response rate and non-response handling.
- Sample size planning: for EFA, commonly 5–10 respondents per item (min ~100–150 for small scales); for CFA, at least 200 (more with complex models) or cases-per-parameter rules (e.g., ≥5:1, target 10:1). Report the basis, not just the final n.
- If the instrument must generalize across groups (regions, school levels, teacher types), plan a sample that permits measurement invariance testing.
- Independent samples for EFA and CFA are strongly preferred; if the same sample is split, report the split and its limitations.

## 2. EFA (exploratory) stage

- Check suitability: KMO (report value; target ≥ 0.6–0.7) and Bartlett's test.
- Extraction method and rotation must be justified (e.g., principal axis vs ML; oblique rotation when dimensions correlate — usually the right default for governance constructs).
- Report: number of factors retained and the criterion (eigenvalue > 1, scree, parallel analysis — prefer parallel analysis), factor loadings table, cross-loadings, communalities.
- Item deletion rules applied with evidence (low loading < 0.40, cross-loading ≥ 0.32 within 0.15 of the primary loading, theoretical misfit).
- Expected structure confirmed → proceed; unexpected structure → return to construct definition and justify any dimension change (do not silently redefine).

## 3. CFA (confirmatory) stage

- Pre-specify the model: dimensions, items per dimension, correlated errors allowed only with justification, higher-order factors if theorized.
- Report fit indices with thresholds used: CFI/TLI (≥ 0.90 acceptable, ≥ 0.95 good), RMSEA (≤ 0.08 acceptable, ≤ 0.06 good, with 90% CI), SRMR (≤ 0.08), and χ²/df as descriptive.
- Report standardized loadings (target ≥ 0.50, ideally ≥ 0.60) and their significance.
- Compare the theorized model against plausible alternatives (e.g., one-factor model) when structure is contested.
- Modification indices: report how many were used and why; extensive post-hoc modification without replication is a validity threat.

## 4. Reliability evidence

- Internal consistency: Cronbach's α AND McDonald's ω (ω preferred when assumptions of τ-equivalence are doubtful); report per dimension and overall with sample size.
- Test-retest reliability: interval stated, sample stated, ICC or correlation reported — required if the construct is treated as stable.
- Inter-rater reliability (if the instrument is observer/panel-rated): κ or ICC per the coding guidance in `mixed-methods-evidence-template/references/qualitative-coding-guide.md`.

## 5. Validity evidence matrix

| Validity type | Evidence required | Method |
|---|---|---|
| Content validity | Items cover the construct domain | Expert review (I-CVI/S-CVI), construct definition linkage |
| Construct validity (structural) | Factor structure matches the theory | EFA + CFA results |
| Convergent validity | Correlates with similar constructs | Correlation with established related scales; AVE ≥ 0.50 and factor loadings significant |
| Discriminant validity | Distinct from different constructs | AVE vs squared inter-construct correlations (HTMT < 0.85–0.90); correlations with unrelated constructs |
| Criterion validity | Predicts relevant outcomes | Correlation/regression with criterion measures (e.g., scale scores vs supervisor ratings or behavior logs) |
| Measurement invariance | Same construct across groups/time | Configural → metric → scalar invariance tests (ΔCFI ≤ 0.01 as a common criterion) |

## 6. Norms and cut-off points

- Only derive norms/cut-offs when the instrument supports decisions (screening, tiered support, certification-like evaluation).
- Methods: percentile-based norms, ROC analysis against a criterion, or latent profile analysis — justify the choice.
- Report: sample representativeness for the norm population, the criterion used, sensitivity/specificity at the chosen cut-off, and cross-validation evidence.
- Explicitly forbid: setting a cut-off on a small convenience sample and treating it as a standard.

## 7. Reporting gates (Strict mode)

- [ ] Construct definition with theory anchor and dimensions.
- [ ] Full item pool and deletion log.
- [ ] Expert review with I-CVI/S-CVI and revision decisions.
- [ ] EFA and CFA on clearly described samples with pre-specified criteria.
- [ ] α and ω with sample size; test-retest where claimed.
- [ ] Convergent/discriminant/criterion evidence or explicit statement of what is missing.
- [ ] Invariance and fairness checks when the scale is used across groups or for high-stakes decisions.
- [ ] Norms/cut-offs only with representative samples and cross-validation.
