# Content layout audit — November 8, 2026

Historical audit with subsequent changes below. For the current consolidated
CSS review and measurements, see `css-audit-2026-11-08.md`.

Scope: SSRI page source, shared content layout rules/templates, and general-grid
usage in the available GEO and style-guide consumers. This was a source audit,
not browser verification. No layout migration was performed.

## Findings

- SSRI's six content/sidebar pages consistently use Bootstrap rows and columns.
  Bootstrap controls their outer widths and 992px wrap threshold.
- The research listing and shared unit-contact component also use Bootstrap.
- Shared sidebar-resources-grid now uses a Bootstrap row with responsive child
  columns: stacked on phone/desktop, equal halves on tablet. A single child
  retains its half-width tablet column.
- The content-sidebar tablet divider explicitly resets the sidebar's Bootstrap
  top gutter and the preceding content's trailing spacing. This is an integration
  override, not evidence of a broken layout, but it must remain centrally scoped.
- The shared .container overrides Bootstrap container geometry intentionally for
  college-wide content width and gutters. This affects all consuming sites.
- A broader architectural overlap does exist: layout.css also defines generic
  grid-two/three/four/five classes. GEO actively uses grid-two, grid-four, grid-five,
  and grid-welcome; shared course-resources uses grid-two. These coexist with
  Bootstrap's general column system. They cannot be deleted safely as unused CSS.
- People-directory grids align structured directory records. They are a component
  concern and were excluded from changes as requested during the SSRI review.

## Direction

Use Bootstrap as the standard for general page columns and responsive gutters.
Keep shared styling for typography, section backgrounds, image treatments and
component-specific behavior. Do not create another generic column utility family.
The existing generic custom grids need a separate migration to Bootstrap, with
GEO and shared consumers checked before removing old definitions. Special behavior
such as centered incomplete card rows must be retained deliberately.

Do not rewrite the accepted SSRI layouts during the content review merely because
CSS Grid occurs within a component. A future decision to implement all component
columns with Bootstrap should include sidebar single-item half-width behavior,
container-relative wrapping, and directory alignment in its migration criteria.

## Required content/sidebar gutter

All content/sidebar rows use Bootstrap `gx-lg-5` (3rem horizontal gutter from
992px upward), across sites. No page-specific desktop gutter variants. SSRI's
homepage, HCRI, HAM, OENAS, TASI/PHIDC, and Grant Development now all use it.
Smaller-screen gutters and vertical component gaps remain separate settings.

## Alignment standard

Content is flush left, including office blocks, sidebar resources, faculty
profiles, profile directory cards, portraits and personal links. Use no centered
content variants for these components. SSRI's homepage graphic callouts are an explicitly centered exception.
Language navigation in the footer is left aligned; legal subfooter text is centered.
Shared header/footer alignment is still a separate review area.

The shared unit-contact office now wraps its photo, heading and address in
`sidebar-group`, inheriting the same detail spacing as research contacts.
Bootstrap office/map columns are 4/8 at md (768px), returning to their existing
3/9 at lg (992px). At phone widths they remain stacked. The row uses gx-lg-5.

## Footer alignment follow-up

The shared footer outer columns now use Bootstrap row/col classes and gx-lg-5,
matching content's 992px layout threshold. Its container geometry and upper
section padding share content's settings. The former 900px outer grid and
525px mobile centering rules were removed. See `docs/footer.md` for the current
width/breakpoint map and browser verification results. Internal link lists and
language components retain their dedicated presentation rules.

Centered graphic callouts are an explicit reusable exception to flush-left
content: `graphicCallout` in `layouts/content/graphic-callout.njk` uses existing
Bootstrap alignment utilities. SSRI's two homepage SVG promotions consume it;
contact and profile components remain left aligned. No new CSS was added.

Content/sidebar width constraint: the sidebar must never be narrower than
3 of Bootstrap's 12 columns. Maximum main/sidebar split is 9/3; no 10/2 variant.
Research detail and Grant Development rows retain 8/4 at lg and use 9/3 from
xl upward, including xxl. The homepage already uses 9/3 from lg. Below lg
they remain stacked. This standard applies to future content/sidebar designs.

## Unified Bootstrap gutters

All actual Bootstrap rows in available shared templates, SSRI, GEO and style-guide
source now use gx-0 gx-sm-5 gx-lg-5: no horizontal gutter below 576px, 3rem from
576px upward. Old gx-3/gx-4 variants are removed; vertical gutter choices remain
separate. This aligns research/media row outer edges with the upper footer grid
and keeps nested row gutters consistent. No new gutter CSS is introduced.
Chrome verified all seven SSRI research rows against footer grid left/right edges
at ten widths (320–1920px): every pair matched, without footer overflow. Results:
exports/content-footer-grid-edges-2026-11-08.json. All three builds passed.

## Single-column content sections

SSRI Research/Directory/Contact opening sections, both Research Services and
Fiscal Compliance sections, all Directory bands, and Boilerplate's content
now use the same outer/inner/Bootstrap row/col-12 structure. Ten sections across
six pages were wrapped. Existing homepage/research-detail/Grant Development
grids and the office/map and research listing grids were not rewrapped.
Boilerplate's long-form class moved to the column so its direct-heading rule
continues working. Shared column edge normalization now applies to every
primary row, not only content-sidebar. No new page-specific padding rules.
Chrome checked 18 page/width cases (375/820/1440px): matching footer row edges,
3px diagnostic column borders and zero last-child margins. Results:
exports/single-column-sections-2026-11-08.json. SSRI build/shared checks passed.
