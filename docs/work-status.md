# Current work handoff

Updated November 12, 2026 (Pacific/Honolulu).

## November 12: SSRI social preview origin corrected

- Published GitHub homepage advertised university-domain /ssri/ image URL, which
  is the wrong deployment host. Actual GitHub image returns 200 image/jpeg.
- Added SITE_ORIGIN https://cssweb-stack.github.io to SSRI deployment workflow,
  matching PUBA's established setting. Production site URL remains unchanged.
- Repositories: ssri (fix), css-shared (handoff). Push workflow change to rebuild;
  message previews may cache old metadata. No commit/push/deployment performed.

## November 12: RTRF report redirected to confirmed dashboard replacement

- User confirmed Looker Studio College/SSRI Funding Levels dashboard replaces the
  old reporting; /rtrf-fy2019/ now maps directly to supplied HTTPS URL.
- Supersedes retirement decision below. Inventory: five unchanged, ten moved,
  zero retired/unresolved. Generator supports validated external HTTPS destinations
  without adding preview prefix; internal target checks remain unchanged.
- Build/shared/SEO checks passed; generated external destination, canonical,
  fallback and preview-prefix handling verified. Unsafe URL checks passed.
- Repository: css-shared. No commit/push/deploy.

## November 12: RTRF FY2019 retired — decision closed

- User confirmed /rtrf-fy2019/ is an obsolete report: return custom 404, no redirect.
- Updated migration mapping and comparison JSON/CSV/report. Final inventory:
  five unchanged, nine moved, one retired, zero unresolved. Earlier pending notes
  below are superseded by this decision.
- Repository: css-shared. No page created; no deployment required for existing 404
  behavior. Indexing remains disabled until production launch is authorized.

## November 12: SSRI helper lines off

- Set SSRI site-settings.json layoutGuides to false; other units unchanged.
- User confirmed deployed redirects and custom 404 work on the live site.
- Repository: css-shared. Push and rebuild SSRI to publish the guide setting.

## November 12: Sidebar divider optical spacing

- Browser measured all sidebar dividers at identical 12px above/8px below.
  Contact links additionally have 4px internal top padding; supplemental headings
  lacked that inset. Added matching 4px heading inset in shared profile CSS.
- Existing divider margins and office/contact spacing preserved. Applies to every
  populated bio supplemental heading, including websites/publications/awards.
- Shared checks and SSRI build passed.
- Repository: css-shared. No commit/push/deploy.

## November 12: Central website icon text treatment

- Replaced black external globe images with inline shared SVG website links.
- Moved linked email/phone icon geometry from profile.css to special-text.css;
  reusable website-link shares those exact selectors, 1rem size, var(--icons),
  alignment, gap and padding. Removed obsolete profile-only globe rules.
- Build/shared checks passed. Browser confirmed email, phone and both globes
  compute identically: 16px icons, rgb(136,136,136).
- Repository: css-shared. No commit/push/deploy performed.

## November 12: Bio sidebar divider consistency

- Confirmed Jack's SSRI page uses layouts/profiles/faculty-profile.njk and the
  current common sidebar/identity/contact includes. No alternate template.
- Shared bio sidebars now reuse the existing thin contact divider before office
  and each populated supplemental section; removed oversized supplemental spacing.
- Removed Jack's first biography HR; recorded first-H2 exception for all future bios.
- SSRI build/shared checks passed; rendered Jack sidebar and populated/empty
  supplemental fixtures verified matching dividers and first-H2 exception.
- Repositories: css-shared and ssri. No commit/push/deployment performed.

## November 12: Final 404 simplification

- Removed moved-page listings from the shared 404 template and SSRI not-found data.
  Four primary quick links and navigation/search guidance remain. Known moves use
  generated redirects; unknown/retired URLs use genuine custom 404 responses.
- This supersedes earlier recovery-list presentation. URL inventory remains saved.
- Repository for this cleanup: css-shared. Upload shared changes, rebuild SSRI,
  verify live redirect/404 behavior, then request Siteimprove rescan.
- No commit, push or deployment performed. RTRF FY2019 decision remains open.

## November 12: Shared generated migration redirects

- Added opt-in shared URL migration generator and SSRI mapping for nine confirmed
  moves; only _site redirect HTML generated, no source dummy pages. Zero-second
  refresh, production canonical, accessible fallback; preview prefix respected.
- Guarded collisions, bad paths, duplicate sources, chains/loops, missing targets
  and conflicting statuses; stale generated outputs cleaned via ignored build cache.
- Build/nine output checks, prefix/escaping/cleanup and rejection checks passed.
  SEO checker excludes generated redirects; 15 regular/error pages pass, one existing
  OENAS title advisory. 404 recovery + quick links retained as user approved.
- Local browser confirmed /hcri/ immediately reaches its replacement and unknown
  paths retain custom HTTP 404. RTRF FY2019 remains unresolved.
  Live GitHub/production checks after publishing.
- SOP: url-migration-audit.md. Repository: css-shared; local only, no push/deploy.

## November 12: SSRI original URL comparison

- Preserved supplied 15-URL export and saved CSV/JSON comparisons under exports/ssri.
- Five URLs unchanged; nine confirmed moves added to shared SSRI 404 recovery data,
  with four general quick links. No redirect stub pages created.
- One unmatched historical RTRF FY2019 report awaits keep/archive/retire decision;
  no destination invented. All 14 current regular pages accounted for.
