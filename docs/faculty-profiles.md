# One shared faculty biography layout

Effective November 10, 2026: GEO, PUBA, PSY, SOC, SSRI, and future faculty biography
pages use exactly `layouts/profiles/faculty-profile.njk`. It has no unit-specific
or portrait-only layout branches. This replaces the earlier first-pass designs.

## Page and data ownership

Each faculty member retains an individual HTML source file in the site repository.
Front matter owns `title`, `description`, `permalink`, and `personSlug`:

```yaml
---
layout: layouts/profiles/faculty-profile.njk
title: "Example Person"
description: "This will be the meta description."
permalink: "/faculty/example-person.html"
personSlug: "example-person"
---
```

The HTML body contains the biography sections, starting with headings such as
Background or Awards. Do not add a second H1, inline headshot, or duplicate contact
block: the shared sidebar provides the portrait, name H1, and identity details.

`src/data/units/<unit>/faculty.json` in shared supplies the same record to both
the directory card and bio sidebar. Portrait path/dimensions, academic title,
`roles`, office, email, phone, keywords, websites, additional links, awards, and
publication links belong in that record. Optional missing fields are omitted from
the output; do not invent details merely to fill a card.

`resolveFacultyPerson` in `scripts/unit-site/faculty-profiles.mjs` is the single
record resolver. The common unit build calls it through computed data. GEO's
legacy directory-data helper imports that same resolver through its configured
shared source. It is not a separate page layout or record-lookup implementation.
Missing referenced records fail the build. Retired `profilePhoto` metadata and
`profile-portrait.njk` must not be reintroduced.

When a name changes, update the shared name and the page's local title/description
as appropriate. Image replacements and contact updates need only the shared record,
not separate bio and directory photo metadata. URL changes must update the source
permalink, record URL/slug, relevant links, and migration inventory.

## Shared presentation

The layout uses `shell.njk`, an explicit page section/container, and one responsive
row. Left: `col-12 col-md-4 col-lg-3 profile-sidebar`. Right:
`col-12 col-md-8 col-lg-9 profile-biography`. They stack below 768px.

`profile-sidebar.njk` and `profile-identity.njk` render the same sidebar structure
for every unit. Portraits use `photo-style profile-photo`. Office is plain text;
email and phone use the shared linked icon treatment. Keywords are omitted from
both bios and directories. Supplemental groups use `websites`, `publicationProfiles`,
`awards`, and `additionalLinks`; omit empty groups and render awards without links.
There is no permanent vertical separator; diagnostic guides remain independently
controlled by each unit's `layoutGuides` setting.

Unit content and hero imagery can differ; the bio template cannot. GEO retains
its person-specific satellite heroes. PSY, SOC and PUBA retain their assigned
Saunders murals. GEO faculty and staff portraits are centralized under
`src/media/units/geo/faculty-staff/`; both JSON records and ordinary GEO page
references use that shared location.

## Completed migration and verification

All 51 individual profiles migrated: GEO 10, PSY 21, SOC 14, PUBA 6. Metadata stays
in HTML. Background-and-beyond biography source text is unchanged. SOC personal and
publication links moved into shared records, while teaching awards remain in the
biography. User-provided current SOC contact data supersedes the old inline block.

All four builds, existing PSY/SOC checks, and shared checks passed. Checked all 51
profiles for one H1, one shared-style portrait, common column markup, and sidebar
values matching shared records. Confirmed GEO hero records were unchanged. No browser
visual review or deployment is implied.
