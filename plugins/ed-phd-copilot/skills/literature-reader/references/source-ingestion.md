# Source Ingestion Guide

How to read literature from the three supported input modes. The host agent performs the actual file access, JSON parsing, PDF extraction, and SQLite queries; this guide defines the field mappings, ordering rules, and failure handling.

## Mode 1: Zotero Better BibTeX JSON Export

A Better BibTeX export is a JSON array of items. Use the host's JSON parser; do not regex the file.

Fields to map per item:

- `itemType` — journalArticle, conferencePaper, book, thesis, report, preprint, etc.
- `title` — the item title.
- `creators` — list of `{firstName, lastName}` (or `{name}` for institution creators). Preserve order.
- `date` — publication date; normalize to year.
- `publicationTitle` / `bookTitle` / `publisher` — venue.
- `volume`, `issue`, `pages` — citation detail.
- `DOI` / `url` — locators for verification.
- `abstractNote` — abstract text if present.
- `tags` — Zotero tags (may contain your reading notes or classification labels).
- `collections` — folder structure in Zotero; useful for grouping.
- `attachments` — local PDF paths if exported with files; check `path` and `mimeType`.

Order of work: parse the full array once; then group by `collections` when present; then read attachments only for items the user wants deep-read (ask if the list is long).

## Mode 2: Local Literature Directory

- List the directory and its immediate subdirectories. Classify files:
  - Text sources: `.md`, `.markdown`, `.txt` — read directly.
  - PDF sources: `.pdf` — extract with the host platform's PDF capability.
  - Other files (`.docx`, `.caj`, `.epub`) — report as unsupported unless the host has a converter.
- For Markdown notes, prefer the file's own structured fields (YAML frontmatter with title/authors/year is common) over guessing from the filename.
- For PDFs: extract title page and abstract first; if the PDF has no embedded metadata, derive a provisional title from the filename and mark it as low-confidence.

## Mode 3: Zotero SQLite Database

Use a **copy** of `zotero.sqlite` (copy first, then open read-only) to avoid locking the user's live Zotero.

Typical default locations (verify with the user):

- macOS: `~/Zotero/zotero.sqlite`
- Windows: `%APPDATA%\Zotero\Zotero\Profiles\<profile>\zotero.sqlite`
- Linux: `~/.zotero/zotero.sqlite`

Relevant tables:

- `items` — core item rows (`itemID`, `itemTypeID`, `key`, `dateAdded`).
- `itemData` + `itemDataValues` + `fields` — field values (title, DOI, etc.).
- `creators` + `itemCreators` — author lists with order.
- `itemAttachments` — attached files; combine with the storage directory (`<Zotero data dir>/storage/<key>/`) to locate PDFs.
- Better BibTeX tables (if the plugin is installed) — `better-bibtex_*` citation-key tables.

If the schema is unfamiliar, fall back to Mode 1 (ask the user to export Better BibTeX JSON) rather than querying blind.

## Cross-mode Rules

1. Never fabricate metadata that is not in the source (no invented abstracts, page ranges, or DOIs).
2. When metadata conflicts between sources (e.g., PDF says 2023, JSON says 2024), report both values and mark the discrepancy.
3. Record which mode and file each item came from — the verification gate needs the provenance.
4. If a source path does not exist or is unreadable, stop and ask for the correct path instead of scanning the whole disk.