- SSRI build and shared checks passed. Report: ssri-url-comparison.md.
- Repository for this change: css-shared. Local only; no commit/push/deployment.

## November 12: Shared 404 template, SSRI first consumer

- Added shared pages/not-found.njk and not-found.css: 20/80 row, large Inter 900
  404 in cool accent left, H1/update/navigation/search guidance right. Existing
  shared responsive geometry; decorative number hidden from assistive technology.
- SSRI src/404.html supplies metadata/isNotFound; shared unit not-found.json owns
  current quick links and recoveryLinks (now populated by the comparison above).
  No old-to-new destinations invented; no redirect HTML pages generated.
- Shell forces noindex for isNotFound and canonical computation skips it, even
  when regular indexing is later enabled. SEO checker accounts for 404 semantics.
  Hero assignment saved; other units can adopt template without copying code.
- Local missing nested URL confirmed genuine HTTP 404 with custom body. Desktop,
  intermediate/mobile layout and main-content axe checks pass; SSRI build now
  15 pages and metadata/shared checks pass. Live hosting verification after publish
  remains pending. URL comparison completed above. Docs: not-found-pages.md.
- Repositories: ssri and css-shared; local changes only, no deployment.

## November 12: SSRI SEO review

- Reviewed 14 titles/H1s; already aligned and unique. Homepage omits repeated
  acronym intentionally; OENAS's long full-name title retained as informative.
- Replaced 13 placeholder descriptions with page-specific summaries, preserving
  Privacy Policy's existing description. Visible content, H1s, titles and URLs
  unchanged. Added self-canonical coverage via existing canonicalSections ["/"].
- Shared seo-audit.py checks built metadata, duplicates, canonical/social tags
  and H1 alignment; optional --launch catches disabled indexing. Reusable process
  docs/seo-review.md; report docs/ssri-seo-audit.md; metadata exports/seo/ssri-2026-11-12.json.
- Checker: 14 pages, zero errors, one reviewed title-length note. SSRI build and
  shared checks pass. Indexing deliberately remains off until launch. Next is
  original-URL comparison and shared 404 page when user supplies the URL export.
  Repositories: ssri and css-shared; local changes only, no commit/push/deployment.

## November 12: SSRI accessibility review

- Completed red-flag accessibility review; scope narrowed with user: Siteimprove
  owns comprehensive scans, focused shared fixes are authorized. Audit report:
  docs/ssri-accessibility-audit.md; compact evidence exports/accessibility/ssri-2026-11-12.json.
- Fixed shared desktop dropdown visibility/aria/Escape behavior, including hover
  dismissal. Bootstrap owns visible state; shared JS adds pointer hover and Escape
  handling. Fixed mobile Search text contrast (4.37 to 15.71:1) using dark text.
- 14 pages × desktop/mobile baseline: no confirmed violations. Expanded mobile
  search exposed the fixed contrast issue; keyboard testing exposed Escape issue.
  Three targeted post-fix states now pass axe; hover and keyboard dismissal pass.
  Earlier 56 reflow/text-spacing checks showed no horizontal overflow.
- SSRI/shared checks and JS syntax pass; POLS 51-page build/verify passes.
  Patterned/pseudo-element contrast and external map remain documented tool/manual
  limitations, not claimed automatic passes. No full screen-reader audit done.
- Next: SEO audit, then old-URL comparison/404, when user directs. Repository for
  this audit: css-shared only; no content edits, commit, push or deployment.

## November 12: Standard hero overlay

- Standardized all 12 non-GEO unit/college hero overlays to SSRI's
  var(--uh-green), #024731, opacity 0.33. Eleven unit settings updated; SSRI was
  already correct. Includes prepared CSS/DURP/ECON settings without starting those
  sites. Heights, images, crops, attribution and other settings preserved.
- Geography and disabled style-guide settings verified byte-for-byte unchanged.
  Shared checks now compare other units' overlay color/opacity with SSRI's.
  Shared checks pass; POLS build/51-page verification passes and rendered hero
  styles confirm the green overlay at 0.33 opacity.
  Repository: css-shared only. Local changes; unit sites need rebuilding to publish.

## November 12: SSRI opening paragraphs

- Standardized SSRI main-content section H2 dividers, including first headings:
  explicit hr.section-divider before local prose headings; 13 inserted and seven
  existing HRs classed/reused. Shared privacy/directory/service section headings
  use section-heading.njk with SSRI mainContentDividers opt-in. No new CSS rule
  needed: the named class inherits our standard HR styling and supplies a future
  styling hook. H2 typography unchanged.
- Rendered verification: 36 main section H2s have exactly one preceding divider;
  17 sidebar/card H2s excluded. All eight sidebar blocks byte-for-byte unchanged,
  and all 14 pages retain identical text. SSRI build, POLS 51-page regression
  build/verify and shared checks pass. Other units do not opt in. Repositories:
  ssri and css-shared; local changes only.

- Removed embedded strong wrappers from Grant Development's Priority H2 and a
  trailing space in TASI/PHIDC's Pacific Collaboration H3. Heading text and links
  preserved; ordinary paragraph emphasis retained. Audited all 14 source and
  rendered SSRI pages: no strong/b/em/i tags remain inside h1–h6.
- Recorded all-site rule: heading weight/style comes from shared CSS, with no
  bold/italic heading wrappers. Standard cleanup now reports heading_formatting
  via scripts/heading_formatting.py, including shared JSON HTML fragments.
  SSRI build, cleanup heading check and shared checks pass. Other sites were
  not edited. Repositories: ssri and css-shared; local changes only.

