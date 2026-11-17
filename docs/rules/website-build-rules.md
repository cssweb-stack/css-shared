# Website build rules

Agreed November 14, 2026. These rules cover how we organize and run websites.
They are separate from writing, accessibility and SEO rules.

## Keep the working setup

Use the established Eleventy setup and the standard clean, build and dev commands.
Do not replace a working setup with a different server or workflow without agreement.
The existing `go` shortcut runs clean, then dev. That sequence must build the pages,
start the local server and print its actual, copyable localhost address.
Never report a server as working merely because the build succeeded.
The user starts and owns local servers through their terminal with go. After an
agent starts a temporary verification server, stop that server and confirm its
port is free before handing control back, unless asked to leave it running.
Do not leave a competing server in a separate agent session.
When a page reads an editable shared document, saving that document must trigger
a local rebuild and update the served page without restarting or asking for a
manual build. Verify an actual edit and restoration through the running server;
a successful startup build does not prove the watcher works.

## Keep page addresses simple

An ordinary page uses a descriptive filename ending in `.html`.
Do not create a folder just to hold that page inside an `index.html` file.

- Correct: `/heroes/es.html`
- Incorrect for that same page: `/heroes/es/index.html` or `/heroes/es/`
- Correct: `/redirects-404s/soc.html`

Folders organize related pages. Do not add an extra folder for each individual page.
Set page addresses explicitly so framework defaults cannot silently change them.
This includes generated Review pages.

Existing, deliberately established section landing pages and the site homepage
may use `index.html`. This rule does not authorize a wholesale move of existing
faculty directories, degree sections or SCI program sections. Review those routes
separately before changing them. Preserve actual legacy public addresses with redirects;
development-only filenames do not need redirects.

## Use consistent folders

The About folder is `about`, without a unit acronym. The main Courses page is
`courses.html` at the site root, not inside About or a Courses folder.
Use lowercase filenames and folder names, with hyphens between words where needed.
Do not prefix standard page filenames with the unit acronym: use `courses.html`,
not `pols-courses.html`. Apply already-approved naming conventions during creation
and review; do not defer them as optional SEO work.

For development-only renames on non-indexed preview sites, update the source filename,
permalink, navigation, internal links, hero mappings and current route records together.
Do not create redirects for those development names. Redirects are for actual legacy
public URLs, not intermediate development routes. This supersedes blanket redirect
planning for every rename.
Do not create empty folders for sections that do not exist.

## Keep editable pages available

Department content pages must have identifiable HTML source files in the site's
`src` folder. Shared layouts and centrally maintained content remain shared;
do not duplicate them into every page. Review's generated listings are an explicit
exception: its generator assembles them from existing site records.

## Keep shared work shared

Reusable layouts, styles, assets and common records belong in `css-shared`.
Unit page sources belong in the unit site. Reuse established components rather
than inventing a separate implementation for each page or department.

For legacy public URL classification, redirects and retirement decisions, follow
[404s & Redirects](redirects-404s.md). Keep those rules there; this document owns
current filenames and route construction.

## Verify the actual result

After changing routes or the build setup:

- Run the affected build and confirm expected output files exist.
- Check internal links and local image paths.
- For server changes, start the actual development server and request the exact
  address being given to the user. A different working page is not proof.
- For moved pages, update navigation, hero mappings and current route records;
  preserve old published routes with direct redirects.
- State whether changes are local, committed, pushed or deployed. Do not imply
  that a local fix is already live.

## Change a rule deliberately

Record an agreed change here or in its relevant topic rule, replacing the previous
instruction rather than keeping conflicting versions. Do not treat an experiment
or a framework default as an approved exception.

## Academic-program course resources

Every academic-program page, including degree, minor, certificate, combined-pathway and program subpages, ends with its unit’s shared course-resources widget directly above the footer. Use `layouts/content/course-resources.njk` inside the standard page-section/container/row/col-12 wrapper. The course widget always has its own dedicated container. Put advising/application callouts in a separate section/container above it. Keep catalog sections and other content before it. Check this when creating pages and during final review; ask if program scope is unclear.

## Permanent source archives

Store original WordPress ZIP backups and XML exports, catalog PDFs, supplied course
DOCX/text files and other source references in sibling `../CSS-Exports/<unit>/`.
Never store these archival inputs in css-shared or consuming website repositories.
Preserve original filenames and bytes. For a same-name revised source, use a dated
subfolder rather than overwrite the previous source. Verify copies before removing
old locations; preserve original supplied files unless removal is explicitly requested.

The archive is separate from website repositories and published sites. A dedicated
private CSS-Exports Git repository is approved for retaining these sources. It has
no website build, Pages deployment or consumer dependency. Commit and push new
intake there; copying files alone does not upload them. Verify the remote commit
before claiming GitHub backup protection. A local move or local commit alone does
not establish backup protection. Keep independent backup copies where available. Never claim
it is backed up without checking the destination and a recoverable copy. Record any
remaining backup setup as unfinished. Migration tools may read the sibling archive;
normal website builds and publishing must not require it.

