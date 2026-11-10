# Accepted project conventions

Established November 10, 2026 (Pacific/Honolulu). These are working agreements,
not a claim that every older file has already been migrated.

## Scope and ownership

The current five site directories are `geo`, `puba`, `psy`, `soc`, and `ssri`, beside
`css-shared`. `style-guide` documents the shared system. Keep shared layouts,
styles, assets, and reusable content in `css-shared`; keep page sources in their
site repositories. Consult existing topic documentation before making changes.

## Folder names

Use lowercase repository folders. Psychology's local folder is `psy`, formerly
`PSY`. Avoid introducing absolute paths tied to one computer.

## Page sources and metadata

Every published content page has its own HTML source file with YAML front matter
containing explicit `title`, `description`, and `permalink` values. Faculty profiles
follow the same editing convention as ordinary pages. Do not reintroduce a single
pagination template that owns metadata for all faculty pages.

Titles follow the visible H1 as closely as practical. A homepage gets a descriptive
title based on its H1, rather than “Home.” The shared shell appends ` | {site.name}`;
do not manually add that suffix in the page title. If a page has no H1, retain a
sensible existing title and note the missing heading instead of inventing content
outside the requested scope.

Preserve existing meta descriptions. During the current standardization phase,
missing descriptions use exactly `This will be the meta description.` Do not
replace placeholders with custom copy unless requested. Geography's existing
rendered descriptions are preserved, including its faculty descriptions.

Geography faculty pages now live in `geo/src/faculty/<slug>.html`, containing
metadata and biography content. `faculty.11tydata.js` resolves `personSlug` to the
shared faculty record for the reusable profile layout. Contact details and profile
identity remain shared data; changing a name may require updating that record too.

Each site has `src/privacy.html` with local metadata and an include of the shared
policy body. Keep the policy content shared. Other consumers without this local
page retain the shared generated fallback. GEO still has a retired, ignored
`src/privacy/` source; it is not the published policy.

Existing GEO pages may use `base.njk` and the profile layout; other current pages
use `shell.njk`. Shared layouts remain reusable. The metadata agreement does not
require a wholesale rewrite of older page structure. Includes, fragments, and
nonpublished diagnostic templates are not standalone content pages.

## Site settings and shared components

Hero and Open Graph controls belong in each unit's
`css-shared/src/data/units/<unit>/site-settings.json`.
SSRI retains its mural images, crop positions, compact 145px hero at all three
breakpoints, and green overlay at 0.33 opacity. Its Open Graph image temporarily
uses Puba's `/media/open-graph/puba.jpg`, including Puba's image alt text and
1200 by 630 dimensions, pending replacement by the user.

The shared `course-resources` include places its high contrast buttons directly
on the containing column, without a surrounding gray panel or panel padding.

## Recording decisions and moving between computers

“Lock this down” means record an accepted convention here and implement any
already-authorized supporting changes. Record other clear agreements proactively.
Maintain `docs/work-status.md` for current progress; do not turn it into a transcript.

These files survive closing the editor because they are ordinary repository files.
They travel between machines only when the relevant repositories are committed,
pushed, and pulled (or otherwise explicitly synchronized). Chat availability is
not a substitute for that process. Do not promise automatic memory or syncing.

Before a machine handoff, review Git status in every changed repository, preserve
work through the agreed version-control workflow, and state what has actually been
synced. On the receiving machine, fetch/pull the relevant repositories without
clobbering local changes, then read `AGENTS.md` and the handoff. Shared and site
changes may need to travel together. A shared-source CI configuration pinned to a
remote ref also needs the corresponding shared changes available remotely.

## Sociology and URL migration inventories

Sociology follows the reviewed hierarchy and content merges in
[`soc-migration.md`](soc-migration.md). Treat that approved walkthrough as the
reference when refining SOC. Its feed remains a placeholder until requested.

For site migrations, keep an inventory comparing old WordPress URLs with new
published paths, including unchanged, moved, merged, and unresolved sources.
Review whether URL changes can be avoided before deciding on redirects or removals.
Do not create HTML redirect pages by default; the user explicitly wants to avoid
them. Hosting redirect support is not assumed. An inventory records proposed
mappings and is not evidence that redirects have been installed.

## Hero imagery across sites

Agreed November 10, 2026: unit-specific hero photography is not the default.
Use a common pool of generic student, youth, and campus imagery across sites.
Assign images from that pool to individual pages through their hero JSON records;
shared-pool images should live in shared media rather than be duplicated per unit.
A unit may receive custom imagery when it supplies suitable images or proposes
images that are reasonably obtainable. Do not invent a bespoke visual theme for
every department. Geography's satellite imagery is an existing exception whose
future treatment remains undecided; do not replace it without direction.