- Added reusable landscape=true variant to shared imageTextRow; wide desktop
  image/text split 20/80, retaining standard 25/75, 33/67 and mobile stack/75%
  image behavior. Converted all seven SSRI Research listing articles to that
  macro, preserving text, destinations, image alt/paths/dimensions and heading
  IDs. Redundant image-link aria-labels are represented by the identical image
  alt accessible name. Native landscape proportions retained.
  POLS square/default and reverse variants unchanged. Browser measurements:
  66 row/viewport cases across SSRI and POLS at six widths, expected column
  ratios/mobile photo sizing and no horizontal overflow. SSRI build, POLS build/
  verification (51 pages) and shared checks pass. Repositories: ssri and
  css-shared; POLS has no source changes from this update.

- Standardized five SSRI content/right-sidebar grids: HCRI, HAM, OENAS,
  TASI/PHIDC and Grant Development. Reuse shared profile-page/profile-biography/
  profile-sidebar geometry: 80/20 at 1600px+, 67/33 at 768–1599px, stacked below
  768px with sidebar images at 75%. Removed legacy content-sidebar/resource-grid
  classes; sidebar groups remain vertically stacked with normal shared gaps.
  Shared mobile rule now covers sidebar-media within profile-sidebar too.
  Text, links, image attributes and HTML structure independently verified intact
  (class changes only). SSRI build and shared checks pass. Browser checks across
  five pages × six widths (390–1800px) confirm expected ratios, stacking, mobile
  photo widths and no horizontal overflow. Repositories: ssri and css-shared;
  local changes only, no commit/push/deployment.

- Missing-diacritics review added to standard cleanup as report-only findings,
  including human-readable alt/title/aria-label and shared support text. Helper
  scripts/hawaiian_diacritics.py excludes emails/URLs/code; no automatic name edits.
  SSRI scan: 10 recommended missing ʻokina occurrences, three context-dependent
  names/titles and two additional ʻāina lookalikes. HCRI research landing heading
  and alt/aria labels confirmed missing; shared support and UHERO labels also
  flagged. Report: docs/ssri-diacritics-review.md. No content changed in this review;
  shared checks pass. This update: css-shared only; prior SSRI edits preserved.

- Standard SSRI text cleanup complete: 24 incorrect Hawaiʻi ʻokina characters
  corrected across five HTML pages (including HCRI metadata/H1). Scanned 14 HTML
  pages and 11 unit JSON files. No NBSP, extra-space, empty-paragraph or other
  mechanical fixes proposed. Repeat scan zero patches; attributes/links/tables,
  template/code text and prior intro removal independently verified unchanged.
  SSRI build (14 pages) and shared checks pass. Optional ʻāina quote/dash-label
  observations retained in docs/ssri-text-cleanup-report.md; no user action needed.
  Repositories: ssri and css-shared (report/handoff only); local changes only.

- Removed all 11 intro class instances from SSRI's opening paragraphs. Text and
  other markup verified unchanged against the clean starting checkout. No other
  site swept; shared CSS rule retained for later removal. SSRI build passes
  (14 pages), no intro class remains in SSRI HTML sources.
- Repositories: ssri, plus css-shared for the saved convention/handoff only.
  Local changes; no commit, push or deployment performed.

## November 11: SCI people phase

- Moved five program landing pages to /programs/<program>/index.html sources,
  publishing /programs/<program>/. Updated nav, central program/affiliation URLs,
  bio links, saved hero keys and original URL inventory. Removed old flat source
  pages and their five stale built files; no redirect pages created.
- Degrees dropdown now immediately follows Courses, with Undergraduate and
  Graduate landing pages under /degrees/. Preserved the existing export's seven
  undergraduate and five graduate listings/descriptions. Detail links remain
  current WordPress/external URLs until those pages are migrated into program
  folders. This structural task does not import individual degree-detail pages.
  SCI now 47 pages; local and isolated /sci/ build/verification plus shared checks
  pass. Folder and navigation order checked. Repositories: sci and css-shared;
  local changes only.

- Added Courses dropdown with the same five program labels/icons, targeting
  /courses/<program>.html. Five placeholders each have a white H1/paragraph
  section (program name, course prefix in parentheses, Courses), followed by a
  full-width gray section containing PLACE COURSES HERE. User will supply course
  content. Prefixes COM, COMG, JOUR, LIS, PACE; local page metadata and saved heroes.
  No Degrees dropdown added. SCI now 45 pages; build/verify and shared checks
  pass. Repositories: sci and css-shared.

- Removed Contact's top-right placeholder, retaining School Inquiries there.
- Added Programs dropdown and five lowercase /programs/<program>.html pages.
  Exported overview/academic/resource text retained without source images;
  links to unbuilt degree/resource/news pages remain on the current site.
  Each page reuses central office details in program-office-card.njk and a gray
  shared people grid filtered by program. Local program URLs now resolve from
  people affiliations and existing bio links; nav/icons/heroes/inventory updated.
  Mandi Hull's explicit exported LIS category supplies her program assignment;
  no assignments inferred for Cassandra or Janelle. LIS directory now includes
  five faculty plus Mandi; School Staff still lists all three staff.
  SCI now 40 pages; local and /sci/ prefix build/verify, shared checks and
  directory-membership checks pass.
  Repositories: css-shared and sci; local changes only.

## Deferred site starts

- User deferred DURP and ECON pending discussion with the dean. Finish SCI and
  polish the other existing sites first; do not start those migrations yet.

