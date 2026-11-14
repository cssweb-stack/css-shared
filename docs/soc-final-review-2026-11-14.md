# Sociology final review

November 14, 2026. Focused recheck after the user's complete page-by-page review;
November 13 text/accessibility/SEO reports remain the full baseline.

## Completed locally

- Source cleanup: 48 SOC HTML files and one shared profile include formatted.
  All 60 current HTML sources are flush-left with no blank lines. List wrappers
  and list items occupy separate consecutive lines. Compared parsed built tags,
  attributes and text before/after formatting: all 67 then-existing outputs were
  unchanged apart from insignificant whitespace. Protected whitespace-sensitive
  content and front matter. Other units were not swept.
- Text: standard mechanical scan proposed zero further patches. Resolved prior
  concrete findings: inline word boundaries in Le Lin and Hörmann Prize, missing
  thesis sentence period, prime characters in Hawaiʻi, two geographic Hawaiʻi
  spellings in Wei Zhang's biography, and the full TMS definition's missing and.
  Preserved the official Manoa Political Internships label pending confirmation.
- Voice: earlier approved institutional cleanup retained. Remaining first/second
  person is personal biography, privacy/procedural guidance, source labels or
  shared 404 recovery wording; Roman-numeral matches are false positives. No
  new wholesale voice rewrite. Degree naming variants remain context-specific.
- Courses: colon-and-space format retained. Shorthand lab suffixes and Alpha
  designators are valid exceptions. No new dash-separated title entries found.
  Conflicting substantive course titles from the earlier report were not guessed.
- SEO: root and GitHub project builds have zero checker errors, with two review
  notes: the intentionally full Asia/Pacific research-area title, and Courses
  versus SOC Courses (branding already supplies the department name). Preview
  noindex remains enabled; no production-domain/indexing change authorized.
- Accessibility/reflow: focused axe scan on 15 changed/representative pages at
  320px and 1800px (30 scans): zero violations or document overflow. No helper
  guides in the finished SOC build. Every scan retains incomplete contrast
  findings; these are manual follow-up, not an automated contrast pass. Full
  screen-reader/PDF/external-site audits were not repeated.
- Root/project-prefix internal links, fragments, CSS assets, metadata presence,
  H1/main counts and alt attributes checked using the updated SOC verifier.
  Replaced its stale original-migration inventory/content assumptions with the
  reviewed current sources and configured redirects. Original migration reports
  and source export evidence remain unchanged.
- Created the standard shared 404 recovery page with SOC-specific quick links.
  Prepared 63 immediate HTML redirects, including existing eight mappings,
  clear reviewed old WordPress matches, restored emeritus/affiliate listings and
  the relocated Courses route. No redirect chains or overwrites of content pages.
  Former undergraduate/graduate landings go to Why Study; former supplementary
  faculty biographies go to the Faculty page containing their restored listings.
  Colloquia Archive remains explicitly unresolved pending the question below.
- Disabled SOC layout guides through its existing unit setting. Shared guides
  remain available to other units. Kept existing preview indexing settings.
- Shared check and whitespace checks passed. SOC root and /soc/ builds passed;
  SSRI, PUBA and GEO regression builds also passed without source edits there.

## Decisions and content still open

- News and Events now uses Sociology's X link and events email-list contact; the
  broken XDevelopers diagnostic was removed. No working X feed is claimed. This
  fallback was announced while awaiting optional user preferences. Old News and
  Events URLs now route here.
- Colloquia Archive: historical content remains in the export; its route remains
  explicitly unresolved. Not silently deleted or represented as preserved in the
  new news page. This does not prevent preview scanning; resolve before cutover.
- Old Undergraduate Advising now routes to Contact for the individual advisors,
  announced as the default; current advising functions span reviewed pages/widgets.
- Courses: three placeholder images; Why Study: three placeholder images.
- Le Lin: original final sentence remains unfinished pending his supplied text.
- External funding and other external links: live Siteimprove scan after upload,
  as requested; no claim those destinations are all working.

## Release state

Local changes only at report preparation. No commit, push, deployment or live
Siteimprove submission performed. Resolve the archive route before production cutover.
Production custom-404 HTTP status and prefix/social metadata must be checked on
the actual deployed host; local output is not evidence of deployment.

## Evidence

- exports/soc/SOC-code-cleanup-2026-11-14.json
- exports/soc/SOC-seo-final-root-2026-11-14.json
- exports/soc/SOC-seo-final-prefix-2026-11-14.json
- exports/accessibility/soc-final-2026-11-14.json
- Existing reviewed workbook remains untouched: exports/soc/SOC-page-review-2026-11-14.xlsx.
