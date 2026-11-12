# Standard text cleanup

Reusable request: **“Run standard text cleanup for [UNIT].”** Follow this checklist
and produce a unit-specific report using [the report template](text-cleanup-report-template.md).
For multiple units, give each its own counts and findings. State explicitly whether
the user needs to answer anything; optional observations are not pending tasks.

Ask for “standard text cleanup” and specify the unit(s). Work on editable page
HTML and relevant shared text records, not original exports or migration snapshots.
Preserve words and meaning. Keep all links, filenames, template expressions,
HTML attributes, table structure and code/preformatted text unchanged.

## Mechanical pass

- Headings h1–h6 use shared heading styles: remove embedded strong/b/em/i
  formatting wrappers while preserving text, links and IDs. Do not remove normal
  paragraph emphasis. The tool's heading_formatting findings list catches these
  in HTML and shared JSON HTML fragments for review during each unit cleanup.

- Replace accidental non-breaking spaces (literal U+00A0, `&nbsp;`, decimal/hex
  equivalents) with regular spaces in prose. Preserve any intentional binding
  of values/units or other context where wrapping would change meaning.
- Collapse repeated horizontal spaces within prose; preserve indentation and
  intentional formatting. Remove accidental spaces before ordinary punctuation.
- Investigate zero-width spaces, stray byte-order marks and soft hyphens. Do not
  indiscriminately remove joiners/non-joiners that can be meaningful in languages.
- Remove genuinely empty paragraphs only when they contain no anchors, controls
  or other content. Flag whitespace around inline markup rather than rewriting
  structure to solve it.
- Correct unmistakable Hawaiʻi backtick/apostrophe variants to U+02BB ʻokina;
  use University of Hawaiʻi at Mānoa for that institution's name in ordinary prose.
  Preserve all other Hawaiian spelling/diacritics; do not guess unfamiliar names.
- House style uses spaced em dashes: `word — word`. Normalize existing em-dash
  spacing; do not blanket-convert hyphens or numeric ranges into em dashes.

## Review rather than automatically rewrite

- Look for **missing** Hawaiian diacritics as well as wrong-character lookalikes.
  The standard tool includes a report-only `diacritic_review` list in findings.json.
  It screens known forms such as Hawaii/Manoa/Oahu, human-readable alt/title/
  aria-label attributes and shared text fields (including staff support labels).
  URLs, filenames, identifiers and code are excluded. Official names, quotations
  and context-dependent words are review candidates, never blind replacements.
  The finite watchlist is not an exhaustive Hawaiian-language spellchecker.

- Spaced hyphens or en dashes used as sentence separators.
- Numeric ranges: en dash is the usual range mark, but dates, phone numbers,
  identifiers and links must not be caught by a blind conversion.
- Curly quotes, capitalization, repeated words/punctuation, and suspected
  encoding damage such as mojibake. Proper names, citations and quotations need care.
- Non-breaking spaces that may be intentional, and meaningful invisible characters.

## Verification

`python3 scripts/text-cleanup.py <unit>` prepares patches and measured JSON findings
in a fresh temporary directory without modifying the source. Inspect the patches
for intentional spacing/context before applying, then write the readable report
from `text-cleanup-report-template.md`. Original exports are never scanned for edits.

Preview a patch first. Record counts, validate that attributes/URLs and table
structure are unchanged, then build and run the unit's normal checks. Report
editorial candidates separately. Imported original snapshots remain unchanged.
Finish each sweep with a readable findings report: correction counts, concrete
before/after examples, items deliberately left for review, and checks actually run.

November 11, 2026: first cleanup applied to ANTH; see work-status.md for counts.
