# Anthropology migration

November 11, 2026. Lowercase sibling repository `anth`; shared data, templates,
heroes, and media remain in css-shared. Local preview: http://localhost:8089/.
No remote added, commits made, push performed, or deployment started.

## Sources and decisions

The three explicitly supplied WordPress exports are preserved in `exports/anth`:
the unnumbered file contains Pages; `(1)` contains graduate-student custom posts;
`(2)` contains People custom posts. Attachments were not downloaded or imported.
The workbook's Navigation Review pass supplies navigation/icon conventions;
the ANTH pass and user walkthrough define the final structure and core roster.
The initial file inspection was stopped at the user's request; generation began
only after the user explicitly supplied all three exports and authorized work.

- Why Study ANTH combines Undergraduate and Graduate landing-page text.
- Subfields and Specializations is a folder/index plus seven sibling HTML pages.
- Undergraduate has eight dropdown entries, an explicit exception to the usual
  seven-item target. Advising and Funding remain separate pages.
- Experiential Learning merges Practical Experience and Internships, Networking,
  and Field Schools without images.
- UMP and AUSA live in undergraduate; AGSA lives in graduate, all outside navigation.
- Lambda Alpha is root-level. Department News and Degrees Awarded remain
  explicit placeholders. Courses now has user-supplied prose, an intro section,
  four shared image-and-text rows in a gray band, and the resources section below,
  matching POLS. Course images use shared anth/courses/course-01.webp through
  course-04.webp, in order, with decorative empty alt.
  Blog posts were not supplied or migrated.
- Main faculty and cohort pages use separate introduction and full-width gray
  listing sections. All 25 graduate portraits and 15 faculty/staff portraits now
  use supplied normalized WebPs under `src/media/units/anth/graduate-students` and
  `src/media/units/anth/faculty-staff`, referenced in the shared JSON with actual
  dimensions. The universal placeholder remains available for future missing images.
- Thirteen core bios use the shared faculty layout. Their custom fields supply
  title, roles, office, email, phone, websites and publication profiles. Awards are
  unlinked sidebar records; specializations remain in biography text, not sidebars.
- One unit `people.json` stores 13 faculty and two staff, with directory/contact
  inclusion flags. Contact includes department, graduate, undergraduate chairs
  and both staff, mixed alphabetically in the shared people grid.
- Twenty-five published graduate records use the shared schema. Seven drafts are
  excluded and named in the report. PHP-serialized subfields were decoded.
  Advisor aliases link to matching core bios. Alex Mawyer stays plain text because
  there is no matching core bio; no guessed profile was created.
- Associated Faculty has three text groups: Adjunct, Affiliate, Cooperating.
  A third faculty navigation page, Emeriti and Retired Faculty, contains the
  Emeritus/Retired and In Memoriam groups, including custom-post retirees plus
  Additional emeriti. Only the core thirteen have local individual bio pages.
  Jack Bilmes's two publication links remain clickable. Original associated-group
  HTML is retained under `exports/anth/associated-*.html` for later review.
- Saunders Hall contact uses the existing shared building/map include, room,
  street, city/ZIP address order and email before phone. Phone display omits 1;
  tel links use +1. Main office is Saunders Hall 346.
- ANTH's two spreadsheet buttons are unit-specific data/include, styled with the
  common responsive resource buttons. They appear above the standard resource
  group on degree-program pages and Courses. In-prose links remain.
- Policies and Procedures is one shared include with attributed PUBA and ANTH
  source sections. This is a source-preserving collection for editorial review,
  not a claim that differing unit policies are identical. Other existing sites
  have not been silently changed to publish it.

## Shared configuration

Records live under `src/data/units/anth`. Site settings include hero controls and
the already supplied ANTH Open Graph image. Non-bio heroes use stable student-bank
assignments; core bios use stable Saunders mural assignments. Indexing remains
disabled; layout guides remain on. The Courses main link is root-level at
`/anth-courses.html`.

