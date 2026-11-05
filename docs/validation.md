# Validation of the paired migration

## Completed

- Installed GEO's dependencies from its updated lockfile with npm ci.
- Shared npm run check passes.
- Clean GEO builds pass at / and /geo/.
- The workflow's SHARED_SOURCE location inside GEO/.shared-source was exercised successfully with /geo/.
- All 32 generated HTML pages retain the baseline parsed content, attributes, links and heading IDs after accounting for renamed asset URLs and path-prefix changes.
- Every local image, stylesheet, script and page-link target referenced by the generated pages exists. All CSS url() targets resolve.
- JSON, Nunjucks templates, CJS formatters and biography source fragments are not published as standalone pages.
- Shared code is not recreated inside GEO/src. A duplicate shared/local asset was deliberately introduced and correctly rejected before building, then removed.
- A temporary shared hero image was published and assigned to the homepage; its own alt text and suppressed attribution rendered correctly, while other GEO imagery retained its attribution. Test data and images were then removed.
- All nine original department JSON datasets retain their content. Image paths are migrated; explicit hero alt text preserves the previous accessible descriptions. Privacy and webmaster settings are moved to shared footer JSON; canonical-section settings are centralized.
- Live development preview was exercised with shared JSON and footer template edits and both restores. Watcher behavior passed with native filesystem notifications and polling.
- Root .github workflows remain unchanged from the uploaded projects. No remote deployment occurred.

## Preview dependency compatibility

The installed Eleventy glob-watcher wrapper did not register watched directories when Eleventy remapped external shared paths through a relative parent cwd. A targeted package override uses the API-compatible chokidar 3.6.0 watcher under that dependency name. Preview tests confirmed detection of shared JSON/template edits after this change. This avoids adding a source mirror or custom watcher script.

## Still requires user review

- Visual appearance on actual desktop, iPhone and iPad browsers.
- GitHub Pages publication after the paired repositories are installed and pushed.
- The new unit/college logo collection and shared hero photographs, which were not in the supplied archive.
- Other departments and the style-guide footer showcase.

No layout redesign, degree messaging changes, external-link audit, or blanket accessibility-conformance claim is included in this source migration.
