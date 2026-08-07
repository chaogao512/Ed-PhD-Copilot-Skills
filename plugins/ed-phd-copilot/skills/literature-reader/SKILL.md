---
name: literature-reader
description: >-
  Reads and organizes academic literature for education technology and education governance research from user-provided sources: a Zotero Better BibTeX JSON export, a local Zotero SQLite database, or a local folder containing PDFs and Markdown notes. Use when the user asks to read literature from Zotero or from a specified local directory, needs structured literature cards (title, authors, year, source, abstract points, methods, relevance to their research direction), wants to screen a reading list against a research direction, or needs to verify whether a retrieved record is safe to cite.
---

# Literature Reader

## Overview

Read literature from the sources the user actually keeps it in — Zotero exports, the Zotero local database, or a plain folder of PDFs and Markdown notes — and turn raw files into structured literature cards that downstream skills (`governance-idea-evaluator`, `edtech-intro-drafter`, `mixed-methods-evidence-template`) can consume. The skill is platform-agnostic: the host agent performs the actual file access and PDF parsing; this skill defines what to read, in what order, and what to produce.

## Reference Navigation

- Always read `references/source-ingestion.md` before touching any input source.
- Always produce cards using `references/literature-card-template.md`.
- Always apply `references/verification-gate.md` before any record may be treated as a citable reference.
- Read `references/systematic-review-workflow.md` when the user wants a systematic review, scoping review, evidence map or reproducible synthesis (PRISMA-style flow, quality appraisal, gap identification) instead of a reading list.

## Input Modes

The user provides one of the following:

1. **Zotero Better BibTeX JSON** — a `Better-BibTeX` export file path (`.json` with `"itemType"`, `"title"`, `"creators"`, `"date"`, `"abstractNote"`, `"tags"`, `"collections"`, `"attachments"` fields). Parse it with the JSON parser available to the host agent.
2. **Local literature directory** — a folder path containing PDFs and/or Markdown notes. List the directory first; for `.md`/`.markdown`/`.txt` read the text directly; for `.pdf` use the host platform's PDF extraction capability. If the host cannot parse PDFs, report that and process only text files (degraded mode).
3. **Zotero SQLite database** — a path to `zotero.sqlite` (or a copy). Query the `items`, `itemData`, `creators`, `itemAttachments`, and (if present) Better BibTeX tables. Prefer a copy of the database over the live file to avoid locking Zotero.

Ask the user which mode applies if none is obvious. Never guess a Zotero data directory path — ask for it or for an export file.

## Workflow

0. If the user asks for a systematic review, scoping review or evidence map, read `references/systematic-review-workflow.md` first and follow its protocol stages.
1. Confirm the source path exists and is readable. For a directory, list files and sort into PDF vs text groups.
2. Read the ingestion rules in `references/source-ingestion.md` for the chosen mode.
3. Extract per-item metadata. For PDFs without metadata, fall back to filename heuristics and state the confidence level.
4. Screen each item against the user's stated research direction (if provided). Tag as `high-relevance`, `partial-relevance`, or `low-relevance` with a one-line reason.
5. Produce one literature card per item using `references/literature-card-template.md`.
6. Apply `references/verification-gate.md` and mark every card `CITE-READY`, `NEEDS-VERIFICATION`, or `NOT-CITEABLE`. Keep AI-inferred metadata visually separate from metadata present in the source file.
7. Output the cards grouped by relevance, then list which records can enter `docs/verified-source-registry.md` and which still need CNKI / publisher-site / DOI / local-PDF verification.

## Degraded Mode

If the host platform cannot parse PDFs or cannot open SQLite, say so explicitly, process JSON and Markdown sources only, and tell the user what was skipped. Do not fabricate abstracts or page ranges for unread files.

## Boundary

This skill reads and organizes literature; it does not make citation decisions. Only records that pass `references/verification-gate.md` may be used as formal citations, and AI-generated bibliographic entries are never acceptable as formal references.
