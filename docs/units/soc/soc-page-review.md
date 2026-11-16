# Sociology final page review workbook

Prepared November 14, 2026. Start with the
[SOC Excel checklist](../../../exports/soc/SOC-page-review-2026-11-14.xlsx).
User requested this review before any new 404 or redirect implementation.

## How to review

- Page Review lists all 59 current content pages, including faculty biographies
  and split MA/PhD subpages. From links open original production pages. To links
  open the current local site at localhost:8086. A separate column links the
  GitHub preview, whose freshness is unverified. Mark status Done, In progress,
  Needs follow-up or Deferred and enter notes. Initial status is Not reviewed,
  except the unfinished news-feed page, marked Needs follow-up.
- Old URLs accounts for each of the 57 published WordPress page URLs exactly
  once, with proposed current destinations and explanations. A match indicates
  a route/content relationship, not proof of verbatim content preservation.
- URL Decisions isolates seven originals requiring a choice before redirects:
  Patricia Steinhoff, Yean Ju Lee, Hagen Koo, Colloquia Archive, News, Events and
  Undergraduate Advising. No retirement has been inferred.
- Route Changes records eight existing configured redirects, left untouched,
  and the proposed old local Courses route to its new root destination.
- Read Me explains scope, counts, evidence, review priorities and next steps.

Keep the annotated workbook and send it back. Do not regenerate over the reviewed
copy. Changes in the workbook do not automatically alter the website. The shared
workbook writer refuses to overwrite an existing workbook.

## Source comparison and accounting

Parsed the supplied sociologysoc.WordPress.2026-11-14.xml as source data only.
Its 242 items contain 57 published pages, 122 inherited attachments, 52 menu
items and 11 builder/theme/style entries; no blog posts. The 57 published page
IDs, titles, URLs and raw content bodies match the saved November 10 export.
The new export SHA-256 and individual page body hashes are recorded in the plan.
No source content imported, no media downloaded, no students/portraits changed.

| Original published URL classification | Count |
| --- | ---: |
| Unchanged path | 2 |
| Moved, proposed destination | 40 |
| Merged, proposed destination | 8 |
| Needs decision | 7 |
| Confirmed retired | 0 |

Stale inventory destinations were resolved to current real content pages rather
than intermediate redirects. Removed obsolete fragment candidates where anchors
no longer exist; preserved valid undergraduate/graduate Why Study anchors.
About proposes the Research Areas landing because the old About page contains
the five research summaries and History link; this updates the stale Why Study
candidate in the historical inventory, not live routing.

Funding rows point to the consolidated resource directory with an explicit note
that old detailed eligibility/deadline text was intentionally rewritten. MA/PhD
detail pages share their respective original program page for comparison.
Undergraduate Advising is not silently mapped to Academic Planning: its original
functions now span degree declaration content, shared advising widgets and planning.
The workbook flags the primary destination decision instead of claiming equivalence.

News and Events candidates are held because the current page still has the
XDevelopers timeline diagnostic rather than a final Sociology news replacement.
The unmatched archive and faculty pages are preserved in the source evidence;
their absence from approved navigation does not authorize retirement.

## Verification and limits

SOC rebuilt successfully with 59 current content pages and eight pre-existing
generated redirect outputs. All proposed nonblank internal destinations and
fragments resolve in the local build. Checked workbook ZIP/XML integrity, exact
row contents, 59-page status dropdown, 360 hyperlinks, unique accounting of all
57 originals and all 59 current pages. Evidence:

- [Machine-readable URL plan](../../../exports/soc/SOC-url-review-plan-2026-11-14.json)
- [Workbook source data](../../../exports/soc/SOC-review-workbook-data-2026-11-14.json)
- [From/to CSV](../../../exports/soc/SOC-from-to-2026-11-14.csv)
- [Validation results](../../../exports/soc/SOC-review-validation-2026-11-14.json)

This compares routes, page structure and known editorial changes, not a new
line-by-line academic content audit. No live original/preview fetch verification,
fresh accessibility/SEO sweep, custom 404, retirement list or new redirect mapping
was performed. The eight existing redirects are configuration evidence only;
their deployed state was not checked. Future static redirects are immediate
HTML meta refresh, not HTTP 301 responses.

Only css-shared workbook/evidence/docs changed for this task; existing soc source
work preserved. Local only, no commit/push/deployment. After workbook review,
resolve decisions, implement agreed routing/custom 404, run final text/voice,
accessibility/SEO and live-host checks in the user-directed order. Do not publish
or enable indexing merely because the workbook validates.
