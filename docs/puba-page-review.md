# PUBA page review and URL migration inventory

Prepared November 12, 2026. Start with
[PUBA Excel checklist](../exports/puba/PUBA-page-review-2026-11-12.xlsx).

## Manual review

- **Page Review:** 29 current HTML content pages, including all six faculty bios.
  Review status dropdown, clickable GitHub preview and original URLs, proposed URL
  handling, guidance, and a blank Your notes column. Mark Done as you finish.
  New Courses and Associated Faculty pages are included. News landing is explicitly
  on hold pending blog migration. Development-only Hero Review is excluded.
- **URL Decisions:** three old pages without confirmed current destinations:
  Academic Program, GCERT Public Service Leadership, Policies and Procedures.
  First two were excluded in the earlier import; policies content is preserved in
  the shared template but has no PUBA page. Neither exclusion proves retirement.
- **Blog Pending:** 54 old URLs absent from the saved WordPress page-only export.
  These are post candidates awaiting the blog export/workflow, not retired pages.
  Student Bio titles in this tab are historical post candidates, not the six
  current faculty biography pages. No blog content imported or rewritten here.
- **Read Me:** usage, counts, scope and redirect terminology.

Keep the annotated workbook and send it back when ready. Workbook edits do not
change website data automatically. Do not regenerate over your annotated copy.

## Migration accounting

The supplied export has 84 unique URLs. Cross-checked the saved page-only WordPress
XML and earlier migration inventory against 29 current HTML pages/built H1s:

| Classification | Count |
| --- | ---: |
| Unchanged | 1 |
| Moved, proposed destination | 26 |
| Needs page decision | 3 |
| Blog/post candidates, deferred | 54 |
| Confirmed retired / 404 | 0 |

Original Directory maps to Core Faculty; associated faculty review remains a
separate current-page task. News mapping remains proposed/on hold until blogs
are resolved. No active url-migration.json or new 404 page was created in this task.
Known moves are proposals, not deployed redirects. Static redirects use immediate
meta-refresh; they are interpreted as permanent but are not HTTP 301 responses.

- [Original export](../exports/puba/original-urls-2026-11-12.json), byte-identical.
- [Machine-readable URL plan](../exports/puba/url-review-plan-2026-11-12.json).
- [Workbook input](../exports/puba/review-workbook-data-2026-11-12.json).

The workbook writer `scripts/review-workbook.py` is reusable for other units using
sheet-data JSON. It refuses to overwrite an existing workbook to protect notes.
Verified workbook ZIP/XML integrity, sheet counts, hyperlinks, all 84 original
URLs accounted for exactly once, all 29 current pages included, and all proposed
internal destinations exist. No website source changed in this task.

Repository to update: **css-shared**. Local only; no commit/push/deployment.
