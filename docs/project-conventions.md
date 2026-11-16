# Accepted project conventions

Established November 10, 2026 (Pacific/Honolulu). These are working agreements,
not a claim that every older file has already been migrated.

## Documentation organization

Agreed November 15, 2026: keep current rule documents in docs/rules, unit records
in docs/units/UNIT, shared technical explanations in docs/shared, cross-site
reports in docs/reports and report forms in docs/templates. docs/README.md is the
human-readable index. Keep this agreements file and work-status.md at docs root
as stable entry points. Unit review/migration reports are records, not competing
general formatting rules. Moving documents does not itself resolve all historical
instruction conflicts; consolidate those explicitly when reviewing each rule set.

## Website construction and startup

The accepted [website build rules](rules/website-build-rules.md) govern folder structure,
explicit HTML addresses, editable sources, shared components, startup and route
verification. Review pages use `/heroes/es.html`, never an automatically created
`/heroes/es/index.html`. Existing intentional section indexes remain exceptions;
this is not authorization to relocate them indiscriminately.

## Manual publishing during development

Agreed November 15, 2026: all ten unit publishing workflows run only when
manually started with GitHub Actions Run workflow. Remove automatic push and
hourly schedule triggers. This supersedes hourly shared-source refreshes during
the current development cycle. Develop locally, push source changes when ready,
then manually publish each affected site after the required unit and shared
changes are on GitHub. A shared push alone does not refresh published sites.
A daily schedule may be considered later; it is not enabled or agreed now.
Shared-source validation on pushes and pull requests remains separate.

Review also publishes manually through its single Build and publish Review
workflow. Its GitHub repository is cssweb-stack/review and its project address
is https://cssweb-stack.github.io/review/. Local development retains root paths;
publishing builds with SITE_PATH_PREFIX=/review/. Review requires the five reviewed unit
sources (ANTH, ES, PUBA, SOC, SSRI) and builds them before generating its inventory.
Other unit sources are optional; unavailable repositories produce a warning and
are omitted from the listings. This supersedes requiring all ten repositories. Push
required css-shared and unit changes before manually publishing Review.


## Scope and ownership

Across college websites, order comparable items alphabetically by their displayed
name, starting with the first word. Depart only for a clear reason, and explain
the reason in the relevant documentation. Academic-program tiles are an accepted
exception: minor, BA, BAM, MA, PhD follow academic progression. SOC homepage
research-area tiles use alphabetical order. Confirmed November 14, 2026.

Accessibility reviews here focus on major red flags and shared fixes; Siteimprove
provides the comprehensive scan. Do not routinely repeat exhaustive viewport
cross-products when a targeted check will answer the question. The user explicitly
authorizes verified shared accessibility corrections that benefit all sites;
recheck the affected interaction and a representative consuming site. Keep
manual-review limitations separate from confirmed failures and automated passes.

SCI may be migrated in phases. Its first phase covers people and a grouped
directory only, using central people/program data and the existing shared cards
and bio layout. The same records can feed later program-page directories;
multiple affiliations or roles never require duplicate people records.

SCI program landing pages live at `programs/<program>/index.html`, published as
`/programs/<program>/`. Future individual degree pages belong alongside that
index in their program folder. Separate `degrees/undergraduate.html` and
`degrees/graduate.html` are browsing routes to the same detail pages, not copies
of the degree content. Courses retain their five HTML pages under `courses/`.

The current seven site directories are `geo`, `puba`, `psy`, `soc`, `ssri`, `pols`, and `es`, beside
`css-shared`. `style-guide` documents the shared system. Keep shared layouts,
styles, assets, and reusable content in `css-shared`; keep page sources in their
site repositories. Consult existing topic documentation before making changes.

## Folder names

Use lowercase repository folders. Psychology's local folder is `psy`, formerly
`PSY`. Avoid introducing absolute paths tied to one computer.

## Page sources and metadata

Page-review run sheets default to a simple Excel workbook with one worksheet and
two columns only: Old page and New page, containing page names rather than URLs.
List matched pairs first, then old pages without a new match, then new pages
without an old match; leave the absent side empty. A source page split across
two new pages may appear twice to show both matches. Keep route analysis,
statuses, notes and redirect/404 decisions out of this run sheet; prepare the
fuller comparison separately when requested. Preserve reviewed workbooks rather
than overwriting them. Confirmed November 14, 2026 for ES and future review sheets.

Retain user-confirmed external URL moves in src/data/common/url-replacements.json
so they can be reused across unit sites. Check a unit with
`python3 scripts/link-replacements.py UNIT`; apply those exact known replacements
with `--apply` when link correction is authorized. Match only the recorded old
paths, including their HTTP/HTTPS and www variants where configured; retain query
strings, fragments and link wording. Do not guess replacements for unlisted
Graduate Division pages or modify other units during a unit-specific task.
These are outbound-link corrections, not redirects installed on UH's servers.
Five Graduate Division mappings supplied November 14, 2026 are recorded there.

HTML/Nunjucks source formatting is governed by [Code Formatting](rules/code-cleanup.md).
That document is the single authoritative formatting rule set, displayed directly
on Review at /rules/code-formatting.html. It replaces the former duplicate rule
list here. Read it before editing or reviewing HTML/Nunjucks source. Update that
same document when a rule changes; do not maintain competing formatting lists.
The Rules section was requested November 15, 2026; other review categories remain
separate and have not yet been consolidated there.

Course names in website prose and lists use SUBJECT NUMBER: Course Title, for
example SOC 300: Principles of Sociological Inquiry. Keep a space between subject
and number and after the colon. Code-only references (SOC 300), prerequisites
and ranges do not acquire a colon or invented title. Preserve letter suffixes,
cross-listings, topic designators, credits and substantive title wording until
reviewed. Standard text review reports deviations and conflicting titles for the
same code; punctuation cleanup does not authorize choosing an academic title.
Confirmed November 14, 2026; SOC scan recorded in soc-course-format-review.md.
SOC research-area Related Courses lists omit credit counts because they introduce
topics rather than degree requirements. Academic requirement/program pages retain
their existing credit values. Do not remove credits across all pages as a side
effect of punctuation standardization.

SSRI main-content H2s use `<hr class="section-divider">` between content groups.
Do not add a leading HR when an H2 opens a new page section/band or biography
column: the section boundary already supplies the separation. Keep dividers
between later groups within that section, including headings following preceding
prose. Reuse an existing HR rather than inserting a duplicate. These inherit the standard shared HR styling; section-divider is the
hook for future adjustments. H2s keep their normal shared heading style.
Sidebar names, office headings, profile/card titles and research-list card titles
retain their component styling and are excluded. Other sites are not swept by
this SSRI standardization. Shared section headings (privacy/directory/service
groups) use sectionHeading with context and opt in via mainContentDividers in
unit site-settings; local prose pages retain explicit HR/H2 HTML.

Across all sites, h1–h6 headings must not contain strong, b, em or i formatting
tags. Heading weight and style come from shared CSS. Preserve heading text,
links and IDs when removing these wrappers; paragraph emphasis is unaffected.
Check imported headings and include this check in standard text cleanup. SSRI
was swept November 12, 2026; other existing sites are reviewed in their own scope.

Opening paragraphs use normal paragraph styling; do not add the retired `intro`
class to new or edited pages. SSRI's existing opening-paragraph instances were
removed November 12, 2026. Other sites are not swept automatically. Keep the CSS
rule until remaining consumers are reviewed and its removal is requested.

Every published content page has its own HTML source file with YAML front matter
containing explicit `title`, `description`, and `permalink` values. Faculty profiles
follow the same editing convention as ordinary pages. Do not reintroduce a single
pagination template that owns metadata for all faculty pages.

Titles follow the visible H1 as closely as practical. A homepage gets a descriptive
title based on its H1, rather than “Home.” Updated November 14: reviewed sites use a configured abridged-unit/campus titleSuffix and optional page searchTitle; the legacy ` | {site.name}` suffix remains only as a fallback for unconverted sites. Do not manually repeat the configured suffix in the page-specific title. If a page has no H1, retain a
sensible existing title and note the missing heading instead of inventing content
outside the requested scope.

Preserve existing meta descriptions. During the current standardization phase,
missing descriptions use exactly `This will be the meta description.` Do not
replace placeholders with custom copy unless requested. Geography's existing
rendered descriptions are preserved, including its faculty descriptions.
An explicitly requested SEO review authorizes replacing those placeholders with
unique summaries grounded in each page's content. Keep metadata in local HTML;
use the shared seo-audit.py checker and docs/rules/seo-review.md procedure. Do not
enable indexing merely because the local metadata audit passes; launch is a
separate check after URLs/404 and publishing are settled.

Geography faculty pages now live in `geo/src/faculty/<slug>.html`, containing
metadata and biography content. `faculty.11tydata.js` resolves `personSlug` to the
shared faculty record for the reusable profile layout. Contact details and profile
identity remain shared data; changing a name may require updating that record too.

Each site has `src/privacy.html` with local metadata and an include of the shared
policy body. Keep the policy content shared. Other consumers without this local
page retain the shared generated fallback. GEO still has a retired, ignored
`src/privacy/` source; it is not the published policy.

Custom 404 pages use the shared pages/not-found.njk template with local metadata,
permalink /404.html and isNotFound:true. The shell forces noindex and omits
canonical output for this error page. Unit quick/recovery links belong in shared
not-found.json. Populate real old-to-new links after URL comparison; no invented
redirect files or destinations. Verify actual HTTP 404 on the host. See
docs/shared/not-found-pages.md for the 20/80 design and adoption instructions.

Existing GEO pages may use `base.njk` and the profile layout; other current pages
use `shell.njk`. Shared layouts remain reusable. The metadata agreement does not
require a wholesale rewrite of older page structure. Includes, fragments, and
nonpublished diagnostic templates are not standalone content pages.

## Site settings and shared components

Reusable decorative SVG backgrounds live under src/media/shared/backgrounds/.
SOC academic homepage tiles opt into the shared tile-pattern-jigsaw modifier;
it sets the existing --tile-background variable rather than a separate overlay
implementation. Preserve the supplied SVG's transparent line geometry; filled
paths can represent thin outlines and must not be blindly changed to fill=none.
GEO's legacy local contour-lines.svg stays in place pending its separate cleanup.

