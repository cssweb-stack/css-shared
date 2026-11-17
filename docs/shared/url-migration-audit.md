# URL migration implementation and historical checks

The authoritative review procedure is [404s & Redirects](../rules/redirects-404s.md).
Read and maintain that sheet for classification, decision-making, development-name
exceptions, verification and completion requirements. This document explains the
existing implementation and retains historical checks; it is not a competing run sheet.

Unit mappings live in `src/data/units/<unit>/url-migration.json`. The shared Eleventy
build writes redirects after content pages are built. Redirects are generated output,
not editable content pages. Internal destinations honor SITE_PATH_PREFIX; confirmed
external HTTPS destinations preserve their URL and query parameters. The build
rejects invalid paths, duplicate sources, chains/loops, missing destinations,
conflicting statuses and attempts to overwrite real content.

Static redirect output uses immediate meta refresh, a production canonical and a
visible fallback link. It is normally an HTTP 200 HTML response, not a server 301.
Existing query/fragment support must be reviewed for the particular legacy URLs;
path redirects alone do not establish query-string handling.

## Historical SSRI results

These results describe the earlier SSRI implementation, not current certification.

SSRI: ten confirmed moves enabled, including RTRF FY2019 to the user-confirmed
external Looker Studio replacement.
Build, all nine output checks, prefix handling, escaping, stale cleanup and failure
safeguards passed. Regular-page SEO checks pass (one existing long-title advisory).

Local browser verification passed: /hcri/ immediately reached /research/hcri.html;
an unknown URL returned the custom page with HTTP 404.

External HTTPS destinations are supported when a replacement is confirmed. Their
URL (including query parameters) is preserved and never receives the preview prefix.
