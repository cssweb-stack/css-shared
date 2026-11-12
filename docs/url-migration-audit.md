# URL Migration Audit

Final unit review sequence: Accessibility Audit, SEO Audit, URL Migration Audit.

Keep unit mappings in `src/data/units/<unit>/url-migration.json`. Classify original
URLs as unchanged, moved/merged, retired, or unresolved. Verify replacement content;
never guess a destination. Preserve original URLs where practical.

```json
{
  "redirects": [{"from": "/old/", "to": "/new.html", "label": "Full page name"}],
  "retired": [],
  "unresolved": [{"from": "/historical-report/", "note": "Decision needed"}]
}
```

The shared Eleventy build generates redirect HTML directly in `_site` after real
pages are built. There are no redirect source pages, navigation entries, or Eleventy
collection entries. Keep redirects out of sitemap/search indexes. Build cache lives
under ignored node_modules/.cache; stale generated files are removed on rebuild.

Redirects use zero-second meta refresh, a production canonical, and a visible linked
fallback. These are HTTP 200 HTML responses, not server-level HTTP 301 responses.
[Google interprets instant meta refresh as permanent redirects](https://developers.google.com/search/docs/crawling-indexing/301-redirects).
Server redirects remain preferred if hosting eventually supports them.

Destinations are root-relative and honor SITE_PATH_PREFIX, so local and GitHub
project previews stay on their current host. Canonicals identify production URLs.
No production-domain switch is needed to test navigation. The build rejects invalid
paths, duplicate sources, chains/loops, missing destinations, conflicting statuses,
and overwriting real pages. Other units opt in by adding their own mapping.

## Verification and launch

1. Build; verify generated old paths contain immediate refresh, canonical and fallback.
2. Open old URLs locally and on the GitHub preview; confirm the final page and URL.
3. Open an unknown URL; confirm custom 404 content and genuine HTTP 404 status.
4. After the domain switch, repeat on production. Submit current-page sitemap and
   monitor Search Console. Local tests cannot prove production hosting behavior.

Keep mappings until a deliberate review; do not automatically expire them after a
year. Retired/unresolved URLs receive the custom 404 unless a real page still exists.
The helpful 404 retains primary quick links; moved-page listings are omitted.

SSRI: ten confirmed moves enabled, including RTRF FY2019 to the user-confirmed
external Looker Studio replacement.
Build, all nine output checks, prefix handling, escaping, stale cleanup and failure
safeguards passed. Regular-page SEO checks pass (one existing long-title advisory).

Local browser verification passed: /hcri/ immediately reached /research/hcri.html;
an unknown URL returned the custom page with HTTP 404.

External HTTPS destinations are supported when a replacement is confirmed. Their
URL (including query parameters) is preserved and never receives the preview prefix.
