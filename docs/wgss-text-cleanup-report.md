# WGSS text-cleanup report

November 11, 2026. Scope: newly imported WGSS editable HTML and shared WGSS text
records. The original export remains unchanged under `exports/wgss`.

**Status: complete. Action needed from you: none.**

## Follow-up sweep after Associated Faculty import

Rerun November 11, 2026, after splitting Core/Associated Faculty and importing
the Word-document roster. The standard scanner proposed **zero changes**.
No additional accidental non-breaking spaces, invisible characters, soft hyphens,
checked Hawaiʻi apostrophe/backtick variants, repeated prose spaces, or empty
paragraphs required correction in the selected editable prose/data.

The new roster retains supplied personal-name spellings and department names.
This check does not verify people's names or current appointments, and it does
not rewrite protected template arguments such as imported video titles.
The earlier informational punctuation observations below remain nonblocking.

Shared checks and current WGSS verification passed: 28 pages, seven core faculty,
seven YouTube embeds, links/assets/fragments, metadata, image alt and heroes.
No site-source changes or rebuild were needed for this repeat pass. Only this
report/handoff changed in **css-shared**. The corrections below describe the
original import cleanup, not additional edits from this rerun.

## Findings and corrections

| Finding | Corrections | Before → after |
|---|---:|---|
| Accidental non-breaking spaces | 31 | Invisible binding spaces → normal wrapping spaces |
| Incorrect Hawaiʻi ʻokina characters | 2 | `Hawai'i` → `Hawaiʻi` |
| University name spelling | 1 | `University of Hawaii at Manoa` → `University of Hawaiʻi at Mānoa` |
| Repeated spaces | 2 | Accidental doubled spaces → one space |
| Empty paragraphs | 3 | Three empty paragraphs removed from Support |
| Em-dash spacing | 0 | No corrections needed |
| Invisible characters / soft hyphens | 0 | No corrections needed |

Twelve editable files changed. All links, image paths and HTML attributes were
preserved during cleanup. This pass did not alter requirements or rewrite prose.

## Informational observations — no response required

- Some sentence hyphens and year ranges remain in faculty biographies, for example
  Kathy Ferguson's `now - these are intellectual and political values` and
  `1870-1940`. They were left for optional editorial review rather than blindly
  changing hyphens in ranges, titles and compound words.
- Video titles retain source wording, including legacy naming/spellings inside
  imported macro arguments. Template code and attributes were not rewritten by
  the mechanical cleanup pass.
- The source outcomes are called undergraduate learning objectives; their BA-only
  applicability was not explicitly stated. That scope was not invented.

Separate import notes: Ayu has the user-approved bio shell; Monisha's office/email
were absent from the export. These are recorded for later content work, not blockers.

## Checks

- Repeat scan proposed zero further cleanup patches.
- Shared checks and local 28-page WGSS verification passed, including all seven
  core profiles and seven retained YouTube embeds.
- Source-text comparisons passed for 252 paragraph/list blocks, including merged
  and extracted sections. No source tables occurred in inspected content.
- An isolated GitHub Pages `/wgss/` prefix build and verification passed.
- Local preview responds HTTP 200. This is not a full editorial/factual review or
  proof of live analytics event collection.

Repositories to update: **wgss, css-shared**. Local only; no deployment performed.
