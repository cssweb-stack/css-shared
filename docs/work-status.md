# Current work handoff

Updated November 10, 2026 (Pacific/Honolulu).

## Latest completed task: Ethnic Studies draft

- Built `../es`: 26 pages, nine complete faculty sidebars/bios from custom fields,
  shared core directory, Associated Faculty (Emeritus/Retired + Affiliate), and
  retained staff information. All published source pages mapped; Department News
  kept outside navigation. No source-image downloads; supplied temp JPEG used.
- Shared ES JSON owns navigation, faculty, contacts and social links, hero and
  Open Graph settings. Existing analytics/search verification records preserved.
  Source export, URL inventory and content comparison data retained in reference/.
- Contact uses George Hall 301 before 2560 Campus Road and shared map layout.
  ES omits the building photo pending a supplied George image; the common George
  record currently has a Saunders photo. Other unit photo settings unchanged.
- Root and `/es/` builds, shared checks, and 26-page verification passed, including 22
  preserved content bodies and all local links/assets/anchors. Draft only; no
  commit, push, or deployment. Local ES Git repository initialized on main;
  GitHub remote not supplied. See docs/es-migration.md.
- The shared audit exposed imported POLS body mailto links incorrectly rewritten
  as website URLs. Corrected only those imported links and the one-time importer;
  faculty/student JSON contact links were already correct. POLS rebuilt and verified.

## Latest completed task: Political Science draft

- Built `../pols` from the supplied November 11 WordPress export and Navigation
  Review/Sheet2 workbook plus the user walkthrough. 51 local HTML pages, 18 shared
  faculty records with full bios/sidebars, and 27 shared graduate-student records.
  All portraits use user-supplied centralized temp JPEGs; no images downloaded.
- Shared POLS data owns navigation, contacts, social X link, compact hero controls,
  stable student/mural assignments, Open Graph placeholder, and directory records.
  Existing analytics/search verification records retained. Uses shared POLS logos.
- Why Study merges About and both program overviews; Specializations has six
  sibling pages. Internship folder, Community Internships, both learning outcomes,
  Teaching Opportunities, root Pi Sigma Alpha, Support, and Contact are in place.
  Contact uses existing shared include, correct Saunders image via unit override,
  map and office details; remaining imported contacts retained below it.
- Applications/Admissions, News, and Colloquia retained outside main navigation.
  Three unlisted faculty profiles are preserved in source XML for later decisions:
  Richard Chadwick, Manfred Henningsen, Michael Shapiro. No redirect pages added.
- Shared checks, root and `/pols/` builds and site verification passed. Compared content text
  for 48 source pages/merged inputs with zero missing text chunks. No source tables
  were present in those inputs. URL inventory and source export in pols/reference.
- Draft indexing disabled. Open Graph temporarily uses shared PSY image. Review
  current cohort and temporary portraits before launch. No commit/push/deployment.
  See `docs/pols-migration.md`; local POLS Git repository initialized on main;
  GitHub remote has not been supplied. Root-path local build restored.

## Latest completed task: SSRI Jack Barile bio

- Replaced SSRI's placeholder with its own biography using the existing shared
  faculty-profile layout and a unit-specific `ssri/faculty.json` record. Uses the
  supplied shared SSRI portrait, current SSRI titles, contact data, websites,
  publication profiles, and a Saunders mural hero. Psychology record unchanged.
- Preserved the original production `/john-jack-barile/` URL and updated SSRI's
  directory link. Source HTML retains page metadata and SSRI biography content.
- Shared checks and SSRI build passed. Changes local; no commit/push/deployment.

## Latest completed task: remove faculty sidebar keywords

- Removed keyword output from the shared faculty identity template for every
  unit. Existing JSON values retained; graduate-student research lists unaffected.
- Shared checks and GEO build passed. Local changes only; no deployment.

## Latest completed task: centralized GEO faculty/staff portrait references

- User moved 12 portraits into shared `src/media/units/geo/faculty-staff/`.
  Updated faculty/staff JSON plus GEO Contact, Why Study, and Support page image
  references. No old `/media/faculty-staff/` references remain in active sources.
- All 12 images match the original Git image bytes. Shared checks, GEO's 32-page
  build, and whitespace checks passed. Satellite hero assignments unchanged.
- Commit/push both shared additions and GEO deletions/reference changes together;
  changes remain local and have not been deployed by this task.

