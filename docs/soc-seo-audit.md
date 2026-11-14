# Sociology SEO review

November 13, 2026 (Pacific/Honolulu). Local metadata cleanup complete.
No response needed from the user tonight. Indexing remains disabled for the draft.

## Corrections and verification

- Reviewed all 59 current content pages, including rendered shared content.
  Replaced 57 placeholder descriptions with unique, content-supported summaries.
  Preserved the existing Privacy Policy and Policies & Procedures descriptions.
  Faculty summaries use each person’s existing research material; Le Lin’s
  unfinished sentence was not completed or used as a source for guessed claims.
- Kept all page titles/H1s. Titles are descriptive, unique and aligned with H1s,
  and the shared shell adds the department name once. One long rendered title
  remains: “Asia, Pacific, and Hawaiʻi in Regional and Global Contexts | Department
  of Sociology.” Retained its full meaning; length is an advisory, not a failure.
- Enabled self-canonicals through SOC canonicalSections: ["/"], using its existing
  configured production host https://sociology.manoa.hawaii.edu. The public host
  still serves the original site; preview publication is separate from launch.
- Shared read-only SEO checker passed all 59 pages in root and GitHub prefix
  builds: zero errors, one intentional long-title review note. Eight generated
  migration redirect documents are excluded by the checker.
- Verified synchronized HTML/Open Graph/Twitter titles/descriptions and production
  canonicals; preview-specific page/image origins checked on all 59 pages.
  Shared SOC image exists, is 1200×630 JPEG, and is copied into build output.
- Verified all 57 edited page bodies remain byte-for-byte unchanged using hashes.
  Good existing descriptions, URLs, links, headings and academic requirements were
  preserved. Shared structural checks passed; both repositories’ whitespace checks
  passed. Root build restored after testing the /soc/ preview build.

## Open Graph diagnosis and fix

The live GitHub preview homepage returns HTTP 200 but advertises:

`https://sociology.manoa.hawaii.edu/soc/media/open-graph/soc.jpg`

That URL returned HTTP 200 with **text/html**, not an image. The correct preview
image at `https://cssweb-stack.github.io/soc/media/open-graph/soc.jpg` returned
HTTP 200 with **image/jpeg** and matches the local export’s SHA-256 hash. Thus
there is a confirmed wrong-host/path problem; cache delay alone does not explain
these current tags.

SOC’s deploy workflow specified SITE_PATH_PREFIX=/soc/ without SITE_ORIGIN, so the
shared socialUrl helper fell back to the production hostname. Added explicit
SITE_ORIGIN=https://cssweb-stack.github.io to that build step. Prefix-build checks
confirm all 59 Open Graph page/image URLs and Twitter image URLs now use the
preview host correctly. Root production builds retain the production host and
omit /soc/. Production canonicals remain independent of the preview social host.

This fix is local only. Push both repositories and rerun SOC deployment before
checking live tags again. Sharing services may retain their own cached previews
once the advertised URL has been corrected; no crawler-cache refresh was requested.
No shared helper changes were necessary and other site workflows were not swept.

## Remaining final-pass work

- Rebuild/recheck after tomorrow’s edits, especially new text and Le Lin’s reply.
  Today’s metadata/accessibility artifacts provide a measured baseline, but do
  not replace checking modified content and the actual published build.
- Retain noindex/nofollow until launch URLs and publishing are approved. No
  production indexing, sitemap, Search Console submission or domain switch made.
- Final URL migration/custom 404 and live HTTP checks remain; no custom SOC 404
  is currently emitted. A passing metadata audit is not launch approval.
- The original migration verifier still has a stale page inventory and stops on
  retired graduate/gssa.html. It has not been repaired in this SEO scope.
- Earlier text findings and manual accessibility contrast/map review remain
  recorded in their reports. No full factual, external-link or ranking audit.

Evidence: [before](../exports/seo/soc-before-2026-11-13.json),
[after/root](../exports/seo/soc-2026-11-13.json),
[prefix](../exports/seo/soc-prefix-2026-11-13.json),
[preview social metadata](../exports/seo/soc-social-prefix-2026-11-13.json),
[live Open Graph diagnosis](../exports/seo/soc-social-live-2026-11-13.json).

Repositories to commit/push: **soc and css-shared**. Rerun SOC deployment after
both are available remotely. All changes local; no commit, push or deployment.
The ignored SOC `_remove/` archive remains local and does not travel with Git.
