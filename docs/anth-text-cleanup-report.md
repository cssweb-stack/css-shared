# ANTH text-cleanup report

November 11, 2026. Scope: Anthropology's editable HTML, relevant shared ANTH text
records, and the shared policy text rendered by ANTH. Original WordPress exports
and preserved source snapshots were not edited.

## Findings and corrections

| Finding | Corrections | Example |
|---|---:|---|
| Accidental non-breaking spaces | 312 | `Beta[NBSP]of Hawaiʻi` → `Beta of Hawaiʻi` |
| Wrong character used for Hawaiʻi's ʻokina | 37 | ``Hawai`i``, `Hawai‘i`, `Hawai’i`, `Hawai'i` → `Hawaiʻi` |
| University name / Mānoa spelling | 2 | `University of Hawaii at Manoa` → `University of Hawaiʻi at Mānoa` |
| Unspaced em dashes | 6 | `societies—social formations` → `societies — social formations` |
| Repeated spaces in prose | 3 | `Artifacts,  Urbanism` → `Artifacts, Urbanism` |
| Space before punctuation | 1 | Removed an accidental horizontal space before punctuation |

The main ANTH files contained 289 non-breaking spaces; the shared policy body
contained another 23. The number of repeated-space corrections includes one
introduced/exposed when a non-breaking space was converted to an ordinary space.
Counts describe edits, not unique words or people.

## Why the invisible spaces matter

An ordinary space permits a line break. A non-breaking space prevents it, so a
phrase that looks normal in the editor may refuse to wrap in a narrow column.
Examples appeared beside inline emphasis and links, in funding text, program
requirements, and faculty biographies. Their removal lets the browser wrap prose
naturally without changing its words.

No zero-width characters, stray byte-order marks, soft hyphens, or genuinely empty
paragraphs required removal. No suspected mojibake was found in the initial scan.

## Deliberately left for review

Some spaced hyphens occur in form or link titles, including:

- `UHM Graduate Division - Online Application`
- `Department of Anthropology - Graduate Program Application`
- `Department of Anthropology - Letter of Recommendation Form`
- `Doctorate Form II - Advance to Candidacy`
- `Doctorate Form I - Pre-Candidacy Progress`

These may be document labels rather than sentence punctuation, so they were not
automatically changed. Straight quotes, capitalization and wording were not
globally rewritten. En dashes in ranges and hyphens in compound words remain.
This was mechanical cleanup, not a full editorial or factual review.

## Preservation and checks

- HTML attributes were compared before/after; URLs and image references stayed intact.
- No table markup, template code, filenames, or original export snapshots changed.
- Rescan found no remaining non-breaking spaces or the checked Hawaiʻi
  backtick/apostrophe variants in the selected editable sources.
- Shared checks and ANTH build/verification passed: 51 pages, 13 faculty,
  25 graduate students, links, assets, fragments, metadata and hero assignments.

Local changes only. Repositories to update: **anth** and **css-shared**.
Future requests can use “standard text cleanup”; the procedure is in
[text-cleanup.md](text-cleanup.md).