## Latest completed task: GEO faculty sidebar cleanup

- Migrated all 10 GEO faculty records to the common `roles`, `websites`,
  `publicationProfiles`, `additionalLinks`, and optional `awards` structure.
  Removed publication image fields and retired the shared template's old field
  fallbacks. Added six awards across five people and removed duplicate award
  sections from those five biography sources. All other biography text retained.
- Set Qi Chen's office to Saunders 435–445B. Mary's existing clean Scholar URL
  is retained; export whitespace was not imported. Social/reference links now
  appear under Additional Links. Satellite heroes and portrait paths retained.
- Shared checks and GEO, PSY, PUBA, and SOC builds passed. Checked all 10 GEO
  rendered profiles for publication links, awards, empty groups, updated office,
  and absence of legacy publication-logo markup and duplicate award sections.
- Local changes only; no commit, push, or deployment performed.

## Latest completed task: SOC graduate-student directory

- Added 12 supplied SOC records to centralized `graduate-students.json`, including
  program, optional email, research interests, linked adviser, and centralized
  portrait. Liam Burke and Kelly Duong intentionally have no email field value.
- Replaced the imported hard-coded cohort markup with the same shared renderer and
  two-section page treatment used by PSY and GEO. Added a broad SOC introduction;
  the full name Yuka Takatsuka Koitabashi uses the existing normalized
  `yuka-koitabashi.webp` portrait.
- Validated all 12 records, portraits, and adviser pages. Shared checks, SOC build,
  50-page site verification, rendered-record checks, and whitespace checks passed.
  No legacy cohort-media paths remain in the rendered page.
- Changes are local only; no commit, push, or deployment performed.

## Earlier completed task: SOC graduate-student portrait filenames

- Normalized all 12 newly supplied SOC cohort portraits to lowercase, hyphenated
  student names; removed imported hash prefixes and the duplicated trailing
  `Shimul`. Image contents and hashes are unchanged. No page or JSON references
  were added in this filename-only cleanup. Shared checks passed.
- Changes are local only; no commit, push, or deployment performed.

## Earlier completed task: faculty supplemental profile data

- Harvested and structured optional website, publication-profile, award, and
  additional-link data for PSY and SOC; added verified active publication profiles
  for PUBA. PUBA's export contains dormant ACF service labels with empty URL fields,
  which are intentionally omitted.
- Replaced the shared sidebar's old publication-logo treatment with conditional
  text-link sections, a shared globe icon for websites, and plain-text awards.
  Standardized “College of Social Sciences” award names.
- Shared checks and PSY, PUBA, SOC, and GEO builds passed. Representative output,
  empty supplemental states, and removal of old publication-logo markup passed;
  SOC's 50-page verification passed. PSY verification completed with its existing
  `support-psy.html` legacy-layout notice.
- Changes are local only; no commit, push, or deployment performed.

## Earlier completed task: PSY faculty details

- Populated all 21 PSY faculty records with the supplied academic titles, offices,
  phone numbers and emails. Administrative roles are separate lines for Charlene,
  Jack (two roles), Brad, Anthony, Kristin, and Scott; seven role lines total.
- Same records now populate directory cards and individual bio sidebars through
  the unified template. No department page or layout edits needed.
- Jack Barile's SSRI people record remains unchanged and independent of his PSY
  faculty record; unit-specific roles are intentional. Documented the rule.
- PSY 56-page build and verification passed; shared checks passed. Verified every
  supplied detail and contact link in all 21 cards and matching bio sidebars.
- Local changes only; no commit, push or deployment performed by this task.

## Earlier completed task: one faculty bio template for all units

- Removed the portrait-only/GEO split. All 51 faculty bios now use the same shared
  layout, sidebar components, and faculty record resolver. Portrait, name H1,
  available titles/roles/office/contact data and keywords render on the left;
  biography content remains on the right. Directory and bio use the same record.
- Puba's six bios now show supplied contact details and Helen's two roles; SOC's
  14 show supplied data (Ashley has no phone). PSY shows available name/portrait
  data until further details are provided. GEO uses the same layout and keeps
  all satellite hero assignments, contact data, and publication links.
- Removed per-page profilePhoto metadata and duplicate H1s from PSY/SOC/PUBA;
  every page has personSlug. Moved SOC personal/publication links into shared
  records; retained teaching awards in biography content. Removed old inline SOC
  contact blocks. All 51 Background-and-beyond bodies preserved exactly.
