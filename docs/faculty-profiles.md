# One shared faculty biography layout

SCI's people-only phase uses the same layout and one shared `people.json` array.
Its five-program directory selects the same records using a `programs` ID array;
it does not copy records or introduce program-specific bio templates. Optional
`affiliations` are labeled links in the existing supplemental sidebar. See
`sci-migration.md` for source review and the deferred full-site scope.

Effective November 10, 2026: GEO, PUBA, PSY, SOC, SSRI, and future faculty biography
pages use exactly `layouts/profiles/faculty-profile.njk`. It has no unit-specific
or portrait-only layout branches. This replaces the earlier first-pass designs.

## Page and data ownership

POLS now pilots one centralized `people.json` array for faculty and staff. Its
visibility flags select the faculty directory and mixed Key Contacts grid, while
individual bios resolve the same record. `faculty.json` no longer exists for POLS.
Other units keep the legacy data contract below until their approved migration.
Faculty directory and Key Contacts share `people-grid.njk` and `profile-card.njk`;
all grid sizing, gaps, and card markup are maintained once. Photos are optional;
staff without a profile URL receive no bio link.

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

An explicit `url: null` in a person record disables the biography link while
retaining their photo, name and details in the directory. Do not generate a bio
for that person. The legacy inferred URL applies only when `url` is absent;
an intentional null must never be replaced with a guessed URL. WGSS's L. Ayu
Saraswati uses this opt-out, at the user's direction.
Hover/focus underline rules must target anchors with an href; never style the
unlinked identity wrapper as an interactive link.

The layout uses `shell.njk`, an explicit page section/container, and one responsive
row. Left: `col-12 col-md-4 profile-sidebar`. Right:
`col-12 col-md-8 profile-biography`. Shared CSS sets desktop widths to 20%/80%
from 1600px, matching the approved smaller portrait treatment. Narrower widths use
4/8 from 768px; columns stack below 768px, with the portrait at 75% of available width and
left-aligned. Text stays full width. This applies to every unit's faculty bio.

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

## Bio divider standard (November 12, 2026)

Individual faculty bios omit an HR before the first main-biography H2; later
main-content H2 dividers remain. This is an exception to the SSRI main-content rule.
The shared bio sidebar uses profile-contact-divider (1px, margin .75rem above and
.5rem below) between titles and office, before email/phone, and before each visible
supplemental section (websites, publications, awards, affiliations/additional links).
No empty sections or dividers. The office divider applies to bios and all shared directory/contact profile cards.
