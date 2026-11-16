# SCI: people and directory phase

Source snapshot: `exports/sci/communicationandinformationsci.WordPress.2026-11-12.xml`.
Working site: `../sci`; local preview: http://localhost:8093/directory/.

## Built now

### Course placeholders

Courses dropdown repeats the five program labels, linking to the same five HTML
filenames under `../sci/src/courses/`. Each page has its own metadata and H1 such
as Journalism (JOUR) Courses, a placeholder paragraph in a white section, then
a full-width gray section with exactly PLACE COURSES HERE. User will edit those
local HTML files to supply the course content. Other prefixes: COM, COMG, LIS,
PACE. Stable hero assignments saved in shared JSON. No Degrees menu yet.
Site total now 45 pages.

### Program pages

The five program landing pages now live in their own subfolders as index.html:
`programs/communication/`, `programs/communicology/`, `programs/journalism/`,
`programs/library-and-information-science/`, `programs/matsunaga-institute-for-peace/`.
This supersedes the original flat filenames below. No content lost in the move;
all local links, central metadata, hero keys and URL inventory updated. The old
flat sources and generated files removed, without fake redirect pages. Individual
degree pages will live alongside each program index when migrated.

Degrees now follows Courses in navigation, linking to degrees/undergraduate.html
and degrees/graduate.html. Their listings/descriptions come from the supplied
WordPress Our Degrees page (seven undergraduate options, five graduate options).
Individual degree-detail links stay on the current site or their existing
external destination until those pages are migrated. Total now 47 pages.

Programs dropdown links to five pages in `../sci/src/programs/`:
communication.html, communicology.html, journalism.html,
library-and-information-science.html and matsunaga-institute-for-peace.html.
Their URLs are owned by central programs.json and shared navigation; links from
people affiliations and existing bios now use these local destinations.

Each page preserves the export's program overview, academic links and resources.
Contact/office details use the same central program-office-card.njk as Contact,
not duplicated literal contact text. Empty social labels/query placeholders are
omitted; actual program-directory records replace WordPress query markup in a
gray section. No source images downloaded. Degree/resource/news links not yet
migrated remain external current-site URLs. Existing descriptions retained where
supplied, placeholder elsewhere. Stable student-bank hero assigned per page.

Mandi Hull's source page carries the explicit Library and Information Science
category, so her programs array now includes LIS. Its directory contains five
faculty and Mandi. Other staff still have no inferred program assignment.
School Directory also reflects this source-backed membership while retaining
the School Staff group. Contact's top-right placeholder is removed at the user's
request; the inquiry details and linked chair remain in the right column.

These additions bring the site to 40 pages. Local build/verify and all five
program membership/portrait checks pass. Repositories: css-shared and sci.

- 27 published faculty and three published staff records in
  `src/data/units/sci/people.json`; 30 individual HTML people pages in
  `../sci/src/faculty/`, using the existing shared biography layout.
- Directory groups: Communication 7, Communicology 7, Journalism 3,
  Library and Information Science 5, Matsunaga Institute for Peace 5; School
  Staff 3. Names sort by the supplied last-name metadata within each group.
- All 30 user-supplied faculty/staff portraits are connected from shared media.
  Filenames normalized to lowercase/dashes, trailing version numbers and fake
  JPEG suffixes removed; `ava2.webp` is now `ava-kikut-stein.webp`. Image bytes
  preserved, actual dimensions recorded. No source photos downloaded.
  Patricia's old Buskirk filename is verified against her Amaral page's exported
  featured-image ID (6816). Jenifer Winter and Maya Soetoro-Ng filenames are
  explicitly mapped to their existing people records; display names unchanged.
- Existing academic titles, administrative roles, offices, emails and supplied
  phones preserved. Phone display uses `(808) xxx-xxxx`, with international tel
  links. Missing phones remain absent.
- 37 publication-profile links and four awards imported. Awards have no links.
  Personal website, Scholars links and primary/secondary affiliations retained.
- Stable student-bank heroes for ordinary pages, mural heroes for people pages,
  hero controls and SCI's existing Open Graph image in shared site settings.
- Minimal home, Directory, Contact and privacy pages: 34 pages total. Broad navigation
  deferred; original proposed navigation saved in
  `exports/sci/navigation-before-people-phase.json`.

### Contact page addition

`/contact/` added SCI's 34th page. The top section uses shared 80/20 desktop
geometry, with H1/intro left and School Inquiries right. The sidebar has the
decorative shared placeholder, existing unit email/phone and School Chair Wayne
Buente linked from the people record. No school address added. Chair/director
labels use Main Office's semibold treatment with names on the next line.
Below it, five program-office cards use the
same responsive five-across grid and contact typography/divider/icon macro as
the people cards. Office photos use supplied shared sci/programs/com, comg, jour,
lis and pace WebPs, with actual dimensions recorded in programs.json. Decorative
alt remains intentionally empty (`alt=""`); adjacent headings identify the cards.
Program images retain their native proportions using the shared
program-office-photo modifier, rather than the square person-portrait crop.
Each card lists program name, Main Office, room/building then street then city/ZIP,
email then phone, and a linked program director.

