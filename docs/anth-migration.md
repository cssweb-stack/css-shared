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