## Earlier SCI changes

- Contact top section now uses shared 80/20 desktop geometry: H1/intro left,
  School Inquiries in the right sidebar with decorative shared placeholder.
  Shared intermediate/mobile behavior retained. School Chair and Program Director
  labels use Main Office's title treatment, with linked names on separate lines.
  Central names/contact data unchanged. SCI build/verify (35 pages) and shared
  checks pass. Repositories: sci and css-shared.

- Program contact images now retain their native aspect ratios rather than the
  square portrait crop. Shared program-office-photo modifier; existing grid,
  photo styling and mobile width retained. Image files unchanged. css-shared only.

- Replaced five Contact program-office placeholders with supplied shared
  sci/programs/com, comg, jour, lis and pace WebPs. Central programs.json owns
  paths and actual dimensions. Decorative alt intentionally empty; adjacent
  program headings identify the cards. Images unchanged. SCI rebuilt and all
  35 pages verified. This update changes css-shared only.

- Support SCI heading alignment: shared program-directors component now uses
  CSS subgrid to match heading space within each visual row; full names stay
  above the photos, no hardcoded heading height. Same column breakpoints/gutters
  and mobile photo sizing. Browser checks at six widths from 390 to 1800px show
  zero photo-top offsets per row and no horizontal overflow. SCI build/verify
  and shared checks pass. This update changes css-shared only.

- Added Support SCI (/support-sci.html): H1/intro in its own white section, then
  gray band with five program directors and real photos/contact details. Reuses
  profile-card.njk and the same central directorSlug references as Contact;
  no new person records or invented giving-account links. Nav/hero/report updated.
  SCI now 35 pages; build/verification and shared checks pass. All five director
  portraits, name alt, email and bio links checked. Repositories: css-shared and
  sci; local changes only.

- Added /contact/: School Inquiries email/phone plus Wayne's linked chair listing;
  five program-office cards on the shared responsive five-across grid. Central
  programs.json owns office address/email/phone/photo and directorSlug references;
  directors' names/URLs resolve from people.json. Correct room/street/city order,
  email before phone, shared dividers/icons, decorative placeholder photos.
  Office details checked against each current program page (contactSource saved).
  Contact nav, hero and URL inventory updated. SCI now 34 pages; build/verify and
  shared checks pass, five office/director references validated. Repositories:
  css-shared and sci; local changes only.

- Connected all 30 supplied SCI portraits from shared faculty-staff media after
  lowercase/dash, trailing-number and fake JPEG suffix cleanup. Ava is now
  ava-kikut-stein.webp. Verified Patricia Buskirk/Amaral using source featured-image
  ID; mapped Jenifer Winter and Maya Soetoro-Ng aliases. Actual dimensions saved;
  image hashes unchanged. This supersedes initial placeholder portraits below.
  SCI rebuilt and all 33 pages verified; shared checks pass.
  Changes for this portrait update: css-shared only.

- New lowercase sci site: 27 published faculty, three staff, all 30 people pages
  on the existing shared bio template. Directory groups faculty into five
  programs, plus School Staff; one central people.json and programs.json.
- Source snapshot retained under exports/sci. Five draft people excluded;
  remaining school content deferred. Minimal home/privacy included: 33 pages.
  Original proposed navigation preserved before temporary Home/Directory nav.
- Placeholder portraits only; saved mural/student hero assignments and existing
  SCI Open Graph settings. Contact information, roles, 37 publication links and
  four unlinked awards imported. Affiliations support multiple programs/roles.
- All biography words retained; sole normalized comparison difference is a
  removed space before a comma in Andrew Wertheimer's text. See sci-migration.md
  and ../sci/reference/migration-report.json for source review, deferred links,
  Rich's two exported titles and Ava's Google Sites edit URL needing a public URL.
- Local and isolated /sci/ builds/verification pass (33 pages). WGSS regression
  passes (28 pages); shared checks pass. Desktop grouped directory visually
  reviewed. Local preview port 8093; Git initialized main, no remote supplied.
- Repositories: css-shared and sci. No commit, push or deployment performed.

## November 11: POLS role confirmation

- User confirmed Noenoe Silva is not Interim Undergraduate Chair; removed that
  role from her shared people record. She remains Professor. Jamaica's record
  remains unchanged. This resolves the previously recorded role conflict.
- Local POLS preview rebuilt and verified; css-shared only.

## November 11: WGSS first-pass site and cleanup

- Corrected shared profile-name hover rule: underline only an actual anchor
  with href, not the div wrapper used by unlinked people such as Ayu or staff.
  Directory/bio opt-out remains intact. Repository changed: css-shared only.
- Reran standard text cleanup after Associated Faculty import: zero proposed
  changes. Updated wgss-text-cleanup-report.md with this follow-up and clear
  distinction from initial correction counts. Shared/current WGSS checks pass;
  no source rebuild needed. Repository changed: css-shared (report/handoff only).
- Supplied associated-faculty DOCX imported centrally: 65 Affiliate Faculty,
  8 Cooperating Graduate Faculty, 15 Lecturers. Two existing emeriti retained
  on Associated Faculty. Single associated-faculty.json replaces separate emeriti
  JSON; source DOCX preserved under exports/wgss. No person/status facts inferred.
- Faculty now has Core/Associated dropdown destinations. Core moved to
  /faculty/core-faculty.html; old source/stale output index removed. Existing bios
  and Ayu's intentional no-bio setting unchanged. Navigation, hero assignments,
  URL inventory/report updated. WGSS now has 28 pages. Changed: wgss, css-shared.
