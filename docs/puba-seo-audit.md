# PUBA SEO review

November 12, 2026 (Pacific/Honolulu). Content metadata review complete.

- Replaced 28 placeholder descriptions with distinct summaries grounded in each
  page. Preserved the existing privacy/policy descriptions and all body text.
- Retained descriptive titles, including the homepage's intentional shortened
  title, Education for Public Service. New 404 has its own recovery description.
- Enabled production self-canonicals using canonicalSections; the 404 omits its
  canonical and stays noindex. Open Graph/Twitter metadata is synchronized.
- Read-only SEO checker: 31 pages, zero errors and zero review notes, in root and
  GitHub project-prefix builds. Social images reference existing assets.
- PUBA layout guides are disabled. The development-only hero review retains its
  source but no longer emits a published page. Shared canonical calculation now
  safely handles an unpublished template's false page URL.

Indexing remains disabled pending the publishing destination. This is a prelaunch
pass, not a production launch pass. The GitHub workflow publishes the preview at
https://cssweb-stack.github.io/puba/; the configured production canonical host is
https://puba.manoa.hawaii.edu. Confirm the intended destination before changing
indexing or replacing WordPress. Production sitemap, live HTTP/indexing checks,
and Search Console submission remain publishing work.

Evidence: [measured metadata](../exports/seo/puba-2026-11-12.json).
Changes local only; no commit, push, or deployment.
