# SSRI missing-diacritics review

Date: November 12, 2026 (Pacific/Honolulu).
Scope: 14 SSRI HTML pages and human-readable fields in 11 shared SSRI JSON files,
including image alt text, accessible labels and staff support descriptions.

**Status:** Report complete; no page text or unit records changed in this review.
**Action needed from you:** None to understand this report. Corrections listed
below have not been applied; ambiguous names are separated from recommendations.

## Confirmed research-page omission

Yes: `ssri/src/research/index.html` has **Hawaii Coral Reef Initiative Research
Program (HCRI)** in its heading at line 36. Our recommended spelling is
**Hawaiʻi Coral Reef Initiative Research Program (HCRI)**. The image alt text and
link's accessible label on line 33 repeat the same omission.

The [individual HCRI page](https://ssri.manoa.hawaii.edu/hcri/) uses an ʻokina-shaped
character in that word already; our local HCRI page now uses the correct U+02BB.
The earlier mechanical pass replaced incorrect existing characters but did not
detect completely absent characters or change attributes. This follow-up
explicitly expands the review to both cases.

## Recommended corrections: 10 occurrences

These are occurrences in source records, not a count of distinct words or pages.

| Location | Occurrences | Suggested correction |
|---|---:|---|
| `ssri/src/research/index.html:33,36` — HCRI heading, alt and aria-label | 3 | `Hawaii Coral Reef…` → `Hawaiʻi Coral Reef…` |
| `css-shared/src/data/units/ssri/people.json:508` — staff support description | 1 | `Hawaii Coral Reef Initiative` → `Hawaiʻi Coral Reef Initiative` |
| `ssri/src/research/index.html:83,86` — UHERO heading, alt and aria-label | 3 | `University of Hawaii Economic Research Organization` → `University of Hawaiʻi Economic Research Organization` |
| `ssri/src/research/oenas.html:73,74` — project descriptions | 2 | `Hawaii’s` → `Hawaiʻi’s` (retain the possessive apostrophe) |
| `ssri/src/research/tasi-phidc.html:50` — geographic parenthesis | 1 | `(Hawaii, USA)` → `(Hawaiʻi, USA)` |

The UHERO spelling is also used in [University of Hawaiʻi reporting about
UHERO](https://www.hawaii.edu/news/2026/03/06/uhero-report-lost-generation/).

## Context-dependent candidates: 3 occurrences

Do not automatically change these solely because a watchlist matched a word.

| Location | Text | Reason for review |
|---|---|---|
| `ssri/src/research/oenas.html:60` | `Friends of the Library of Hawaii` | Verify the organization's preferred name in this historical project reference |
| `ssri/src/research/tasi-phidc.html:47` | `Hawaii Health Systems Corporation` | Its [current site](https://www.hhsc.org/) uses diacritics in public-facing prose, but confirm whether to normalize this historical corporate-name reference |
| `ssri/src/research/oenas.html:60` | `KEIKI TO KUPUNA` | Quoted project title; do not silently change its published name or assume singular/plural intent |

## Two additional wrong-character findings

These are not missing-diacritic counts; they are quote/ʻokina lookalikes that the
earlier report already flagged outside its Hawaiʻi-specific replacement rule.

- `ssri/src/research/ham.html:15`: `‘āina-based` (encoded as `&#8216;āina-based`)
  should use the ʻokina form `ʻāina-based`.
- `ssri/src/support/boilerplate.html:19`: `mālama ‘āina` should use `mālama ʻāina`.

## Procedure improvement and limits

The standard cleanup now includes a **report-only missing-diacritics review**.
`python3 scripts/text-cleanup.py ssri` writes a `diacritic_review` list alongside
the mechanical findings. This run produces zero automatic edit patches and
15 review findings: 10 recommended missing-character corrections, three
context-dependent candidates and two quote/ʻokina corrections.

The review checks human-readable labels/attributes and shared text fields,
including `support`, while excluding email addresses, URLs, paths, template code
and preformatted code. It does not rewrite links, filenames or identifiers.
Other watchlist terms such as Manoa and Oahu produced no candidates in this scan.

This finite watchlist does not identify every Hawaiian word, establish a person's
preferred name spelling or replace a Hawaiian-language editorial review.
Unfamiliar words and personal names should not receive guessed diacritics.

Shared structural checks passed. No site build was needed: this task changed
only the audit tooling and documentation, not SSRI content or templates.

**Repository to update:** `css-shared` only for this review/tooling update.
Earlier SSRI intro/text-cleanup edits are still separate, uncommitted work.

Procedure: [standard text cleanup](text-cleanup.md).
