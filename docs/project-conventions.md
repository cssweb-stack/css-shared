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
