# SSRI quick SEO review

Date: November 12, 2026 (Pacific/Honolulu).

**Result:** Content metadata pass complete. Shared checker reports zero errors.
**Immediate action needed:** None. Indexing remains intentionally disabled for
development; it must be enabled and checked as part of launch.

## Completed

- Reviewed all 14 page titles against their visible H1s and page content. Titles
  are unique and descriptive, and already follow the headings. No visible
  headings or page titles needed rewriting.
- Homepage title remains Research and Grant Services; H1 adds the SSRI prefix.
  That shortened title is intentional because the shared title suffix already
  supplies Social Science Research Institute. The old duplicated institute-name
  title shown in the earlier screenshot is not present in the current build.
- Replaced 13 placeholder descriptions with distinct, content-grounded summaries.
  Preserved the existing relevant Privacy Policy description. Metadata is still
  editable in the individual HTML page front matter, not a new JSON copy.
- Description topics cover research/grants on the homepage; office/contact and
  directory details; Jack's SSRI role and research; each research unit's subject;
  each support office's actual services. Boilerplate's description explicitly
  reflects its October 2020 content date; no claims or statistics were refreshed.
- Added SSRI's `canonicalSections: ["/"]` using the existing shared renderer.
  All 14 pages now have a single canonical URL under the configured production
  domain, https://ssri.manoa.hawaii.edu. Preview pages retain their noindex state.
- Verified one title, description and H1 per page, no duplicate descriptions or
  titles, title/H1 alignment, document language, valid canonical URLs, and
  synchronized Open Graph/Twitter titles/descriptions. Social image URLs are
  absolute HTTPS and point to the existing shared SSRI Open Graph image.
- Verified every visible page body, H1, title and permalink is unchanged by this
  pass: the 13 local edits modify descriptions only. SSRI build and shared checks
  pass. Saved measured metadata in the JSON inventory below.

## Intentional exception and launch checklist

- OENAS has a long rendered title because it spells out Office for Evaluation
  and Needs Assessment Services and includes the standard brand suffix. Retained
  its useful full name/H1 alignment. The checker emits an informational length
  note; this is not a fixed-character-limit failure. [Google's title guidance](https://developers.google.com/search/docs/appearance/title-link)
  treats clarity and unnecessary verbosity as the concern rather than a hard cap.
- `indexingEnabled` remains false, producing noindex/nofollow. This is correct
  for the current development stage and would block launch indexing if left on.
  The new checker has a separate `--launch` mode to flag it.
- Final sitemap/live indexing checks follow final URL/404 work and publishing.
  This was a local content/head-tag review, not a live Google indexing report.
- Existing missing-diacritics recommendations remain separate from this task;
  no additional research-list labels or other body text were changed.

**Repositories to update:** ssri and css-shared. No commit, push or deployment.

Inventory: [all 14 pages' measured metadata](../exports/seo/ssri-2026-11-12.json).
Reusable procedure: [quick unit SEO review](seo-review.md).
