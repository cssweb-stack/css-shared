# Accepted project conventions

Established November 10, 2026 (Pacific/Honolulu). These are working agreements,
not a claim that every older file has already been migrated.

## Scope and ownership

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
title based on its H1, rather than “Home.” The shared shell appends ` | {site.name}`;
do not manually add that suffix in the page title. If a page has no H1, retain a
sensible existing title and note the missing heading instead of inventing content
outside the requested scope.

Preserve existing meta descriptions. During the current standardization phase,
missing descriptions use exactly `This will be the meta description.` Do not
replace placeholders with custom copy unless requested. Geography's existing
rendered descriptions are preserved, including its faculty descriptions.
An explicitly requested SEO review authorizes replacing those placeholders with
unique summaries grounded in each page's content. Keep metadata in local HTML;
use the shared seo-audit.py checker and docs/seo-review.md procedure. Do not
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
docs/not-found-pages.md for the 20/80 design and adoption instructions.

Existing GEO pages may use `base.njk` and the profile layout; other current pages
use `shell.njk`. Shared layouts remain reusable. The metadata agreement does not
require a wholesale rewrite of older page structure. Includes, fragments, and
nonpublished diagnostic templates are not standalone content pages.

## Site settings and shared components

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
See `faculty-profiles.md` for the exact editing contract and completed migration.

Navigation labels always use `&` instead of the standalone word `and`, across
all units. Preserve that compact convention when importing or editing navigation;
do not silently expand ampersands. This applies to navigation labels, not URLs,
ordinary prose, or automatic changes to page headings and official body text.
People can appear in a directory without an individual bio: set their shared
record's `url` to null and omit the bio page. Keep the name/photo unlinked;
never infer a URL over an explicit null. WGSS Ayu is an intentional example.
“Standard text cleanup” means the scoped, source-preserving checklist in
`text-cleanup.md`, followed by a unit-specific `text-cleanup-report-template.md`
report with measured counts, examples, verification and explicit action-needed status.
House style uses spaces around em dashes. Correct unmistakable
Hawaiʻi/University of Hawaiʻi at Mānoa spelling in prose; do not change URLs,
attributes, filenames, original export snapshots, code or table structure.
Flag ambiguous dash, quote, wording and encoding choices instead of guessing.

ANTH explicitly uses eight undergraduate dropdown entries, keeping Advising &
Support and Funding Sources separate. Its course-planning spreadsheets are an
ANTH-only resource row above the common course buttons; no extra HTML landing
pages are invented for those external spreadsheets. See `anth-migration.md`.
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
page layout. See `faculty-directories.md` for editing and verification details.

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
See `image-text-rows.md` for usage. This supersedes the previously deferred course-row work.
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
See url-migration-audit.md for deployment-prefix behavior and verification.

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

Policies & Procedures uses one core body in pages/policies-procedures.njk for all
consumers. Optional per-unit policies-procedures.json supplementalTemplate selects
a shared units/<unit>/policies-procedures.njk appendix below the core. No appendix
means no unit-specific block. Never show another department's position statements
as universal policy. Anthropology's race/racism statement is its own appendix.

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
profile audit in docs/profile-style-audit.md.

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