- All four builds and existing PSY/SOC checks passed; shared checks passed.
  Checked 51 common layouts, one H1/portrait each, supplied sidebar data, and
  unchanged GEO hero records. No browser visual QA, commit, push or deployment.
- Canonical rules: `docs/faculty-profiles.md` and project conventions. Earlier
  handoff entries below describe historical steps; portrait-only rules are obsolete.

## Earlier completed task: SOC faculty directory details

- Entered all 14 user-supplied titles, offices and emails in shared SOC faculty.json,
  plus 13 telephone numbers. Ashley Rubin has no phone field or phone row.
- Separated administrative roles: Jennifer Darrah (Undergraduate Chair), Ashley
  Rubin (Graduate Chair), Manfred B. Steger (Department Chair), Wei Zhang (Interim
  Dean). All use the shared multiple-role field; academic titles remain separate.
- Existing shared directory automatically displays details. No department page
  edits, portrait/hero changes, or individual biography changes were needed.
- SOC 50-page build and verification passed; shared checks passed. Verified all
  14 cards, contact links, role lines, and Ashley's omitted phone row.
- Changes local; no commit, push, or deployment performed by this task.

## Earlier completed task: PUBA faculty directory details

- Entered user-provided academic titles, offices, telephone numbers and emails for
  all six PUBA faculty in shared `src/data/units/puba/faculty.json`.
- Helen H. Yu alone has administrative titles: `roles: [Director, Graduate Chair]`.
  Shared identity markup supports multiple roles while preserving GEO's legacy role.
- Shared directory automatically renders detailed cards when a record has details;
  no PUBA page-source edit needed. Other sites with minimal records stay image-only.
- PUBA/GEO builds and shared checks passed. Verified all six rendered records,
  plain-text office locations, mailto/tel links, and exactly Helen's two role lines.
  Local changes only; no push/deployment. Individual biographies unchanged.

## Earlier completed task: faculty contact presentation

- Standardized faculty office rows as plain text without an icon; email and phone
  retain their shared linked icon treatment.
- Directory cards no longer display keywords; shared faculty JSON is unchanged and
  individual profiles still display keywords. Verified on all 10 GEO profiles.
- Profile name links inherit normal shared link styling. Existing details, photos,
  and hero assignments retained. Other sites' minimal cards have no keywords yet.
- All four builds and PSY/SOC checks passed; shared checks passed. Checked office
  output and retained profile keywords. No visual browser QA or deployment.

## Earlier completed task: two-section faculty directory pages

- GEO, PUBA, PSY, and SOC main faculty pages now have two explicit sections:
  title/brief intro on white, then a full-width gray section containing the shared
  directory grid. Text links and GEO's detailed cards retained. GEO uses shell.njk
  to own its sections explicitly; no individual biography pages changed.
- Added short neutral intros to PSY/PUBA; retained SOC/GEO existing introduction
  paragraphs. Removed GEO's extra tagline to match the requested title/paragraph.
- All four builds passed; PSY/SOC checks passed. Parsed output confirms two top-level
  main sections and the portrait grid inside gray on all four pages. Shared checks
  and whitespace checks passed. No browser visual review, commit, or deployment.

## Earlier completed task: shared four-column faculty directories

- Added shared `faculty-directory.njk` and minimal PSY/SOC/PUBA `faculty.json`
  records referencing processed shared portraits and profile URLs. Surname sort,
  four desktop columns, two smaller-screen columns, one mobile column, normal gaps.
- Main faculty HTML pages in all four sites include the same grid. Retained
  PSY/SOC/PUBA text-link lists. GEO uses its existing shared profile cards inside
  the grid, keeping faculty names and full details; satellite hero settings untouched.
- Scoped GEO card image/link widths to their columns and used shared photo styling.
  GEO portraits remain local assets; centralization is still pending direction.
- Four builds and PSY/SOC existing checks passed, shared checks passed. Verified all
  51 portraits are ordered correctly, styled, linked to existing pages, and backed
  by existing images. Browser visual review not performed. No push/deployment.
- Editing/reference notes: `docs/faculty-directories.md`. If changing a portrait,
  name, or URL, update both the page metadata and its explicit directory record.

## Earlier completed task: PUBA portrait filenames and profile layout

