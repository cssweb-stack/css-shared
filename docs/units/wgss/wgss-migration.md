# WGSS migration

November 11, 2026. New lowercase sibling repository `wgss`; preview at
http://localhost:8090/. Shared templates, styles, data and media remain in
css-shared. No source images downloaded. People use the shared placeholder.
No remote added, commits made, push performed or deployment started.

## Sources and structure

The explicitly supplied WordPress export is preserved under `exports/wgss`.
Navigation Review supplies first-pass structure/icons; WGSS and the user walkthrough
supply second-pass changes. The corrected seven-name roster includes L. Ayu Saraswati.

- Why Study combines About, Undergraduate, Graduate and Job Prospects.
- Alumni retains six YouTube embeds; Home retains one. All use a shared responsive
  video macro. Original video IDs, caption and rel parameters retained; added
  enablejsapi=1 and production origin to support the YouTube API.
- Colloquia retains its source list. Courses is a root-level placeholder.
- Major (BA) is a folder with index and Transnational Courses subpage sourced
  from Design Courses. Both the design-courses and legacy focus-courses links
  map to that destination. Online BA stays a separate page.
- Both undergraduate certificates, Double Majors, Honors and Graduate Certificate
  retain their supplied content. No degree requirements have been rewritten.
- Applications & Admissions extracts the Applying for Graduate Study section
  from Graduate. The full Graduate text is also retained in Why Study as requested.
- Student Learning Outcomes is an off-menu undergraduate page, linked from
  Why Study's undergraduate section and both BA pages. The source calls these
  Undergraduate Student Learning Objectives; BA-only scope was not asserted.
- Funding Sources is root-level, sourced from Scholarships. Existing prose links
  point there; Why Study also has a funding button using the cash-coin icon.
- Support uses the common reverse image-and-text row and shared Foundation logo;
  the supplied fund URL is retained, not replaced with a guessed short link.
- Contact uses shared Saunders Hall/map and Key Contacts: Mire Koikari, Brooke
  Tanaka, Lani Teves, Lisa M. Vallin, mixed alphabetically. Room/address/city-ZIP
  order and email-before-phone follow the shared template.
- Faculty navigation now has Core Faculty and Associated Faculty under the same
  faculty folder. Core moved from `/faculty/` to `/faculty/core-faculty.html`;
  source URL inventory was updated, without a fake redirect page. Existing bios
  retain their paths, and Ayu remains deliberately unlinked.
- Associated Faculty imports the supplied Word document into one central
  associated-faculty.json: 65 Affiliate Faculty, 8 Cooperating Graduate Faculty,
  15 Lecturers. The two existing emeriti also move there, replacing the older
  separate emeriti data file and external roster link. Names/departments are
  preserved as supplied; repeated membership across roles is intentional.
  The original DOCX is preserved in exports/wgss, with its hash in the report.

## People and data

One `src/data/units/wgss/people.json` supplies the seven-person main directory,
individual bios and contact cards. Six core biographies came from the export;
the user later clarified that Ayu does not want a bio page. Her shell was removed;
`url: null` retains her directory card with no link. Monisha Das Gupta's office/email
were absent from the export; the user subsequently supplied dasgupta@hawaii.edu.
Her office remains unset; no fields were inferred from another unit.

Meda Chesney Lind's supplied emeritus biography is retained outside the core grid.
Meda and Ruth Dawson's emeritus information and the external affiliate/cooperating
faculty document link remain on the Faculty page. No bio was invented for Ruth.
The eight supplied core faculty/staff portraits are normalized WebPs under
`src/media/units/wgss/faculty-staff` and connected through people.json. Meda's
portrait remains the shared placeholder because no image was supplied for her.

Academic titles, roles, offices, normalized phone display/+1 tel links, email and
publication links come from shared records. No keywords are added to card sidebars.
Names/directory/bio/contact styles use the established common profile includes.

Site settings contain hero controls and the already supplied WGSS Open Graph image.
Stable student-bank heroes serve regular pages; Saunders mural assignments serve
bios. Indexing remains disabled; development layout guides remain enabled.
The existing production GTM identifier and production-host restriction are retained.
The source X account is added to shared social data.

## Tracking limits

Enabling the YouTube API makes embeds eligible for compatible video-event tracking;
it does not prove the GTM container/GA4 data stream collects those events. Confirm
video engagement settings and real events after production deployment.

References: [YouTube parameters](https://developers.google.com/youtube/player_parameters),
[GA4 enhanced measurement](https://support.google.com/analytics/answer/9216061?hl=en).

## Verification

- Shared checks and WGSS build/verification pass: 28 pages, 7 core faculty,
  7 YouTube embeds, local links/assets/fragments, metadata, image alt and heroes.
- 252 paragraph/list-item source comparisons passed, accounting for approved
  extraction and mechanical cleanup. No source tables occurred in inspected pages.
- An isolated `/wgss/` GitHub Pages prefix build and verification passed.
- Preview server responds HTTP 200 at localhost:8090.
- A second cleanup scan produces zero patches; the report is
  [wgss-text-cleanup-report.md](wgss-text-cleanup-report.md).

Reference URL inventory/report are in `wgss/reference`. Migration generation is
recorded in `scripts/migrations/wgss-wordpress.py`; do not rerun over editorial work.

Next: Courses write-up; optional Meda portrait and Monisha office; visual/editorial
review and production analytics check. Ayu intentionally has no biography page.
