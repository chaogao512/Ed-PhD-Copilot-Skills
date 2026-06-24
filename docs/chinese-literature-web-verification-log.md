# Chinese Literature Web Verification Log

> Date: 2026-06-24
> Purpose: record public-web verification attempts for Chinese EdTech / education informatization governance literature candidates. This file prevents unverified search hits from being silently promoted into formal citations.

## Verification Principle

Public web search is useful for discovering leads, but it is not enough for formal citation unless the result exposes reliable bibliographic metadata. A Chinese academic source can move to `docs/chinese-core-literature-verified.md` only when title, author, venue, year and traceable source are confirmed through CNKI, journal website, DOI, publisher page, local PDF or school database export.

## Search Attempts

| Date | Query target | Search pattern | Result | Decision |
|---|---|---|---|---|
| 2026-06-24 | 祝智庭 + 智慧教育 / 教育信息化新境界 | General web search, exact-title variants, journal-site/domain variants | Returned unstable or insufficient metadata; no complete public bibliographic record confirmed | Keep as `needs_cnki_verification` / candidate |
| 2026-06-24 | 黄荣怀 + 智慧教育 / 智慧教育三重境界 | General web search, exact-title variants, journal-site/domain variants | Search results did not provide enough stable metadata for formal registry migration | Keep as `needs_cnki_verification` / candidate |
| 2026-06-24 | 顾小清/顾小青 + 学习分析 / 教育数据伦理 | General web search and topic variants | Ambiguous results and incomplete metadata; risk of author/name mismatch | Keep as candidate; require CNKI, journal page or local PDF |
| 2026-06-24 | 教育数据治理 + 中国电化教育 / 现代教育技术 | General web search and journal keyword variants | Topic leads found conceptually, but no specific article was verified with complete metadata | Keep as topic target |

## Non-Promotion Rule

Do not move a candidate entry into `docs/chinese-core-literature-verified.md` when:

- only the title or author appears in a search snippet;
- the result is a secondary repost without journal metadata;
- the author name is ambiguous;
- year, issue, pages or source are missing;
- access depends on a login page that was not actually opened and checked;
- the item is remembered from a local plan but not bibliographically verified.

## Next Verification Route

1. Use CNKI or the institution library export for entries 9-25 in `docs/chinese-core-literature-inventory.md`.
2. For each candidate, save exact title, authors, source, year, volume/issue/pages and DOI/CNKI URL when available.
3. If a PDF is available in the user's local corpus, verify metadata from the PDF first page and references section.
4. Add only verified entries to `docs/chinese-core-literature-verified.md`.
5. Convert verified papers into skill rules only after metadata are recorded.

## Skill Rule Translation

- `ai-assisted-edtech-research-workflow`: AI may generate search strings and candidate tables, but cannot promote unverified Chinese journal records to citations.
- `edtech-pre-submission-reviewer`: mark fabricated or incomplete Chinese citations as CRITICAL if they support manuscript claims.
- `edtech-intro-drafter`: use Chinese policy sources for background when verified journal literature is not yet available, but label the academic literature gap honestly.
- `mixed-methods-evidence-template`: treat unverified literature lists as exploratory background, not systematic or scoping review evidence.