- Normalized all six new PUBA portraits in `src/media/units/puba/faculty/` to
  lowercase hyphenated filenames; removed embedded `-jpg` suffixes. Helen Yu's
  portrait is `helen-h-yu.webp` to match her profile URL. Image hashes unchanged.
- Applied the same shared portrait-left/content-right layout to all six PUBA
  individual profiles. Added their previously missing name H1s, preserving the
  original biographies verbatim. Metadata remains in each page's HTML source.
- Directory pages and fixed directory banners unchanged; profile mural heroes kept.
- PUBA 30-page build passed; checked six styled portrait renders, one H1 each,
  biography preservation and saved hero images. Shared checks and whitespace
  checks passed. Local changes only; no push/deployment performed.

## Earlier completed task: Sociology shared profile layout

- All 14 SOC profiles now use the same shared portrait layout as Psychology:
  processed portrait in the left column and existing H1/content in the right.
  Removed the old inline headshot to avoid duplicates; all other source text kept.
  Local title/description/permalink retained. Manfred's portrait resolves explicitly.
- Explained the desktop profile divider was visual-only before removing its shared
  `border-left` rule. Kept padding, column spacing, and diagnostic helper lines.
- SOC and PSY builds/verification passed; GEO build passed. Verified exactly one
  processed SOC portrait per profile. Shared checks passed. No visual browser QA.
- Changes local; no commit/push/deployment performed.

## Earlier completed task: PSY and SOC layout guides enabled

- Set `layoutGuides: true` in PSY/SOC shared site-settings and rebuilt both sites.
- PSY portrait profiles use 3/9 columns at large widths, 4/8 on tablets, and stack
  below 768px. SOC profiles still use full-width content pending portrait wiring.
- No profile proportions changed. Builds passed. Settings are local; no push or
  deployment performed by this task. Guides must be disabled before final launch.

## Earlier completed task: Sociology portrait filename cleanup

- Cleaned new SOC portraits in `src/media/units/soc/faculty/`: lowercase hyphenated
  names, removed numeric/version suffixes including `-v2`. Checked collisions
  before renaming and verified original image hashes unchanged. Shared checks passed.
- There are 15 images for 14 approved profiles. `webp.webp` has no identifying
  filename; preserved it without guessing identity. `manfred-steger.webp` maps to
  the `manfred-b-steger.html` profile when wiring portraits later.
- No SOC profile page/layout edits in this cleanup step. SOC portrait layout work
  remains next, following the Psychology first-pass shared profile layout.
- Local files only; no commit/push/deployment performed.

## Earlier completed task: Psychology profile portrait first pass

- Shared faculty-profile layout now supports a portrait-only left column through
  `profilePhoto` front matter. Reuses `photo-style` and `profile-photo`, with explicit
  Bootstrap columns; stacks on narrow screens. New shared `profile-portrait.njk`.
- All 21 PSY individual HTML profiles use this shared layout and their processed
  portraits, including `anthony-papa.html` -> `tony-papa.webp`. Metadata remains
  local; original H1/biography remain in the right column. Contact details and other
  sidebar content are deferred for user review. Dimensions come from the images.
- GEO keeps its existing person-based sidebar branch and satellite heroes.
- PSY build and existing checks passed; GEO build passed; verified all 21 portraits
  render once with shared photo styling, alt text, and dimensions. Shared checks
  passed. No browser visual review or deployment performed.

## Earlier completed task: Psychology portrait filenames

- Normalized all 21 new portraits in `src/media/units/psy/faculty/` to lowercase,
  hyphenated names, removing trailing version numbers with or without separators.
- Checked destination collisions before renaming and verified image hashes unchanged.
  No existing references to these new portrait paths were found. Portrait wiring
  into directory/profile layouts remains future work; no page changes made.
- Shared checks passed. New portraits are local; no commit/push performed.

## Earlier completed task: faculty murals for SOC, PSY, and PUBA only

- SOC (14) and PSY (21) already used stable randomized Saunders murals; retained
  those assignments. Moved PUBA's six profile entries out of `heroes.json` into
  a new `faculty-heroes.json`, assigning six distinct random Saunders murals.
- PUBA Main/Associated directory banners remain fixed. Geography's person-specific
  satellite assignments were not edited; SSRI also unchanged in this task.
