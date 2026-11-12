# SSRI text-cleanup report

Date: November 12, 2026 (Pacific/Honolulu).
Scope: 14 editable SSRI HTML pages and 11 shared SSRI unit JSON files.
Original exports, other sites and common shared page bodies were not edited.

**Status:** Complete.
Follow-up: [missing-diacritics review](ssri-diacritics-review.md) expands the scope
beyond replacing existing lookalike characters. Its recommendations are not yet
applied; the original 24-correction counts below remain unchanged.
**Action needed from you:** None. The observations below are optional editorial
notes, not questions holding up this cleanup.

## Findings and corrections

| Finding | Corrections | Before → after example |
|---|---:|---|
| Accidental non-breaking spaces | 0 | No replacements proposed in scanned prose |
| Incorrect Hawaiʻi ʻokina characters | 24 | `Hawai‘i` / `Hawai’i` → `Hawaiʻi` |
| University name / Mānoa spelling | 0 | Existing Mānoa spelling retained |
| Em-dash spacing | 0 | No changes needed under the agreed rule |
| Repeated spaces | 0 | No replacements proposed |
| Spaces before punctuation | 0 | No replacements proposed |
| Invisible characters / soft hyphens | 0 | No removals proposed |
| Empty paragraphs | 0 | None removed |

All 24 corrections replace an apostrophe/quotation-mark lookalike with U+02BB,
the proper ʻokina. No words were rewritten. Five HTML files changed:

| Page source in SSRI | Corrections |
|---|---:|
| `src/john-jack-barile.html` | 5 |
| `src/research/hcri.html` | 3 |
| `src/research/index.html` | 2 |
| `src/research/tasi-phidc.html` | 3 |
| `src/support/boilerplate.html` | 11 |

Examples include `State of Hawai‘i` → `State of Hawaiʻi` and
`University of Hawai‘i at Mānoa` → `University of Hawaiʻi at Mānoa`.
HCRI's local page title and matching H1 were both corrected. Shared SSRI JSON
needed no corrections. Correction counts include editable page metadata.

## Observations deliberately left unchanged

These are informational; no response is required.

- `src/research/ham.html` contains `‘āina-based` encoded as `&#8216;āina-based`;
  boilerplate contains `mālama ‘āina`. These use quotation-mark forms outside the
  automated, Hawaiʻi-specific spelling rule. Flagged for a future Hawaiian-text
  editorial review rather than silently broadening this mechanical pass.
- OENAS uses en dashes in project date ranges. Those remain intact. It also has
  `Cultural – Science, Technology, Engineering and Math`, while boilerplate has
  the classification label `Doctoral Universities – Very High Research Activity`.
  Retained labels and ranges rather than blanket-converting their dashes.
- Proper organizational names, quotations, dated boilerplate statistics and
  project terminology were not fact-checked or rewritten.

## Preservation and verification

- Reviewed the five proposed patches before applying them.
- Compared against a snapshot taken after the earlier intro-class removal:
  every changed character matches the approved Hawaiʻi ʻokina substitution.
  The earlier intro-class changes remain intact.
- Independently compared HTML tag/attribute events: all tags, attributes, links
  and table structure are unchanged. Template expressions and code/preformatted
  blocks are unchanged. No media, filenames or source exports were edited.
- Reran `python3 scripts/text-cleanup.py ssri`: **zero proposed patches**.
- `npm run build` in SSRI: **passed**, 14 pages generated.
- `node scripts/check-shared.mjs`: **passed**, including shared structure, unit
  records and navigation checks.

This is mechanical text cleanup, not a full factual/editorial or accessibility
audit. The scope covers SSRI-owned editable pages and unit records, not every
shared fragment rendered across the entire website system.

**Repositories to update:** `ssri` and `css-shared` (report/handoff only in shared).
**Publication status:** Local changes only; no commit, push or deployment performed.

Procedure: [standard text cleanup](text-cleanup.md).