- Connected all eight supplied faculty/staff portraits after lowercase/dash and
  suffix cleanup (Lisa Vallin2-1, Heijin alias), actual dimensions saved and hashes
  unchanged. Meda remains a placeholder; other people now use their real photos.
- User clarified Ayu does not want a bio: removed source and stale generated shell,
  set url:null, removed her bio hero assignment, updated report to 27 pages. Shared
  template honors explicit null without reconstructing a link. Directory details
  and photo remain. This supersedes the earlier shell approval. Repositories:
  wgss and css-shared. No push/deployment.
- User supplied Monisha Das Gupta's email: dasgupta@hawaii.edu. Added to the one
  shared WGSS people record; directory and bio inherit it. Office remains unset.
- WGSS origin connected to https://github.com/cssweb-stack/wgss.git as supplied
  by the user. Remote verified; no fetch, commit or push performed.
- New lowercase wgss repository, 28 pages and seven-person core roster. Six core
  bios imported; user explicitly approved Ayu's bio shell. Meda emeritus bio and
  Ruth's listing preserved. Contact uses Saunders and four mixed Key Contacts.
- Why Study merges four source pages. BA folder/Transnational Courses, off-menu
  outcomes, extracted grad admissions, root Funding Sources and placeholder Courses
  follow the walkthrough. Text-only import; central placeholders/data/heroes/OG.
- Six Alumni videos plus one Home video preserved in a shared responsive macro
  with API/origin parameters. Live GA4/GTM tracking still requires production check.
- Standard cleanup corrected 31 NBSPs, 2 ʻokina variants, 1 university name,
  2 repeated spaces and 3 empty paragraphs. Report in wgss-text-cleanup-report.md;
  no required user decisions. Original source and URLs preserved during cleanup.
- Shared checks, local 28-page verification, isolated /wgss/ prefix verification,
  252 source paragraph/list comparisons and repeat zero-change cleanup scan passed.
  Local preview localhost:8090 returns HTTP 200. Monisha office/email absent in source.
- Added shared migration sanitizer, video macro, unit verifier and reusable
  patch-only cleanup script. Git initialized locally; no remote/commits/push/deploy.
  Repositories changed: wgss and css-shared. Details in wgss-migration.md.

## November 11: Anthropology first-pass site

- ANTH origin connected to https://github.com/cssweb-stack/anth.git as supplied
  by the user. Remote configuration verified; no fetch, commit or push performed.
- Standard text cleanup is now a reusable checklist plus unit-neutral report
  template, linked to the ANTH worked example. Request phrase: “Run standard text
  cleanup for [UNIT].” Reports explicitly distinguish informational observations
  from required decisions. Documentation only; css-shared changed.
- Detailed cleanup findings, before/after examples, intentional exclusions and
  validation are saved in docs/anth-text-cleanup-report.md. User wants a findings
  report at the end of future cleanup sweeps as well.
- Standard text cleanup completed on 34 ANTH HTML/shared-data files plus the
  shared policies body ANTH renders: 312 accidental NBSPs replaced, 37 Hawaiʻi
  backtick/apostrophe variants corrected, 2 institution-name/kahakō corrections,
  6 em-dash spacing corrections, 3 repeated spaces and 1 space before punctuation.
  No invisible characters or empty paragraphs required removal. HTML attributes
  compared before/after; URLs and original exports unchanged. Source table
  structure preserved. Ambiguous sentence hyphens left for editorial review.
- Added reusable text-cleanup.md checklist and house style. Repositories changed:
  anth and css-shared. Shared checks pass; local ANTH preview rebuilt/verified.
- ANTH Courses now uses the four supplied shared courses/course-01.webp through
  course-04.webp top to bottom, actual dimensions 600×600. Decorative empty alt
  retained. No text/layout changes; local ANTH build refreshed. Repositories:
  anth and css-shared (supplied images and handoff).
- POLS and ANTH course-level H2s now include the user-supplied number ranges:
  Lower-Division (100–299), Upper-Division (300–499), Graduate (600–699),
  Advanced Graduate Study (700–800). Prose/layout unchanged.
- ANTH Courses: preserved user-authored H1 and all five paragraphs verbatim;
  intro in its own section, four course levels in a full-width gray band using
  the same imageTextRow macro as POLS. Shared square placeholder until course
  images supplied. Both resource-button groups remain in the section below.
  Repositories changed: anth and css-shared (handoff).
- Graduate portraits: all 25 supplied WebPs normalized and connected through
  graduate-students.json. Removed -jpg and trailing version suffixes, including
  -1-jpg; matched Carola Franzen to Carola (Kaho) Franzen. Actual dimensions saved,
  binary hashes unchanged. Local ANTH build/verification refreshed; css-shared only.
- Faculty/staff portraits: normalized and connected all 15 supplied WebPs in
  media/units/anth/faculty-staff through the one people.json. Removed trailing
  -1 and -png artifacts; matched Pat Kirch and Ty Tengan to full-name records.
  Recorded actual 333×333 dimensions (Ty 300×300); verified image hashes unchanged.
  Graduate portraits remain placeholders pending user supply. Shared checks pass;
  local ANTH build/verification refreshed. Repository changed: css-shared only.
