# GEO consumer migration completed

Use the paired GEO project from this same archive. It requires shared schema version 2. Older department builds that expect the previous copied-source layout must be migrated separately before using this shared revision.

## Direct source integration

- GEO's shared.config.json selects unit geo and defaults to sibling ../css-shared.
- scripts/shared-source.mjs verifies the shared schema, reads selected unit JSON and UH JSON, rejects source collisions, and records a build receipt.
- No shared stylesheets, templates, JSON, scripts, or branding graphics are copied into GEO/src.
- Eleventy dir.includes is GEO/src/includes for local biography fragments. dir.layouts points to the shared includes directory for base and profile page layouts.
- Nunjucks searches shared includes, shared src for inline media/icons, then local biography includes. Same-name local/shared templates are rejected rather than silently overriding each other.
- Shared public assets and GEO public assets merge into output assets/media. Same-name files are rejected. README files and Finder metadata are excluded from publication.
- CSS imports shared css/common.css followed by GEO src/css/geo.css, then rewrites asset URLs relative to root-level geo.css. It retains the copied font preload path.
- GEO canonicalSections configuration replaces the two repeated undergraduate/graduate directory JSON files while preserving their canonical URLs.

## Centralized records

The original nine GEO JSON datasets were moved, retaining their content and relationships. students.json became graduate-students.json, lectures.json became events.json, and faculty_heroes.json became faculty-heroes.json. Runtime aliases preserve current templates. Privacy and webmaster settings moved from site.json into shared UH footer.json. All image paths were updated to the renamed media folders. Hero assignments now contain full image paths and explicit accessible descriptions.

No staff dataset or new department facts were invented. The unit logo collection and shared hero photographs still need to be supplied.

## Retired development material

Removed from GEO:

- Generated shared mirrors and generated ignore lists.
- Old sync-shared.mjs, adopt-shared.mjs and remove-retired-includes.mjs.
- One-time download-student-photos.mjs; the supplied student data already references local photographs, which are retained.
- Unreferenced graduate-how-to-apply draft include.
- Unused heroImages.js gallery helper.
- Superseded page-level fallback hero fields, all covered by central assignments, and the unused media/dev placeholders.
- The already-incorporated geo-buttons.patch.

Removed the superseded css-shared-buttons.patch from shared. Kept other supplied department assets, even when they might be unused; identifying unrelated asset deletions is outside this migration.

## Remaining work

- Review responsive appearance on desktop, tablet, and phone.
- Add approved unit/college logos and shared hero photographs.
- Build the style-guide footer showcase later using the real shared footer.
- Review repeated university footer links and other design/content cleanup separately.
- Validate actual GitHub publication after installing the paired projects. No remote repository was modified or deployed here.

See the archive's INSTALL.md for exact replacement locations. Preserve repository .git directories.