For GitHub Pages preview builds, set SITE_ORIGIN to the GitHub Pages origin and
SITE_PATH_PREFIX to the project path. Social page/image URLs use that deployment
host/path; production canonicals still use the unit’s configured site.url. Omitting
SITE_ORIGIN with a project prefix can advertise nonexistent production paths.
SOC’s workflow now sets both explicitly; root production builds retain site.url
as the social origin fallback. Do not enable indexing merely for preview sharing.


Horizontal research-list photographs can use the shared imageTextRow macro with
`landscape=true`: 20/80 at 1600px+, then the existing 25/75 and 33/67 intermediate
splits, stacked on mobile with images at 75%. Square POLS-style course rows keep
the default 17/83 wide-desktop split. Keep both variants in the same shared macro
and stylesheet; do not make per-unit copies. See image-text-rows.md.

The reusable square placeholder supplied by the user is
`src/media/shared/placeholders/temp.jpg` (500×500). Use that shared file for
temporary decorative graphics, with empty alt text; do not duplicate it per site.

All 13 unit/college Open Graph images now have matching settings in their unit
`site-settings.json`: ANTH, CSS, DURP, ECON, ES, GEO, POLS, PSY, PUBA, SCI, SOC,
SSRI, WGSS. Exports live at `src/media/open-graph/<unit>.jpg`, 1200×630, with
image-specific alt descriptions. This supersedes earlier temporary cross-unit
Open Graph image assignments, including SSRI's former PUBA placeholder.

Editable artwork lives in repository-root `design-sources/`, with Open Graph PSDs
under `design-sources/open-graph/`. Commit/push these to carry them between machines.
Only web exports belong under published `src/media/`; design sources stay outside
the build's asset-copy roots and are not published on unit websites.

Hero and Open Graph controls belong in each unit's
`css-shared/src/data/units/<unit>/site-settings.json`.
All units use SSRI's hero overlay as the starting standard: `var(--uh-green)`
(`#024731`) at opacity `0.33`. This includes the prepared settings for CSS, DURP
and ECON. Geography keeps its separate satellite-image hero settings unchanged;
the disabled style-guide is excluded. Shared checks enforce matching SSRI overlay
color/opacity for other units. Preserve each unit's hero height, image assignments,
crop, attribution and other settings when changing the overlay. Custom unit hero
imagery can be used when suitable images are available; it is not guaranteed.
SSRI retains its mural images, crop positions, compact 145px hero at all three
breakpoints, and green overlay at 0.33 opacity. Its Open Graph image temporarily
uses Puba's `/media/open-graph/puba.jpg`, including Puba's image alt text and
1200 by 630 dimensions, pending replacement by the user.

The shared `course-resources` include places its high contrast buttons directly
on the containing column, without a surrounding gray panel or panel padding.

## Recording decisions and moving between computers

Keep user-facing completion handoffs brief. Explicitly list repository names to
commit/push and any site workflows to rerun. Do not enumerate edited files or
change counts unless requested or needed to explain an unresolved issue.

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

## Shared grid review and standardization

Agreed November 16, 2026: use SSRI, PUBA, ES, ANTH and SOC as the initial
inventory for one cohesive, named responsive grid system. The user is generally
satisfied with current layouts; start with a faithful visual baseline rather than
changing proportions or gaps speculatively. Review's `/grids.html` is the common
specimen page, using production shared CSS/components and simple labeled cells,
with source-page references. Consolidate equivalent arrangements after reviewing
the proposed specification. Exact new gaps, breakpoints and family names remain
unapproved. Keep useful content-driven exceptions explicit; do not retain
unexplained per-page differences. Clarified November 16: this review and
standardization cover general visual page layouts only. Responsive data tables
(including NASPAA requirements) and record directories are separate systems;
exclude them from `/grids.html` and handle their rules independently. Portrait/card
grids and ordinary contact-page columns remain general layouts. This supersedes
the initial inclusion of directory/table specimens on that page.
Review grouping agreed November 16: show common patterns first within four tabs:
Sidebars, Equal Columns, Cards & Tiles, and Combined Layouts. Faculty bios belong
to Sidebars; portrait directories belong to Cards & Tiles. Profile appearance may
remain in profile.css, but the cleanup should consolidate its column geometry
into the shared general layout rules. This is the cleanup direction, not a claim
that the CSS migration is already complete. The tab labels organize review;
they do not approve final CSS class names or breakpoint/gap values.
See [Grid review](shared/grid-system-review.md).

## Shared five-column tile grid

The shared grid-five layout uses five tiles across at 1400px and above,
three across from 768px through 1399.98px, and one below 768px. Never introduce
four or two across. These November 14, 2026 breakpoints supersede the earlier
992px/576px transitions. Centering placement for incomplete rows applies only
inside the three-across media range, preventing implicit columns on mobile.
This applies to both photo and academic-program tiles across consuming sites.

## Sociology and URL migration inventories

Research-area descriptions preserve source scope, concepts and topics. Short
landing summaries lead with varied third-person present-tense verbs (Explores,
Examines, Investigates, Studies, Traces), with the research-area heading supplying
an understood singular subject. This keeps their descriptive role consistent
with institutional prose rather than addressing the reader. The user delegated
selection of the grammatical form to the editor, not approval of an -ing form.
This supersedes the incorrectly recorded participial trial and prior subject-led
short-description trial. Long descriptions use natural third-person prose without
identical template openings. Rebuild from supplied source when requested rather
than continuing to revise rejected drafts.
During the authorized November 14, 2026 editorial review, displaced original
statements stay verbatim under Material for Review immediately below the long
description. Each excerpt must have its own specific reason explaining what was
separated, why, and which substantive material remains in the revised description.
A blanket explanation is insufficient. Do not silently delete them or treat them as approved final copy;
await user decisions. Faculty-specific material has an approved destination:
relocate it to an introductory sentence immediately below Research Area Faculty,
above the cards, and remove its displaced upper review entry. Preserve source
claims without implying fresh verification. Flag areas lacking source material
rather than inventing an introduction. Field-level or interpretive review items
remain individually explained above. See soc-research-descriptions.md.

SOC Courses belongs at the root: source `../soc/src/courses.html`, published
`/courses.html`. November 14, 2026 correction supersedes the original migration
placement under About. Navigation and hero assignment follow the root route.

SOC research-area faculty memberships live in unit research-areas.json as person
slugs referencing people.json. Related Courses sections have an HR before the
heading and use shared list-columns-two: two equal flowing columns from 992px,
one below, with items kept intact. Preserve course wording and source order.
The list fills down the first column then the second, like footer link lists.
Faculty memberships use
the shared people grid/card, alphabetized
by surname, in a full-width gray band after each area's descriptions and related
courses. Never duplicate faculty identity/contact/photo records into area data.
Memberships reflect existing page lists unless the user supplies a roster update.

SOC homepage uses five research-area tiles in a gray band followed by five
academic-program tiles on white: minor, BA, BAM, MA, PhD. Honors remains available
elsewhere but is excluded from this promotional grid. Academic-program palette updated November 14: undergraduate tiles use shared blue; graduate tiles use shared purple; BAM splits blue/purple evenly. This supersedes the original teal undergraduate palette because teal competes visually with UH green. Applied to ES and SOC; older GEO instances await their next palette update. Do not recolor unrelated teal components as part of this decision.
Research tiles now use the supplied shared SOC research-area images with readable
HTML labels, decorative empty alt text and white text on a padded black label
band aligned to the tile bottom at 80% black opacity, with labels at weight 400,
0.9375rem normally and 0.875rem at 1600px+. The shared photo-tile component
reserves two text lines plus uniform padding controlled by one variable,
`--photo-tile-label-padding` (0.5rem). This replaces the oversized fixed 6rem
trial. Bands align at equal height when labels occupy up to two lines; longer
labels can expand at narrow widths or increased text size rather than clip.
Avoid container-relative label font sizing: changing tile padding previously
enlarged labels. See shared/photo-tiles.md for reusable markup and controls.
This supersedes the initial full-photo dark overlay and opaque label band to retain image color
and brightness. Reuse the shared
five-column grid and tile styles used by Geography rather than local copies.

Sociology follows the reviewed hierarchy and content merges in
[`units/soc/soc-migration.md`](units/soc/soc-migration.md). Treat that approved walkthrough as the
reference when refining SOC. On November 14, 2026, the user authorized trying
the official X timeline for `@UHM_Sociology` on News and Events, superseding the
placeholder-only restriction. Keep a direct account link available. This is a
local integration trial; reliable live post rendering has not been confirmed.

SOC social-feed replacement must be entirely free, including ongoing updates
(November 14, 2026). Paid subscriptions and trials that require payment for the
required ongoing behavior are outside scope. A Bluesky migration is a proposed
alternative, not yet an instruction to create an account or replace the feed.

Agreed November 13, 2026: keep SOC’s working source free of the unused original
inline-image imports. Current site images come from shared media. Quarantine the
unused local imports and retired downloader in root `_remove/`, outside `src`,
ignored by Git, for the user to move out and retain. Do not rerun the original
media downloader or restore these images as a side effect of migration work.
Keep source exports and URL/migration inventories as evidence; they do not
constitute instructions to reimport. This supersedes keeping the original downloaded
SOC images under `src/media/content/`; active shared assets are unaffected.

For site migrations, keep an inventory comparing old WordPress URLs with new
published paths, including unchanged, moved, merged, and unresolved sources.
Review whether URL changes can be avoided before deciding on redirects or removals.
Do not create HTML redirect pages by default; the user explicitly wants to avoid
them. Hosting redirect support is not assumed. An inventory records proposed
mappings and is not evidence that redirects have been installed.

## Imported tables

Preserve imported tables as tables during the initial migration. Do not reinterpret
their headings, captions, rows, columns, labels, or surrounding content, and do not
convert them into cards, prose, lists, or another component without explicit user
direction. Import first; then make only the specific table changes the user requests
during cleanup. Styling must not silently alter table content or structure.

## Current graduate-student cohorts

Treat current graduate-student cohort listings as a special migration category,
not ordinary page content. Before importing or rebuilding one, stop and warn the
user that it requires coordinated review of the current roster, names, degree or
program details, advisors, contact information, portraits, alt text, and students
who have entered or left the cohort. Confirm the intended source and whether images
should be imported before proceeding. Do not silently download, reorganize, omit,
or publish cohort portraits as a side effect of a general HTML import.

