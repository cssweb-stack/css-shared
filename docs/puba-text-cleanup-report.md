# PUBA text-cleanup report

Date: November 12, 2026. Scope: 29 HTML source pages and relevant shared PUBA
JSON text fields. Original WordPress exports were not edited.

**Status:** Complete; four report-only spelling candidates remain.
**Action needed from you:** None required. Optional observations below can be
handled during your page-by-page review.

## Findings and corrections

Initial pass: 17 HTML pages changed; shared PUBA JSON needed no mechanical changes.
Follow-up: removed 10 retired intro classes using the updated standard procedure.

| Finding | Corrections | Example |
| --- | ---: | --- |
| Retired intro classes | 10 | `<p class="intro">` → `<p>` |
| Non-breaking spaces | 59 | `provide[NBSP]limited` → `provide limited` |
| Incorrect ʻokina | 10 | `Hawai‘i`, `Hawai’i`, `Hawai'i` → `Hawaiʻi` |
| Em-dash spacing | 7 | `approaches—equipping` → `approaches — equipping` |
| Doubled spaces | 2 | Two spaces → one in prose |
| Stray hyphen after em dash | 1 | `Amy Marvin —- Executive Director` → `Amy Marvin — Executive Director` |
| University name / Mānoa spelling | 0 | No mechanical correction needed |
| Spaces before punctuation | 0 | None found |
| Invisible characters / soft hyphens | 0 | None found |
| Empty paragraphs | 0 | None found |
| Bold/italic inside headings | 0 | None found |

Counts describe individual correction operations; some occur in the same phrase.
Ordinary paragraph emphasis and quotation wording remain intact.

## Observations deliberately left unchanged

These are informational, not required decisions:

- Advisory Board: “Manoa Academy” could use “Mānoa Academy.”
- Soyun Jeong biography: “Hawaii Medicaid program” could use “Hawaiʻi Medicaid program.”
- Practicum Placements: “Hawaii Insurance Division, DCCA” and “Hawaii State Senate”
  are missing ʻokina candidates. Official organization labels were left for review.
- Practicum Placements uses `Managing Partner - The Inovi Group` and
  `Hawaii State Senate- Carol Fukunaga`; separator punctuation could be standardized
  during editorial review. No blind conversion of hyphens or numeric ranges.

The diacritic watchlist is finite, not an exhaustive Hawaiian spelling audit.

## Preservation and verification

- Compared before/after parsed HTML tag sequences and attributes for all 17 pages:
  identical in the initial pass. The follow-up changed only intro class attributes.
  Links, table markup, template expressions, filenames and page metadata
  remain unchanged. No content rewritten or images imported.
- Second standard cleanup pass: zero proposed mechanical changes, zero formatted
  headings; same four report-only diacritic candidates.
- Shared `npm run check` passed. PUBA `npm run build` passed: 30 pages.
- [Measured findings](../exports/puba/text-cleanup-2026-11-12.json).

This is mechanical text cleanup, not a factual, accessibility or SEO audit.

**Repositories to update:** puba and css-shared (report/handoff).
**Publication status:** Local changes only; no commit, push or deployment.

Procedure: [Standard text cleanup](text-cleanup.md).