- All three builds passed, SOC/PSY checks passed, shared checks passed, and all
  41 rendered profile pages were checked against their saved mural assignments.
- Changes local only; no commit, push, or deployment performed.

## Earlier correction: preserve Geography satellite imagery

- User clarified that the fixed `faculty/main.webp` and `faculty/associated.webp`
  directory banners apply to PUBA only. Restored GEO `/faculty/` to Kaunakakai,
  Molokaʻi and `/faculty/associated.html` to Ulaanbaatar, Mongolia, including
  original location labels and inherited satellite attribution.
- PUBA directory assignments and PSY/SOC renamed student bank paths remain as set.
- Corrected conventions and media documentation so this exception is explicit.
- GEO build and satellite/credit output checks passed; shared checks passed.
  Changes local; no push or deployment by this task.

## Earlier completed task: Psychology and Sociology hero assignment

- Found 59 WebP student-bank images and seven Saunders murals in shared media.
- Saved randomized, stable assignments: PSY 35 non-profile pages / 21 profiles;
  SOC 36 non-profile pages / 14 profiles. Non-profile images do not repeat within
  either site; all seven murals are used evenly across each site's profiles.
- Each site's `heroes.json` owns non-profile images; new `faculty-heroes.json`
  owns individual profiles. Faculty directories use student-bank images.
- Hero heights, overlays, and Open Graph settings were left as found.
- Updated existing site verification to validate assigned images and collection
  selection rather than the previous single placeholder. Both builds and existing
  site checks passed (106 pages), plus shared checks. No push/deployment performed.

## Earlier completed task: GEO settings standardization

- Added explicit hero height/overlay/visibility controls and Open Graph image
  settings in shared `src/data/units/geo/site-settings.json`. Moved site URL from
  GEO unit-details to site-settings. Used the user's existing `geo.jpg` asset.
- Preserved satellite assignments, crop positions, 210/187.5/90px heights, location
  labels, and attribution. Shared CSS defaults remain compatibility fallbacks.
- GEO's older Eleventy configuration lacked `socialUrl`; added the same helper as
  the shared unit build. Shared checks and GEO's 32-page build passed. Checked
  generated image URL/asset and hero heights, location and credit output.
- Changes are local; no commit/push/deployment performed. Existing user edits to
  other units' settings and Open Graph assets were preserved.

## Latest agreed direction: shared hero image pool

Default heroes across sites come from a shared pool of student/youth/campus images,
not bespoke unit imagery. Custom unit imagery is optional when suitable images are
reasonably obtainable. Geography's satellite treatment may be revisited, but no
replacement is authorized. User is preparing assets from a CSS backup; wait for
those assets and assignment instructions. Heights 210/180/150 are under
consideration; no current settings or assets changed. Recorded in conventions.

## Current task: Sociology draft

- Built `../soc` using the reviewed Navigation Review/SOC workbook and user walkthrough.
  Detailed accepted structure and source handling: `docs/soc-migration.md`.
- 50 pages, including 14 individual faculty profiles; agreed folder/index structure,
  three-page Why Study merge, non-navigation graduate/root pages, and X feed placeholder.
- All pages have local metadata and individually adjustable placeholder hero assignments.
  Shared SOC site settings use Psychology's current hero treatment. Downloaded 46 images.
- Saved original WordPress export, migration/media reports, and a complete old-to-new
  URL inventory in `soc/reference/`. Four omitted source pages need later decisions;
  no HTML redirect pages created.
- Shared checks and SOC root/prefix builds and validation passed. No browser visual
  review or publication. Local preview responds HTTP 200 at `http://localhost:8086/`. A local Git
  repository has `origin` set to `https://github.com/cssweb-stack/soc.git`.
  Old remote and rebuilt local histories were reconciled with a merge retaining the
  rebuilt site's exact file tree. Backup branches preserve both prior tips:
  `backup/soc-before-history-reconciliation` and `backup/soc-previous-github`.
  Local `main` tracks `origin/main`; checked as 2 commits ahead, 0 behind after
  reconciliation. User can now push normally from GitHub Desktop. No push or
  deployment was performed by this task.

## Earlier completed work

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

Sociology draft is ready for user review and later content/profile cleanup.

Read `AGENTS.md` and `docs/project-conventions.md`, inspect affected Git statuses,
then continue the user's next requested site task. No further content rewrite is
authorized merely by this handoff.