`scripts/migrations/anth-wordpress.py` records the one-time extraction logic and
refuses to overwrite existing site pages. Do not rerun it over editorial work.
The new repository contains source URL inventory and a migration report with
source hashes, draft exclusions, unresolved advisor, output URLs and counts.

## Verification and remaining work

Shared checks and ANTH build/verification pass: 51 pages, 13 faculty, 25 students,
local links/assets/fragments, one H1 and metadata per page, stable heroes. Normalized
source text from 32 pages/merged source sections matches the generated output;
listing/contact pages and deliberate placeholders were checked separately. No
source tables were present in the nine inspected program/funding pages.
Local server responds HTTP 200. Shared responsive layouts were already tested
in POLS; ANTH-specific visual/editorial review remains before launch.

Next: replace placeholders as the user supplies portraits; develop Courses and
Degrees Awarded; decide blog migration; reconcile policy wording; review current
roles, cohort, associated listings and source URL changes; connect the GitHub remote.

## November 15: MA page structure

The former graduate/master-ma.html source is preserved in the unit reference
folder as master-ma-before-page-split.html. Editable MA pages now live in
src/graduate/master-ma: index, first-year, advising-candidacy, requirements,
thesis, scholarly-papers, research-policies and learning-outcomes. All except
the index retain explicit .html routes; index publishes at /graduate/master-ma/.

Advisor selection, three-person committee and candidacy conference are together
on Advising, Committees & Candidacy. General course requirements, annual progress
reporting, the course-requirements note and progression to PhD are together on
Degree Requirements & Progress. Remote committee meeting policy and IRB content
are together on Research & Committee Policies. The original applied-track note,
course links, next steps and two shared resource includes remain on the overview.
No source paragraph was rewritten, deduplicated or discarded in this pass.

Checks: all67 source paragraphs and27 source href occurrences match the new
files after insignificant whitespace normalization; all12 old section IDs occur
once and have explicit legacy-fragment destinations. MA hero54 and eight-link
navigation verified on every new rendered page; desktop1440 navigation uses one
row, mobile390 stacks without horizontal overflow; old Plan A fragment tested
in Chrome. This is a structural preservation check, not approval of current
academic requirements or the deferred text/voice/SEO review.

## November 15: PhD page structure

The former graduate/doctorate-phd.html is preserved in the unit reference folder
as doctorate-phd-before-page-split.html. Editable pages now live in
src/graduate/doctorate-phd: index, first-year, advising-candidacy, requirements,
comprehensive-exams, dissertation, dissertation-by-publication, research-policies
and learning-outcomes. The overview publishes at /graduate/doctorate-phd/.

Overview retains introduction, Program Competencies, course links, Next Steps
and resource includes. Advising combines advisor, committee formation and initial
candidacy conference. Requirements includes residency/course/progress rules and
advancement to candidacy. Dissertation combines proposal defense, exam/defense
timing and final dissertation defense. Dissertation by Publication remains its
own page; remote participation and IRB stay together under Research Policies.
Learning Outcomes preserves the original SLO list separately from competencies.
No academic wording, errors, duplication or requirements edited in this pass.

Preservation checks:59 paragraphs,70 list items,21 links and15 original section
anchors retained. Both resource includes retained once. All nine pages have the
shared PhD nav and57.webp hero. Desktop1440 uses one nav row; mobile390 stacks
without overflow. Old comprehensive-exam fragment tested in Chrome and redirected
to its new page. Copy/voice/SEO and missing introductions remain for later review.

## November 15: MA overview refinement after initial split

Supersedes the initial standalone MA outcomes page: outcomes and rubric now live
in the MA overview gray section; their original wording remains intact. MA
navigation has seven pages. Its alternative-track note closes the introduction;
the redundant course list and Next Steps copy were removed by user instruction.
Jan Brunson and Marti Kerton are selected from central people data by the shared
advising widget, on white immediately above course planning/resources. Retired
learning-outcomes.html and original monolithic MA SLO fragment both point directly
to the overview's preserved source ID. PhD's duplicated competencies/SLOs have
not yet been substantively compared or merged.