Keep optimized published images in shared src/media and code/data/templates in Git.
Existing design-sources artwork remains in place pending a separate decision.
Routine working reports remain in ignored .local-notes. Shared checks reject a
recreated exports folder; .gitignore also excludes it from accidental future intake.
Removing archived files from today's checkout does not remove them from Git history.
History rewriting, force-pushing and remote cleanup are separate deliberate actions;
do not perform them as a side effect of source intake or local archive moves.

## Shared repository size ceiling

User decision, November 17, 2026: css-shared must remain strictly below
1,000,000,000 bytes (1 GB). This is our hard project limit, regardless of hosting
allowances or recommendations. It includes Git history, not just today's files.
Monitor the working files and Git database separately and their combined local
size conservatively. Address growth before reaching the ceiling; never justify
crossing it by citing provider flexibility. Keep source archives outside this
critical repository. Size cleanup must preserve current work; history rewriting
and force-pushing remain separate deliberate actions requiring authorization.

## Equal-column layouts

November 17, 2026: SSRI, PUBA, SOC, POLS, ES, ANTH and WGSS use exactly six
content-independent equal-column layouts: grid-one through grid-six. Two columns
means 50/50. The shared grids.css owns their column structure and progression;
layout.css owns the single --grid-gap: 33px token, also used by standard sidebars.
Horizontal and vertical layout gaps stay 33px at every viewport width.

Cards, images, resource buttons, videos, portraits and tiles reuse those classes.
Content hooks may own their presentation, never another equal-column layout or gap.
Keep row/col-12 outer wrappers around inner layouts. A full-width wrapper row can
use row grid-one. Preserve the existing sidebar family and responsive data tables;
these are not additional equal-column patterns. Do not apply layout gap rules to
ordinary inline icon/text spacing or typography margins.

Review's Equal Columns tab shows exactly one specimen for each count, independent
of contents, and inventories all seven selected units. Flowing multi-column lists
retain their reading order and share the 33px column gap; they are text-flow
formatting, not a seventh equal-grid variant. GEO, SCI and PSY are deferred: do not
migrate their source pages during this pass. Legacy component fallbacks needed by
unconverted consumers remain separate until those consumers are reviewed.

Responsive progression, authorized November 17: below 768px every grid has one
column. At 768px use up to two columns; at 992px up to three; at 1200px up to four.
Updated November 17 after visual review: grid-five reaches five at 1400px,
so it holds five across longer; grid-six reaches six at 1600px. Every grid stops at its
named count, so grid-one stays one and grid-two stays two after its first transition.
The 33px horizontal and vertical gap never changes. This replaces the provisional
mixed progressions. The 576px transition remains retired; the new 1400px
transition applies only to the universal five-column count, never a content type. Faculty,
Contact and specialization portrait lists use grid-five with this same progression;
portrait-card-grid is presentation only. Do not add content-specific breakpoint
exceptions. Read this rule before grid work; revise it as responsive decisions change.

## News article heroes

All articles using the shared news layout inherit the main news page's hero
assignment through the unit's news-settings.json indexUrl. Change that index-page
hero once in the unit heroes.json; all articles inherit its image, crop and credit
settings. Do not duplicate assignments across article pages or suppress article
heroes independently. Shared hero and attribution rendering use the same lookup.

## Authorized publishing from VS Code

GitHub CLI is available for agent-managed commits, pushes and manual workflow
runs when the user requests uploading/publishing. GitHub Desktop is optional.
Development checks belong to editing/review work, before that work is declared
finished. Upload/publish requests do not start new audits, tests or editing.
For uploading, identify the approved changes, preserve unrelated work, commit and
push required shared and unit sources, then dispatch the selected publishing
workflows and Review last when affected. Publishing performs the necessary build
and deployment only; it does not rerun the shared validation suite. The shared
checker remains available locally and on explicit/manual or pull-request review,
not automatically on ordinary pushes. This supersedes the upload-time preflight
added earlier on November 17.

Default handoff is immediate after the pushes are confirmed and requested workflow
dispatches are accepted. Report uploads complete and publishing started; do not
wait for builds, repeatedly poll statuses or inspect live pages unless the user
explicitly requests monitoring or deployment troubleshooting. A failure to push
or dispatch is part of this task and must be reported. Background workflow
completion is separate: never call a merely started deployment published. This
supersedes waiting for every deployment and live-page check during routine uploads.

Authentication setup alone does not authorize uploading pending changes. Do not
turn manual development publishing into automatic triggers. Never print or store
credentials in project files or ask the user to paste tokens into chat. Use the
installed gh authentication flow; verify identity, private-repository access and
workflow visibility with read-only calls. Keep archive uploads separate from site
deployment; CSS-Exports has no publishing workflow.
