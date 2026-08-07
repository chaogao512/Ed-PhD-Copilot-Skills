# Verification Gate

The gate decides whether a literature record may be treated as a formal, citable reference. It mirrors the project-wide rule in `docs/verified-source-registry.md`: AI-generated bibliographic entries are never acceptable as formal references, and every external source must be registered before it can be cited formally.

## Three Statuses

1. **CITE-READY** — the record's bibliographic metadata was confirmed against a primary source: the publisher/DOI landing page, the journal's official site, CNKI for Chinese journal articles, or a local PDF of the actual paper. For Chinese CSSCI/core-journal articles, CNKI or the journal's official site check is required.
2. **NEEDS-VERIFICATION** — metadata plausibly complete but not yet confirmed against a primary source. Usable for exploration and reading lists, never for formal citation.
3. **NOT-CITEABLE** — any record whose metadata was inferred, guessed, or recalled by the AI (including hallucinated titles, wrong authors, or fabricated DOIs). Mark clearly and exclude from any citation list.

## Gate Steps (per record)

1. **Provenance check** — where did the record come from (Zotero JSON / SQLite / local PDF / model memory)? Records whose only origin is model memory are NOT-CITEABLE immediately.
2. **Field-level confirmation** — title, authors, year, venue, DOI must match a primary source. Discrepancies between sources (e.g., PDF vs JSON) keep the record at NEEDS-VERIFICATION until resolved.
3. **Chinese literature rule** — for Chinese journal articles, confirmation at CNKI, the journal's official website, or a local full-text PDF is mandatory before CITE-READY. Web search snippets are not sufficient (see `docs/chinese-literature-web-verification-log.md`, Non-Promotion Rule).
4. **Registration** — a record may be registered in `docs/verified-source-registry.md` only when CITE-READY. Registration includes the verification method (CNKI / DOI / publisher site / local PDF) and the verification date.

## Output

After the gate, the skill returns, for the whole batch: (a) counts per status; (b) the list of CITE-READY records ready for registry registration; (c) the list of NEEDS-VERIFICATION records with the exact verification action each still needs (e.g., "check DOI 10.xxxx at publisher site"); (d) NOT-CITEABLE records flagged for deletion or re-import from a reliable source.

## Boundary

The gate decides citation-readiness, not scholarly judgment. Relevance, theoretical fit, and quality appraisal of the literature remain the researcher's responsibility.
