# Content layout audit — November 8, 2026

Scope: SSRI page source, shared content layout rules/templates, and general-grid
usage in the available GEO and style-guide consumers. This was a source audit,
not browser verification. No layout migration was performed.

## Findings

- SSRI's six content/sidebar pages consistently use Bootstrap rows and columns.
  Bootstrap controls their outer widths and 992px wrap threshold.
- The research listing and shared unit-contact component also use Bootstrap.
- Shared sidebar-resources-grid uses CSS Grid inside a Bootstrap column. It does
  not replace the outer row display or Bootstrap column widths. It provides the
  reviewed equal-width resource groups, including an empty track for one item.
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