Graduate-student data uses one unit file named `graduate-students.json`. Records
support `name`, `lastName`, `slug`, `program`, optional `studyArea`, optional
`email`, `research`, an `advisors` array of `{ name, url? }` objects, and `photo`.
The shared renderer omits empty fields, selects “Advisor” or “Advisors” from the
array length and links only advisers with real profile URLs. The shared student
row uses 20% photo / 80% details from 992px, 4/8 tablet columns, and stacks below
768px. Display order is name, program/study area, research interests, the shared
profile contact divider, optional email, then adviser(s). Show the divider only
when email or advisers exist. Optional photoWidth/photoHeight record actual image
dimensions. This supersedes the original 3/9 desktop split and email-first order.
Unit portraits live centrally under
`src/media/units/<unit>/graduate-students/`; do not import images automatically.

PSY, GEO, and SOC cohort records and portraits now follow this shared model. PSY
and SOC cohort pages use the shared renderer instead of imported hard-coded rosters.

## Hero imagery across sites

ES is an explicit exception to the general student-pool default below. The user’s
reviewed workbook USE column is authoritative for the current ES-specific
assignments. Faculty biographies are the approved exception within ES: select
Saunders mural heroes once and save those choices, never randomize per build. Its
existing website heroes were deliberately selected and must be mapped from the
original WordPress assignments and template rules into the new site when the
unit assets are supplied/renamed. Do not replace those choices with arbitrary
shared-pool images. Source featured images are not always hero backgrounds:
faculty featured images are portraits, while their original banner is defined
by the Hero-Faculty template. November 14 mapping evidence and a three-column
review sheet are in exports/es/. Current temporary shared assignments remain
until the actual remapping is requested.

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
faculty directory images: `/faculty/` uses `/media/heroes/hawaii-hall/hero-01.webp` and
`/faculty/associated.html` uses `/media/heroes/hawaii-hall/hero-02.webp`.
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

SOC contact terminology: Sociology Undergraduate Advising is no longer a defined
office or entity. Do not use it as an office label in revised copy. Pending a
confirmed AKD contact, route Alpha Kappa Delta membership inquiries to the general
Department of Sociology contact page. The unit may supply a specific recipient
later. Confirmed November 14, 2026.

Shared profile website/social-link heading is Online, not Website/Websites.
Use destination labels such as Website, Website / CV (only for a combined
destination), Research Lab or the platform name. SOC Ashley Rubin's existing
Twitter link is labeled X and appears under Online after Website; preserve the
account link unless removal is requested. Person names remain only in the hidden
accessible link context, not redundant visible labels. Confirmed November 14, 2026.

POLS is the pilot for unified unit `people.json` (an array). It replaces POLS
`faculty.json` and contains faculty and staff once each, with `type`,
`showInFacultyDirectory`, and `showInKeyContacts` fields. Edit a name, title, photo,
office, or personal email in that one record. The loader derives faculty and
key-contact collections; bios resolve the same people array. Do not create a
second editable faculty/staff file for migrated units. Other units remain on their
existing data until explicitly migrated; SSRI's older people object is unaffected.

Contact pages use one mixed Key Contacts grid, sorted by surname without rank or
faculty/staff groupings. This supersedes the proposed two-grid and chair-first
orders. `people-grid.njk` and the same profile card/identity/contact includes own
all grid markup for Faculty and Contact. Missing photos are omitted; staff without
profile URLs are displayed without invented bio links. Program inquiries remain
separate above the grid. POLS is the review pilot before rollout to other sites.

Faculty bio, directory, and contact person listings always use that person's
individual faculty email. Program or role inboxes belong in a separately labeled
inquiry table on Contact and relevant advising/program pages, not as substitutes
for a person's email. Store inquiry addresses centrally in the unit's
`contact-inquiries.json` and render the shared `program-inquiries.njk` include.
This supersedes the proposed contact-card role-email override. POLS undergraduate
inquiries use `polungrd@hawaii.edu`; Jamaica Osorio's faculty email is
`osorio2@hawaii.edu`. Do not infer missing graduate or other inquiry inboxes.

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
See `shared/faculty-profiles.md` for the exact editing contract and completed migration.

Navigation labels always use `&` instead of the standalone word `and`, across
all units. Preserve that compact convention when importing or editing navigation;
do not silently expand ampersands. This applies to navigation labels, not URLs,
ordinary prose, or automatic changes to page headings and official body text.
People can appear in a directory without an individual bio: set their shared
record's `url` to null and omit the bio page. Keep the name/photo unlinked;
never infer a URL over an explicit null. WGSS Ayu is an intentional example.
“Standard text cleanup” means the scoped, source-preserving checklist in
`rules/text-cleanup.md`, followed by a unit-specific `templates/text-cleanup-report-template.md`
report with measured counts, examples, verification and explicit action-needed status.
Superseded November 14, 2026: the former spaced-em-dash house style no longer
applies. Do not use dashes to separate clauses or introduce explanations in
new or revised website prose across any unit. Use sentences, commas, colons or
parentheses instead. Preserve technical hyphens in URLs/code and legitimate
compound words and ranges; do not sweep retained source-comparison copy.
Exception approved November 15, 2026: associated-faculty directory entries should
use a spaced em dash between a person’s name/contact details and research
interests, rather than a colon. This supersedes the generic colon/no-dash rule
for that directory-entry context only. Course references retain colon-space.
Record this distinction in the future prose-formatting rule page; the current
ANTH initially requested HR separators only; subsequently approved applying the
spaced em dash to its associated-faculty page now. Preserve it during later
reviews. This does not authorize a global punctuation sweep.
Spell out University of Hawaiʻi at Mānoa in new or revised prose rather than
abbreviating it to UH Mānoa. Preserve Hawaiian diacritics. Present study options
from smaller to larger: minor, BA, MA, PhD. Why Study SOC's new opening is one
paragraph. These directions do not authorize a wholesale rewrite of other pages.
Department website prose uses third-person institutional voice: students,
faculty, and the department. Do not switch to second-person reader address
(you/your/you’ll), imperative promotional openings, or first-person institutional
we/our in new or revised narrative copy. Confirmed November 14, 2026 after the
SOC draft incorrectly changed voice. Retained source comparison and attributed
quotations remain distinct from newly written department prose.
Correct unmistakable
Hawaiʻi/University of Hawaiʻi at Mānoa spelling in prose; do not change URLs,
attributes, filenames, original export snapshots, code or table structure.
Flag ambiguous dash, quote, wording and encoding choices instead of guessing.

ANTH explicitly uses eight undergraduate dropdown entries, keeping Advising &
Support and Funding Sources separate. Its course-planning spreadsheets are an
ANTH-only resource row above the common course buttons; no extra HTML landing
pages are invented for those external spreadsheets. See `units/anth/anth-migration.md`.
ANTH faculty navigation has Core Faculty, Associated Faculty (Adjunct, Affiliate,
Cooperating), and Emeriti and Retired Faculty (including In Memoriam). Use the
same shared grouped-list renderer rather than separate visual templates.

Main faculty directories for GEO, PUBA, PSY, and SOC use one shared
`layouts/profiles/faculty-directory.njk`, with unit `faculty.json` records sorted by
explicit `lastName`. The shared grid uses five equal columns at 1600px and wider,
four at 1200px, three at 992px, two at 768px, and one below 768px, with shared
Bootstrap gaps. Content measurements supersede the earlier three-stage trial and
applies equally to faculty directories and mixed Key Contacts. Preserve existing
text sizes until separately adjusted. Individual bio portrait sizing remains
controlled by the shared responsive rule below. Initial PSY/SOC/PUBA grids
show linked portraits above the existing text lists; GEO retains existing card
details within the same grid. This directory include is distinct from the bio
page layout. See `shared/faculty-directories.md` for editing and verification details.

People and office/contact layouts respond to content fit, not device labels.
Graduate-student rows, individual bios, and office/map use 20/80 at 1600px+,
33/67 at 768–1599.98px, and full-width stacked below 768px. Faculty and Key Contacts
use the five-to-one column progression above. These intermediate arrangements
prevent contact text crowding when five columns no longer fit comfortably.
Mobile portraits/building photos are 75% of available column width, left-aligned;
text stays full width. These rows enable horizontal gutters from 768px onward.
Bio rows use a compact 1rem gutter at 768–991px and normal shared gutters above;
do not add independent sidebar/biography padding over the grid gutter.
Decorative image/content rows have a distinct shared `image-text-row.njk` macro:
2/10 at 1600px+, 25/75 at 992–1599px, 33/67 at 768–991px, stacked below 768px with
75%-width left-aligned images. Keep prose in the calling HTML page, not in the
macro or new JSON. Request these as “shared image-and-text rows, like POLS Courses.”
See `shared/image-text-rows.md` for usage. This supersedes the previously deferred course-row work.
The same macro's reverse option places text left and image right, as on Support
POLS: 75/25 from 992px upward, 67/33 at 768–991px, then text before image on
mobile. The reverse variant keeps its larger sidebar even on the widest screens.
It supports linked logos without
photo framing. Do not fork a separate support-page grid for this arrangement.
Choose alt text by the image's purpose in context. Informative photos need concise
descriptions; purely decorative photos and graphics intentionally use `alt=""`.
Support POLS's student sidebar photo is confirmed decorative by the user and uses
empty alt. Never omit the attribute; faculty portraits use the person's name.
Shared course-resource buttons use their own available-width rule: three equal
buttons only when their container is at least 60rem wide; otherwise all stack.
Two-button variants use 40rem. Keep labels short and show any prefix-filter
instruction below the group, outside buttons, centered with the shared info icon.
This is an explicit centered-text exception for the button group.
Do not create a two-plus-one row.
This container-based rule adapts automatically to future shell-width adjustments.
The UH content-width match remains pending; recheck viewport-based people grids
after that global geometry is finalized rather than treating current widths as final.

The four main faculty directory landing pages use two explicit sections in their
HTML source: heading/brief intro, then a full-width gray section containing the
shared portrait grid (and retained working text links). The background section
wraps the width-constrained container, not the reverse. This is the directory
page treatment; it does not move individual biographies into gray panels.