Office contacts and `directorSlug` references live in central `programs.json`;
`schoolChairSlug` is in unit-details. Names and bio URLs resolve from people.json,
so no second editable copy of directors' names is introduced. The shared include
is `layouts/content/program-contact-grid.njk`. Existing SCI program pages were
reviewed for office contacts; `contactSource` on each record identifies its page.
Communication/Journalism use Crawford 320; Communicology George 326; LIS Hamilton
Library 002; Matsunaga Saunders 723. No personal faculty contact is substituted
for a program inbox or office phone. Directors follow the published roles already
imported into the shared people data. Contact added to navigation, stable hero
assignments and migration URL inventory. Local 34-page build/verification and
shared structural checks pass; all five records and director links checked.

## Data contract

### Support SCI

`/support-sci.html` adds a white H1/introduction section and a gray band with the
five program directors, selected using the same `programs[].directorSlug` values
as Contact. `layouts/profiles/program-directors.njk` uses the existing shared
profile-card include for their real portraits, linked bios, titles, offices,
email and supplied phone. No duplicate director/contact data or inferred giving
fund URLs. User requested direct conversations with directors in place of account
links. Intro invites support for the five programs and directs visitors to them.
Support SCI navigation and stable hero assignment added; total now 35 pages.

Program director headings now share the tallest heading height within each
visual row using CSS subgrid in shared profile.css. Full names remain above the
portraits; no fixed heading height or JavaScript. The existing 5/4/3/2/1 column
breakpoints, gutters and mobile 75% photo treatment remain. This applies only to
the shared program-directors component, leaving ordinary people grids unchanged.
Browser measurements at 1800, 1440, 1100, 850, 600 and 390px confirmed zero portrait
top offsets within each row and no horizontal overflow. SCI build/verify and
shared checks passed. Alignment changes are in css-shared only.

`people.json` is the only editable people source. `programs` on each person is an
array of program IDs, resolved against the shared `programs.json` list. A future
program page can select `people | peopleForProgram(programId)` and include
`layouts/profiles/people-grid.njk`; this reuses the same records, card and bio.
Administrative titles stay in the existing `roles` array. Other affiliations
(DURP/UHERO) are preserved as labeled links, not invented as SCI programs.

`program-directory.njk` groups those same records and uses the existing shared
grid. Group-specific identity prefixes prevent duplicate IDs if a person later
appears under multiple programs. Mandi's LIS assignment comes from her source
category; Cassandra and Janelle remain unassigned. School Staff includes all three
and does not infer program membership from office location. Selection
for a future Key Contacts grid remains undecided (`showInKeyContacts: false`).

## Source review and limits

- Five draft people excluded: Brett Oppegaard, Brien Hallett, Hye-ryeon Lee,
  Noriko Asato and Angie Hamilton-Lowe. Drafts were not promoted to published.
- Rich Gazan's export supplies Professor and Program Chair, CIS. Andrew Wertheimer
  is listed as Program Director, LIS. No third Rich title was invented.
- Ava Kikut-Stein's supplied website URL is a Google Sites editing address. It is
  retained for review; a public website URL is still needed.
- Maya's visible name is Maya Soetoro; source sorting metadata is Soetoro-Ng.
  Both source values are retained, without guessing a preferred display name.
- Some staff page bodies contain general school/program text rather than personal
  biographies. Source text is retained for later editorial review.
- Existing descriptions retained where supplied; missing descriptions use the
  agreed placeholder. Remaining school/degree/resource pages are not imported in this
  phase. Links to those current-site resources remain external.
- The common Crawford photo is still a placeholder;
  do not treat it as a verified Crawford Hall photograph.

`../sci/reference/url-inventory.csv` includes all 81 exported page records by ID
and original URL, preserving duplicate leaf slugs. The migration report records
the source hash, group counts, excluded drafts and omitted images. All 30 people
retain their biography words: 29 normalized text comparisons match exactly;
Andrew Wertheimer differs only by removal of a space before a comma after
`(minor)`. Original XML remains unchanged.

## Verification and handoff

Local build/verification passed for all 47 pages: one H1 per page, descriptions,
unique IDs, internal links/assets/anchors, portrait name alt text and saved hero
assignments. An isolated GitHub-style `/sci/` build also passed. WGSS's existing
28-page build and verification passed after the shared changes. Shared structural
checks passed. Desktop directory visually reviewed with the shared stylesheet.

Local Git repository initialized on main; no remote supplied, no commits, push or
deployment performed. Repositories to update: **css-shared and sci**.