The user is collecting images from the College of Social Sciences backup for
possible batch resizing and later assignment. Responsive display heights of
210px desktop / 180px tablet / 150px mobile are a proposed direction, not yet an
instruction to change current settings or resize assets. Choose source dimensions
with viewport width, crop, and display density in mind; display height alone does
not determine the required image resolution.

Geography now explicitly defines hero controls and Open Graph in its unit
`site-settings.json`, including the site URL (moved from `unit-details.json`).
Its preserved standard hero treatment is 210/187.5/90px with transparent overlay,
location labels and attribution enabled. Uses `/media/open-graph/geo.jpg` at
1200 by 630. Shared CSS fallback values remain for compatibility; GEO's explicit
JSON values override them. Page image assignments and credits remain in hero data,
as with other units; do not duplicate them in site settings. GEO's legacy build
registers the same `socialUrl` helper as the common unit build.

Faculty hero treatment is now implemented for Psychology and Sociology: their
`faculty-heroes.json` files contain only individual faculty profile URL assignments
from the Saunders mural pool. Their `heroes.json` files contain all other pages,
including faculty directory landing pages, from `src/media/heroes/students/`.
Selections are randomized once, balanced to reduce repeats, and saved as explicit
paths. Do not shuffle on page load or rebuild. Use “Students at the University of
Hawaiʻi at Mānoa” as the shared-bank description; preserve decorative semantics.

The student bank folder was renamed from `shared/` to `students/`; PSY and SOC
assignments now use that path without reshuffling. PUBA alone uses the fixed
faculty directory images: `/faculty/` uses `/media/heroes/faculty/main.webp` and
`/faculty/associated.html` uses `/media/heroes/faculty/associated.webp`.
These assignments live in PUBA's `heroes.json` and are excluded from randomization.
Correction: GEO was briefly included in this change, then explicitly excluded by
the user. GEO retains its established satellite imagery, including Kaunakakai on
its main faculty directory and Ulaanbaatar on Associated Faculty, with location
labels and inherited satellite credits. Do not apply PUBA directory imagery to GEO.
When retiring bank images, replace all active JSON references before deleting
files; adding an image does not automatically change existing saved assignments.

Faculty profile mural assignments apply to Sociology, Psychology, and PUBA only:
use their separate `faculty-heroes.json` files, with stable randomized choices
from Saunders murals. PUBA's six profiles now use six distinct murals. Retain
existing randomized SOC/PSY assignments unless reshuffling is requested. GEO is
explicitly excluded: its person-specific satellite imagery must stay intact.
PUBA's fixed Main/Associated directory banners remain separate from its profiles.

## One faculty biography template

Effective immediately, all four sites and future sites use exactly one shared
`layouts/profiles/faculty-profile.njk`, with one responsive sidebar/content layout.
No GEO-specific, unit-specific, or portrait-only bio branches. This supersedes
all earlier first-pass portrait layout agreements.

Each individual HTML page retains title/description/permalink and `personSlug`.
The shared unit `faculty.json` record supplies the portrait and all sidebar details
for both directory cards and bios. No `profilePhoto` metadata duplication. The
single shared `resolveFacultyPerson` function resolves records; missing records
fail the build. Put biography sections in the page body, without a duplicate H1,
portrait, or contact block. GEO's satellite hero assignments remain intact.
See `faculty-profiles.md` for the exact editing contract and completed migration.

Main faculty directories for GEO, PUBA, PSY, and SOC use one shared
`layouts/profiles/faculty-directory.njk`, with unit `faculty.json` records sorted by
explicit `lastName`. Four equal desktop columns use the normal shared Bootstrap
gaps, reducing to two/one columns on smaller screens. Initial PSY/SOC/PUBA grids
show linked portraits above the existing text lists; GEO retains existing card
details within the same grid. This directory include is distinct from the bio
page layout. See `faculty-directories.md` for editing and verification details.

The four main faculty directory landing pages use two explicit sections in their
HTML source: heading/brief intro, then a full-width gray section containing the
shared portrait grid (and retained working text links). The background section
wraps the width-constrained container, not the reverse. This is the directory
page treatment; it does not move individual biographies into gray panels.

Faculty directory cards omit research keywords/interests. Keep the keyword data
and show it on individual profiles; do not delete it during directory cleanup.
Faculty name links use the normal shared link color/underline, without black or
green component overrides. Shared profile contact markup renders office information
as plain, non-interactive text. Email and telephone retain their linked icon
treatment. Further spacing is deferred.

Faculty identity records are unit-specific. A person affiliated with multiple
units may have separate records with different roles, offices, or contact details.
John (Jack) Barile's PSY faculty record is independent of SSRI's existing people
record; do not automatically synchronize them. Update only the unit requested,
and check the other listing when a user explicitly requests a cross-unit change.