Faculty directory cards and individual profile sidebars omit research
keywords/interests. Existing keyword data may remain in JSON, but the shared
identity template does not render it.
Faculty name links use the normal shared link color/underline, without black or
green component overrides. Shared profile contact markup renders office information
as plain, non-interactive text. Email and telephone retain their linked icon
treatment. Shared person cards and bio sidebars give the primary academic/job
title semibold (600), administrative roles medium (500), and office regular (400),
with both primary title and administrative roles at 1rem; office remains 1rem.
The final size decision supersedes the intervening paragraph-size trial. Bio, directory and
contact names share 1.25rem/600 weight with 1.5 line-height; preserve the bio H1.
Within these cards, no text exceeds weight 600; titles/roles do not use bold or italics.
Donation links: prefer an existing Foundation fund URL when its destination can
be verified. Otherwise retain the unit's working supplied donation-form URL,
including its designation ID and supplied parameters. Never substitute a campaign
ID for a fund/designation ID or invent a short URL without checking it. Flag missing
donation links after widget imports; link the named fund in the support-page text.

For people and departments across all units, display North American phone numbers
as `(808) 956-3689`, without a leading country code. Clickable telephone links use
the international form `tel:+18089563689`. Preserve the actual number.
Publication-profile links remain text only; do not add book icons.
Main Office and person contacts share the `contact-links.njk` macro and
`profile-contact` wrapper: one divider, the same icon/link rows, and no additional
office grid gaps or address margins around the divider. Keep these synchronized
through this single renderer rather than parallel office/person markup.
This supersedes the smaller title/role experiment that overemphasized offices. A thin
neutral `profile-contact-divider` separates office/identity details from linked
contact details. Always list email before phone in person components and Main
Office. No administrative-role icon is used in this first approved treatment.

Faculty identity records are unit-specific. A person affiliated with multiple
units may have separate records with different roles, offices, or contact details.
John (Jack) Barile's PSY faculty record is independent of SSRI's existing people
record; do not automatically synchronize them. Update only the unit requested,
and check the other listing when a user explicitly requests a cross-unit change.

Faculty portrait alt text is derived from the unit faculty record's `name` field
in every directory and individual profile view. Do not maintain separate portrait
alt fields or emit empty alt text for faculty portraits.

Faculty profile supplemental content also lives in each unit's `faculty.json`.
Use optional arrays named `websites`, `publicationProfiles`, `awards`, and
`additionalLinks`. Website, publication-profile, and additional-link records use
`{ label, url }`; award records use `{ name, year? }`. The shared sidebar renders
only populated groups after the core identity block and a standard horizontal rule,
with singular/plural Website headings as appropriate. Websites use the shared globe
icon; publication profiles are linked service names without imported logo images;
awards are unlinked text. Use full canonical award names, including “College of
Social Sciences” rather than “CSS.” GEO, PSY, SOC, and PUBA now use this model.
All faculty administrative titles use `roles`; legacy `role`, `links`, and
`publications` fields and their template fallbacks have been retired. GEO's six
awards are owned by sidebar JSON, with duplicate biography award sections removed.

## URL Migration Audit

After accessibility and SEO review, compare old/current URLs. Shared per-unit
url-migration.json generates instant redirect files only in build output for
confirmed moves/merges. No dummy source pages. Retired pages use the custom 404;
unresolved pages require a decision. Preserve clean sources and document mappings.
See shared/url-migration-audit.md for deployment-prefix behavior and verification.

404 pages show general quick links, not lists of moved pages already handled by
generated redirects. This supersedes the initial SSRI recovery-list design.

## Bio divider standard (November 12, 2026)

Individual faculty bios omit an HR before the first main-biography H2; later
main-content H2 dividers remain. This is an exception to the SSRI main-content rule.
The shared bio sidebar uses profile-contact-divider (1px, margin .75rem above and
.5rem below) between titles and office, before email/phone, and before each visible
supplemental section (websites, publications, awards, affiliations/additional links).
No empty sections or dividers. The office divider applies to bios and all shared directory/contact profile cards.

Website icon links use `.website-link` with an aria-hidden `.special-text-icon`
containing the inline shared globe SVG and a text span. Shared special-text.css
owns their geometry/color alongside profile email/phone aliases: 1rem icons,
var(--icons), identical gap/alignment and link target padding. No separate black
external globe images or profile-only website icon sizing. Reuse across units.

Standard text cleanup includes removing the retired `intro` class token, retaining
text and other classes/attributes. Record counts. Shared intro CSS removal remains
a separate task. This applies to every unit cleanup going forward.

Shared people cards use the same profile-contact-divider before office as bio
sidebars, separating any titles/roles from an existing office. Email/phone grouping
continues to use that identical divider. No office means no office divider.

## Core faculty landing-page filename

Use `src/faculty/index.html` for every unit's core faculty landing page, published
at `/faculty/`. Do not create `core-faculty.html` or `faculty/core.html` alternatives.
Associated and emeriti directories are sibling HTML files in the faculty folder.
When correcting an existing exception, inventory its old public URL and add a
confirmed redirect in the unit's URL migration mapping. This rule is recorded
for future builds; existing unit exceptions have not been swept by this update.

## Faculty landing-page display name

Use `[UNIT] Faculty` (for example PUBA Faculty) for the primary faculty dropdown
item, page H1 and HTML page title, rather than Core Faculty. Keep the parent
Faculty menu label and Associated Faculty/emeriti distinctions as appropriate.
Keep `src/faculty/index.html` and `/faculty/` unchanged. Check this during new-unit
builds and existing-unit reviews. PUBA updated now; other units await their review.

Unit faculty and staff portraits share one lowercase `src/media/units/<unit>/faculty-staff/`
folder, referenced by central people records. Do not create separate faculty/staff
portrait folders for new units. PUBA now follows this standard.

## Shared policies with optional unit appendices

ES retains its three published racial-justice statements as an ES-only appendix
below the shared policies, using the existing supplementalTemplate mechanism.
Use original post titles as H2s, original dates and complete copy, with HRs between
statements. Preserve historical wording and resource links; dated statements use
newest-first order rather than the usual alphabetical list order. The statements
remain available independently of the retired news feature. Confirmed November
14, 2026.

Policies & Procedures uses one core body in pages/policies-procedures.njk for all
consumers. Optional per-unit policies-procedures.json supplementalTemplate selects
a shared units/<unit>/policies-procedures.njk appendix below the core. No appendix
means no unit-specific block. Never show another department's position statements
as universal policy. Anthropology's race/racism statement is its own appendix.

Agreed November 13, 2026: Policies & Procedures belongs on every unit/college/
research site, including CSS and SSRI, with a footer link available on every page.
Keep the common university policy body, including clearly labeled student-related
sections; non-degree sites do not need a separate trimmed policy copy. All policy
pages use /media/heroes/saunders-mural/03.webp (November 14 selection supersedes the November 13 Hawaiʻi Hall image). The shared
common/page-heroes.json assignment overrides unit hero choices for this URL. This does not authorize changes to unrelated page hero assignments.

Graduate Division resources are grouped under a Graduate Division H2 in the shared
policy body, with linked H3 entries for Academic Progress and Conduct Code.
Keep their graduate-specific scope clear; retain the university-wide Student
Conduct Code as a separate entry.

## Standard contact-page section backgrounds

Use white for the contact H1/intro, full-width gray for the shared main office /
building / map section, and white for any people grid beneath it. Approved after
PUBA trial; applied to PUBA and SSRI. Carry this pattern into new units and unit
reviews. Units without a central office/map may need their existing alternative
layout; do not invent an office just to fit the pattern.

Current handoff preference: user is reviewing locally; omit repository-to-update
lists from replies until they explicitly switch back to a remote workflow.

When a gray page section is the final direct content section, add one responsive
layout-section-spacing margin beneath it, in addition to the main content's
existing bottom padding. Other final sections keep zero final margin. Shared CSS
owns this conditional spacing; do not add empty spacer sections to unit pages.

## Lead-off and supporting-content bands

Use a white lead-off section for page purpose/introduction, then a full-width gray
band to contain the supporting detail when that grouping helps. This is a content
hierarchy pattern, not an automatic alternating-background rule. Individual bio
pages remain white and never receive gray bands. Current neutral surface/border
colors remain approved for continued work; possible softening is deferred, not
authorization to change tokens now.

## Sidebar block spacing and diagnostics

Stacked sidebar blocks use .sidebar-stack with one --sidebar-block-gap token
(1.5rem). Do not combine Bootstrap vertical gutters with sibling spacing for the
same stack. PUBA program button groups reuse the token; compact utility links
remain one block with smaller internal spacing. Helpers outline logical stack
children and button groups, not arbitrary individual headings/paragraphs.

PUBA MPA/certificate program pages use shared profile-page main/sidebar geometry,
not legacy content-sidebar wrappers. Program actions form four logical groups:
Contact, Info Session, Apply, and combined Testimonials/Funding. Below 768px use
two equal columns and two rows; combined links occupy one ordinary cell, never
span the full grid. At tablet/desktop sidebar width, groups stack in one column.

## PUBA review and deferred news migration (November 12, 2026)

The user confirmed all current PUBA pages reviewed and approved. Proceed through
accessibility, SEO, URL migration/404, publishing, and live re-scan as separate
checks. Defer importing the news posts so this work can continue. The inspected
Posts export contains 54 published posts, two drafts, and 74 attachment records;
all 54 published URLs match the pending inventory. Drafts stay unpublished.
Deferral is not retirement: preserve access to the existing WordPress news archive
when planning any production-domain switch.

Agreed subsequently: preserve all existing published PUBA post slugs and public
URLs during migration. This supersedes the proposal to shorten old slugs and
avoids a separate rename/redirect step. Source files may be grouped independently
of public URLs; source-folder selection remains an implementation detail.
For future articles supplied by the user for publication, choose a concise,
descriptive, lowercase hyphenated slug using editorial judgment rather than
copying every word of the headline. Keep the headline independently descriptive;
check slug uniqueness before publishing. Rename an existing post URL only when
explicitly requested, with its old address accounted for.

## Approved tablet footer arrangement (November 12, 2026)

