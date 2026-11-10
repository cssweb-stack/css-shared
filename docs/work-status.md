# Current work handoff

Updated November 10, 2026 (Pacific/Honolulu).

## Completed

- Standardized metadata across GEO, PUBA, Psychology, and SSRI. Verified explicit
  page titles/descriptions on 131 published content pages; titles match rendered
  H1s where present. Six PUBA faculty pages have no H1 and retain person-name titles.
- Missing descriptions use `This will be the meta description.` GEO's existing
  rendered descriptions remain unchanged. SSRI homepage title is
  `Research and Grant Services`.
- Converted GEO's ten generated faculty profiles to individual HTML source files;
  preserved biographies, URLs, and descriptions. Shared profile data still provides
  identity/contact information through the faculty directory data helper.
- Added local privacy HTML pages owning metadata, with a shared policy body and
  generated fallback for other consumers.
- Renamed the Psychology checkout folder to lowercase `psy`.
- Added SSRI hero height and Open Graph settings; removed the shared course-resource
  gray panel and its padding.
- Added repository instructions and durable conventions, with pointers in all six
  workspace repositories. Future substantial tasks should refresh this handoff.

## Verification

Before this documentation update: all four site builds passed, shared `npm run check`
passed, metadata was checked across 131 pages, GEO descriptions and faculty biography
content were compared against the prior implementation, and diff whitespace checks
passed. No browser visual review or deployment is claimed. This update changes only
Markdown documentation and instructions; documentation links and whitespace checked.

## Outstanding

- Replace placeholder descriptions when requested; custom copywriting is deferred.
- User plans to replace SSRI's temporary Puba Open Graph image and its alt text.
- Six PUBA faculty pages lack H1s; fixing those headings has not been requested.
- This documentation update has not been committed or pushed by this task. Previous
  implementation work was clean in shared and GEO at the start of this update;
  that alone does not establish remote sync. Check every affected repository before
  switching machines. Do not assume the work has been deployed.

## Resume

Read `AGENTS.md` and `docs/project-conventions.md`, inspect affected Git statuses,
then continue the user's next requested site task. No further content rewrite is
authorized merely by this handoff.
