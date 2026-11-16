# Shared grid review

November 16, 2026. Baseline review, not the final grid specification.

## Scope and review page

Inventory SSRI, PUBA, ES, ANTH and SOC before changing their layouts. The general-layout baseline identifies 28 signatures; these are not 28 approved grids. The user
likes their general behavior and wants a smaller, dependable set of named layouts
with consistent responsive spacing. Preserve that behavior while identifying
accidental differences; do not treat every existing variation as intentional.

Review's `/grids.html` displays the current arrangements in one place. Its colored
cells use production classes and shared CSS. All sidebar examples use the same
user-supplied Sidebar and Content area paragraphs, including arrangements that
normally contain images, maps or resources. Their column classes remain intact;
the image/text macro is intentionally not used for these text-only specimens. No specimen CSS defines columns, grid gaps or breakpoints.
Seven items exercise incomplete card/tile rows. Nested program-button examples
retain their sidebar context. Headings identify patterns; expandable details list
the consuming pages. A small script reads current widths and gaps without changing
the layout. Labels are descriptive baseline names, not approved API names.

Review is divided into four tabs, with the most widely reused patterns first:
Sidebars (including faculty bios), Equal Columns, Cards & Tiles (including portrait
grids), and Combined Layouts (homepages, advising and nested button groups).
Tabs support arrow keys, Home/End and direct group links. Hidden groups are not
measured until displayed; without JavaScript all groups remain visible. The
browser audit opens every tab at phone/tablet/desktop widths, checks keyboard
navigation, then expands all groups for its geometry sweep and screenshots.

The inventory reads all 218 explicit HTML content sources and their current built
main-content markup, including shared includes and profile layouts. Build the five
sites before rebuilding Review. Missing output fails explicitly. Existing outputs
are not automatically certified fresh; rebuild after changes to units or shared
components. Header/footer grids, navigation, internal icon/text alignment and
single-column spacing stacks are outside this page-layout inventory. Responsive
data tables and record directories are excluded from this page and reviewed as
independent systems. The initial inclusion of these specimens is superseded by
the user’s scope clarification. Portrait/card grids and contact office/map columns
remain in scope.

## Findings

- Bootstrap rows and native CSS grids currently coexist. Equivalent purposes do
  not always share gutter values or responsive transitions.
- Profile rows use a 16 px horizontal gutter at 768–991 px, while most comparable
  multi-column Bootstrap rows use 48 px. Both use 24 px vertical gutters. These are
  observed default-size values, not a newly accepted spacing scale.
- Card grids vary:1/2/3/4/5 people columns,1/2/4 cards with different transition
  widths, and the deliberately agreed 1/3/5 tile grid. Evaluate fit before merging.
- The two media-left wide variants differ at 1600 px: square 17/83, landscape 20/80,
  wide 25/75. The reverse variant retains 75/25 text/image. These may become one
  component with named proportions rather than independent grid systems.
- Advising combines an outer paired-person grid (48 px gap) with an inner photo/text
  grid (24 px gap); its inner proportions change at 1200 px. Program buttons also
  change behavior inside sidebars. Preserve nesting in tests.
- Course-resource buttons use 16 px gutters and container-width transitions;
  they need room for labels rather than a device-name assumption.
- Flowing lists retain down-column reading order. Record directories and responsive
  data tables have separate alignment/record semantics and are outside this review.
- General page geometry lives mainly in `src/css/layout.css`, with profile/contact
  sizing in `src/css/profile.css` and resource-button rules in `src/css/callouts.css`.
  Record directories live in `src/css/people-directory.css`; traditional/responsive
  data tables, including NASPAA requirements, live in `src/css/tables.css`. All
  are imported by `common.css`, but their selectors and maintenance are separate.
- Several older `.grid-*` definitions have no consumers among these five sites.
  That does not prove they are unused by GEO, PSY, POLS, SCI, WGSS or other
  consumers. Do not delete them without checking those consumers.

## Proposed consolidation for review

These are proposals only. No new proportions, gap values or breakpoints are
approved by this baseline work.

| Candidate family | Existing patterns | Proposed treatment |
| --- | --- | --- |
| Sidebar | Profiles, logo/text pages, office/map, student rows,404 | One left/right component; named proportion variants only where needed. Resolve the tablet gutter discrepancy. |
| Media row | Square, landscape, wide and reversed image/text rows | Keep the existing shared macro; consolidate its proportion vocabulary with Sidebar where practical. |
| Equal items | Portrait cards, program/photo tiles, image rows and resource buttons | Shared spacing tokens and named column-count presets. Preserve the agreed five/three/one tile behavior pending an explicit change. |
| Composite | PUBA homepage, ES introduction/program tiles, advising | Compose shared arrangements; retain a special preset only for a demonstrated content need. |
| Flow list | Two-column course/research lists | Keep its down-column reading order; share the appropriate spacing token. |

Next: visually review this baseline, agree the compact arrangement/spacing table,
then implement shared rules and migrate the five sites. Remove superseded CSS
only after checking all consumers. Save approved visual baselines after that
agreement; today's screenshots record existing behavior, not the desired final
standard.

## Repeatable checks

Review supplies `npm run audit:grids`, using its Playwright Core and axe-core dev
dependencies. It reads built local files through browser request routing; no test
server is needed. `GRID_BROWSER` can select a Chrome/Chromium executable; the
default is the standard macOS Chrome installation. `GRID_BOOTSTRAP_CSS` can select
a cached copy of the exact Bootstrap 5.3.3 stylesheet for offline checks.

The audit records breakpoint-boundary measurements, overflow, representative
consumer comparisons, browser errors and automated accessibility findings under
`exports/grids/` in this shared repository. It compares real horizontal/vertical
layout rules and first-column width ratios with specimens. It also captures full-page screenshots
at 375,820,1180 and 1800 px. Headless Chrome does not replace physical iPad/Safari
review or establish full accessibility conformance.

Review is a separate Git repository connected to `cssweb-stack/review`. Its
generator/config/package changes must be committed and pushed alongside shared
source when transferring machines; committing css-shared alone will not save them.

Earlier November 16 verification (before scope narrowing):34 specimens at 18 viewport widths,170 representative
consumer comparisons passing, no page overflow, browser errors or axe violations.
Review build, source syntax, links/assets/anchors/IDs and shared checks passed.
The Review route returned HTTP 200 and a saved/restored CSS probe automatically
reached the running server. Screenshots were inspected for the tablet sidebar;
physical Safari review remains outstanding. No five-site layout changes or
publication performed.

After tab grouping: the 28 general-layout specimens pass12 tab-state checks at
375/820/1800px, keyboard navigation,18 geometry widths and140 consumer comparisons.
No page overflow, browser errors or automated axe violations were found. The audit
expands groups only for its all-specimen measurements/screenshots; normal review
shows one group at a time. Evidence: `exports/grids/review-grid-audit.json`.
