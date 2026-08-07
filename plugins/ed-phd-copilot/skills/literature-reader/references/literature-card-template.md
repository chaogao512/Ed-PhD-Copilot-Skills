# Literature Card Template

One card per item. Fill every field; write `N/A` only when the source genuinely lacks the value. Keep the card in the language of the user's research notes (default Chinese for this project's docs), while keeping titles and author names in their original language.

## Card Structure

```markdown
## [relevance-tag] 题名 Title

- **条目 ID / Key**: <source item key, e.g. Zotero key or filename>
- **来源**: <Zotero JSON / Zotero SQLite / 本地目录 + 文件路径>
- **类型**: <journalArticle / conferencePaper / thesis / book / report / preprint>
- **作者**: <完整作者列表，保持原序；机构作者用机构名>
- **年份**: <4 位年份>
- **发表载体**: <期刊名 / 会议名 / 出版社 / 学位授予单位>
- **卷期页码**: <volume(issue): pages，无则 N/A>
- **DOI / URL**: <DOI 优先，其次 URL>
- **标签**: <Zotero tags 或目录分类；无则 N/A>
- **摘要要点**: <3-5 条要点；逐条标注“原文摘要”或“AI 概括”>
- **研究方法**: <如：混合方法、案例研究、政策文本分析、准实验、理论建构；来自原文摘要或全文>
- **核心发现**: <1-3 条；仅当能从已读全文/摘要确认时才写>
- **与研究方向的关联**: <high / partial / low + 一句话理由>
- **引用状态**: <CITE-READY / NEEDS-VERIFICATION / NOT-CITEABLE，见 verification-gate.md>
```

## Filling Rules

1. 作者、年份、载体、DOI 等 bibliographic 字段只可从源数据（JSON / SQLite / PDF 元数据）读取，禁止凭记忆或凭模型知识补全。
2. 摘要要点区分「原文摘要」（来自 abstractNote 或 PDF 摘要页）与「AI 概括」（模型对已读内容的总结）。两者不可混排。
3. 研究方法与核心发现必须基于已读文本；未读全文的条目，这两栏写「未读全文，暂缺」。
4. 关联性判断以用户给出的研究方向为准；未提供方向时全部标 `unassessed` 并在卡片顶部注明。
5. 卡片头部按相关性排序输出：先 high，再 partial，最后 low；unassessed 放末尾。

## Batch Output Format

当条目多于 10 条时，另附一个汇总表（Markdown 表格）：条目 | 年份 | 类型 | 关联性 | 引用状态。表格用于快速筛选，卡片用于逐条精读。
