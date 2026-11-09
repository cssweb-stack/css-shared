# Academic course resources

`src/includes/layouts/content/course-resources.njk` renders the gray rounded panel
with Class Availability, Course Descriptions, and UH Mānoa Catalog buttons. Links are
read directly from JSON; the former `site.courseResources` assembly is retired.

- Shared Class Availability and Course Descriptions URLs: `src/data/common/links.json`.
- Catalog URLs: `src/data/common/uh-catalog.json`, one record per unit.
- Unit prefix and catalog reference: `src/data/units/<unit>/catalog-courses.json`.

For PUBA the unit file contains:

```json
{
  "prefix": "PUBA",
  "catalogKey": "publicAdministration"
}
```

GEO uses `GEO` and `geographyAndEnvironment`. Other units can adopt the same shape
as their panels are added. Course Descriptions links to the unfiltered main page
and shows `(filter by prefix PUBA)` or the configured unit prefix. No filtered
per-unit Course Descriptions URL is required. Existing direct `catalog` records
remain supported if no `catalogKey` is supplied. Units without a catalog record
render the two shared links until one is configured.

PUBA Courses, both Graduate Certificate pages, and the MPA landing page place
this include in their own explicit bottom section:

```html
<div class="page-section">
<div class="container content-section">
<div class="row gx-0 gx-sm-5 gx-lg-5">
<div class="col-12">
{% include "layouts/content/course-resources.njk" %}
</div>
</div>
</div>
</div>
```

The include supplies the panel and responsive button grid; the page owns the
outer section/container/column structure. Three buttons sit alongside each other
from tablet width, with equal heights; they stack on phones. Existing GEO panels
also use the common URLs and its catalog reference. PUBA and GEO builds, shared
checks, and generated link/section checks passed. The catalog blocks automated
web fetching (403), so the supplied URL is preserved without claiming an external
HTTP verification.

Chrome verified no page/text overflow and buttons contained in the panel at
375, 820, and 1440px, with equal button heights on tablet and desktop.
Measurements: `exports/puba-course-resources-2026-11-09.json`.

Catalog display text comes from each record's `label` in `common/uh-catalog.json`,
e.g. `UH Mānoa Catalog (PUBA)` or `(GEO)`, without an academic year. All catalog
records have labels; records without a separate unit abbreviation use their
existing program name in parentheses. Original names and destination URLs stay
unchanged. A direct legacy unit catalog record without a label falls back to
`UH Mānoa Catalog (<unit short name>)`.
