# Shared faculty directory grid

Current standard, locked November 11, 2026: `faculty-directory.njk` delegates to
`people-grid.njk`; POLS Key Contacts uses that same grid and profile cards. Five
equal columns at 1600px+, four at 1200–1599px, three at 992–1199px, two at
768–991px, one below 768px. This supersedes the three-stage trial after measured
contact-text crowding. Mobile photos use 75%
of the column width, left-aligned, while text remains full width.
Keep normal shared gaps. Text sizing and individual bio portraits are separate
follow-up decisions. POLS reads its unified people.json; other units retain their
existing faculty data until migrated. The original implementation history below
does not supersede this current standard.

Established November 10, 2026. The main faculty landing pages for GEO, PSY, SOC,
and PUBA include `layouts/profiles/faculty-directory.njk` from shared.

The directory is separate from the individual biography layout
`layouts/profiles/faculty-profile.njk`. Develop directory presentation in the shared
directory include rather than copying a grid into every site's HTML page.

## Data and behavior

Each unit has `src/data/units/<unit>/faculty.json` in shared. Initial records for
PSY/SOC/PUBA contain `name`, `lastName`, `slug`, `url`, `photo`, `photoWidth`, and
`photoHeight`. The directory sorts by `lastName`; explicit surname fields handle
compound names such as Auelua-Toomey. Images link to local individual profile pages
through the shared `url` filter, using actual portrait dimensions and shared
`photo-style`. The image-only links use each person's name as their alt text.

PSY/SOC/PUBA retain their existing text-link lists below the portrait grid. Further
visible names, titles, phone numbers, and directory details remain future work.

GEO uses the same include with `facultyDirectoryDetails = true`; it renders the
existing shared `profile-card.njk` within the new grid. This preserves GEO's names,
roles and contact details, and reuses its existing faculty data
and local portrait paths. GEO portrait centralization has not been performed.
Neither directory implementation changes any hero assignments.

## Layout

The shared Bootstrap row uses `gy-4 gx-0 gx-md-5` and
`row-cols-1 row-cols-md-2 row-cols-lg-3 row-cols-xl-4` with equal `col` children;
shared CSS enables five 20% columns from 1600px.
Existing image cards stretch to their column width through a scoped
rule in shared `profile.css`. The existing GEO flex directory remains available
for other consumers; this change does not rewrite Associated Faculty pages.

## Editing

Keep individual page title, description, permalink, and `personSlug` in the HTML
source. Portrait and contact details live only in the shared faculty record, used
by both this directory and the unified bio layout. Update page metadata too when
changing a name or URL. See `faculty-profiles.md` for the editing contract. The
explicit faculty record lists only faculty who should appear, not every HTML page
under the faculty folder.

Checked all 51 linked portraits: PSY 21, SOC 14, PUBA 6, GEO 10. Builds pass for all
four; PSY/SOC existing validation and shared checks pass. Directory output was checked
for alphabetical order, responsive column classes, image/link targets, shared image
styling, and preservation of GEO names/emails and other sites' text lists. No browser
visual review or deployment is implied by these build checks.

## Two-section landing page

Each of the four main faculty HTML pages uses `shell.njk` and explicitly owns two
sections: title/brief introductory paragraph on white, then the directory include
inside `page-section page-section--gray`. The gray section is outside its contained
content width, so its background spans the screen while the portrait grid stays
aligned to normal content columns. Working text lists remain in that gray section.
GEO now owns these sections explicitly too; its directory cards retain their details.
Individual faculty biography pages are not changed by this directory treatment.

Directory cards omit research keywords; those remain in data and appear on
individual profiles. Office rows use plain text; email and telephone retain their
linked icons. Linked names inherit the standard shared blue link styling.

PUBA now has populated academic titles, offices, emails and phone numbers. The shared
directory selects detailed cards automatically when a record has these fields;
GEO's explicit detail flag remains supported. `roles` is an optional array for
multiple administrative titles (Helen H. Yu: Director and Graduate Chair). Legacy
single `role` remains supported. Do not invent administrative roles for other people.

## Required landing-page location

Core faculty lives at `src/faculty/index.html`, published as `/faculty/`, across
all units. Associated/emeriti pages live beside that index. Check this convention
when creating or reviewing a unit. Preserve old URLs through the shared migration
mapping when standardizing existing exceptions.

Primary faculty landing-page display labels use `[UNIT] Faculty`, not Core Faculty:
match the dropdown item, H1 and page title. File remains faculty/index.html and
public URL /faculty/. Applied to PUBA; check other units during their review.