- Locked cross-unit navigation convention: always & rather than the standalone
  word and. Updated ten labels in shared unit navigation data, including ANTH's
  Subfields & Specializations and Emeriti & Retired Faculty. Prose/headings/URLs
  unchanged. Shared validation now rejects navigation labels containing standalone
  and, preventing recurrence. Shared checks and ANTH verification pass.
  Repository changed for this follow-up: css-shared only.
- Follow-up: corrected common Saunders Hall building record, which incorrectly
  referenced Sakamaki's photo; Sakamaki's separate building record remains intact.
- Split Associated Faculty into three groups plus a dedicated Emeriti and Retired
  Faculty page with two groups. Updated navigation, heroes, former-person links,
  URL inventory, report and verification. ANTH now emits 51 verified pages.
- Local compiled POLS/ANTH CSS typography rules match: names 1.25rem/700,
  primary titles 1.125rem/600, administrative roles 1rem/500, offices 1rem/400.
  No unit-specific title override introduced; browser computation checked separately.
- Built new lowercase sibling anth from all three explicitly supplied Pages,
  People and Grad exports, preserved under exports/anth. Earlier inspection was
  stopped when requested; no generation preceded the fresh authorization.
- 50 HTML pages, 13 core bios, 25 published students, five associated groups and
  mixed contact grid with three faculty roles plus two staff. Shared people.json,
  graduate-students.json and supplied universal placeholder; no image downloads.
- Eight undergraduate dropdown entries; seven subfields; requested merged pages,
  off-menu student organizations, root Lambda Alpha; News, Courses, Degrees
  Awarded placeholders. ANTH spreadsheet buttons use shared button behavior.
- Policies source collection combines attributed PUBA and ANTH content centrally;
  wider rollout/editorial reconciliation pending. See anth-migration.md.
- Shared checks and ANTH build/50-page verification passed. Source-text audit
  matched 32 regular/merged sections. Local preview HTTP 200 at localhost:8089;
  dev server running. Seven draft students excluded; Alex Mawyer advisor unlinked.
- Local git initialized, no commits/remote/push/deployment. Changed repositories:
  css-shared and anth. Original source URL inventory/report in anth/reference.

## November 11: Reusable image-and-text rows

- User confirmed Support POLS student sidebar photo is purely decorative.
  Restored intentional empty alt; descriptive alt experiment superseded. Select
  alt based on purpose, not whether the asset is a photo. Keep the attribute.
- Reverse sidebar approved at 75% text / 25% media for all desktop widths from
  992px, replacing its 83/17 wide-screen split. Narrower and mobile behavior
  retained; normal image-left course rows unchanged. Shared CSS only.
- Support POLS now shows supplied shared sidebar/side-01.webp (600×400) above
  the Foundation logo via an optional leadImage argument, with shared photo style
  and spacing. Both images retain the 75%-width mobile treatment.
- Reverse option now applied to Support POLS: text left, linked Foundation logo
  right; same responsive proportions; mobile text first and logo at 75% width.
  Shared macro supports optional image link and image class, retaining plain logos.
  Support text and all donation URLs preserved. Shared checks and POLS build pass.
- Converted four POLS Courses rows to one shared Nunjucks caller macro; all
  headings and paragraphs retained in local HTML. Decorative photos remain in shared.
- Kept approved 2/10 wide-desktop split >=1600px; widened image columns to 25/75
  at 992px, 33/67 at 768px; stacked below 768px with images 75%, left-aligned.
- Documented request phrase and usage in image-text-rows.md. Shared checks and
  POLS 51-page build/verification passed. Chrome checked all four rows at 12 widths
  (320–1800px): correct proportions, mobile image sizing, loaded images, and no
  horizontal overflow across all 48 row/viewport cases.
  Local only. Repositories changed: css-shared, pols.

## November 11: Shared course-resource button fit

- Follow-up: centered the prefix instruction and applied the existing shared
  info-circle treatment, scoped to course resources across units.
- Shortened labels to Class Availability, Course Descriptions, UH Mānoa Catalog;
  prefix instruction retained below the buttons. Donation/course destinations unchanged.
- Three-button groups stack until their own container reaches 60rem; two-button
  variants use 40rem. Container queries adapt to future UH shell-width changes.
  Unsupported queries safely retain stacked buttons. Decorative image rows unchanged.
- Shared checks and local POLS build/51-page verification passed. Chrome viewport
  checks at 11 widths from 320–1600px found no wrapped labels or horizontal
  overflow, with all three stacking together. Only css-shared changed; no deployment.
- UH shell width still needs confirmation before further layout fine-tuning;
  viewport-based people thresholds will need a follow-up fit check afterward.

## November 11: POLS Courses supplied images

- Replaced four decorative placeholders with shared pols/courses/course-01.webp
  through course-04.webp, top to bottom. Actual dimensions 600×600; empty alt
  retained for decorative images. Page content and layout unchanged.
- Local POLS build/verification run for this change. Repositories: pols and
  css-shared (supplied media and handoff); no push/deployment.

## November 11: Measured responsive people/contact layouts

- Supersedes the three-stage trial below. Browser measurements found narrow
  five-column desktop cards and 20% office/bio sidebars caused contact wrapping.
- Shared faculty/Key Contacts now use 1 column below 768px, 2 at 768px, 3 at
  992px, 4 at 1200px, 5 at 1600px. Bio, office/map and grad-student rows use
  33/67 from 768px until 1600px, then 20/80. Mobile photos remain 75%, left-aligned.
- Removed extra independent bio padding; narrow tablet bio gutters are 1rem and
  contact links omit horizontal padding while retaining their minimum touch height.
  No contact text/font sizes reduced. Decorative course rows unchanged.
