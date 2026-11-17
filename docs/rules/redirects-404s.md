# 404 and redirect review

This is the authoritative procedure for reviewing legacy URLs, redirects and 404s.
Read it before starting this work. Website Build Rules owns current filenames and
folders; this sheet owns what happens to actual old public addresses. Technical
implementation notes and past unit reports do not override these rules.

## Establish the scope

- Use the original public website export and any supplied URL inventory as evidence.
  Preserve source documents unchanged. Identify the selected unit and current routes.
- Separate actual legacy public URLs from development-only filenames. Renaming a
  non-indexed development page does not require a redirect. Do not create mappings
  merely to preserve intermediate development names.
- Inspect existing mappings before editing. Preserve unrelated and user-approved
  decisions; do not delete or redirect content just because it was not migrated.

## Classify every original public URL

- Unchanged: the current page still serves that address.
- Moved or merged: a confirmed replacement serves the same relevant content.
- Retired: the page is intentionally gone and should return the standard 404.
- Unresolved: content, identity or destination needs a decision. Ask the user;
  do not silently retire it or guess a replacement.

Use exports and current content to establish matches. Do not send unrelated missing
pages to the homepage or faculty directory as a blanket fallback. A directory,
section, external URL or page fragment is a replacement only when supported by the
content or an explicit user decision. Preserve meaningful fragments and query-based
legacy addresses when the evidence requires them; do not invent blanket handling.

## Keep one mapping source

- Store unit mappings in `src/data/units/<unit>/url-migration.json`, using the
  existing redirects, retired and unresolved structures. Existing supported query
  and fragment mappings belong in that same system; do not invent a parallel one.
- Redirect directly to the final destination. No chains, loops, duplicate sources,
  conflicting statuses, missing targets or overwriting real pages.
- Internal destinations use root-relative paths and the existing deployment-prefix
  handling. Confirmed external HTTPS destinations retain their URL and parameters.
- Update current navigation, internal links, hero mappings and route inventories to
  the final addresses; do not make current links depend on legacy redirects.
- The shared build generates redirect output. Do not create editable redirect
  content pages, navigation items, search entries or sitemap entries for redirects.
- Keep genuine legacy mappings until a deliberate review authorizes their removal.

## Use the shared 404

- Each unit uses root `/404.html`, the shared `pages/not-found.njk` include and
  `isNotFound: true`. Keep unit metadata local and recovery links in the central
  unit `not-found.json`; reuse the established layout and accessibility treatment.
- The 404 must be noindex, with no canonical to the homepage or another page.
- Retired and unknown addresses must remain missing requests, not redirect to a
  normal homepage or a manufactured success page. A retired-list entry alone does
  not remove an existing content page; inspect and remove only authorized sources.
- Do not add a 404 page to ordinary navigation. Recovery links must lead to real,
  helpful current pages.

## Check the result and report honestly

1. Read the completed original-to-current comparison. Every original public URL
   needs a classification; list unresolved decisions rather than claiming completion.
2. Build the affected unit. Inspect changed redirect outputs and final destinations,
   including relevant prefixes, fragments, Unicode or query cases when present.
   Confirm the shared 404 has the expected content and indexing directives.
3. Rebuild Review when its redirect/404 or page listings are affected. Check those
   generated listings against the actual current routes and classifications.
4. Test missing and moved requests on the available host. A generated HTML file
   does not prove an HTTP status. Local results do not prove preview or production
   behavior. After authorized publishing, check the deployed host separately.
5. Report remaining decisions and failed or unperformed checks first. Distinguish
   local, committed, pushed and deployed work. Do not claim server-level 301s:
   the existing static implementation uses immediate HTML meta-refresh redirects
   with canonical and linked fallback, normally served as HTTP 200. Missing requests
   must return actual HTTP 404 on the deployment host.

Use targeted checks and stop when the changed behavior is covered. This procedure
is not permission to deploy, change hosting, enable indexing, install tools or
rewrite all site routes.

## Maintain this rule sheet

Add, remove or revise rules here as decisions are agreed during work. Replace
superseded instructions rather than keeping competing versions. Ask about uncertain
content or consequential new decisions; implement already-authorized decisions.
Before declaring completion, compare the actual work against this sheet. A passing
build alone is insufficient. Keep unit findings in the current local handoff;
historical reports record past work and do not certify the current site.

Technical references: [URL migration implementation](../shared/url-migration-audit.md)
and [shared 404 component](../shared/not-found-pages.md).
