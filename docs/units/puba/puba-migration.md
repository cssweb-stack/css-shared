# PUBA first-pass migration — November 9, 2026

The local consumer is `../puba`, beside GEO and SSRI. It uses the shared Eleventy
configuration, branding, navigation, footer, contact include, privacy policy, and
CSS. Layout diagnostics remain ON through the existing common.css import.
This is a local migration; no site was published.

## Sources and ownership

- Navigation: **PUBA** worksheet in `exports/unit-navigation-review.xlsx`.
  The Navigation Review worksheet is out of sync and was not used.
- Content: `exports/puba/publicadministrationpuba.WordPress.2026-11-09.xml`.
- Shared settings/navigation/heroes: `src/data/units/puba/`.
- Shared hero assets: `src/media/heroes/puba/01.webp` through `15.webp`.
- Page destinations, original image URLs, and source checksum:
  `exports/puba-migration-2026-11-09.json`.
- Migration helper: `scripts/migrations/puba-wordpress.py`. It is a one-time
  importer for a fresh scaffold; do not rerun over subsequently edited pages.

## Structure and scope

There are 28 content pages, plus two automatically generated shared privacy
addresses. Body text, lists, links, emphasis, and genuine data tables were
preserved. WordPress comments, layout wrappers, classes, inline styles, icons,
inline images, embeds, and nonfunctional feed pagination were removed.
No editorial corrections were made. The three agreed page titles were updated:
Program Overview → Why Study PUBA; Give a Gift → Support PUBA;
Apply for Admission → Applications & Admissions.

Root-only pages are `applications-admissions.html`, `funding-opportunities.html`,
and `testimonials.html`. Courses has the authorized lorem ipsum placeholder.

`masters-mpa/` contains `index.html`, `practicum-placements.html`, `timelines.html`,
and `learning-outcomes.html`. Its main-nav entry has no dropdown; the landing
page's existing text links to all three sub-pages.

`faculty/` contains `index.html`, six hyphenated lowercase faculty HTML files
named from the spreadsheet, and `associated.html`. The index is a plain linked
list. Individual bios contain only the existing write-ups beginning at Background,
with no profile name/photo/contact blocks. Cooperating, lecturer, and emeriti lists
moved to Associated Faculty. Kyla Ranker's existing graduate-assistant details
were retained there under Staff rather than silently dropped. The original
cleaned directory remains in `exports/puba/directory.html` for the profile pass.

Contact uses the unchanged office-hours introduction followed by the shared
`layouts/content/unit-contact.njk` include. Helen H. Yu and **Sarah Amend**
(the spelling in the source) are reserved for the later contact profiles.
No profile components or portraits were built/downloaded in this pass.

NASPAA has Accreditation and Requirements dropdown entries, both with info-circle
icons. Active hero assignments follow the original page-to-attachment mappings;
shared images are downloaded once and reused. New pages use the existing default
hero or directory image as appropriate. Faculty portrait featured images were
excluded from the hero pool. All 15 downloaded files have actual WebP signatures;
12 are 1920×333 and three are 1920×210. Numeric names are independent of page names.

Internal content URLs use the shared `url` filter. Legacy `/academic-program/mpa/`
links now resolve to `/masters-mpa/`; the one old Academic Program delivery-mode
link also points to the MPA landing page. Body wording stays unchanged, including
inconsistent admissions deadlines and historical accreditation figures.

## Deferred work

- Design the centralized profile system for PUBA, SSRI (Jack), and GEO.
  PUBA faculty portrait filenames should match the spreadsheet-based bio
  filenames (`helen-h-yu.webp` / `helen-h-yu.html`, etc.).
- PUBA News is a dynamic WordPress feed. This Pages export contains its
  introduction but no news articles. Obtain a Posts export if articles are to be
  migrated; the current page intentionally has only its available introductory text.
- Add inline images and design content columns later.
- Replace Courses lorem ipsum with the graduate assistant's content.
- Academic Program and GCERT Public Service Leadership are excluded by request.
- Centralize Policies & Procedures alongside shared Privacy. Preserve the PUBA
  source in `exports/puba/policies-and-procedures.html`; compare Political Science
  and subsequent units before generalizing the wording. No policy/footer changes
  in this pass. Candidate footer: `Policies & Procedures · Privacy`, with
  `Webmaster` on a second line.

## Validation

Shared checker and PUBA production build passed. The build emits 30 HTML pages.
Generated local links, assets, and fragment destinations resolve. Faculty and MPA
folder counts are eight and four respectively. Non-contact/non-feed page text was
compared to the original export with whitespace normalized and the three approved
heading changes accounted for; all 23 comparisons passed. Contact's duplicate
manual office block is replaced by the shared include. Original directory and
policy text and the complete XML remain available outside published `src`.
Browser visual QA has not been performed in this environment.

Run `npm run dev` from `../puba` for the preview at `http://localhost:8084/`.

## Standalone page paths

Support PUBA and Contact use `/support-puba.html` and `/contact.html`, with
matching root source files. Folders are reserved for groups of multiple pages.
Navigation, internal links, hero assignments, and migration mappings follow these
paths. Original source URLs in the migration manifest remain unchanged.

## Explicit page layout — November 9, 2026

Every PUBA and SSRI content page now uses `layout: shell.njk` and explicitly
contains its own `.page-section`, `.container.content-section`, `.row`, and
column markup. There are no `fullWidthSections` page flags or unit-level automatic
column settings. Single-section and multi-section pages use the same source
pattern. The shared privacy source and future unit scaffolds use it too.
`base.njk` remains a compatibility adapter for older consumers and delegates the
document frame to the same shared shell. Shared CSS and content remain unchanged.

## Program page layout

Nonprofit Management, Public Policy, and the MPA landing page share three explicit
sections. The opening section has a 9/3 desktop split: heading, styled tagline,
and introductory paragraphs on the left; Interested? Next steps through Apply
for Admission on the right. Columns stack below 992px. The second section holds
Program Requirements and everything that follows it in a full-width column.
The existing three-button course-resource panel remains in its own final section.
Text and links were compared to the previous source and remain unchanged.
PUBA builds and link checks passed. Chrome verified all three pages at 375, 820,
and 1440px: correct column stacking, three sections, full-width requirements,
and no horizontal overflow. Results: `exports/puba-program-layouts-2026-11-09.json`.