- Headless Chrome checked 70 page/viewport cases (390–1601px including boundaries):
  POLS office/Key Contacts, all 18 faculty directory cards, Kathy Ferguson and
  Noelani Goodyear-Kaʻōpua bios, and graduate listing. Zero wrapped contact links
  or horizontal page overflow in these fixtures. Local map replaced by a placeholder
  during measurement; actual Google widget internals were not tested.
- Shared checks and POLS 51-page build/verification passed. Local only;
  repository changed: css-shared. Other units inherit this on their next build.

## November 11: Three-stage shared people/contact grids locked (superseded)

- Desktop >=992px: bio, grad students and office/map 20/80; faculty and mixed
  Key Contacts five equal 20% columns. Tablet 768–991px: 33/67 or two 50% columns.
  Mobile <768px: stacked, photos 75% of available width left-aligned, text full width.
- Shared templates now enable horizontal gutters from md, not sm. Removed the
  office/map 25/75 desktop variant. Decorative POLS course rows deliberately unchanged.
- Shared checks and local POLS build/51-page verification passed. Browser visual
  resizing remains user review; no push/deployment. Repository changed: css-shared.

## November 11: POLS main donation link

- Linked Political Science Department Fund in Support POLS opening paragraph to
  the supplied fallback form, preserving designation_id=12044904 and parameters.
- Candidate short fund URL could not be verified: Foundation returned Cloudflare
  HTTP 403 to this client. Did not substitute an unverified address. Campaign
  63435 is distinct from fund 12044904. Recorded future donation-link convention.
- Changed repositories: pols and css-shared; local only.

## November 11: Cross-unit phone convention

- Standardized shared people records and remaining GEO/PSY/SOC hard-coded phone
  displays to omit the leading 1; telephone links use +1 international format.
  Shared telephone fallback now supplies +1 for ten-digit North American numbers.
- Department settings already used the approved display/link format. Publication
  icons explicitly remain off. Changed repositories: css-shared, geo, psy, soc.

## November 11: Profile typography and supplemental-label review

- Bio H1 and directory/contact H2 names share the same 1.25rem/700 style.
  Primary job titles now 1.125rem/600, above office/roles at 1rem.
- Removed redundant website suffix from Kathy Ferguson's Anarchist Women link.
- Reviewed supplemental labels across existing unit faculty records: generic
  Website/Faculty Website/Lab Website labels remain cleanup candidates. Publication
  book icons remain a proposal, not implemented. No link destinations changed.
- Shared checks and POLS 51-page build/verification passed. Local only; css-shared.

## November 11: Shared faculty bio 20/80 layout

- Individual faculty bios now use a 20% sidebar and 80% biography on desktop
  (992px onward), replacing the previous 25%/75% split across every unit.
  Existing tablet/phone behavior and shared gutters remain in place.
- Shared checks passed; refreshed the local POLS build for review. css-shared only.

## November 11: Main Office/profile contact-spacing unification

- Office had the same divider CSS but extra address margins/grid gaps and separate
  special-text links. Both Main Office and person contacts now call one shared
  contact-links macro, using the same wrapper, divider, icons and row spacing.
  Removed office's extra spacing by nesting address/contact under that wrapper.
- Shared checks and POLS build/verification passed; inspected rendered office
  classes, single divider and email-first order. css-shared only; no deployment.

## November 11: POLS Courses three-section layout

- Retained all user-authored headings and five paragraphs verbatim. H1/intro in
  their own white section; four course-level descriptions in one full-width gray
  section using standard 2/10 rows and shared gaps; existing course-resource include
  in a separate white section below. Rows stack below md.
- Uses supplied shared placeholders/temp.jpg, 500×500, decorative empty alt.
  POLS local build and 51-page verification passed. No push/deployment;
  changed repositories pols and css-shared (placeholder/convention notes).

## November 11: POLS local HTML save/rebuild recovery

- User's Courses HTML edit was correctly saved in src/pols-courses.html, but
  generated output was older and the existing port-8087 server stopped responding.
  Restarted `npm run dev` from pols; verified the four added course headings over
  HTTP and an unchanged-content save event triggered Eleventy File changed/rebuild.
- Local preview requires the dev terminal to stay running. Startup: in pols,
  `npm run dev`; edit src HTML, save, then refresh localhost:8087. No content was
  changed and no deployment was required. Session 7895 serves the local preview.

## November 11: POLS Courses root-level correction

- Moved Courses source from about-pols/pols-courses.html to src/pols-courses.html,
  with root permalink /pols-courses.html. Updated shared navigation and the saved
  hero key, plus the one-time importer. Removed only the obsolete generated
  About-path output from local _site; no redirect page created.
- Shared checks, POLS build and verification passed. Local only; changed repos
  css-shared and pols.

## November 11: POLS graduate portraits and shared 20/80 student layout

- Normalized all 27 supplied POLS cohort portrait names (lowercase, hyphens, no
  trailing versions), verified collisions and unchanged image hashes. Matched
  shortened filenames to full student names and updated centralized student JSON
  with real portrait paths and dimensions. Roster/contact/research data retained.
- Shared student template now uses desktop 20/80, tablet 4/8, stacked phone;
  name, program/study area, research, shared profile divider, email, advisers.
  Divider omitted when both contact fields are absent; optional email still hidden.
- Shared checks and POLS build/51-page verification passed. Other cohort layouts
  rebuilt locally for shared-template review. No push/deployment. css-shared only.

