# Format Gates: APA 7th and Chinese CSSCI Journal Conventions

Use this reference in the review dimension "Academic style" (and in Strict depth) to check manuscript formatting before submission. Format defects are usually MINOR issues individually, but systematic violations signal lack of journal readiness and are MAJOR.

## 1. APA 7th core gates (for SSCI/English-language submissions)

### Citations and references

- In-text citation: (Author, year) or Author (year); direct quotes need page numbers (p./pp.).
- Reference list entries: Author, A. A., & Author, B. B. (Year). Title of article. *Journal Name, Volume*(Issue), pages. https://doi.org/xxx
- Journal titles italicized, article titles in sentence case; DOI always when available.
- Up to 20 authors listed; beyond that, first 19 + ellipsis + last author.
- Each reference must be cited in the text and vice versa; no dangling references.

### Statistics and numbers (APA 7th)

- Report effect sizes with confidence intervals; italicize statistical symbols (M, SD, p, r, t, F, β).
- Report exact p values (p = .023) rather than only thresholds (p < .05), except very small values (p < .001).
- Use leading zeros for values < 1 in statistics (0.42), none for p, r, β (p = .023, r = .41).
- Degrees of freedom in parentheses: t(58) = 2.31, p = .024, d = 0.62.

### Tables and figures

- Numbered consecutively (Table 1, Figure 2); every table/figure must be mentioned in text.
- Table notes: general note, specific notes, probability notes (e.g., *p < .05. **p < .01.).
- Figures: self-contained captions, accessible color, consistent axis labels.

### Headings and language

- Five levels of headings per APA 7th; Level 1 centered bold, Level 2 flush-left bold, etc.
- Bias-free language: person-first where appropriate; avoid labels like "the disabled" without justification.

## 2. Chinese CSSCI journal gates (e.g., 电化教育研究, 中国电化教育, 现代教育技术)

### General structure

- Abstract: 200–300 字, structured or unstructured per journal; keywords 3–5 个; often requires 英文摘要与关键词.
- 作者信息: 姓名、单位、职称/学历、研究方向、基金项目编号、通讯方式（按期刊要求）。
- 正文层级: 一、二、(一) 三级标题体系（中文期刊惯例，具体按目标期刊体例）.

### References (参考文献)

- 采用顺序编码制（GB/T 7714-2015）: 正文按出现顺序编号 [1][2]，文末列表按序号排列。
- Journal: 作者. 题名[J]. 刊名, 年, 卷(期): 页码.
- Book: 作者. 书名[M]. 出版地: 出版社, 年: 页码.
- Web/policy: 发布机构. 文件名[EB/OL]. (发布日期)[引用日期]. URL.
- 中文文献著录用中文，英文文献保留原文; 部分期刊要求文献总量、近五年文献占比（投稿前查目标期刊稿约）.
- 政策文件引用规范：教育部等官方文件必须核验发布机构、文号与发布日期，见 `docs/verified-source-registry.md`。

### In-text citation style

- 顺序编码制: "已有研究指出数字形式主义问题[3]"; 同一位置多文献用 [3,5-6]。
- 转引/间接引用不得伪造页码; 未核验文献不得进入参考文献表（见 `ai-assisted-edtech-research-workflow` 验证门）。

### Other common CSSCI requirements

- 基金项目标注位置与格式按期刊稿约（通常置于首页脚注或文末）。
- 图表: 三线表为主; 图需有图题与来源说明; 表格上方表题、下方表注。
- 数字与单位、标点符号（中文全角/英文半角）按期刊要求统一。
- 查重率与 AI 生成披露要求按期刊最新规定（部分期刊要求说明 AI 使用情况）。

## 3. Format audit procedure

1. Ask the user which target venue (specific journal or dissertation committee) so the right gate set applies.
2. Check format dimensions systematically: title page / abstract / headings / citations / reference list / tables / figures / numbers / AI disclosure.
3. For each violation, output: location, the rule violated, the corrected form, and severity (MINOR if isolated; MAJOR if systematic, e.g., whole reference list in wrong style).
4. Do not rewrite the whole manuscript for format; deliver a correction list and, for the reference list, a sample of corrected entries.
5. If the journal style guide contradicts these defaults (e.g., author-date instead of numbered citations), the journal guide wins — state this explicitly.

## 4. Anti-patterns

- Applying APA 7th to a Chinese CSSCI journal (or GB/T 7714 to an SSCI journal) without checking the target venue.
- Inventing DOI or page numbers for unverified records during format "correction" — forbidden; mark them NEEDS-VERIFICATION instead.
- Reporting statistics in APA style but misformatting symbols (p-values without italics, missing degrees of freedom).
- Format-only review that misses substantive issues: format gates run after, never instead of, content gates.