Shared footers at 576–991.98px place the unit acronym on its own full-width row,
then identity/address and contact in equal halves below, with the standard 1.5rem
stack gap. The user explicitly approved this arrangement after reviewing PUBA.
It supersedes the earlier equal-thirds tablet layout: it prevents large acronym
overlap and improves the grouping of footer information. Phone and desktop
stacking, fixed acronym sizes, and colors remain unchanged. Applies to all
consumers of the shared footer; no unit-specific exceptions agreed.

Subsequent decisions: footer acronyms across shared consumers use solid white
(#ffffff), no text opacity, and no text shadow. The user explicitly requested
white after the shadow-removal experiment. This supersedes both the original
#c4d1cb color and the temporary instruction to retain that color during testing.
Keep the existing footer background and approved tablet arrangement. Whether
these changes clear Siteimprove’s contrast-review warning requires a fresh scan.

## Sociology shared contact data (November 12, 2026)

SOC now uses the shared three-section contact layout: white heading/hours, gray
Main Office with shared Saunders Hall image/map and icon contact links, then
white surname-sorted people grid. Fax is omitted. SOC’s people.json replaces
faculty.json and owns all 14 faculty plus Lisa Nhomi-Koza; faculty directory,
bios, and Key Contacts derive from those same records. Portraits live together
in media/units/soc/faculty-staff. This supersedes SOC’s legacy faculty-only data
contract. Confirmed Contact roster: Jennifer Darrah, Lisa Nhomi-Koza, Ashley
Rubin, and Manfred B. Steger, sorted by surname. The user clarified Ashley only;
this supersedes the earlier reply suggesting an additional Ashlyn/Ashland contact.

## Profile academic-title weight (November 12, 2026)

Final corrected hierarchy: name 1.25rem/600, academic/job title 1rem/600,
administrative subtitle 1rem/500. Both title lines must be visibly smaller than
the name; no independent breakpoint sizes. Normal paragraphs remain 1.125rem/400.
The explicit smaller-title instruction supersedes the preceding paragraph-size
trial and the temporary academic-weight-500 adjustment.

All identity typography is owned by one block and its named tokens at the top of
src/css/profile.css, used by the same profile-identity.njk for contact cards,
faculty directories and individual bios. Do not add later duplicate rules, local
unit overrides or inline formatting for these title/role classes. See the measured
profile audit in docs/reports/profile-style-audit.md.

## Maximum regular-copy weight: 600 (November 12, 2026)

The 600 maximum applies to regular page copy: headings, paragraphs, bullet items,
profile names, academic titles, and administrative subtitles. Profile names are
1.25rem/600, academic titles 1rem/600, and administrative subtitles 1rem/500;
normal paragraphs remain 1.125rem/400. These sizes supersede the paragraph-size
trial for title lines. Shared typography owns emphasis for strong and b.

Explicit graphic exceptions: the footer acronym stays 800, and the decorative
404 display stays 900. They function as graphics, not regular copy. The user
explicitly corrected the overly broad cap; restore and preserve those graphic
weights. This supersedes the prior no-exceptions instruction as interpreted in
implementation. Footer color remains solid white and its shadow remains off.

Shared checks enforce the regular-copy cap, exempting only those exact graphic
selectors/weights and font-face capability metadata. Do not exempt whole files,
ordinary footer copy, or the actual 404 heading. Direct font-variation overrides
remain disallowed in authored styles.

Hero bank formerly named faculty is now hawaii-hall (plain ASCII, lowercase and
hyphenated). Former main.webp is now hero-01.webp; associated.webp is now hero-02.webp. PUBA’s saved
faculty-directory assignments follow the rename without changing their images.
Universal shared-page heroes now use the Saunders mural bank: Policies and
Procedures uses 03.webp; Privacy Policy uses 06.webp; 404 uses 02.webp.
The common assignment overrides per-unit selections and remains visible when
other heroes are disabled. This supersedes the earlier Hawaiʻi Hall policy,
privacy and 404 choices. Faculty landing-page selections are unchanged.


## Graduate students share profile styling (November 13, 2026)

Graduate-student profiles belong to profile.css alongside faculty/staff profiles,
building cards and profile columns. This supersedes the graduate-students.css
separation; that file/import is removed. Student names use profile-name (20px/600),
program lines use profile-titles/profile-job-title (16px/600), and research/adviser
lines use profile-detail (16px/400), also used for faculty office details. Shared
name/detail/divider gap tokens own spacing. Contact links and dividers retain the
existing shared classes. Do not create independent student typography rules.
Keep student fields/data and responsive cohort row geometry intact.

## Copy changes require consultation (November 13, 2026)

Do not rewrite website copy without first consulting the user and receiving
consent. Layout requests authorize structural changes, not rewritten paragraphs
or factual/name corrections. The user may separately approve new H2s, specific
spelling fixes, or a scoped standard mechanical cleanup; limit changes to that
approval. No silent editorial improvements, name normalization, or factual updates.
For the Hörmann Prize page, the approved edits are the intro/gray section split,
Awards / Eligibility and Submission / Selection and Publication H2s, and Monitary
→ Monetary. Subsequently, the user approved Hörmann throughout the prize page’s
visible text, supported by the supplied LCH family tribute and existing university
fund wording. Keep /hormann-prize.html unchanged.

Standard text cleanup includes a report-only voice/pronoun consistency review,
including we/us/our, I/me/my and potentially inconsistent you/your. Context matters:
faculty biographies, attributed quotations and testimonials may intentionally
use first person. Flag mixed voice with page/excerpt; never automatically replace
pronouns or adopt a global voice without user consultation. This adds review
coverage, not permission to rewrite copy. Procedure/report template updated.

## Preserve every original WordPress site (November 13, 2026)

For every site being migrated/cleaned up, retain both a downloaded full WordPress
backup (database plus files, including uploads) and a Tools → Export → All content
WXR/XML export. These are complementary: the full backup supports restoration;
XML supports direct inspection and content import but does not embed media files.
Record unit, date, source URL, backup tool/format, archive locations, scope and
verification state. Keep copies independent of the retiring host; do not place
raw backups containing private data/configuration in published media or public Git.
Capture before deleting old content and refresh before final retirement if the
source changed. Confirm both archives cover the site and that recovery is feasible
before shutting it down; never infer completeness from the download filename.
This is a required migration checklist item, not a claim backups already exist.

## Role-based inquiries go to Contact (November 13, 2026)

When prose directs readers to a current chair, undergraduate/graduate chair,
director or comparable unit role, link the role reference to that unit’s Contact
page, not a named person’s biography or a hard-coded personal/role email link.
The Contact page is the maintained source for current role holders. Include this
in standard text cleanup and report unresolved cases if a role is missing there.
Personal email links in faculty bios, directories and Contact cards remain valid;
this rule concerns role-based inquiry instructions in prose. Preserve wording
when changing the link target; consult before any copy rewrite.

Standard text cleanup includes report-only institutional-name capitalization
consistency (Department/department, College/college, University/university).
Distinguish official names and sentence beginnings from generic references;
consult before adopting a capitalization policy or normalizing existing copy.

## Tables and a single supporting gray section (November 13, 2026)

Place content tables in a full-width gray page section. Prefer a short white intro
followed by one gray supporting section per page; any further supporting content
can follow on white. Multiple gray sections are possible exceptions, not the
default, and should not be introduced merely to alternate backgrounds. Preserve
existing table content/structure unless its conversion or restructuring is
explicitly authorized. This refines the lead-off/supporting-band convention.

For the proposed Sociology degree split, overview-page gray sections are reserved
for learning outcomes. Suggested Timeline belongs on a separate page whose gray
section holds its table. This is agreed design direction; the page split and
timeline-table implementation were initially planning only. The user subsequently
authorized the MA split (five pages: overview, requirements/progress, suggested
timeline, Plan A thesis, Plan B research report), including brief new subpage
intros and converting the existing semester sequence to a table. Original program
requirements/procedures remain verbatim. PhD restructuring is still deferred.
Use one reusable degree-navigation include and shared per-degree page list at the
top of each page only; retain aria-current without a visible “current” label.
At the bottom use the unit’s standard course-resources include, without Back to
top links or a repeated degree-navigation block. Preserve old MA URL
and section bookmarks through the shared generated-redirect mechanism. Details:
docs/units/soc/soc-ma-pages.md.

Degree page navigation does not show the word “current”; retain aria-current on
the selected item. A future button navigation treatment is only proposed, not
authorization to implement its colors/interactions yet. MA pathway headings and
labels use Plan A: Thesis and Plan B: Research Report (colon), not dash variants.
This supersedes the temporary visible current-page text marker.

MA academic subpages use Sociology’s standard course-resources include at the
bottom (class availability, descriptions, UH catalog). The user subsequently
rejected Back to top links; do not include them. This supersedes the initial
repeated top/bottom degree navigation and the temporary back-link treatment.
Do not maintain a second copy of the course-resource links in page prose.

Use full default HR spacing (2rem each side) between major content chunks. A
subsection divider within the same topic can use the existing Bootstrap my-3
spacing utility (1rem each side), preserving the standard line appearance and
width. Do not borrow the profile-contact-divider style for ordinary page prose.
Applied to the divider before MA Coursework Notes; other dividers unchanged.

## Reusable undergraduate advising widget

Agreed November 13, 2026: advising uses a shared data-driven component, with
Undergraduate Chair first and General Education Advisor second (role order rather
than alphabetical order). Wide layouts use photo/text/photo/text in 20/30/20/30
proportions after gutters; smaller screens stack the advisor groups. Reuse profile
text/contact styles; keep layout-only rules in layout.css. Unit people data owns
the chair identity; common advisor data owns shared advisors such as Jason Higa.
Jason is appointment-only through Navigate360, with the existing destinations
and user-approved concise instructions; no phone/email is shown. See advising-widget.md. The Sociology Minor page uses this widget as its sole advising section after
user review. The BA overview also includes the same widget above course resources;
BAM uses the same widget with its own JSON variant: Undergraduate Chair, Graduate
Chair, then General Education Advisor. The Undergraduate Chair uses the same description on BA, Minor and BAM:
undergraduate course selection, program requirements and planning. The Graduate
Chair uses the corresponding graduate description on BAM. Omit SOC in these
descriptions and do not assign declaration approvals. Jason’s general education/appointment guidance is unchanged.

## Sociology admissions page naming

Use Applications & Admissions consistently for the Sociology page title,
navigation label, cross-link labels and the BAM application section heading.
Use &amp; in HTML and & in JSON/front matter. Supersedes earlier labels using
Applications and Admissions or singular Application and Admission. This is a
page-label convention, not a replacement of ordinary application/admission prose.

## Sociology Funding Sources entry format

Use name: description for new or revised funding award/resource list entries,
with a capitalized description opening. The November 14, 2026 prohibition on
prose dash separators supersedes the earlier spaced-em-dash format; existing
entries await scoped review. Link the resource name where a
destination exists; avoid extra application-explanation links when the name can
carry that destination. STAR (UH Foundation Scholarships) is a General Funding
Resources bullet, not a separate example-based section. Preserve hyphens in
compound words and use en dashes for ranges. This presentation decision does
not authorize guessing eligibility, deadlines, contacts or benefit guarantees.

## Sociology funding descriptions: general resource directory

Agreed November 13, 2026: Funding Sources is a concise directory to providers,
not a duplicate of their current application terms. Use name — short description.
Keep broad audience/purpose distinctions, but omit dollar amounts, annual deadlines,
old award years, quotas, GPA/credit thresholds, specific named contacts, detailed
application procedures and benefit promises. Direct students to linked providers
for current availability and terms. This supersedes retaining those imported
specifics on the combined page; it does not authorize deleting detail-page content
or claiming an award is currently available without verification.

## Course widget page-specific prefix

The shared course-resources include accepts optional page front matter
courseResourcesPrefix; otherwise it uses the unit catalog_courses.prefix.
Sociology Honors Track alone sets SOC or HON so students can find both subjects
in course descriptions. Keep this exception page-specific, not a unit-wide prefix
change, and do not duplicate the course widget template for it.

## Reusable Siteimprove dismissal text

When Bill asks for “no crawl dismiss forever text,” “dismiss forever,” or the
crawler-blocked link dismissal wording, return the saved text below. Use this
version when the link has been manually verified in a browser and the reported
error is due to automated-access restrictions. Do not rewrite it for a specific
provider unless requested. Saved November 14, 2026.

> Verified working in a browser. The destination restricts automated access, causing a false positive in the link checker. Dismissed permanently because the reported error reflects crawler access restrictions rather than a broken link.

### Hostname-resolution failure

Retrieval phrases: “hostname dismiss forever text” or “can’t resolve hostname.”
This records a decision to retain the form, not a claim of verified availability.

> External form retained intentionally. Persistent hostname-resolution errors from the automated checker are excluded from further review. Dismissed permanently.

### Reported 404, manually available

Retrieval phrases: “false 404 dismiss forever text” or “404 but works.” Use when
the user has repeatedly verified that the destination is available in a browser;
do not infer a specific technical cause for the checker’s differing result.

> Repeated manual checks confirm that this link is available in a browser despite the automated checker reporting 404. Retained intentionally and dismissed permanently as a recurring false positive.

## Security objective of static publishing

The shared static publishing architecture intentionally reduces reliance on a
publicly exposed CMS, database and plugin runtime. Platform simplification and
attack surface reduction are explicit project objectives and belong in the
services inventory. Describe this as an architectural risk-reduction measure,
not a penetration test, security certification, quantified incident reduction or
monetary loss avoided. Legacy WordPress installations retain their own exposure
until retired; hosting/deployment accounts, build dependencies and third-party
scripts still require security maintenance. Confirmed November 14, 2026.

## Ethnic Studies faculty label

The ES dropdown entry, faculty landing H1 and page title use ES Faculty, with
uppercase ES. Source remains ../es/src/faculty/index.html and URL /faculty/;
this is a label change, not a route change. Supersedes Core Faculty for this
unit. Other units retain their own labels. Confirmed November 14, 2026.

## Ethnic Studies contact roster

ES uses one people.json array for faculty/staff identity and photos. The mixed
Contact Key Contacts grid contains ʻAnoʻilani Aga, Ethan Caldwell, M. Kunmi Yu
Danico, Monisha Das Gupta and Ulla Hasager, sorted by surname. Staff belong on
Contact, not ES Faculty; Aga has showInFacultyDirectory false. Existing faculty
rank and administrative roles remain visible. This supersedes the temporary
Staff section on ES Faculty. Confirmed November 14, 2026.

## Shared building photographs

Building photographs belong in src/media/shared/buildings/, with lowercase
building filenames such as george-hall.webp. This replaces the vague shared/other
folder. Common buildings.json owns the default photograph, dimensions and alt
text; unit overrides are for real exceptions. ES uses the common George Hall
photo rather than an empty override. Confirmed November 14, 2026.

ES Associated Faculty uses a white H1/one-paragraph intro followed by a full-width
gray listing section. Emeritus/Retired Faculty precedes Affiliate Faculty by
explicit request; members within each group are alphabetical by surname. Preserve
their supplied interest descriptions pending the separate text cleanup. Confirmed
November 14, 2026.

Shared Policies & Procedures uses compact my-3 HRs between individual policy
items, including the Graduate Division subitems. A standard larger-spaced HR
separates Tobacco Products Policy from the Graduate Division group. This is the
shared policy page's explicit spacing hierarchy rather than a large divider
before every policy H2. ES statement separators are compact too. ES Associated
Faculty uses a standard HR above Affiliate Faculty; its group record enables
dividerBefore in the reusable include without changing other units' listings.
Confirmed November 14, 2026.

## Support page appreciation line

Support intros end with a separate non-italic paragraph using exactly
“Contributions of any size are sincerely appreciated.” Apply the shared
appreciation class with its icon-text span so the smiley-face treatment matches
PUBA. Do not append it as italic text inside the preceding paragraph or vary the
wording by unit. Applied to SOC and ES November 14, 2026; follow this convention
as other support pages are reviewed.

ES Support is an explicit equal-weight funds layout: white H1/intro/appreciation
with the Foundation logo on the right through reverse imageTextRow, then a
full-width gray Available Funds section listing all funds alphabetically. Do not
promote a single ES fund into the intro. Other units may retain their approved
featured-fund arrangement. Confirmed November 14, 2026.

## Acronyms in narrative copy

Normally omit a parenthetical acronym if it will not be used again on the same
page. A one-time name can simply be written in full. Define an acronym at first
use on each page where it recurs; a definition elsewhere on the site is not a
substitute. Preserve official degree labels, useful branding/navigation
abbreviations and verbatim quotations. Include this review in standard text
cleanup; do not count image filenames or logo artwork as repeated prose use.
ES Center for Oral History now links the full name in its first paragraph,
omitting the unused COH and the redundant Visit paragraph. Confirmed November
14, 2026.

ES has no news feature: remove the Department News landing and homepage news
heading rather than keeping an empty placeholder. The three historical position
statements belong under Policies & Procedures; remaining news posts are not to
be imported into the new site. Preserve original exports and account for old URLs
in the final migration/404 review. Footer social links are independent and remain.
Confirmed November 14, 2026.

## ES homepage heading

Agreed November 14, 2026: ES homepage H1 is “ES: What World Do You Want to Make?” with no separate tagline. This supersedes the interim university-name H1 and separate question tagline. The unit bar already identifies the department and university; the acronym/purpose heading intentionally follows PUBA’s approach. This is an ES homepage decision, not a requirement to abbreviate headings throughout the sites.

## Homepage institutional identification

Agreed November 14, 2026: the opening homepage paragraph explicitly identifies the full unit name, the College of Social Sciences, and the University of Hawaiʻi at Mānoa. Updated November 14: start with “E komo mai — Welcome to the [full unit name] within the College of Social Sciences at the University of Hawaiʻi at Mānoa.” This supersedes the earlier declarative opening and the interim English-only welcome. The welcome can end with a period before the remaining introduction. An abbreviated/purpose-led H1 does not replace this identification. Apply during homepage editing/review; this instruction does not authorize an immediate portfolio-wide rewrite. After the welcome, intro prose follows the existing third-person institutional voice. The user approved “E komo mai — Welcome to…” on November 14. Its em dash is an explicit exception to the general prohibition on prose dashes. SOC’s H1 was subsequently approved as “SOC: Understanding Society, Inspiring Change” for the current design, subject to department review.

## Academic-program page names and search titles

Agreed November 14, 2026: degree, minor and certificate overview H1s identify the full credential and subject, e.g. Minor in Sociology, Bachelor of Arts in Ethnic Studies, or Graduate Certificate in Public Policy. Avoid standalone Minor, Major or Certificate as program-page H1s. Navigation/tile labels may stay short. Double-major and combined-degree pathways must describe their actual scope without inventing a separate credential. Superseded later November 14: HTML titles now follow Page name | Unit name | UH Mānoa, using the abridged unit name without Department of/Program; program pages follow the same suffix as every other page. H1 remains the full credential/subject. This is a clarity/search-context convention, not a ranking guarantee or a requirement to repeat the institution in every H1.

The intermediate seoTitle full-university overrides were applied to four ES, five SOC and three PUBA overviews. SOC, ES and PUBA have now been converted to the approved shared-suffix pattern; their intermediate full-university seoTitle overrides have been removed. Unit titleSuffix supplies the stable unit/campus ending, and optional page searchTitle supplies the approved page-specific part. The shell reuses the composed result for HTML and social titles. Legacy seoTitle remains supported until those reviewed conversions. URLs, navigation labels and subpage headings were not changed.

## Complete title-list review in SEO checks

Agreed November 14, 2026: SEO review must explicitly assess the complete page-title inventory, semantic labels, unit/campus suffix consistency and excessive repetition/length, not only the presence of metadata. Supply a plain proposed title list when requested and obtain the user's review before applying it. Audit configured suffixes mechanically after building. Maintain concise unit labels (Sociology, Ethnic Studies, Public Administration), UH Mānoa campus branding, and Page name first. Policies & Procedures and Graduate Applications & Admissions use ampersands; research-area names retain their conjunctions. SOC's approved Asia title is shortened to Asia, Pacific, and Hawaiʻi while its full H1 stays unchanged.

Agreed November 15, 2026: SSRI uses Fiscal & Compliance consistently for its service-page H1, navigation and HTML title, replacing Fiscal/Compliance. Preserve the full Fiscal Office and Compliance Unit Services (FOCUS) name in its introduction. OENAS retains and in its official name.

SSRI title inventory approved and applied November 14, 2026 with SSRI | UH Mānoa suffix. Retain recognizable program acronyms alongside names (HAM, HCRI, OENAS); use TASI/PHIDC alone where expanded names are impractically long. This is a deliberate page-title recognition exception to omitting unused acronyms in body prose, not evidence of measured search demand.

PUBA title inventory approved and applied November 14, 2026 with Public Administration | UH Mānoa suffix. Certificate HTML titles use Public Policy Certificate and Nonprofit Management Certificate while their H1s retain the full Graduate Certificate in… credential names. The program overview retains Master of Public Administration (MPA).

## Content heading scale and unit identity

Agreed November 14, 2026: keep the unit identity and page heading visually distinct. Unit branding retains its responsive 24–32px/600 style. Shared content H1/H2/H3/H4 use 28/24/20/18px at weight 500 (rem equivalents), with H1/H2 reduced to 26/22px below 576px. Body remains 18px/400. This supersedes previous generic H1 32/30/28px and H2 20.4px/600 defaults. Keep existing line-height/margins and intentional component styles. Implement centrally in src/css/typography.css, not page overrides. Hierarchical heading markup remains semantic; no fixed numeric heading ratio is required by this design. See docs/shared/typography.md for rationale and measured checks.

## ES course-group descriptive labels

Agreed November 14, 2026: Certificate/BA Group 1 and Group 2 descriptions are strong paragraphs beneath H3 group labels, using sentence case, no trailing period, and and rather than an ampersand. Their wording was compared and is identical apart from original case/punctuation. Preserve meaning; this does not authorize rewriting official course names or changing the credit requirements (six credits per group Certificate, twelve BA).

## Why Study navigation and H1 naming

Agreed November 14, 2026: Why Study dropdown labels use the established unit acronym and a question mark, e.g. Why Study ES?, Why Study SOC?, Why Study PUBA?. Page H1s spell out the full subject and retain the question mark. This keeps narrow navigation concise while the destination heading is descriptive; identical wording is not required. Applied to ES, SOC and PUBA. Other units adopt during their review; URLs remain unchanged. Existing unit-bar full-name/acronym styling is unchanged pending any separate visual decision.

## Unit-bar acronym treatment

Agreed November 14, 2026: when showShortName is enabled, render the full unit name followed by the acronym in parentheses, e.g. Department of Ethnic Studies (ES). Acronym uses the same font family and size as the unit name, superseding the previous 0.875em short-name size and unparenthesized markup. Updated after visual review: acronym now inherits the full unit name’s color and 600 weight, superseding the gray/400 treatment. Parentheses alone distinguish it. Implement once in the shared unit-name template/header.css; preserve each unit's existing visibility flag. Footer/search shorthand unchanged.

## Root-level Courses pages

Confirmed November 14, 2026: the main Courses page belongs at /courses.html, with source src/courses.html, across consuming unit sites. Do not create a courses/ folder or place Courses beneath About. This generalizes the earlier SOC-specific correction; applied to ES as well. Preserve individual course-related subpages where separately justified; existing unrelated sites are corrected during their review rather than silently swept. Update navigation, hero mappings and active URL/title inventories when relocating.

## Run-in explanatory labels

Agreed November 14, 2026: across unit sites, use a bold label followed by a colon and one space before its explanation, e.g. <strong>Save money:</strong> Approved coursework… or <strong>Business:</strong> Management…. Labels use sentence case, not italics. This supersedes the mixed standalone-period and dash separators used in ES BAM advantages/job prospects; those differences were not an intentional editorial distinction. Apply during the authorized text-cleanup sweep; do not change pages during the user's current page-by-page review. Existing course-code colon rules remain separate and unchanged. Preserve true sentence punctuation, standalone headings, official names, quoted/historical text and explicitly approved welcome em dash; do not mechanically turn every period/dash/italic into a label separator.

## Review utility site

Agreed November 14, 2026: maintain a minimal sibling ../review site with redirects-404s and heroes sections, one page per active shared unit. Redirect/retired-page lists are bullets from actual shared unit mappings, with honest no-mapping/unresolved labels. Link tests target GitHub previews; local changes require uploading before those tests can pass. Hero pages show normal paragraph labels/paths and images, grouped main pages, faculty, policies/privacy and alphabetized within groups. Add units as their shared records/sites become available. No interactive dashboard or style-guide redesign; preserve ../style-guide. Rebuild the generated review pages when unit records change.

All sites use lowercase `about/` for About pages, matching the About navigation label (November 14, 2026). No unit acronym suffix: the site root already identifies the unit. This supersedes the earlier ES-only scope and legacy about-soc/about-geo/about-pols/about-psy/about-anth/about-wgss folders. Preserve old published paths with direct redirects; sites without About content need no empty folder.

Review follows the existing unit startup model: npm clean/build/dev with Eleventy serving locally and a copyable localhost URL printed after listening. Do not substitute a custom development server for an established working workflow without user agreement. Confirmed November 14, 2026.

Review is a consumer of the shared presentation system, not a separately styled utility (November 14, 2026). Use the shared Review shell/common CSS, blue CSS Review banner, university-gray primary navigation and existing degree-navigation component for unit switching. Omit UH brand header/footer. Primary links are Home, Redirects and 404s, Heroes; expand only as requested. Keep review-specific presentation in css-shared, not a private local theme.

Hero images in Review show the original image without fixed-height cropping, stretching, enlargement or the production overlay. Constrain to the shared content width while preserving native aspect ratio with max-width:100%, width:auto and height:auto. Production site hero cropping is separate. Confirmed November 14, 2026.

Review hero inspection groups repeated main-page images together before Single Use, in descending use frequency, with HRs above Title Case H2s. Faculty Landing Pages and Faculty Bio Pages are separate sections; directory precedes associated landing pages. Privacy and Policies is the final section and includes 404. Counts are scoped separately to main, faculty landing, faculty bio and shared-page categories so intentional shared images do not inflate main-page duplication. Keep actual image dimensions/aspect ratios. The common 404 image is Saunders mural 02.webp; see the universal assignment rule below. Confirmed November 14, 2026.

Universal hero assignments for all consuming websites use `/media/heroes/saunders-mural/`: Policies and Procedures → `03.webp`; Privacy Policy → `06.webp`; 404 → `02.webp`; faculty biography pages → `07.webp`. Common page-heroes.json owns these settings and overrides unit choices. Faculty bios are identified by personSlug; faculty landing and associated-directory page selections remain independent and unchanged. This supersedes the earlier Hawaiʻi Hall assignments and distinct per-person mural assignments. Confirmed November 14, 2026.

The shared student hero bank is split into `students/graduate/` (images used on SOC graduate pages at the user’s approved first split) and `students/general/` (all other remaining images). Keep the numeric filenames. This is step one only: featured/supporting classification is deferred. Update references and nested-folder discovery when moving assets. Review Extra Student Images shows the bank images Sociology has not selected, not a claim they are unused by every site. Confirmed November 14, 2026.

## Review secondary navigation placement

Agreed November 15, 2026: Review section button navigation belongs directly below
the primary navigation, above the page H1 in its own standard page-section,
container content-section, row and column inside site-main. This clarifies and
supersedes the initial placement outside main. Apply
the same placement to Rules and the unit review sections, without a second copy
below the heading. ANTH is now in the current-review group alongside ES, PUBA,
SOC and SSRI; preserve alphabetical ordering and the gap before remaining units.

## Profile website links without globe icons

Agreed November 15, 2026: remove the globe icon from Online website links in the
shared profile sidebar across units. Retain email and telephone icons. Preserve
website labels and URLs pending review: a person-name label can become Website
when approved, but meaningful labels such as Website/CV and Lab Website must not
be flattened automatically. ANTH website-label inventory is presented for user
review before changing its labels. This is a profile-resource change, not a
removal of unrelated navigation or content icons.

## Course-page heading pattern

Agreed November 15, 2026: course overview pages use Subject (COURSE CODE) Courses
for the H1 and page name, e.g. Anthropology (ANTH) Courses. Keep the navigation
label Courses. Apply to Anthropology now; other units change only when authorized.
This is a page-heading convention, separate from SUBJECT NUMBER: Course Title
for individual course references.

## Current student cohort headings

Agreed November 15, 2026: current-cohort H1s identify Current, the full subject
and the actual degree levels, e.g. Current Anthropology MA & PhD Students. Apply
to other units during their authorized page review; do not invent programs or
force MA/PhD labels on units with different credentials. Keep actual H1, source
path and HTML title visible in Review Page Headings as units enter review.

## Anthropology graduate program sections

Agreed November 15, 2026: split ANTH graduate programs into readable pages under
/graduate/master-ma/ and /graduate/doctorate-phd/.
Each program uses the shared degree navigation on every page and a consistent
hero: MA students/graduate/featured/54.webp; PhD students/graduate/featured/57.webp.
Its content determines the page divisions, not Sociology’s program requirements.
The MA split is structural only: retain all source wording and links, including
awkward, dated or repeated language, until an authorized copy review. Preserve
old page/section links with direct fragment-aware redirects. The subsequent PhD split was authorized and completed November 15 using the
same preservation approach; all of its pages use the approved57 hero.

## Graduate program overview structure

Agreed November 15, 2026: program overview pages orient students with the program
introduction, common degree navigation, learning outcomes in a full-width gray
section, appropriate graduate program contacts/support on white, then existing
course resources.
Detailed policies/requirements belong on linked subpages. Do not duplicate a
course-link list already supplied by the resource widgets or keep generic Next
Steps copy when the advising block provides the contacts. ANTH MA now implements
this: alternative terminal-track note closes its intro, original outcomes/rubric
move into gray, and Jan Brunson/Marti Kerton use the shared advising widget.
No separate MA outcomes nav item/page remains; legacy links redirect to the
overview anchor. This supersedes the initial preserved-copy eight-page MA
arrangement, which was a structural first pass. PhD and Sociology refinements
remain separate authorized tasks; do not automatically deduplicate their text.

## Concise page introductions

Agreed November 15, 2026: introductory sentences should describe the page’s
overall purpose rather than repeat a list of sections or obligations below.
Use the fewest words needed, and avoid unnecessary specifics that create a
second place to maintain when detailed content changes. Scope the introduction
accurately; do not replace required detailed instructions with vague prose.

## Graduate contacts versus assigned advisors

Clarified November 15, 2026 for Anthropology: the graduate chair and graduate
specialist are Graduate Program Contacts, not the assigned faculty advising
team. Students work with their assigned faculty advisor on coursework, research
and degree planning. Overview contacts provide program-level policy/procedural
guidance and administrative support, with distinct role descriptions. This
supersedes the initial Graduate Advising label and coursework-advising blurb on
the ANTH MA overview. Do not infer advising duties from a leadership or staff
title when writing other units; use their own documented responsibilities.

## Introductory text on content pages

Confirmed November 15, 2026: include a brief introductory sentence or paragraph
with each content page H1, before navigation or detailed sections. Describe the
page broadly without repeating its section list or adding unsupported claims.
Apply this during page creation and restructuring rather than waiting for review.

## Short university reference

Updated November 15, 2026 in the Language & Writing Q&A: use UH Mānoa rather
than UHM in ordinary copy, with correct diacritics. This supersedes the earlier
UH Manoa shorthand. Use University of Hawaiʻi at Mānoa for formal identification;
place unit, campus and college names strategically rather than repeating all names
on every page. Preserve protected source statements and approved homepage welcomes.

## Anthropology graduate inquiry routing

Agreed November 15, 2026: MA/PhD overviews and graduate applications use the
shared anthprog@hawaii.edu inquiry callout rather than individual chair/staff
contact grids. This supersedes the earlier Graduate Program Contacts proposal
on those pages and preserves the department’s shared-inbox routing. Individual
people and academic-advising policy references remain on their appropriate pages.

## Anthropology funding structure

Updated November 15, 2026: graduate funding lives under /graduate/funding/
with an index and topic pages. Graduate navigation links directly to that index.
This supersedes the earlier /funding/graduate/ location and shared-landing
routing for graduate students. Undergraduate funding remains a single page
pending its next review; retain explicit award eligibility.

## Anthropology experiential learning placement

Agreed November 15, 2026: use root /experiential-learning/ for Independent
Study (index), Internships, Networking and Field Schools. Undergraduate menu
links to the section. Do not add a Graduate menu link at this time; root-level
placement allows a future shared-audience link without an undergraduate URL.
Preserve source eligibility and flag field-school availability/eligibility for
department confirmation rather than inferring active graduate offerings.

## Anthropology MA navigation and page headings

Agreed November 15, 2026: Anthropology MA pages use this navigation order and
wording: Overview; First Year; Advising, Committees & Candidacy; Requirements &
Progress; Plan A (Thesis); Plan B (Papers); Research & Meetings. Each page H1 and
local title use Anthropology MA: followed by its exact navigation label. This
provides program context while keeping the current topic consistent. Remove the
explanatory sentence above this MA navigation. Scope is Anthropology MA only;
filenames and URLs remain unchanged pending a separate decision. Supersedes the
earlier MA navigation intro and inconsistent topic headings.

MA naming refinement November 15: use parentheses for Thesis and Papers so the
Anthropology MA prefix remains the only colon in each H1. This supersedes the
initial Plan A: Thesis and Plan B: Papers labels.

## Anthropology applied MA track locations

Agreed November 15, 2026: both applied MA tracks belong under Graduate, at
/graduate/applied-archaeology/ and /graduate/applied-cultural-anthropology/,
including coursework and advising/completion subpages. Graduate dropdown has eight
destinations; Funding remains directly linked and Student Organizations is grouped
on Why Study Anthropology, including AUSA, AGSA and Lambda Alpha.
Subfields & Specializations retains links to these tracks. Redirect former About
locations and preserve fragment destinations. This supersedes their About placement.

November 15 refinement: eight Graduate items supersedes the earlier nine-item
decision to fit the user’s publishing constraint. Organization detail pages remain
available; their common discovery section is Why Study Anthropology.

Anthropology undergraduate navigation order, November 15: Funding Sources follows
Experiential Learning; Advising & Support is the final undergraduate dropdown item.
Keep this support destination last when adjusting this menu.

## Anthropology homepage protected voice

Agreed November 15, 2026: Anthropology homepage institutional statement, kuleana
list and closing paragraph are protected unit-authored voice. Preserve wording
and first person; do not rewrite or standardize in later text/voice passes. Layout
and source whitespace may be cleaned without changing meaning. Department News
heading removed from homepage by request. Image placement remains undecided.

## Language rule sheet

November 15, 2026: docs/rules/language-writing.md consolidates accepted language
agreement topics in plain English and is displayed directly on Review as Language
& Writing. Use it for language edits; text-cleanup.md remains the review procedure.
Specific current unit exceptions and approved academic wording remain protected.

## Code Formatting clarification after user review

Confirmed November 15, 2026 through batched Q&A: the canonical Code Formatting
sheet covers HTML/Nunjucks and CSS. HTML remains flush left with no blank lines;
complete paragraphs/headings/simple list items each occupy one source line, with
editor soft wrap allowed. Nested list wrappers and parent closing li use separate
lines. Sentence-level template expressions remain inline; standalone instructions
get separate lines. CSS is flush left with one selector/declaration per line,
opening brace after final selector, closing braces alone and one blank line
between blocks. Other file types retain existing formats. The rewritten sheet
removes duplicate bullets and supersedes its former claim that CSS was excluded.

## Resolving conflicting rule sources

Approved November 15, 2026: flag conflicting instructions rather than silently
combining them. Apply the canonical current rule sheet; consult the user if the
accepted decision is unclear. After resolution, remove or update the obsolete
instruction where it originated. Preserve historical records as history, clearly
marked as superseded, rather than leaving them as competing current directions.
This applies to formatting, language and other maintained rule sets.

November 15 whitespace clarification: Code Formatting owns accidental double
spaces, nonbreaking spaces, trailing spaces before closing tags and spaces before
punctuation. Preserve intentional nonbreaking spaces, word separation around
inline markup and whitespace-sensitive content. Language & Writing refers to
that subsection rather than maintaining a second mechanical whitespace checklist.

## Language & Writing Q&A decisions

Confirmed November 15, 2026: the canonical language sheet now reflects strategic
institutional naming, known Hawaiian diacritics across visible text/metadata,
short-heading title case and full-question sentence case, and matching ampersand
choices between nav labels and H1 topics. Obvious language corrections and missing
broad intros are authorized during requested cleanup; uncertain facts, academic
policy or implications require questions. Degree naming remains contextual, not a
new blanket H1 formula or a claim about search demand; current approved titles
remain until separately reviewed. Supersedes the earlier sheet’s blanket heading
title-case instruction. No portfolio-wide content changes authorized by this Q&A.

## Formatting by default and concise cleanup feedback

Agreed November 15, 2026: follow canonical Code Formatting rules when creating,
importing, generating editable source or editing files, not only on final review.
Check affected source before declaring completion; source generators must follow
the same format. Raw exports, historical snapshots and generated build output stay
excluded. Requested cleanup feedback defaults to a brief evidence-based before/
after formatting grade (or already clean), build status and material exceptions.
Do not generate a separate report unless requested or imply unrelated audits passed.
Internal work-status handoffs remain required; they do not replace concise feedback.

## Fixed academic-unit home, contact and support heroes

Locked November 15, 2026: Anthropology, Ethnic Studies and Sociology use general
featured17 for Home, general featured48 for Courses, general featured41 for Contact
and general supporting22 for Support. These shared unit heroes.json assignments are fixed choices: preserve
across future image allocation and refreshes rather than randomizing them. Same
image across these units is intentional. Geography is explicitly excluded; PUBA,
SSRI and other units are not opted in. User mentioned five choices but specified
only three initially, then clarified Courses as the fourth; do not invent a fifth. These assignments supersede
prior Home/Contact/Support choices for the three named units only.

Correction November 15: Home17 and Courses48 supersede the mistaken Home48
assignment. Contact41 and Support22 remain unchanged for ANTH, ES and SOC.

## Ethnic Studies learning outcomes preservation

Confirmed November 15, 2026 during language review: preserve all six ES student
learning outcomes exactly, including existing italics and punctuation. User
declined proposed copy edits. This is a specific exception to general cleanup
rules; do not reapply those changes in later passes without authorization.

## PUBA accreditation protection

Confirmed November 15, 2026: PUBA NASPAA accreditation content, data and its
presentation are protected from ordinary language cleanup. Do not alter either
naspaa page, accreditation tables or reported data without explicit authorization.
The language pass also preserves mission/values, constitutions, learning outcomes,
biographies and testimonials in their intended voice. Flag uncertain requirements
rather than guessing. User confirmed two annual application deadlines: April 30
and November 1. Preserve both, including existing program-specific admission
seasons; this is not an unresolved date conflict.

## Five-site final review and preview publication

Agreed November 15, 2026: SSRI, PUBA, SOC, ANTH and ES are ready for final folder cleanup, accessibility and SEO checks, then manual publication for Siteimprove scanning. Preview publication is not permission to launch search indexing: keep indexing disabled, allow the access required by the scanner, and do not submit these previews to Google. Prioritize concrete review findings over further open-ended content polishing. Unpublishing until the meeting is an option, not an instruction to unpublish now.

## PUBA preview naming refinement

Approved November15,2026: use support.html and about/news.html without redundant PUBA filename suffixes, matching courses.html. Update references and existing legacy redirect destinations; do not create redirects from these unestablished preview filenames. Courses H1 is Public Administration (PUBA) Courses; Faculty H1 is Public Administration Faculty; admissions H1/search title is Graduate Applications & Admissions. Certificate search titles retain Graduate Certificate in their full names. Support/News H1s spell out Public Administration; established search-title unit suffix remains unchanged. Scope is PUBA; no other site renames implied.

## Descriptive homepage headings and acronym search titles

Approved November15,2026 for SSRI, PUBA, SOC, ANTH and ES: homepage H1 identifies the unit at the University of Hawaiʻi at Mānoa; SSRI uses Social Science Research Institute at UH Mānoa to keep its long name manageable. Homepage HTML title is Full Unit Name (ACRONYM) | UH Mānoa, using a homepage-only seoTitle override so the ordinary subpage suffix is not duplicated. These replace the earlier slogan-led homepage H1/search titles and the shorter Anthropology university heading. Body statements remain protected and unchanged. Taglines are optional and require unit approval; none added automatically. All other page headings/titles remain as approved. Scope is five homepages, not every page on each site.