## November 11: POLS footer social links

- Added supplied Facebook, Instagram, and YouTube links to POLS social.json alongside X.
  Shared checks and local POLS build passed. Only css-shared changed; no push.

## November 11: equal-column development guides

- Diagnostics now recognizes plain Bootstrap `.col` alongside numbered column
  classes. Five-column people grids regain red outlines on each column without
  outlining individual name/title/contact blocks. Inset shadows preserve layout;
  existing per-unit layoutGuides controls still disable them for production.
- Shared checks and POLS local build passed. Only css-shared changed.

## November 11: shared profile text hierarchy and contact order

- Final follow-up: directory names 1.25rem/700; primary titles, administrative
  roles, and offices all 1rem, weighted 600/500/400 respectively. Supersedes the
  smaller title/role experiment that left offices oversized. Kept one contact
  divider; no second name/title rule added.

- Primary academic/job titles now semibold; administrative roles regular and
  slightly smaller. Directory names reduced to 1.125rem, preserving the shared
  minimum 1.5 line-height. Individual bio heading sizes retained.
- Added one subtle profile-contact-divider before email/phone, in shared person
  contact markup and Main Office. Main Office now lists email before phone,
  matching directory cards, mixed Key Contacts, and bio sidebars.
- Shared checks and all seven local site builds passed. POLS verification passed.
  Local review; changes are in css-shared only, no commit/push/deployment.

## November 11: POLS faculty/staff portraits

- Normalized all 18 supplied WebP filenames to lowercase and hyphens, removing
  trailing version digits. No filename collisions; original image hashes retained.
  Matched Nicole Grove to Nicole Sunday Grove. Updated the unified people.json
  photo paths and actual dimensions for 17 faculty plus Laurie Onizuka.
- Noenoe Silva's subsequently supplied 500×500 portrait is now connected too;
  all 19 people have portraits. All four Key Contacts have photos.
- Shared checks and POLS build/51-page verification passed. Local review only;
  changed repositories css-shared and pols (portrait verifier supports no photo).

## November 11: five-column people grid approved and locked

- Shared people grid now uses five equal columns at Bootstrap xl (1200px+),
  four at lg, two at sm, and one below sm. Faculty and Key Contacts share it.
  Individual bio widths and all text styles unchanged. User approved the local
  visual review and locked five across as the desktop standard for all units.
  Canonical conventions updated; bio portrait sizing remains a later task.
- Shared checks and POLS build/51-page verification passed. Local preview:
  http://localhost:8087/faculty/ and /contact.html. No commit/push/deployment.

## November 11: all 13 Open Graph images finalized

- All 13 matching JPEGs verified at 1200×630. Added final CSS, DURP, SCI, and
  WGSS site-settings Open Graph records; existing nine already point to their
  matching images. Descriptions reflect actual images and unit lettering.
- Confirmed all 13 editable PSDs are correctly located in repository-root
  design-sources/open-graph, outside published src/media and asset-copy roots.
- Shared checks and cross-unit path checks passed; existing site image settings
  unchanged from the earlier verified builds. Changes confined to css-shared;
  no commit, push, or deployment performed.

## November 11: Open Graph image catch-up

- Wired all nine supplied 1200×630 JPEGs to matching unit site-settings.json:
  ANTH, ECON, ES, GEO, POLS, PSY, PUBA, SOC, SSRI. Replaced PSY placeholders for
  POLS/ES and added ANTH/ECON settings; updated descriptions to reflect actual
  images and visible unit lettering. User image files retained without alteration.
- DURP, SCI, WGSS, and CSS still have no matching Open Graph image supplied.
- Shared checks and whitespace checks passed. Changes confined to css-shared;
  no commit, push, or deployment performed.

## November 11: POLS unified people/contact-grid pilot

- Replaced POLS faculty.json with people.json: 18 faculty and Laurie Onizuka.
  Each record owns identity/contact/photo details and explicit faculty-directory
  and key-contact visibility flags. Faculty, bios, and Contact use those records.
- Contact has one mixed grid sorted Goldberg-Hiller, Onizuka, Osorio, Saranillio.
  Uses the exact same grid/card/identity includes as Faculty; temporary staff photo
  supplied, no fabricated staff bio URL, and photo omission is supported.
  Program inquiries stay above the gray Key Contacts band. Jamaica's individual
  email stays on her card; Undergraduate Chair role recorded on her one record.
- POLS build and 51-page verifier passed. Checked 18 faculty cards, four contacts,
  surname order, no duplicate JSON, shared bio email/role, and absent staff bio link.
  Shared checks and GEO/SSRI/PSY compatibility builds passed. Existing local POLS
  preview listens on port 8087. Other units have not been migrated. No push/deploy.
- Export still calls Noenoe Silva Interim Undergraduate Chair while the contact
  roster identifies Jamaica as Undergraduate Chair; source titles retained pending
  unit confirmation. Do not silently resolve that discrepancy.

## November 11: POLS personal vs program email

- Added Jamaica's supplied `osorio2@hawaii.edu` to shared faculty JSON and her
  imported Contact listing. Moved undergraduate `polungrd@hawaii.edu` into central
  contact-inquiries.json, rendered by one shared table include on Contact above
  the people and on Undergraduate Advising. Removed the unmaintained hours link.
- This establishes personal emails on people listings and separate program-inquiry
  tables. Contact faculty/staff grid migration remains the next task.
- Changes local; no commit, push, or deployment performed.

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
