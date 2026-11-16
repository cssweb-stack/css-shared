# Current work handoff

Updated November 15, 2026 (Pacific/Honolulu).

## November 15: Approved push blocked by GitHub authentication

- User authorized css-shared first, then the five sites. Shared work committed as6eab057. Push to origin main failed: could not read Username for https://github.com: Device not configured. No usable GitHub credentials in this execution session; gh is unavailable. Remote fetch works for public repositories, but does not establish write authentication. Nothing pushed or deployed.
- Five sites committed and ready: SSRI344e17a, PUBA68fbcff, SOCaa86261, ANTH554a656 (initial commit; remote main absent), ES8d8d09f. Fetched all remotes before preparing commits; existing site branches matched fetched main. No force pushes or remote history changes.
- Shared validation, builds and accessibility/SEO results recorded below. Python cache and Excel temporary lock file remain untracked/excluded in shared; actual user-edited workbook committed. Deployment workflows remain manual. Next: restore GitHub write authentication or push from the user’s authenticated terminal, css-shared first, then five sites. This status update is a local follow-up commit; remote synchronization still pending.

## November 15: Final five-site SEO checks completed

- Checked218 current content pages: SSRI16, PUBA31, SOC60, ANTH82, ES29. All five metadata audits now report zero errors: unique nonplaceholder titles/descriptions, one H1, language, configured suffix, production canonical URLs, synchronized Open Graph/Twitter fields and existing shared social images.
- ANTH initially had80 placeholder descriptions plus duplicate-description error and missing canonical configuration. Added page-specific descriptions in local front matter and canonicalSections:["/"] using existing renderer. All page bodies, protected statements, biographies, outcomes and policy wording unchanged by source comparison. Rebuilt ANTH successfully; formatter zero changes. Full outcome search title retained as approved despite length note.
- Reviewed informational title/H1 notes: approved shorter title prefixes with unit suffix, degree abbreviations, 404 wording and descriptive outcomes search title. No further heading changes. Local link/asset/fragment checks pass across all218 pages with zero missing targets.
- Indexing remains disabled on all five and every content page retains noindex. No robots.txt crawl block; no preview sitemap generated/submitted and no Google indexing request. Canonicals point to configured production domains, not preview URLs. This is local prelaunch technical SEO validation, not external ranking research or a live crawl.
- Evidence: exports/seo/{ssri,puba,soc,anth,es}-2026-11-15.json plus corresponding *-links-2026-11-15.json. Next: user-authorized push/manual publication and Siteimprove scan coverage confirmation. Nothing committed, pushed or deployed during this task.

## November 15: Final five-site accessibility pass completed

- Sequential all-page browser audits: SSRI16, PUBA31, SOC60, ANTH82 and ES29 content pages (218 total), each at320/1800px. All pages pass H1/main/lang/alt-attribute/duplicate-ID structure checks and horizontal overflow checks. SSRI/PUBA/SOC/ES have zero confirmed axe violations.
- ANTH flagged one landmark-unique issue on emeriti page at both widths: repeated Online regions shared the same accessible name. Shared profile-card supplemental section now references the person-name heading plus Online heading. Visible content unchanged. Only ANTH currently enables directoryShowOnline. Rebuilt ANTH; targeted emeriti recheck passes at both widths; no other ANTH violations. Formatter reports zero changes.
- Every unit passes homepage keyboard skip-link/main focus transfer, desktop dropdown open/Escape, open mobile navigation/search axe scans, and homepage increased-text-spacing overflow spot check. These are representative interaction checks, not every interactive state on every page.
- Evidence: exports/accessibility/{ssri,puba,soc,anth,es}-2026-11-15.json and anth-recheck-2026-11-15.json. Original ANTH baseline retains the detected issue; separate recheck proves resolution. axe WCAG A/AA tags through2.2 plus best practices in headless Chrome. Redirect documents excluded. Contrast incompletes remain manual items; external maps/social/analytics blocked. No exhaustive alt-description, screen-reader, PDF or third-party interface review and no legal-conformance/100-percent-score claim. Development helpers hidden only within audit; saved settings unchanged.
- Next: final SEO and publication/Siteimprove coverage checks. Local only; no commit, push or deployment.

## November 15: Anthropology folder cleanup completed

- Quick source/root inventory found only disposable Finder metadata; removed six .DS_Store files including generated output. No abandoned source pages, empty source folders or duplicate review templates identified; migration reference evidence retained.
- npm clean/build passed (82 content/36 redirects). Verified old anth-courses.html, support-anth.html and undergraduate/minor-anth.html outputs absent and current home/courses/support/minor present. Local only; no commit, push or deployment.

## November 15: Four-site folder cleanup completed

- Removed disposable Finder .DS_Store files outside dependency/Git internals in SSRI, ES, SOC and PUBA; removed empty source directories including SOC undergraduate/advising-support. Archived PUBA src/hero-review.njk to exports/cleanup/2026-11-15/puba-old-hero-review.tar.gz, then removed the obsolete duplicate review source.
- Ran npm clean then build on all four sites successfully: SSRI16/10 redirects, ES29/31, SOC60/73, PUBA31/26. Verified obsolete renamed support/certificate/news outputs and PUBA hero-review.html are absent; all four homepages present. Reference evidence, dependencies and required source retained. Local only; no commit, push or deployment.

## November 15: SOC and PUBA development-folder inventory

- Read-only sweep excluding Git/dependency internals. SOC:60 HTML sources, Finder metadata, empty src/undergraduate/advising-support folder and stale _site/support-soc.html output. Keep reference (~7MB): documented migration evidence, not live source or junk.
- PUBA:31 HTML sources plus src/hero-review.njk, an older standalone development hero-review page now duplicating centralized Review functionality. Candidate to archive, not removed. Finder metadata and stale _site/support-puba.html plus _site/about/puba-news.html output also found.
- Nothing moved/deleted or bundled. Clean builds before publication should remove obsolete generated URLs; no build/deployment run during this inventory. Reported candidates to user.

## November 15: SSRI and ES development-folder inventory

- Read-only sweep of both repositories excluding dependency/Git internals:16 SSRI and29 ES source pages, root files/scripts/reference dependencies and empty/temp-file candidates. No empty source folders or obvious abandoned source pages found. Dynamic shared navigation/profile/footer references mean literal-link absence alone was not treated as unused content.
- Found Finder .DS_Store metadata in both roots, .github and src (plus SSRI generated output). ES _site still contains obsolete support-es.html and undergraduate/certificate-es.html output from recent source renames; these are build leftovers, not source pages. A future clean build should remove these before publication.
- ES reference folder (~852KB) retains original export/migration evidence; verify-site.py actively reads two JSON files, so do not move the whole folder as junk. node_modules, _site and .shared-state.json are normal development/build artifacts. Nothing moved/deleted or bundled; reported small candidates to user. No build or deployment performed.

## November 15: Anthropology approved naming refinements

- All page search-title suffixes now Anthropology | UH Mānoa. Renamed anth-courses.html → courses.html, undergraduate/minor-anth.html → undergraduate/minor.html and support-anth.html → support.html; updated source references, navigation, hero keys, unit includes and existing redirect destinations. No new redirects.
- Support H1 spells out Anthropology; Subfields & Specializations and Policies & Procedures use approved ampersands. Outcomes search title expanded to BA Student Learning Outcomes & Institutional Learning Objectives; short H1 and outcome copy retained. Homepage authored wording unchanged, internal paths updated only.
- ANTH build passed (82 content/36 redirects); rendered sample titles, new paths and short outcomes H1 verified; formatter zero changes. Local only; no commit, push or deployment. Review refreshes on its next build.

## November 15: Sociology approved naming refinements

- Applied approved Courses, Faculty, Support, News & Events, current graduate cohort and MA/PhD Requirements & Progress heading/title changes. Renamed support-soc.html → support.html; updated navigation, hero key and existing legacy redirect destination. Degree subnavigation now uses matching Requirements & Progress labels. No new redirects; other page wording preserved.
- SOC build passed (60 content/73 redirects); formatter zero changes. Local only; no commit, push or deployment. Review headings refresh on next Review build.

## November 15: ES approved naming refinements

- Courses H1 now Ethnic Studies (ES) Courses; Support H1 now Support Ethnic Studies. Renamed support-es.html → support.html and undergraduate/certificate-es.html → undergraduate/certificate.html; updated internal references, navigation, hero keys and existing legacy redirect destinations. News H1/search title now News & Updates. No new redirects.
- ES build passed (29 content/31 redirects); rendered headings and certificate output verified; formatter zero changes. Protected history and outcomes sources unchanged. Local only; no commit, push or deployment. Review data refreshes on its next build.

## November 15: PUBA headings, titles and shorter preview paths

- Applied seven approved H1/search-title alignments: Courses, Faculty, Graduate Applications & Admissions, both graduate certificates, Support and News. Renamed support-puba.html → support.html and about/puba-news.html → about/news.html; updated navigation, hero keys and existing legacy redirect destination. No new redirects; existing26 retained. Associated Faculty and other pages unchanged in wording.
- PUBA build passed (32 content/26 redirects), seven rendered headings/titles verified; formatter zero changes. Review heading/hero data should be regenerated on its next build. Local only; no commit, push or deployment.

## Next review: five completed sites

Scope: SSRI, PUBA, SOC, ANTH and ES. User considers current content presentable; avoid further open-ended polishing.

1. Clean each site folder: check obsolete development pages, empty folders and unused relics. Verify references before removing anything; preserve required source, assets, redirects and user work.
2. Run accessibility checks and resolve findings, retaining protected content/data.
3. Run final SEO checks, including preview indexing controls, titles, headings, links, canonicals and sitemap configuration.
4. Push and manually publish for Siteimprove scanning; confirm scan coverage and address concrete findings, aiming as close to100 as practical without claiming automated scores prove full compliance.

These are review previews, not a search launch: do not submit to Google or request indexing. Preserve crawler access needed for Siteimprove while keeping search indexing disabled. User may later unpublish until the meeting; no unpublish action requested yet. Pending work only; no push, deployment or scan performed for this plan.

## November 15: Anthropology language check

- Reviewed82 page sources. Corrected clear grammar, institutional third-person voice, generic capitalization, university shorthand and known Hawaiian spelling; added missing generic graduate-role Contact links. User approved NTH488 → ANTH488. No factual refresh, date/credit/eligibility changes or inquiry rerouting.
- Homepage statement, faculty biographies, BA outcomes page and graduate learning-outcome blocks preserved. Source checks across82 pages confirm numeric values, IDs and existing link destinations retained. Dated donor narratives and ambiguous policy wording left intact.
- ANTH build passed (82 content/36 redirects); formatter reports zero changes remaining. Local only; no commit, push or deployment.

## November 15: PUBA deadline clarification

- User confirmed April30 and November1 are two annual deadlines. Corrected prior unresolved-date note and convention; no page date or admission-season edits. Documentation only, no build required. Local only; no commit, push or deployment.

## November 15: PUBA language check with accreditation protection

- Reviewed32 HTML/Nunjucks sources. Ten ordinary pages received small voice, grammar, known Mānoa spelling, label-colon, generic capitalization and prose-dash corrections. User approved Supports students to complete Wood scholarship sentence. No new factual claims, numerical changes, course requirement changes or inquiry rerouting.
- Both NASPAA pages, all13 tables, alumni-network page, mission/values page, MPA learning outcomes, testimonials and faculty biographies are byte-identical to pre-task sources. All existing links, IDs and numeric values preserved. User subsequently confirmed April30 and November1 are the two annual deadlines; both retained. No unresolved date conflict.
- PUBA build passed (32 content/26 redirects); protected-source/table and link/number checks passed. Formatter reports zero changes. No separate report, accreditation-data update, SEO or accessibility claim. Local only; no commit, push or deployment.

## November 15: Sociology language check

- Reviewed60 local page sources, treating faculty biographies, course titles and learning-outcome content as protected. Twenty pages changed for clear grammar (criteria are, course definitions, thesis defense against), generic capitalization, consistent explanatory label colons, time notation, known Mānoa spelling, and18 missing graduate-chair Contact links. Academic thresholds, dates, numeric values, existing destinations and non-link structure preserved by source comparison. Existing user README/major-page work retained.
- Biographies and BA SLO page byte-identical; MA/PhD SLO bullets not rewritten. Conflicting historical course titles/proper scholarship-name spellings left as source, with no factual refresh. No edits to Anthropology/PUBA or accreditation content.
- SOC build passed (60 content/73 redirects). Formatter reports zero changes remaining; protected source and links/numbers/structure checks passed. No separate report, SEO or accessibility pass claimed. Local only; no commit, push or deployment.

## November 15: Ethnic Studies language check

- Reviewed29 local page sources, ES-specific policy statements and displayed unit data. Seven pages received small generic-subject capitalization, sentence-label case, time notation, requirement punctuation and repetition corrections. Certificate delivery options condensed without changing modes; BAM junior-year timing/grade conditions retained. No course titles, credit values, dates, links, IDs, role assignments or contact routing changed.
- User declined SLO copy edits: entire learning-outcomes page unchanged; protected exception recorded. Our History, Our Way and faculty pages byte-identical to task baseline, preserving existing user history edit. Three unit-authored policy statements left untouched. No factual refresh or shared policy/privacy rewrite performed.
- ES build passed (29 content/31 redirects). Checks confirm links/IDs/numeric values preserved and protected pages unchanged. Formatter reports zero remaining changes. No separate report. Local only; no commit, push or deployment.

## November 15: SSRI language check

- Reviewed16 local pages and SSRI-owned displayed unit text, preserving common policy/privacy bodies. Edited9 pages for institutional third-person voice, known Hawaiian spelling, obvious grammar/capitalization, meteorological typo and consistent service-label emphasis. Applied user-approved HCRI scientists ending and comma separating Sociology from Urban & Regional Planning in coverage data. No contact routing, URLs, IDs, numerical values or dates changed.
- User explicitly preserved October2020 boilerplate. Both Jack Barile and Greg Chun biographies unchanged, including dated biographical claims pending their owners’ updates. Historic OENAS project titles and other factual claims not revalidated. Separate unresolved observation: OENAS calls a link a national American Evaluation Association directory but href points to h-pea.org/directory; left untouched for link review.
- SSRI build passed; source checks confirm links/IDs/numbers preserved and boilerplate/biographies byte-identical. Formatter reports zero changes needed. No separate report generated, no SEO/accessibility pass claimed. Local only; no commit, push or deployment.

## November 15: PUBA code formatting pass

- Reviewed32 editable HTML/Nunjucks source files;26 formatted. No local CSS files. Existing README edit preserved. PUBA build passed (32 content/26 redirects);58 rendered pages preserve tag/attribute structure and normalized wording. Repeat formatter zero changes. Grade C → A for scoped source formatting. Shared generic templates/CSS not swept; no standalone report. Local only; no commit, push or deployment.

## November 15: SSRI code formatting pass

- Reviewed16 local HTML pages;12 formatted. No local CSS/Nunjucks files. Existing fiscal content edit preserved. Build passed; repeat formatter zero changes. Compared26 rendered HTML pages: wording/links/structure preserved after accounting for old Jack output’s two globe icons, already removed by earlier approved shared-template change and now refreshed. Grade C → A for scoped formatting. Shared generic CSS/templates not swept; no standalone report. Local only; no commit, push or deployment.

## November 15: Ethnic Studies code formatting check

- Reviewed29 local HTML pages and ES-specific policies include (30 files). Formatter found no changes needed; no source files modified. No local CSS/Nunjucks to sweep. ES build passed (29 content pages/31 redirects). Grade A → A, already clean under scoped formatter. Shared generic templates/CSS excluded. Local verification only; no commit, push or deployment.

## November 15: Sociology code formatting pass

- Reviewed60 editable HTML pages; only homepage required formatting. No local CSS/Nunjucks or SOC-specific shared includes to format. Existing unrelated README/major-page edits preserved. SOC build passed (60 content/73 redirects);133 rendered HTML pages retain identical tag/attribute structure and normalized wording. Repeat formatter reports zero changes. Grade A− → A: nearly clean already. Shared generic CSS/templates not swept; no standalone report created. Local only; no commit, push or deployment.

## November 15: Sociology nationalism hero

- Nationalism, Globalization and Sustainability now uses general featured51, previously unused in SOC. Replaces48 now fixed for Courses. SOC build passed; rendered path verified. Review rebuild passed. Local only; no commit, push or deployment.

## November 15: Final Anthropology duplicate check

- Hero registry checked: shared images occur only within established MA, PhD, funding, BAM, applied MA and experiential sections, plus the accepted current/pre-2022 BA pair. No unrelated accidental duplicate assignments found. Faculty universal image reuse remains intentional. Review updated to place both BA pages adjacent in primary group, current first; usage tooltip corrected to unit-wide. No hero changes. Review rebuild passed. Local only; no commit, push or deployment.

## November 15: Cultural and faculty directory heroes

- Cultural Anthropology now featured61 as requested. Emeriti uses general supporting30 and Associated uses general supporting32, both unused before assignment; avoided recently displaced07/09. ANTH build passed; three rendered paths verified. Review rebuild passed. Local only; no commit, push or deployment.

## November 15: Organization/cultural supporting replacements

- With no unused featured images available, assigned previously unused supporting graduate02 to AGSA, general21 to AUSA and general23 to Cultural Anthropology. Removed their 07/09/14 assignments without deleting pool assets. ANTH build passed; three rendered paths verified. Review rebuild passed. Local only; no commit, push or deployment.

## November 15: Fixed hero correction

- User clarified Home17 and Courses48 for ANTH, ES and SOC. Contact41 and Support22 unchanged. Updated existing convention to supersede Home48. All three builds passed; six rendered Home/Courses paths verified. Review rebuild passed. Local only; no commit, push or deployment.

## November 15: Fixed home/contact/support heroes locked

- ANTH, ES and SOC Home48, Contact41, Support22 assigned in shared unit hero records. Convention locks these against future random reassignment; GEO explicitly excluded and other units unchanged. Only three specified assignments implemented despite spoken five. Three site builds passed; nine rendered paths verified. Review rebuild passed. Local only; no commit, push or deployment.

## November 15: Honors hero and Review count correction

- Replaced Honors60 with previously unused general featured20; faculty landing retains60. Fixed Review hero counts to count all unit page groups together instead of separately by display section. This resolves missed cross-section duplicates and supersedes category-only counts. ANTH build passed; Honors rendered path verified. Review rebuild passed. Local only; no commit, push or deployment.

## November 15: Three Anthropology hero swaps

- Courses48 ↔ advising36; both current/pre-2022 BA24 ↔ honors60; Colloquia31 ↔ environmental anthropology01. Faculty landing60 unchanged. Preserved BA shared-degree image. ANTH build passed; seven rendered paths verified. Review rebuild passed. Local only; no commit, push or deployment.

## November 15: UMP and medical subfield supporting heroes

- UMP uses general supporting18; Medical Anthropology subfield replaces graduate38 with general supporting19. Both selected images were unused in ANTH before the change. Medical minor and Applied Cultural graduate38 unchanged. ANTH build passed; rendered paths verified. Review rebuild passed. Local only; no commit, push or deployment.

## November 15: Undergraduate supporting hero replacements

- Undergraduate funding uses general supporting08 and major student learning outcomes uses general supporting12. Both were unused in current ANTH assignments before selection; selected separately to avoid new duplication. ANTH build passed; rendered paths verified. Review rebuild passed. Local only; no commit, push or deployment.

## November 15: Anthropology homepage/BAM hero choices

- Homepage uses general featured17; all four BAM pages use general featured55, per explicit assignment. ANTH build passed; homepage and four BAM rendered paths verified. Review rebuild passed. Local only; no commit, push or deployment.

## November 15: Applied Cultural graduate hero

- All three Applied Cultural Anthropology pages now use graduate/supporting/38.webp as requested. ANTH build passed; three rendered assignments verified. Review rebuild passed. Local only; no commit, push or deployment.

## November 15: Anthropology code formatting completed

- Reviewed 82 local HTML pages and 3 ANTH-specific shared includes; formatted 52 of 85 files. Flush-left/no blank lines, structural/list lines, single-line paragraphs/headings and inline whitespace corrected. No local CSS files exist; global shared CSS and shared generic templates not swept. Updated existing formatter to honor current inline-template and whitespace rules rather than perpetuating obsolete behavior.
- ANTH build passed (82 content pages/36 redirects). Compared 118 rendered HTML files before/after: identical tag/attribute structure and normalized wording, including links and IDs. All 85 source signatures preserved; repeat formatter reports zero changes. No browser visual audit claimed. Formatting grade C → A for this scoped source pass (52 files needed correction before; no remaining formatter deviations after). No standalone report created. Local only; no commit, push or deployment.

## November 15: Formatting default and brief grades

- Code Formatting explicitly applies at creation/import/edit time and to generators of editable source, with affected-file check before completion. Cleanup feedback defaults to evidence-based before/after grade or already clean, build status and material exceptions; no separate report unless requested. Updated conventions. Review build passed; rendered rules verified. No site formatting sweep performed. Local only; no commit, push or deployment.

## November 15: Language & Writing Q&A applied

- Reorganized language sheet into six approved sections. Strategic institutional naming, contextual degree terms without search assumptions, Hawaiian spelling scope, sentence-case questions, matching nav/H1 ampersands and approved cleanup/intro scope now explicit. Uncertain facts/policies require questions. Updated obsolete UH Manoa shorthand convention to UH Mānoa. Review build passed; six rendered sections and key rule verified. Rules only; no unit content changes. Local only; no commit, push or deployment.

## November 15: Whitespace rules added

- Code Formatting now explicitly covers accidental double spaces, nonbreaking spaces, trailing spaces before closing tags and spaces before punctuation, preserving meaningful word separation and whitespace-sensitive content. Language sheet refers to this subsection; ownership recorded in conventions. Review build passed; rendered whitespace section verified. Rules only; no site cleanup performed. Local only; no commit, push or deployment.

## November 15: Rule conflict resolution made explicit

- Added approved flag/resolve/update-at-source requirement to Code Formatting and Language & Writing, plus general conventions. Historical records must be marked superseded rather than competing current instructions. Review build passed; both rendered rule pages contain the requirement. Read language sheet fresh for next Q&A; retained user’s UH Mānoa spelling edit. No audit of all older rule sources claimed. Local only; no commit, push or deployment.

## November 15: Code Formatting Q&A consolidated

- Rewrote canonical code-cleanup.md from user-approved Q&A into four sections: HTML & Templates, CSS, Preserve Existing Behavior, Verification. Explained soft wrap versus actual Returns, nested lists, inline template exception and grouped CSS selectors; added examples. Removed duplicates/typos and superseded CSS exclusion. Recorded accepted clarification in conventions. Review build passed; rendered sections and key rules verified. No website source formatting sweep performed. Local only; no commit, push or deployment.

## November 15: Language & Writing rule sheet

- Added editable docs/rules/language-writing.md for agreed pronouns, protected voice, Hawaiian spelling, names/acronyms, course notation, separators, punctuation, headings, lists, emphasis and links. Linked index/conventions; text-cleanup.md remains review procedure. Review Rules submenu in shared shell displays both sheets. New page reads/watches the source document directly, like Code Formatting. Review build passed (30 pages); rendered language content and Code Formatting submenu link verified. Existing Code Formatting document untouched. Local only; no commit, push or deployment.

## November 15: Anthropology unused development pages removed

- Full content-page incoming-link sweep identified only the unused combined funding overview and graduate student-organizations landing. Removed those two source/compiled pages, obsolete funding navigation data and hero entries, and now-empty source funding folder. Audience funding pages and all organization details retained. ANTH build passed (82 content pages/36 redirects); rendered links do not reference removed routes; no empty source folders remain. Review rebuild passed. Existing reviewed Excel workbook preserved. Local only; no commit, push or deployment.

## November 15: Anthropology general featured hero upgrades

- Used seven unused general featured images: minor25, medical minor26, contact41, advising48, subfields overview04, archaeology39, experiential pages47. Ten pages upgraded because existing four-page experiential grouping shares a hero. All graduate routes and assignments unchanged (asserted against pre-edit data). No new duplicate assignments between unrelated groups. Remaining general supporting pages: Colloquia, AUSA, Lambda Alpha; no unused general featured images remain. ANTH build passed. Review rebuild passed to show swaps. Local only; no commit, push or deployment.

## November 15: Anthropology Review heroes refreshed

- Rebuilt Review from current unit sources and hero assignments. Review build passed; Anthropology output includes relocated applied MA paths, custom archaeology hero and latest BA/MA headings. Local only; no commit, push or deployment.

## November 15: Main BA final text and hierarchy

- H1/local title now Bachelor of Arts in Anthropology; tightened generic intro closing sentence. Gray begins Requirements H2 and 37-credit sentence, followed by Required Courses H3 without divider. Applied approved footnote spacing, toward, unquoted fit and third-person registration instruction. Credit/course/grade/petition rules retained. This supersedes the earlier two-H2 main BA treatment; historical BA page unchanged in this task. ANTH build passed; headings, credit total, key policy values and approved copy edits verified. Local only; no commit, push or deployment.

## November 15: Anthropology minor approved text edits

- Applied four approved edits: lowercase minor in opening prose, department’s instead of our courses, Required Courses H3, third-person college-advisor note. Asterisk and following space retained on both minor pages. ANTH build passed; all four rendered edits and asterisk verified. Local only; no commit, push or deployment.

## November 15: Medical minor course categories

- Required Courses H3 now holds ANTH 301 and the theory/methods category requirements. Eligible Courses H3 precedes the original ten-course list, no longer nested under a requirement bullet. Original remaining-credit sentence, course restrictions and grades retained. ANTH build passed; three required items, ten eligible courses and balanced lists verified. Supersedes previously deferred heading proposal after user approval. Local only; no commit, push or deployment.

## November 15: Medical minor approved text edits

- Applied three approved edits: generic academic terms lowercase, fields such as phrasing, and third-person advisor note. Course list/heading structure and HSL wording retained; proposed Eligible Courses H3 not applied. ANTH build passed; rendered wording and unchanged heading verified. Local only; no commit, push or deployment.

## November 15: Why Study Anthropology rebuilt

- New Why Study Anthropology? H1/title and Why Study ANTH? dropdown. Added content-grounded intro. Full-width gray keeps original undergraduate/graduate descriptions with four shared blue undergraduate and four purple graduate program tiles, stacking responsively. Removed old courses/opportunities/graduate-student lists and Degree Offerings headings. Below gray retains honor society, undergraduate/graduate associations and adds UMP under Student Organizations & Mentoring. Honors remains in Undergraduate menu. No custom CSS. ANTH build passed; eight distinct tile destinations exist, headings/menu punctuation and removed clutter verified. No browser visual review. Local only; no commit, push or deployment.

## November 15: Anthropology homepage protected statement layout

- Original H1/intro in white, We extend the concept of kuleana and original list in full-width gray, closing Kuleana paragraph in white below. Removed empty Department News heading. Preserved all wording and emphasis, tidying inline whitespace only. Protected voice recorded in conventions; tentative image idea not implemented. ANTH build passed; section order and news removal verified. Local only; no commit, push or deployment.

## November 15: Undergraduate funding sections

- Removed section navigation and redundant Opportunities heading. Intro in own white section; original Jocelyn Armstrong award content in full-width gray under H2. University Scholarships and University Research & Travel Funding are H2s below gray with divider before second. Source research/travel scope retained rather than relabeling as teaching. ANTH build passed; nav removal and headings verified. Local only; no commit, push or deployment.

## November 15: Mentoring text review approved

- Applied three approved edits: clear mutual-benefit sentence, honors theses correction, concise participation sentence using undergraduate email list. Meeting frequency and assessment requirement unchanged. ANTH build passed; rendered edits verified. Local only; no commit, push or deployment.

## November 15: Undergraduate mentoring structure

- H1 and original intro in white section; Mentoring Activities H2 opens full-width gray containing original meeting description, six bullets and semester assessment requirement. How to Participate replaces Next Steps in white below. ANTH build passed; headings and list verified. Original substantive wording retained. Local only; no commit, push or deployment.

## November 15: Undergraduate menu order and mentoring location

- Funding Sources now follows Experiential Learning; Advising & Support is last. Honors unchanged and approved by user. Mentoring page exists at undergraduate/ump.html and is linked from Why Study Anthropology under ANTH Opportunities; no mentoring page edits. ANTH build passed. Local only; no commit, push or deployment.

## November 15: Both BA requirement pages simplified

- Removed redundant first requirements H2 on current and pre-Fall-2022 BA pages. Required Credit Hours and Required Courses are H2s, divider above second only; legacy IDs preserved. Current BA earlier-requirements link now second intro bullet. Academic requirements unchanged. ANTH build passed; both heading pairs and intro link placement verified. Local only; no commit, push or deployment.

## November 15: Earlier BA italics removed

- Removed remaining italics from pre-Fall-2022 BA course notes; wording retained. ANTH build passed; rendered page contains no em/i elements. Local only; no commit, push or deployment.

## November 15: Earlier BA requirements headings

- Required Credit Hours and Required Courses now plain H3s, title case without colons; 37 is its own paragraph. Existing BA return link and requirements retained. ANTH build passed; rendered headings/value verified. Local only; no commit, push or deployment.

## November 15: Applied Cultural coursework intro compressed

- Combined redundant opening and effective-date paragraphs into one sentence matching Applied Archaeology treatment, retaining Fall 2015 applicability. ANTH build passed; rendered intro verified. Local only; no commit, push or deployment.

## November 15: Field schools note and nav contrast

- Removed field-school department review note at user request; source descriptions retained. ANTH build passed; rendered note absent. Calculated shared nav blue #0a58ca on #f7f7f7 at 6.01:1, above WCAG AA normal-text minimum 4.5:1. Contrast calculation only, not a full accessibility/conformance audit. Local only; no commit, push or deployment.

## November 15: Generic gendered pronouns removed

- PhD outcomes use their (two instances); exams use they do not. Corrected adjacent he student typo to the student. Named-person pronouns retained. ANTH build passed; source search confirms no his or her, he or she or him or her phrases remain. Local only; no commit, push or deployment.

## November 15: Professional organizations and pronoun search

- Networking heading changed to Professional Organizations; ANTH build passed and heading verified. Read-only source search found generic his or her twice in PhD overview outcomes and he or she once in PhD comprehensive exams. Pronouns about named individuals also occur in bios, donor histories and supplied medical caption; retained. No pronoun edits made in this search task. Local only; no commit, push or deployment.

## November 15: Internship subsection hierarchy

- Removed course-name emphasis and newline before period from intro. Time Commitment now H3 without preceding divider, remaining within ANTH 379 requirements. ANTH build passed; rendered heading, divider removal and intro punctuation verified. Local only; no commit, push or deployment.

## November 15: Experiential Learning title alignment

- Four H1/local titles now Experiential Learning: plus exact nav topic. Independent Study removes unrelated opening sentence and course-name italics, fixes spacing before period, and labels gray section ANTH 399 Requirements. Requirement list unchanged. ANTH build passed; four rendered H1s and targeted cleanup verified. Local only; no commit, push or deployment.

## November 15: Lambda Alpha structure

- Intro in own white section; removed Details heading. Full-width gray contains four H2 groups (undergraduate membership, graduate membership, cost, graduation), dividers except first. Membership Contacts replaces Next Steps in white below, retaining two original contacts. Personal Kerton email vs program inbox inconsistency left for department clarification; no routing changes made. ANTH build passed; headings, separators and both email addresses verified. Local only; no commit, push or deployment.

## November 15: Student organization order and AUSA structure

- Why Study organizations now honor society, undergraduate, graduate per explicit user order. AUSA has complete plain-text intro without user-reported dead external link; original four opportunity bullets in full-width gray under Opportunities H2; email contact below. AGSA unchanged and approved by user. ANTH build passed; ordering, heading and dead-link removal verified. Local only; no commit, push or deployment.

## November 15: Applied Archaeology overview and intro

- Overview H1/local title now Applied Archaeology: Overview. Combined coursework intro and effective-date paragraphs into one concise sentence retaining Fall 2024 applicability. Advising/completion unchanged. ANTH build passed; rendered H1 and combined intro verified. Local only; no commit, push or deployment.

## November 15: Applied Archaeology custom hero

- Assigned supplied media/heroes/anth/applied-archaeology.webp to all three applied archaeology pages, retaining crop settings and adding accurate image description. ANTH build passed; all three rendered hero paths verified. Local only; no commit, push or deployment.

## November 15: MA alternative tracks bullet

- Separated final overview sentence into its own bullet below intro, preserving both applied-track links and removing the space before the period. ANTH build passed; rendered bullet and punctuation verified. Local only; no commit, push or deployment.

## November 15: Anthropology guides temporarily off

- Set ANTH layoutGuides false for user visual review. ANTH build passed. Other sites unchanged; restore when requested. Local only; no commit, push or deployment.

## November 15: Ann Dunham scholarship list

- Broke three inline numbered study areas out of the second scholarship paragraph into an ordered list. Original wording retained; following fund-use sentence now a separate paragraph. ANTH build passed; three rendered items and remaining fund-use text verified. Local only; no commit, push or deployment.

## November 15: Graduate funding heading alignment

- Removed funding nav introduction on all six pages. H1/local titles now Graduate Funding: followed by exact nav topic: Overview & Residency, Achievement Scholarships, Travel Awards, Research & Writing, Assistantships & Apprenticeships, Named Awards. URLs/body copy retained. ANTH build passed; six rendered H1s and nav introduction removal verified. Local only; no commit, push or deployment.

## November 15: PhD heading/navigation alignment

- Removed PhD nav intro; nav labels now Overview, First Year, Advising, Committees & Candidacy, Requirements & Progress, Exams, Dissertation, Publication, Research & Meetings. Eight H1/local titles use Anthropology PhD: plus exact nav label. User clarification pending whether spoken final label Wrap means changing Research & Meetings; retained existing final label until answered. ANTH build passed; eight rendered headings and nav intro removal verified. Filenames/body copy unchanged. Local only; no commit, push or deployment.

## November 15: MA Plan B italics

- Removed italics from final-examination form name, retaining italics on four journal titles only; OR between journal titles is plain text. Tidied inline link/list source line breaks. Existing Plan B (Papers) title/nav retained; Scholarly Papers already labels content. ANTH build passed; rendered italic elements verified as journal titles only. User approved Plan A page. Local only; no commit, push or deployment.

## November 15: MA requirements readability

- Simplified gray headings to Degree Requirements and Course Requirements. Converted the opening general requirements paragraphs into nine bullets with original wording, thresholds and links retained. H1/nav remain Requirements & Progress per locked pattern; lower content unchanged. ANTH build passed; headings and rendered nine-item list verified. Local only; no commit, push or deployment.

## November 15: Student organizations on Why Study Anthropology

- Added a grouped Student Organizations section linking AGSA, AUSA and Lambda Alpha with brief source-based descriptions; removed their scattered duplicate links on that page. Removed Graduate dropdown Student Organizations item, leaving eight entries. Organization detail pages and former graduate organizations landing retained. Updated accepted navigation convention to supersede nine-item decision. ANTH build passed; three section links, remaining graduate-study content and eight-item nav verified. Local only; no commit, push or deployment.

## November 15: Applied MA tracks moved to Graduate

- Moved both three-page applied MA tracks into graduate/applied-archaeology and graduate/applied-cultural-anthropology. Updated current ANTH source links, nav, hero keys, existing redirect targets/fragments; added six redirects from former About page routes. Graduate dropdown now nine items with separate funding and organizations. No academic content changed. Review classifier updated for new paths. ANTH build passed (84 pages/36 redirects); all six new pages and old-route redirect outputs verified. Local only; no commit, push or deployment.

## November 15: MA Plan A/B labels refined

- Nav labels and matching H1/local titles use Plan A (Thesis) and Plan B (Papers), leaving one colon after Anthropology MA. Updated accepted convention. ANTH build passed; both rendered H1s verified. Local only; no commit, push or deployment.

## November 15: Anthropology MA navigation locked

- Standardized seven MA nav labels in requested order; each H1/local title now Anthropology MA: plus the exact nav label. Removed MA nav introduction through its data setting. Filenames, URLs and policy copy unchanged. Accepted scope/pattern recorded in conventions. ANTH build passed; all seven rendered H1s and absence of nav intro verified. Local only; no commit, push or deployment.

## November 15: Applied Cultural outcomes resolved

- User approved using the six outcomes supported by supplied MA Plan B (Applied Cultural) Evaluation Rubric DOCX. Removed nine-item duplicate and review notes; corrected outcome two to rubric wording. Other five outcomes retained. Rubric link now uses standard info treatment; legacy anchors retained. ANTH build passed; six outcomes, corrected wording and info treatment verified. Supersedes earlier duplicate-outcome confirmation flags. Local only; no commit, push or deployment.

## November 15: Applied track callouts on all pages

- Added matching coordinator/application callout above course widgets on coursework and advising/completion pages in both applied tracks; overview callouts retained. Cultural overview H1/title now Applied Cultural Anthropology: Overview. ANTH build passed; all six pages have exactly one callout with the correct coordinator; revised H1 verified. Local only; no commit, push or deployment.

## November 15: Applied Cultural coursework readability

- Gray heading shortened to Requirements. Opening requirements split into five bullets with credit, grade and enrollment rules retained. All six subsections use H3; shortened Other Courses heading and retained its advisor/interest qualification in prose. ANTH build passed; list count and heading hierarchy verified. Local only; no commit, push or deployment.

## November 15: Applied Cultural overview placement

- Moved original About the Applied Program paragraph into intro; moved Fall 2015 effective date to coursework intro, removing only the obsolete positional word above. Replaced Next Steps with matching large info callout linking Ty P. Kāwika Tengan and Applications & Admissions above course widgets. Both outcome lists and review notes retained for later review. ANTH build passed; placements, callout and two outcome lists verified. Local only; no commit, push or deployment.

## November 15: Applied Archaeology date and contact links

- Moved the original Fall 2024 curriculum effective-date sentence from overview to coursework intro. Scanned all three track pages; linked all three graduate specialist mentions to Contact. Committee chair references remain unlinked because they refer to individual student committees, not the graduate chair. Existing James Bayman profile link retained. ANTH build passed; date placement and three rendered Contact links verified. Local only; no commit, push or deployment.

## November 15: Applied Archaeology overview placement

- Moved original About the Applied Program paragraphs into the white intro, retaining wording, effective date and legacy anchor. Replaced Next Steps with one large info callout linking James Bayman and Applications & Admissions immediately above course widgets. ANTH build passed; intro placement, callout links and removal of old heading verified. Local only; no commit, push or deployment.

## November 15: Applied Archaeology program faculty

- Rubric link uses standard info treatment. Moved five program faculty into shared profile cards in a three-column desktop grid below gray, followed by Affiliate Faculty H2 and the original two listings. About the Applied Program content retained in place. ANTH build passed; five rendered cards, grid sizing and info treatment verified. Local only; no commit, push or deployment.

## November 15: Applied Archaeology outcome completed

- Restored final outcome using user-supplied wording: Practice archaeology in a fashion that is professionally ethical and culturally informed. Removed the missing-ending review note. This resolves the earlier incomplete-outcome flag. ANTH build passed; rendered sentence and note removal verified. Local only; no commit, push or deployment.

## November 15: Applied Archaeology coursework readability

- Converted the first requirements paragraph into six bullets, preserving wording, numeric requirements and residency link. ANTH build passed; rendered six-item list verified. Local only; no commit, push or deployment.

## November 15: Medical anthropology minor final review

- Changed Minor Requirements H2 to Requirements only. ANTH build passed; rendered heading verified. User approved the rest of this page. Local only; no commit, push or deployment.

## November 15: Anthropology minor final review

- Changed Minor Requirements H2 to Requirements only. All other page content retained. ANTH build passed; rendered heading verified. User approved the rest of this page. Local only; no commit, push or deployment.

## November 15: Medical Anthropology photo

- Renamed supplied photo to nicu-counseling-nepal.webp without changing bytes. Added single image above courses in gray at the same gallery column sizing, with supplied caption and descriptive alt text. ANTH build passed; caption, placement, alt text and copied asset verified. Local only; no commit, push or deployment.

## November 15: Environmental Anthropology photos

- Renamed four supplied images to concise lowercase hyphenated filenames without changing image bytes. Added matching four-column responsive gallery above courses in gray, with supplied captions and descriptive nonempty alt text. ANTH build passed; rendered order, four captions, alt text and copied assets verified. Local only; no commit, push or deployment.

## November 15: Cultural Anthropology photos

- Renamed four supplied WebPs to lowercase hyphenated person names, preserving file bytes. Added captioned four-column desktop gallery above courses in gray, matching Archaeology responsive sizing; captions retain requested order. ANTH build passed; four captions, ordering and copied assets verified. Local only; no commit, push or deployment.

## November 15: Biological Anthropology photos

- Added both supplied 430×242 images and exact captions above Related Courses in gray, using the same responsive four-column desktop sizing as Archaeology. Existing lowercase filenames retained; alt descriptions included. ANTH build passed; rendered order, column class and copied assets verified. Local only; no commit, push or deployment.

## November 15: BAM FAQ GRE cleanup

- Removed the highlighted non-BAM GRE requirement sentence and department review note at the user’s request. Retained the BAM no-GRE answer. ANTH build passed; rendered removal verified. Local only; no commit, push or deployment.

## November 15: Archaeology fieldwork photo row

- Renamed4 supplied430x242 WebPs to lowercase concise hyphenated filenames, preserving byte hashes. Added standard Bootstrap4-column desktop/2-column tablet/1-column mobile figure row above Related Courses in gray, in requested caption order. Native dimensions, alt descriptions and supplied captions included; no new CSS. Courses/faculty unchanged.
- ANTH build passed;4 captions, intended ordering, responsive column classes and gallery-before-courses placement verified. Local only; no commit, push or deployment.

## November 15: Shared heading/row spacing repaired

- Scoped primary-column last-child margin trimming to final section row, preserving H2 bottom margin when a heading-only row precedes content. Consecutive image rows subtract Bootstrap gutter from3rem margin so visible spacing stays3rem rather than72px. No unit-specific CSS added; article-wrapper spacing unchanged.
- ANTH build/shared checks passed. Chrome1800/390 on subfield landing verified both H2 bottom margins and heading/image gaps16px, consecutive visible row gap48px, no horizontal overflow. Local only; no commit, push or deployment.

## November 15: AGSA intro acronym repetition removed

- Intro starts AGSA is because full name/acronym already defined in H1. ANTH build passed; rendered opening verified. Local only; no commit, push or deployment.

## November 15: AGSA page hierarchy

- Intro now identifies AGSA/Department/College/University in own white section. Gray section has Goals with2 original numbered items, Activities and Campus Events with original activity bullets, and Officer Elections (replacing Next Steps), separated by HRs. Existing election text retained.
- ANTH build passed; original goals/activity lists,3 H2s/2 dividers and institutional intro verified. Local only; no commit, push or deployment.

## November 15: Student organization media

- Replaced AGSA placeholder with shared blue tile/people icon and Lambda placeholder with user-provided750x750 lambda-alpha.webp logo. Shared imageTextRow tile now supports optional icon, default mortarboard unchanged for existing degree tiles.
- ANTH build and shared checks passed; rendered blue AGSA tile/logo and absence of placeholders verified. Local only; no commit, push or deployment.

## November 15: Graduate student organizations landing

- Added graduate/student-organizations.html using Sociology’s intro/gray image-row pattern, with linked AGSA and Lambda Alpha descriptions based on existing source pages. Alphabetical AGSA then Lambda; temp.jpg placeholders pending logos. Graduate dropdown includes Student Organizations after Current Cohort. Existing AGSA detail and root Lambda Alpha pages retained; new page temporarily reuses AGSA hero pending selection.
- ANTH build (84 content pages) and shared checks passed; two rows, both destinations and menu entry verified. Review build passed; new page verified in hero inventory. Existing Excel checklist not overwritten (new page added after generation). Local only; no commit, push or deployment.

## November 15: BAM double-counted course notation

- Changed exactly6 double-counted ANTH course listings from hyphen to colon-space notation. Titles/credit policy unchanged. ANTH build passed;6 rendered listings verified. Local only; no commit, push or deployment.

## November 15: Graduate applications ampersand naming

- Graduate application H1/title now Graduate Applications & Admissions. Matching named links updated in BAM application/FAQ review note. Existing main-nav Applications & Admissions retained. ANTH build passed; rendered H1 and BAM reference verified. Local only; no commit, push or deployment.

## November 15: BAM application bullets streamlined

- Admission Requirements now Students must lead-in with four parallel bullets; junior credit definition nested under ANTH300 requirement. Final How to Apply bullet links Graduate Applications and Admissions; dual university/department material requirement nested beneath it. Existing advising/January15 instructions retained; FAQ reference links to its actual page.
- ANTH build passed; required GPA/course grade/deadline retained, nested list balance and rendered lead-in/procedure link verified. Local only; no commit, push or deployment.

## November 15: Eirik Saethre sidebar awards

- Moved3 college/university teaching awards from bio content to central people awards data; existing shared sidebar displays them below Publications without links. Original award names/years retained; other biography text unchanged.
- ANTH build passed; rendered3 plain-text sidebar awards, placement after Publications and removed body award block verified. Local only; no commit, push or deployment.

## November 15: Simple Anthropology page-review workbook

- Created exports/anth/anth-page-review.xlsx: one sheet, exactly2 visible columns (Old Page/New Page), matched pages first, old-without-match section, then new-without-old-page-match section. Page names only; names hyperlink to old live pages/new localhost8089 pages. No additional report columns.
- Used saved Nov11 page/student exports plus latest Nov15 faculty export (latest contains people/attachments only), migration inventory and current redirects to resolve changed routes.91 published old page/person/student entries match current destinations; no unmatched old entries;32 current pages have no standalone old-page counterpart. All83 current pages represented. New split pages appear in new-page section; consolidated old records may share a new destination. This is a review checklist, not final WordPress redirect approval.
- XLSX ZIP/XML validated; two-column schema and current destination coverage verified. No site edits in this task; workbook local, not committed/pushed/deployed.

## November 15: Root experiential learning pages created

- Split original undergraduate page into /experiential-learning/ (Independent Study), internships.html, networking.html and field-schools.html. Shared four-button nav above intro, open gray detail sections, existing source text/links/eligibility preserved. Field-school info note requests current availability and degree-level eligibility confirmation; original descriptions retained. Undergraduate menu/source links updated; Graduate menu unchanged. Existing hero reused across4 pages pending selection. Old route/8 section fragments redirect to corresponding new destinations. Source snapshot saved in ../anth/reference.
- ANTH build (83 content pages/30 redirects) and shared checks passed. All original substantive paragraphs/list items,4 navigation placements and unchanged Graduate menu verified. Review build passed;4 entries verified in Experiential Learning Pages group. Local only; no commit, push or deployment.

## November 15: Wider subfield images

- Added opt-in wide=true to existing shared imageTextRow macro/CSS (25/75 desktop); enabled for7 Anthropology landing rows. Default course/reverse/landscape layouts unchanged. Documented reusable variant.
- ANTH build/shared checks passed. Local Chrome verified25/75 at1800px and100/100 stacked columns at390px, no horizontal overflow. Local only; no commit, push or deployment.

## November 15: Subfields/specializations image-row landing

- Renamed7 user-provided WebPs to lowercase/hyphenated filenames with byte hashes preserved; all400x215. Landing intro now own section; full-width gray holds Subfields H2 +3 image-left rows, then HR/Specializations H2 +4 rows. Existing shared imageTextRow macro and source descriptions/links retained. Decorative row images use empty alt alongside linked descriptive headings.
- ANTH build passed; seven rows, original paragraphs, two headings and lowercase assets verified. Chrome desktop/mobile check run for row count, broken images and horizontal overflow. Local only; no commit, push or deployment.

## November 15: Applied MA tracks split into three pages each

- Applied Archaeology and Applied Cultural Anthropology now each have overview index, coursework.html and advising-completion.html within their existing About subfield directory. Shared three-button navigation above intro; original paragraphs/lists, outcomes, faculty listing and coordinator/application contacts retained. Former subsection headings promoted to H2; coursework sublabels plain H3. Existing track hero reused across each set; course widgets retained. Original source snapshots in ../anth/reference. Old URLs and original About-acronym redirects/section fragments now target corresponding new pages; contextual links updated.
- Visible Department review notes preserve both Cultural outcome lists for reconciliation and flag Archaeology’s incomplete final outcome. No unsupported policy reconciliation performed.
- ANTH build (80 content pages/29 redirects) and shared checks passed; all substantive source paragraphs/list items, section anchors and navigation placement verified across6 pages. Review build passed;3 entries verified in each separate applied-track hero group. Local only; no commit, push or deployment.

## November 15: Five Anthropology subfield/specialization layouts

- Archaeology, Biological, Cultural, Environmental and Medical Anthropology now have own intro sections, full-width gray Related Courses with existing list-columns-two class, and white Research Area Faculty contact-style people grids. New ANTH research-areas.json stores central people slugs using existing loader; no new person copies or CSS. Removed Barry Rolett only from Archaeology/Environmental membership, retaining retired profile data. Alphabetical faculty rosters:5/1/5/6/2 respectively.
- ANTH build and shared checks passed. Original intro/course text and rendered card counts verified. Chrome1440/390 checks on all5 pages: two course columns on desktop, single on mobile, no horizontal overflow. Local only; no commit, push or deployment.

## November 15: Honors track layout

- Intro heading/paragraph/benefits list now own white section; full-width gray Coursework H2 contains5 existing H3 course groups, followed by retained Next Steps requirements. Removed manual ANTH Courses block, italic markup and link-punctuation gaps. Concise white info callout links Honors Program and Anthropology Undergraduate Advising for major advisor meeting; existing course widgets retained.
- ANTH build passed; balanced wrappers,5 H3s, no italics, retained honors/major obligations and callout verified. Local only; no commit, push or deployment.

## November 15: BAM hero review group

- Grouped all4 Anthropology /undergraduate/bam/ pages under BAM Pages in hero review. Existing preview layout/assignments unchanged. Review build passed;4 entries verified together. Local only; no commit, push or deployment.

## November 15: BAM application advising route

- Meeting instruction now uses unlinked major advisor wording with parenthetical see Anthropology Undergraduate Advising (page name linked); removed direct STAR appointment link. Removed em/i markup from application page, retaining underlying course/eligibility text.
- ANTH build passed; advising reference/no direct appointment link and no italic markup verified. Local only; no commit, push or deployment.

## November 15: BAM overview/requirements/FAQ headings

- Overview H1/title now Anthropology BA/MA Pathway (BAM); Notes plain H3 without colon. Removed duplicate requirements body heading;6 detail sections now H2s with5 HRs, original anchor retained on Minimum Credits. FAQ6 questions remain H2s with5 HRs. No HR before first H2; body policy unchanged.
- ANTH build passed; overview title/Notes and6-heading/5-divider counts on requirements and FAQ verified. Local only; no commit, push or deployment.

## November 15: Anthropology BAM split

- Replaced undergraduate/anth-bam.html with undergraduate/bam/index.html plus admission-application.html, requirements-progress.html and frequently-asked-questions.html. Shared four-button nav above intro on each, gray open content, concise undergraduate-advising callout and existing course widgets. Original program policy paragraphs/list items retained; removed redundant manual courses/Next Steps blocks. Same existing BAM hero copied to all4 pages. Old route/5 section fragments redirect to matching pages/anchors; main nav/source links updated.
- Added visible Department review info note immediately after FAQ GRE answer: contradicts graduate admissions GRE-not-required statement. Existing answer retained pending confirmation; note must be resolved before publication.
- ANTH build (76 content pages/27 redirects) and shared checks passed. Original policy paragraphs/list items, navigation placement,4 callouts and visible flag verified. Review build passed; all4 BAM paths verified in hero inventory. Local only; no commit, push or deployment.

## November 15: BA reference links separated from intros

- SOC concentrations and SLO reference sentences now two bullets below BA overview; ANTH SLO reference sentence now one bullet below BA overview. Original sentence wording, destinations and ANTH legacy anchor retained; no new anthropology concentration link invented.
- SOC and ANTH builds passed; rendered intro lists verified at2/1 items respectively. Local only; no commit, push or deployment.

## November 15: Outcomes title shortened

- BA outcomes H1/title now SLOs & ILOs; full terms remain in opening sentence. ANTH build passed; rendered H1 verified. Local only; no commit, push or deployment.

## November 15: BA outcomes single-section layout

- Promoted existing full SLO/ILO heading to H1/title retaining anchor. Opening sentence links Anthropology BA directly; removed extra return sentence and gray section. Four original outcomes follow intro unchanged. Classification as both SLO/ILO remains source wording, not independently confirmed.
- ANTH build passed; one white section, no H2, linked BA and4 outcomes verified. Local only; no commit, push or deployment.

## November 15: BA requirements labels simplified

- Main gray heading now BA Requirements; earlier-cohort note retained. Required Credit Hours and Required Courses are plain H3s, with37 in separate paragraph. Removed all em/i markup from this BA source, retaining underlying course details.
- ANTH build passed; no italic markup and rendered H2/H3/credit count verified. Local only; no commit, push or deployment.

## November 15: BA earlier requirements and outcomes separated

- Created undergraduate/major/requirements-before-fall-2022.html and student-learning-outcomes.html using Sociology linked-reference pattern with Anthropology’s distinct cutoff (before Fall2022, not Sociology’s Fall2022-and-earlier). Moved original earlier requirements and all4 outcomes unchanged. BA intro links outcomes; current requirements contain earlier-cohort info link. Kept former BA fragment IDs on reference links and reused BA hero for both pages.
- ANTH build passed (73 content pages); original earlier-course list/outcome list, balanced wrappers and main-page reference links verified. Review rebuilt for new pages. Local only; no commit, push or deployment.

## November 15: Anthropology BA page structure

- Intro now own white section. Removed Program Details wrapper heading; both requirement cohorts and full SLO section now H2 sections in full-width gray, with HRs between. Removed duplicate ANTH Courses and Next Steps blocks; concise major-advising info callout on white above existing course widgets. Requirement/SLO copy and lists retained.
- ANTH build passed; balanced wrappers, original3 requirement/outcome lists, removed redundant headings and major callout verified. Local only; no commit, push or deployment.

## November 15: Medical anthropology minor structure

- H1/title now Minor in Medical Anthropology; both original intro paragraphs remain in own section. Minor Requirements in full-width gray, Coursework Must Include plain H3. Removed duplicate manual ANTH Courses/Next Steps blocks; same concise undergraduate-advising info callout on white above existing course widgets. Requirement copy/course list retained.
- ANTH build passed; balanced wrappers, retained course list, H3 and rendered callout verified. Local only; no commit, push or deployment.

## November 15: Minor callout shortened

- Shortened advising callout to Visit Anthropology Undergraduate Advising for next steps or questions about the minor. Link/style unchanged; no forced nowrap, so mobile can wrap. ANTH build passed; rendered wording verified. Local only; no commit, push or deployment.

## November 15: Minor advising callout

- Replaced Next Steps paragraphs/appointment link with standard large info-icon callout directing questions to Anthropology Undergraduate Advising. White section remains immediately above course widgets; requirements unchanged. ANTH build passed; rendered callout and removal of Next Steps verified. Local only; no commit, push or deployment.

## November 15: Anthropology minor structure

- H1/title now Minor in Anthropology. Intro in own white section, Minor Requirements in full-width gray, existing Next Steps/advising on white. Removed duplicate manual ANTH Courses block; existing course planning/resources widgets retained. Requirements/advising copy unchanged.
- ANTH build passed; balanced wrappers, section order, descriptive H1 and retained advising link verified. Local only; no commit, push or deployment.

## November 15: Undergraduate funding move and degree nav placement

- Undergraduate funding source now undergraduate/funding.html; copy retained. Main Undergraduate menu points directly there; hero, source links and legacy redirects updated, former /funding/undergraduate/ redirected. Moved navigation sections above intro on all15 ANTH MA/PhD pages, retaining existing standard wrappers and all content. Sociology nav placement unchanged.
- ANTH build passed;15 rendered navigation-before-H1 checks, undergraduate award content and direct menu target verified. Review build passed and updated undergraduate path verified. Local only; no commit, push or deployment.

## November 15: Graduate funding moved under Graduate

- Moved6 funding sources to graduate/funding, updated source links/menu/buttons/heroes and legacy redirect targets. Added6 redirects from former /funding/graduate/ routes. Shared42 hero retained. Review grouping updated and rebuilt. Undergraduate/root funding pages not relocated in this pass. Accepted structure record superseded.
- ANTH and Review builds passed;6 new source/rendered pages,6 hero entries and6 Review group entries verified. Local only; no commit, push or deployment.

## November 15: Faculty landing hero

- ANTH faculty landing /faculty/ now uses general featured60.webp. Faculty bios unchanged. ANTH and Review builds passed; rendered hero verified. Local only; no commit, push or deployment.

## November 15: Other graduate hero selections

- ANTH Current Cohort uses graduate supporting14.webp; Applications and Admissions28.webp; Degrees Awarded34.webp. Other assignments unchanged. ANTH and Review builds passed; rendered assignments and review paths verified. Local only; no commit, push or deployment.

## November 15: Review includes Anthropology404

- Rebuilt Review after ANTH404 addition; verified /404.html appears in Anthropology hero review Privacy and Policies group. Review build passed. Local only; no commit, push or deployment.

## November 15: Anthropology standard404 added

- Added root404.html using shared not-found template and unit quick links Home, Faculty, Contact in requested order. Universal Saunders02 hero applies; no new navigation item.
- ANTH build passed (71 content pages); rendered links, universal hero, noindex and no canonical verified. Hosting404 status not tested/deployed. Local only; no commit, push or deployment.

## November 15: Graduate funding hero selected

- Assigned graduate featured42.webp to all6 Anthropology graduate funding pages. Other funding/MA/PhD assignments unchanged. ANTH and Review builds passed;6 data assignments and6 review labels verified. Local only; no commit, push or deployment.

## November 15: Anthropology graduate hero groups separated

- Review ANTH hero page now has adjacent MA Pages, PhD Pages and Graduate Funding Pages sections, then Other Graduate Pages. Non-graduate funding remains separate. Existing image displays/labels unchanged; no assignments changed.
- Review build passed;7 MA,8 PhD and6 graduate funding entries verified in their sections. Local only; no commit, push or deployment.

## November 15: Anthropology hero review refreshed for funding

- Review generator now groups ANTH /funding/ pages under Funding Pages, preserving existing hero metadata/display and other categories. Rebuilt Review from current70 ANTH pages so eight funding destinations appear together for shared-image selection.
- Review build passed; Funding Pages heading and all eight paths verified in rendered heroes/anth.html. Local only; no commit, push or deployment. No hero reassignment yet.

## November 15: Named award heading hierarchy

- Retained Ben Finney and Ann Dunham Soetoro H2 award titles; all former strong sublabels now plain H3s. Moved Marti submission instruction after Finney timeline as closing sentence before next award. Original text/link destinations retained.
- ANTH build passed; H2/H3 hierarchy, no strong markup, closing position and existing destinations verified. Local only; no commit, push or deployment.

## November 15: Direct graduate funding overview restored

- Graduate funding index restored as Graduate Funding H1 with broad opportunity overview and gray residency section. First graduate funding button now Overview & Residency. Graduate main-menu entry goes directly to /funding/graduate/; undergraduate entry remains /funding/. Former residency filename redirects to index residency anchor; other topic paths unchanged. Supersedes standalone residency landing identity.
- ANTH build passed; rendered H1/nav/gray section and direct menu destination verified. Local only; no commit, push or deployment.

## November 15: Assistantship link punctuation

- Removed2 source whitespace gaps between closing links and punctuation. ANTH build passed; rendered page has no link-to-punctuation whitespace. Local only; no commit, push or deployment.

## November 15: Assistantships intro/eligibility split and hierarchy

- H1/title now GA Teaching Assistantships and Apprenticeships. Original overview before To be eligible moved into intro; eligibility/restrictions/enrollment remain first in gray under Eligibility H2 with original anchor. Teaching Assistantships, Duties, Criteria, Conditions, Closing Date and Teaching Apprenticeships are H2s with dividers. Salary and minimum/desirable qualifications are plain H3s. Removed heading-label colons/strong markup.
- ANTH build passed; intro/eligibility placement,7 H2s/3 H3s/6 dividers, unchanged lists and link destinations verified. Local only; no commit, push or deployment. Current position counts/recruitment claims retained pending department review.

## November 15: Research/writing award subheadings

- Retained broad intro and3 H2 award titles. Converted9 former strong paragraph labels to plain H3s (eligibility, fund use, MA/PhD awards, Application Deadline). Added missing periods to final April20 and online-application bullets; no award criteria changed.
- ANTH build passed;9 H3s/no strong markup and rendered punctuation verified. Local only; no commit, push or deployment.

## November 15: Travel recommendation punctuation

- Removed source newline/space between recommendation-form link and period; browser had collapsed newline to visible space. ANTH build passed and rendered adjacency verified. Local only; no commit, push or deployment.

## November 15: Travel awards first-heading divider corrected

- Removed HR above first H2 (Eligibility); retained dividers above Application Deadline and Completion. Supersedes previous three-divider treatment. ANTH build passed. Local only; no commit, push or deployment.

## November 15: Travel awards intro and headings

- Original travel-award overview moved into intro in place of generated summary. Removed duplicate gray award title; Eligibility, Application Deadline and Completion are plain H2s with HRs above each, retaining old award anchor on Eligibility. Award details/lists unchanged.
- ANTH build passed; original lists, intro placement, three headings and three dividers verified. Local only; no commit, push or deployment.

## November 15: Residency page identity corrected

- Renamed graduate funding index source/URL to funding/graduate/residency-tuition-purposes.html. H1/title now Residency for Tuition Purposes; removed generic funding intro/redundant H2 and retained residency text/anchor. Funding links, nav, hero and legacy fragment targets updated; former graduate directory URL redirects directly to renamed page. Supersedes graduate index page identity.
- ANTH build passed; renamed rendered H1 verified. Local only; no commit, push or deployment.

## November 15: Residency consolidated into intro section

- Moved graduate funding residency heading/paragraph into existing white intro section and removed gray section. Navigation, residency anchor/text/link unchanged. ANTH build passed; no gray wrapper, balanced columns and rendered residency verified. Local only; no commit, push or deployment.

## November 15: Achievement scholarships source intro and headings

- Replaced generated short intro with original award overview paragraph, moved out of gray unchanged. Gray now starts Eligibility H2 retaining anchor; Fund Use and Application Deadline H2s with HRs above. Removed redundant gray title/former strong labels.
- ANTH build passed; original lists unchanged, overview placement and three plain H2s/two dividers verified. Local only; no commit, push or deployment.

## November 15: Funding navigation above intro trial

- Moved existing graduate funding navigation section before H1/intro on all six pages. Standard section/container/row/column retained; headings, copy and gray content unchanged. Trial scoped to graduate funding; MA/PhD unchanged pending review.
- ANTH build passed; rendered navigation-before-H1-before-gray order verified on six pages. Local only; no commit, push or deployment.

## November 15: Graduate funding starts with residency

- Removed residency block from main Funding overview; retained on graduate index (H1 now Graduate Funding). Graduate navigation now starts Residency followed by five funding topics; Funding Home removed. Main overview retains two image rows and common resources. Supersedes prior shared-residency overview placement.
- ANTH build passed; six nav items/order and residency placement verified. Local only; no commit, push or deployment.

## November 15: Funding overview visual layout

- Removed overview button navigation. Gray section now contains shared residency information followed by two standard image-left rows linking Undergraduate/Graduate Funding with brief blurbs. Existing temp.jpg placeholders have meaningful linked-image labels. Common Resources on white links existing STAR and Financial Aid sources with eligibility caveat. Audience pages/details unchanged.
- ANTH build passed; no overview subnav, two image rows and intended section order verified. Local only; no commit, push or deployment. Final row images and dated external funding links remain for later review.

## November 15: Graduate funding split into six pages

- Graduate index now overview/residency, with five topic pages: Achievement Scholarships, Travel Awards, Research & Writing Awards, Assistantships & Apprenticeships, Named Awards. One shared fundingGraduate button navigation connects all six plus Funding Home. Each page has broad intro and standard gray detail section; original award copy, eligibility, amounts, deadlines and links retained. Existing graduate hero reused throughout.
- Updated legacy funding-section redirects to each specific award page/anchor. ANTH build and shared checks passed; all original links/list items retained and nine original section anchors resolve across six pages. Local only; no commit, push or deployment. Finney Summer2022 and current recruitment figures remain flagged for later department review, not silently revised.

## November 15: Anthropology funding home and audience folders

- Created funding/index.html overview plus funding/undergraduate/index.html and funding/graduate/index.html. Existing audience-specific copy moved intact apart from page titles/layout navigation; long graduate material not yet subdivided. Shared funding buttons connect all3 pages; both main menu funding links point to /funding/. Original hero assignments moved; overview reuses undergraduate funding hero pending review.
- Old funding URLs/section fragments redirect directly to corresponding audience pages; contextual source links updated. ANTH build and shared checks passed;3 destinations/nav and2 old-route redirects verified. Local only; no commit, push or deployment. Next: review graduate topic subdivisions and shared/crossover opportunities; no eligibility inferred.

## November 15: Sociology degree navigation context

- Added MA/PhD navigation intros to SOC data; shared optional intro paragraph now has subnav-intro class, also applying to ANTH. No extra CSS styling added. SOC shared annual-review return navigation remains separate.
- SOC and ANTH builds passed; correct class/text verified across26 MA/PhD pages. Local only; no commit, push or deployment.

## November 15: Degree navigation context

- ANTH MA/PhD navigation data now provides brief Explore the key components of the MA/PhD program sentence. Shared navigation include renders optional intro directly above buttons; other units unchanged without intro data.
- ANTH build and shared checks passed; correct sentence appears once above navigation on all15 program pages. Local only; no commit, push or deployment. GEO manual-only workflow remains local/unpushed; remote schedule verified still active this turn.

## November 15: Graduate inquiries replace contact grids

- Admissions, MA overview and PhD overview now reuse units/anth/graduate-contact.njk: white section below gray, large info icon and anthprog email. Standard mt-0 utility removes redundant top margin from callout; no new CSS override. Removed MA/PhD people-contact blocks without changing people/contact-page data. Supersedes graduate-chair/staff routing proposal for these overview pages.
- ANTH build and shared validation passed; all three rendered pages have exactly one margin-reset callout and no Graduate Program Contacts heading. Local only; no commit, push or deployment.

## November 15: GRE applicant voice

- Changed optional GRE-score bullet to third person: Applicants with valid scores may submit them in their application. No other copy changed. ANTH build passed and rendered sentence verified. Local only; no commit, push or deployment.

## November 15: Department nested application bullets corrected

- Both application sections now use Prospective students must lead-in. Department has four main bullets: application, GRE, English proficiency, three recommendations. Nested bullets contain optional scores/writing sample, proficiency link and required recommender form. Questions paragraph/callout unchanged. Supersedes prior application sentence outside list.
- ANTH build passed; matching lead-ins and four-list/eight-item department structure verified. Local only; no commit, push or deployment.

## November 15: Department application flow

- Replaced redundant department lead-in with application sentence, followed by GRE/language/recommendation bullets. Questions guidance now friendly paragraph below list. Review BOTH reminder moved into second deadline-area bullet as Students must complete all application requirements below. Existing callout unchanged.
- ANTH build passed; rendered reminder, application sentence and questions paragraph verified. Local only; no commit, push or deployment.

## November 15: Graduate Division application wording

- Shortened link to Graduate Division online application; two bullets now cover application and fee. Moved questions guidance into friendly Please direct paragraph below list, retaining requirements link. Other sections/callout unchanged.
- ANTH build passed; two-item list and rendered questions sentence verified. Local only; no commit, push or deployment.

## November 15: Admissions shared-inquiry callout trial

- Moved general-inquiry sentence into standard white section below gray. Reused large smile callout styling with info-circle SVG instead of smile icon. Shared anthprog address/text retained; MA/PhD people sections unchanged pending review.
- ANTH build passed; rendered callout verified. Local only; no commit, push or deployment.

## November 15: Admissions application lists

- Added HR before Graduate Division H3, three Division bullets and five Department bullets with brief lead-ins. Consolidated link punctuation; replaced verbose application link labels with descriptive subjects. Deadline, optional GRE/writing-sample language, English exemption, three-letter requirement and all destinations retained. Review BOTH reminder retained pending explicit removal decision.
- ANTH build passed; list sizes, original destinations, deadline/letter count and no link-to-punctuation whitespace verified. Local only; no commit, push or deployment.

## November 15: Graduate applications structure

- H1/title now Graduate Applications and Admissions. Intro/deadline remain white; full-width gray starts Application Requirements H2 and approved dual-requirements sentence adapted to Anthropology. Plain Graduate Division/Department H3s preserve anchors; HR above Department. Other application paragraphs, deadline and links retained.
- ANTH build passed; balanced wrappers, section order, H1 and unchanged application paragraphs/link destinations verified. Local only; no commit, push or deployment.

## November 15: MA/PhD capitalization and contact-only final pass

- Scanned all15 MA/PhD source pages; updated8 for generic department/PhD program/candidacy/fall/regulation capitalization, UHM to UH Manoa and remaining graduate chair/specialist Contact links. Preserved headings, official unit/classification names and linked form titles. No spelling, policy or broader prose rewrite.
- ANTH build passed; parser verified no unlinked graduate chair/specialist references across15 pages. Numeric content and all existing non-Contact destinations unchanged. Local only; no commit, push or deployment.

## November 15: Standalone PhD outcomes removed

- Deleted standalone outcomes source, PhD nav item and hero assignment. Overview outcomes retained. Former page URL and old monolith fragment now redirect directly to overview outcomes anchor. Supersedes retained comparison-page status.
- ANTH build passed:64 content pages/16 redirects; source/nav removal, overview outcomes and generated redirect target verified. Local only; no commit, push or deployment.

## November 15: PhD research/meeting policies

- Matched MA Research & Meeting Policies H1/title and Research & Meetings nav. Added PhD intro, reordered IRB first/remote meetings second with HR between, and changed UHM heading to UH Manoa. All original policy paragraphs/list items retained. Recorded short university-reference preference.
- ANTH build passed; rendered order/naming and unchanged policy paragraphs/list items verified. Local only; no commit, push or deployment.

## November 15: Dissertation by publication structure

- Added broad intro; gray H2 now Guidelines retaining anchor, followed by sentence-case guidelines lead-in. Linked final guideline subject instead of displaying raw URL; all12 guidelines retained.
- ANTH build passed; intro/heading/lead-in and descriptive link verified; first11 guideline items unchanged. Local only; no commit, push or deployment.

## November 15: Dissertation page structure

- Added broad intro, HRs above second/third H2s, and lowercased generic all but dissertation wording. No graduate chair/specialist mentions requiring Contact links; official Graduate Division/form titles retained.
- ANTH build passed; intro, two dividers, original links and otherwise unchanged policy paragraphs verified. Local only; no commit, push or deployment.

## November 15: Comprehensive exams capitalization/contact check

- Lowercased and linked both graduate chair references to Contact. Other body capitals are proper names/acronyms or sentence starts; retained. No specialist mentions on this page.
- ANTH build passed; two contact links and otherwise unchanged visible wording verified. Local only; no commit, push or deployment.

## November 15: Comprehensive exams structure

- Moved original opening paragraph under H1. Gray starts Bibliographies (Reading Lists) H2 retaining anchor, followed by Written Examination and Oral Examination plain H2s with HRs above. Removed redundant body title and former strong subheadings; policy paragraphs unchanged.
- ANTH build passed; three-heading hierarchy, two dividers, intro ordering and all original substantive paragraphs verified. Local only; no commit, push or deployment.

## November 15: PhD external-MA qualifier and contacts

- Moved external-MA qualification into Course Requirements H2 parentheses in sentence case, removing separate colon-led paragraph. Normalized generic candidacy/ABD and requirement-label capitalization; linked graduate chair, specialist and chair-of-program references to Contact. Supersedes previous separate qualification sentence.
- ANTH build passed; rendered heading, four contact links, numeric content and original link destinations verified. Local only; no commit, push or deployment.

## November 15: PhD requirements hierarchy

- Added broad intro. Gray starts General Requirements H2 retaining anchor; Residency Requirements, Course Requirements, Additional Requirements and Advancement to Candidacy are plain H2s with HRs above. Preserved external-MA applicability as sentence immediately under Course Requirements. Detail paragraphs/lists unchanged.
- ANTH build passed; five-heading order, four dividers, qualification and unchanged body requirements verified. Local only; no commit, push or deployment.

## November 15: PhD advising capitalization and contact links

- Added approved Cooperating Graduate Faculty Exceptions and Advisor Requests H3s, splitting interim-advisor paragraph at existing sentence boundary. Normalized generic department/role/study-plan capitalization and list starts; retained official faculty classifications, Admissions Committee and University Representative. All graduate chair/specialist references now link to Contact.
- ANTH build passed; rendered H3s, role-link count, numeric content and existing link destinations verified. Local only; no commit, push or deployment.

## November 15: PhD advising structure

- Added broad intro; PhD nav now includes Committees. Advising H2; Interim Advisor, Initial Advising Meeting, Changing Advisors plain H3s; PhD Committee and Candidacy Conference H2s with HRs above. Body detail copy unchanged.
- Suggested (not inserted): Cooperating Graduate Faculty Exceptions and Advisor Requests H3s, as on MA page. First would require splitting existing interim-advisor paragraph.
- ANTH build passed; unchanged detail paragraphs, intro, nav wording and two dividers verified. Local only; no commit, push or deployment.

## November 15: PhD first-year structure

- Matched approved MA structure: broad intro adapted to PhD, Orientation H2 preserving anchor, HR before First-Year Student Requirements H2, and three unnumbered/plain H3s with library name spelled out. All detail paragraphs and links retained.
- ANTH build passed; intro/headings/divider and unchanged requirement paragraphs verified. Local only; no commit, push or deployment.

## November 15: Program contact outer column

- Standalone shared advising/contact widget now uses standard row/col-12 inside its container, enclosing heading, intro and both people. Existing diagnostic column outline applies; embedded usage unchanged.
- ANTH build and shared checks passed; rendered PhD contact wrapper verified. Local only; no commit, push or deployment.

## November 15: PhD overview SLO hybrid approved

- Replaced duplicate competencies/outcomes display with Student Learning Outcomes, “For PhD in Anthropology:” and five bullets matching MA presentation. First outcome parenthetical now uses approved competencies list: archaeology, biological anthropology, or cultural anthropology. Other outcome wording retained. Old competencies anchor retained. Separate outcomes page/nav still exists pending consolidation.
- ANTH build passed; rendered heading, intro, parenthetical and five source bullets verified. Local only; no commit, push or deployment.

## November 15: PhD overview comparison and contacts

- Copied original PhD learning-outcomes heading/list below Program Competencies in gray with HR between. Both lists unchanged for comparison; separate outcomes source/nav retained pending decision. Removed Program Details heading and redundant ANTH Courses/Next Steps body blocks. Added existing Graduate Program Contacts component on white above course planning/resources.
- ANTH build passed; both original lists, ordering, removed blocks and rendered Jan/Marti contact section verified. Local only; no commit, push or deployment.

## November 15: Cohort spacing unified

- Shared student-details column now uses one flex gap from profile-name-gap (0.5rem), with direct-child margins reset together. Equal name/program/interests spacing; tighter email/advisor gap. Scoped to student directory, preserving faculty styling and contact target size.
- ANTH build and shared validation passed. Local Chrome measured all three gaps at8px at1440px and390px, with no horizontal overflow. Local only; no commit, push or deployment.

## November 15: Research before meeting policies

- Reordered MA policy sections and intro to match title: IRB research first, remote meetings second, with HR between. Policy content/anchors retained. ANTH build passed; rendered section order verified. Local only; no commit, push or deployment.

## November 15: MA research/meeting page structure

- H1/title now Research & Meeting Policies; compact MA nav label Research & Meetings. Added broad intro and HR before IRB H2. Existing policy paragraphs, anchors and URLs unchanged; PhD navigation unchanged.
- ANTH build passed and rendered naming verified. Local only; no commit, push or deployment.

## November 15: Plan B introduction

- Added brief Plan B intro above navigation. Confirmed content-page intro requirement in project conventions for creation/restructuring. ANTH build passed; rendered sentence verified. Local only; no commit, push or deployment.

## November 15: MA Plan B structure

- H1/title now Plan B: Scholarly Papers Requirements. Gray starts Course Requirements H2 with legacy anchor; Scholarly Papers and Final Examination Meeting are H2s with HRs above. Removed strong markup from former subheadings; requirements, three-paper obligation and links unchanged.
- ANTH build passed; rendered headings/dividers and unchanged substantive paragraphs/links verified. Local only; no commit, push or deployment.

## November 15: Course designation info treatment

- Applied existing info/icon-text paragraph classes to the MA requirements course-designation guide sentence; wording/link unchanged. ANTH build passed and rendered markup verified. Local only; no commit, push or deployment.

## November 15: MA Plan A structure

- H1/title now Plan A: Thesis Requirements with one brief intro. Removed redundant gray heading; Coursework Requirements retains its legacy anchor. Advancement to Thesis and Final Examination Meeting and Submission of Thesis are plain H2s with HRs above. No strong markup remains on this page.
- ANTH build passed; rendered headings, two dividers, existing links and substantive requirement paragraphs/list items verified. Local only; no commit, push or deployment.

## November 15: MA requirements introduction

- Added one broad intro sentence for both MA tracks above degree navigation. Requirements unchanged. ANTH build passed and rendered sentence verified. Local only; no commit, push or deployment.

## November 15: Approved MA advising-page cleanup

- Added exception/request H3s; renamed Committee Membership and Plan A Forms; split committee selection, approval and changes into three paragraphs. Normalized generic capitalization, linked six chair/specialist references to Contact, and corrected approved grammar/list capitalization. Official classifications, forms, criteria and obligations retained.
- Both overlapping candidacy-approval statements remain for department confirmation; applicability of the unqualified sentence to Plan A is unresolved.
- ANTH build passed; rendered headings, links, numeric content and retained approval statements checked. Local only; no commit, push or deployment.

## November 15: Approved MA requirements cleanup

- Renamed general/departmental requirements H2s, normalized body capitalization, linked all six chair/specialist mentions to Contact, and split elective permission from the course-substitution process. Preserved focus-area wording and PhD progression wording apart from approved capitalization/link markup.
- ANTH build passed; numeric tokens, repeated focus wording and progression text verified unchanged; rendered heading and paragraph split checked. Local only; no commit, push or deployment.

## November 15: Approved MA elective heading

- Added Elective Courses & Course Substitutions H3 above the existing elective/petition paragraph. Paragraph and anchor unchanged. ANTH build and rendered heading verified. Local only; no commit, push or deployment.

## November 15: Graduate program contacts distinguished from advisors

- ANTH MA shared contact block now Graduate Program Contacts. Intro directs coursework/research/degree planning to assigned faculty advisor. Jan's blurb covers program policies/academic procedures; Marti's covers applications/forms/administrative processes. Official identities/titles, photos and contact details retained; existing component/layout reused. Supersedes earlier Graduate Advising label.
- ANTH build passed; rendered heading/assigned-advisor explanation/Jan guidance verified and former heading absent. Local only, no commit/push/deployment.

## November 15: MA requirements hierarchy clarified

- H1/front matter now Degree Requirements & Progress (Plans A & B). Gray body starts General Course Requirements H2; Course Requirements, Additional Requirements and Progression to the PhD Program are H2s with HRs above. Moved original elective/petition note into Course Requirements and kept its former ID on the paragraph; applied-MA progression caution preserved.
- ANTH build passed; headings/dividers/note position verified. Local only, no commit/push/deployment.

## November 15: MA advising introduction

- Added one broad sentence on faculty/committee guidance supporting MA studies and candidacy to the page intro. Detail sections unchanged. ANTH build passed and rendered sentence verified. Local only, no commit/push/deployment.

## November 15: MA advising/committee heading hierarchy

- MA nav now includes full Advising, Committees & Candidacy label. Body Advising H2; Interim Advisor, Initial Advisory Meeting, Changing Advisors, Eligible Persons and Plan A Only are plain H3s. HRs above Three-Person Committee and Candidacy Conference H2s. Original detail copy/IDs retained; PhD not changed.
- ANTH build passed and rendered nav/headings/dividers verified. Local only, no commit/push/deployment.

## November 15: MA first-year introduction made concise

- Replaced detailed two-sentence overview with user-approved general sentence about shared activities/responsibilities supporting the graduate community. Detail sections unchanged. Recorded concise/nonduplicative intro principle. ANTH build passed and rendered sentence verified. Local only, no commit/push/deployment.

## November 15: Course widgets on all Anthropology MA/PhD pages

- Added existing shared course-resources include in standard white bottom section to14 subpages; retained two overview widgets,16 total. Unit catalog-courses already selects ANTH and shared Anthropology entity694. Existing pattern uses main course descriptions plus ANTH filter guidance, not an automatically filtered search URL.
- ANTH build passed; all16 rendered pages have exactly one widget, ANTH prefix guidance and the Anthropology catalog URL below gray. External catalog fetch returned403, so no external availability verification claimed. Local only, no commit/push/deployment.

## November 15: Anthropology MA first-year structure clarified

- Added brief source-based two-sentence overview. Removed duplicate First-Year Students body heading; Orientation and First-Year Student Requirements now H2s with one HR between. Colloquium, Special Events Room Maintenance and spelled-out Anthropology Graduate Reading Library Monitoring are H3s without added HRs or numbering. Preserved legacy anchor on Orientation and existing obligation details.
- ANTH build passed; heading hierarchy/HR/anchor verified. Current status of lounge/library/refreshment obligations remains unverified for department review; no new policy invented. Local only, no commit/push/deployment.

## November 15: MA outcomes heading and rubric link simplified

- ANTH MA overview H2 now Student Learning Outcomes, retaining its legacy anchor and following MA/Plan A or B context. Rubric link uses shared info/icon-text paragraph styling; label/URL and outcomes unchanged. ANTH build passed and rendered heading/icon markup verified. Local only, no commit/push/deployment.

## November 15: Sociology helper lines re-enabled

- Set SOC site-settings layoutGuides true for requested local cross-check. SOC build passed; diagnostic styles included in generated stylesheet. Other units unchanged. Local only, no commit/push/deployment.

## November 15: Advising grid diagnostic outlines

- Shared advising grid was already the standard component; diagnostics selectors omitted its CSS-grid classes. Added advising-person card and nested photo/details cells to existing red-shadow/foreground-overlay rules. No production layout or dimensions changed; same common diagnostics toggle controls visibility.
- ANTH/SOC builds and shared checks passed. Live Chrome verified six red foreground outlines across two advisors and four inner photo/text columns, with pointer-events none. Local only, no commit/push/deployment.

## November 15: Anthropology MA overview outcomes/advising integrated

- Alternative terminal-track note moved to end of single intro paragraph. Original MA outcomes/rubric moved unchanged into gray. Removed Program Details heading, duplicate ANTH Courses list and Next Steps copy per user. Added standard shared Graduate Advising block on white above existing resources, selecting Graduate Chair Jan Brunson and Graduate Specialist/Support Marti Kerton from central people records with role-specific guidance text.
- Removed standalone MA learning-outcomes source/nav/hero entry; seven MA nav items remain. Old outcomes route and original monolithic SLO fragment redirect directly to preserved overview anchor. Review refreshed. PhD/SOC overview refinements and careful PhD competency/SLO comparison remain pending, not silently applied.
- ANTH build passed (65 pages/15 redirects), shared checks passed. Outcomes block matches original text/rubric apart from heading level/whitespace. Verified intro/nav/outcomes/advisors/resources order; live Chrome1440/390 confirms two correct advisors on white, seven nav items/no overflow and outcomes URL redirect. Local only, no commit/push/deployment.

## November 15: Anthropology PhD split into nine preserved-copy pages

- Created ../anth/src/graduate/doctorate-phd/index.html plus first-year, advising-candidacy, requirements, comprehensive-exams, dissertation, dissertation-by-publication, research-policies and learning-outcomes. Shared sections/nav and Featured57 hero on every page. Original source saved in ../anth/reference/doctorate-phd-before-page-split.html. Competencies remain overview; original SLOs kept separately, no academic copy rewritten.
- Updated main nav, source links, hero mappings and migration generator. Old PhD URL/15 section anchors now direct to new destinations. Review refreshed. MA pages retain54 and existing structure.
- Verified59 paragraphs,70 list items,21 hrefs,15 section IDs and both resource includes preserved. ANTH build passed (66 pages/14 redirects), shared checks passed. Nine rendered pages verified for one H1/complete nav/57; live Chrome1440 nav one row,390 stacks/no overflow, old exam fragment redirects. Local only, no commit/push/deployment. Next: user page-by-page MA/PhD review and introductions/copy refinements when authorized.

## November 15: Anthropology MA split into eight preserved-copy pages

- Created ../anth/src/graduate/master-ma/index.html plus first-year, advising-candidacy, requirements, thesis, scholarly-papers, research-policies and learning-outcomes. Current shared sections/navigation; overview retains original intro/applied-track note/course links/Next Steps/resource includes. Original full source saved in ../anth/reference/master-ma-before-page-split.html. No copy rewrite; dated/repeated wording intentionally preserved.
- Updated ANTH main nav, two source links, migration generator and hero mappings. Every MA page uses graduate Featured54; existing PhD page now uses approved57, but PhD content/folder split is not done. Old MA URL redirects to overview, with all12 source section IDs mapped to their new destinations. Review refreshed.
- Verified67 paragraphs,27 source hrefs,12 anchors and both resource includes preserved. ANTH build passed (58 pages/13 redirects), shared checks passed. Every MA rendered page has54, one H1 and eight-item nav. Live Chrome1440 nav one row;390 stacks with no overflow. Legacy Plan A anchor redirects to thesis correctly. Local only, no commit/push/deployment. Next: user review, then PhD structural planning; later copy/voice review remains separate.

## November 15: Degree-recipient headings link directly to records

- Linked Anthropology MA/PhD H2s to their respective supplied spreadsheets and removed redundant View… action paragraphs. Copy and purple tiles unchanged. ANTH build passed; two heading links and removed duplicate labels verified. Local only, no commit/push/deployment.

## November 15: Anthropology degree records use purple tiles

- Replaced MA/PhD temporary media with existing purple program-tile styling, mortarboard icon and MA/PhD labels. Added optional tile data to current shared imageTextRow; default image behavior unchanged, no new CSS. Copy/links/layout retained.
- ANTH build passed; two purple labeled tiles and retained sheet URLs verified, no placeholder images on this page. Local only, no commit/push/deployment.

## November 15: Graduate Degrees Awarded heading clarified

- ANTH Degrees Awarded H1/front-matter title now Graduate Degrees Awarded; navigation remains Degrees Awarded. ANTH build passed and rendered H1 verified. Local only, no commit/push/deployment.

## November 15: Anthropology graduate research copy drafted from workbooks

- Read both supplied MA/PhD XLSX workbooks, including research titles across their chronology and PhD subfield labels. Replaced three Degrees Awarded placeholders with complementary page/MA/PhD paragraphs grounded in those records. MA records since1930 explicitly include thesis/non-thesis recipients; PhD since1967. Kept URLs, structure and temporary images.
- Source rationale retained in docs/units/anth/anth-degrees-awarded.md. ANTH build passed; three paragraphs, dates and unchanged spreadsheet links verified. Local only, no commit/push/deployment.

## November 15: Anthropology degree-record links added

- Added user-supplied MA/PhD spreadsheet links to respective Degrees Awarded rows. No research copy generated or spreadsheet contents read; placeholders retained pending next supplied content. ANTH build passed and both rendered URLs verified. Local only, no commit/push/deployment.

## November 15: Anthropology Degrees Awarded scaffold

- Reviewed Geography's concept only; ANTH now has its own brief intro and full-width gray section with two current shared imageTextRow blocks for MA and PhD recipients. Temporary square images and explicit Anthropology description/link placeholders; no GEO dates, research claims, descriptions, old layout or spreadsheet links copied. GEO untouched.
- ANTH build passed; two shared rows, degree headings and gray section verified. Await user-supplied descriptions/record links/images. Local only, no commit/push/deployment.

## November 15: Anthropology included in Page Headings review

- Added ANTH to existing Review headings report alongside SSRI/SOC/ES/PUBA, preserving existing unit order/layout and three-line entries. Recorded current-cohort heading pattern for authorized future unit reviews.
- Review build passed; ANTH section and current cohort/course/faculty index labels/paths verified. Local only, no commit/push/deployment.

## November 15: Anthropology current cohort heading

- Updated only cohort H1/front-matter title to Current Anthropology MA & PhD Students. ANTH build passed and rendered H1 verified; prose/directory unchanged. Local only, no commit/push/deployment.

## November 15: Anthropology course heading named

- ANTH course page H1/front-matter title now Anthropology (ANTH) Courses. Recorded Subject (CODE) Courses pattern for future authorized edits; other sites, navigation and URL unchanged. ANTH build passed and rendered H1 verified. Local only, no commit/push/deployment.

## November 15: Anthropology website labels approved

- All eight existing ANTH website labels now Website per user approval; added Miriam Stark's supplied https://miriamstark3.wordpress.com/ as Website. Other URLs retained; no scholarly-resource labels changed.
- ANTH build passed; all website labels checked and Miriam rendered link verified. Local only, no commit/push/deployment.

## November 15: Profile website globe removed; ANTH labels inventoried

- Removed globe markup from shared profile-sidebar Online website links across units; email/telephone icons and labels/URLs retained. ANTH build/shared checks passed; Elizabeth rendered Online section has no SVG and retains existing name label/email. Other units consume change on rebuild; no deployment.
- Eight ANTH website labels for review: Elizabeth Agey, Jan Brunson, Alex Golub, Jonathan Padwe and Christian E. Peterson each use their own names; Alan Howard, Barry V. Rolett and Leslie Sponsel already use Website. No labels changed pending user approval. Local only, no commit/push/deployment.

## November 15: Terry Hunt listing labeled

- ANTH emeriti page now displays its name-only member under Additional Emeriti (H3) as a list item below the Emeritus cards. No invented biography/contact/photo. ANTH build passed; heading/name item verified. Local only, no commit/push/deployment.

## November 15: Profile resource spacing uses original Publications baseline

- Corrected preceding spacing choice: removed44px minimum/padding from scoped supplemental list anchors; Online and Publications now share unpadded inline-flex links and the same heading selector. Global website link styles outside supplemental sections unchanged.
- ANTH build passed. Live Chrome1440/390px measured visible first-link text13px beneath both heading boxes, exactly matching original Publications inline-link baseline; headings both18px/500, link padding0. Supersedes prior44px padded target choice. Local only, no commit/push/deployment.

## November 15: Profile Online/Publications spacing unified

- Root cause: website icon link had44px inline-flex target and4px/6px padding; plain publication links lacked that geometry. Shared profile-supplemental list anchors now use the same geometry; supplemental H2/H3/H4 headings share one existing type/spacing rule, preserving semantic heading levels. No global website icon or general body-link changes.
- ANTH build/shared checks passed. Live Chrome Alex Golub profile measured at1440/390px: both headings18px/500, both heading-to-link boxes10px, both link padding4px6px and height44px. Previously Publication gap13px/height21px versus Online10px/44px. Local only, no commit/push/deployment.

## November 15: Terry Hunt name-only; card Online headings

- Terry Hunt marked directoryNameOnly in central ANTH people record, with placeholder/contact fields removed; shown as plain name below Emeritus portrait grid. Existing membership retained. Nine supplied portrait cards remain.
- Opt-in card online-resource sections now have Online heading (H4 beneath person H3/group H2), using existing supplemental styling and preserving URLs. No heading for people without resources.
- ANTH build passed; verified nine cards, Terry plain-name placement/no placeholder, eight Online headings. Local only, no commit/push/deployment.

## November 15: Anthropology other-faculty portraits connected

- Renamed nine new faculty-other WebPs to lowercase hyphenated names, preserving image bytes. Updated central ANTH people records to those portraits with measured native dimensions. Terry Hunt remains the sole temporary portrait; no supplied file for him.
- ANTH build passed; all nine portrait references/copied assets verified and one intended placeholder remains. Local only, no commit/push/deployment.

## November 15: Anthropology emeritus/retired portrait grids

- Reused shared people grid/profile cards for Emeritus8 and Retired2, with shared temporary500x500 portrait for all10; no photo downloads. Central people.json now owns those records, excluded from active faculty/contact lists and with explicit null bio URLs. Emeriti group membership uses memberSlugs resolved by optional shared loader; In Memoriam remains original8-person text list with links.
- Restored nine people's available email/website/scholarly/social URLs from supplied November15 WordPress export, without fetching external pages or importing bios. Terry Hunt retains prior name-only information. Repeated titles remain omitted per previous instruction. Scoped directoryShowOnline option renders those links; card-name H3 option sits beneath group H2s. No new CSS.
- ANTH build and shared checks passed; verified10 cards/placeholders, all imported online URLs, no empty links, three sections,13 active faculty cards unchanged. Initial card-link array concatenation rendered blank links; corrected to nested array loops and rechecked before completion. Local only, no commit/push/deployment.

## November 15: Anthropology emeritus/retired groups separated

- H1/front matter now Anthropology Emeriti & Retired Faculty, matching nav ampersand. Existing18 people retained in Emeritus8, Retired2 (Barry V. Rolett/Ann Sakaguchi per user), Emeriti In Memoriam8; HRs between groups. Removed repeated rank/status descriptions from living lists; names/emails retained, emeritus names alpha by surname. Memorial details/links retained with approved name/research-interest em dash.
- ANTH build passed; H1, group order, roster counts, retired membership and removed repeated titles verified. Local only, no commit/push/deployment.

## November 15: Anthropology associated names use em dash

- Added an explicit facultyDescriptionSeparator on ANTH associated page and optional shared-template parameter, defaulting to the existing colon elsewhere. ANTH now displays name/contact — research interests; retained text, HRs and links. Updated text-cleanup checklist and superseded earlier deferral in conventions so future reviews preserve this approved exception.
- ANTH build passed; rendered em-dash separator count covers every description. Local only, no commit/push/deployment.

## November 15: Anthropology associated faculty separators

- Added dividerBefore to every ANTH associated-faculty group after the first, using existing shared HR support. ANTH build passed; rendered HR count matches section transitions. No other formatting or punctuation changed.
- Recorded approved spaced-em-dash preference for directory name/research-interest separators as a scoped exception, for the future prose-formatting rule page; course colon rule retained. Local only, no commit/push/deployment.

## November 15: Anthropology faculty landing renamed

- Renamed ../anth/src/faculty/core-faculty.html to faculty/index.html, permalink /faculty/, H1/front-matter title Anthropology Faculty and navigation label Faculty. Updated hero mapping, migration generator and Review landing sort; retained introductory copy and existing hero. Added direct old core-faculty.html redirect; other units and research-area subheadings unchanged.
- ANTH build initially rejected stale output at old URL; removed only that generated former page, rebuilt successfully with12 redirects. Verified new index/H1, old redirect and refreshed Review label. Local only, no commit/push/deployment.

## November 15: Anthropology contact heading/grid cleanup

- Removed visible Key Contacts heading from ../anth/src/contact.html. Kept existing shared map/office grid and people grid; removed redundant outer row/col around self-contained people grid, retaining its gray section. Source formatting normalized locally; contact prose otherwise preserved.
- ANTH build passed; rendered heading absent and map/people grids present. Local only, no commit/push/deployment.

## November 15: Support Anthropology structure aligned

- ../anth/src/support-anth.html now separates intro and right-side Foundation logo in existing reverse imageTextRow, then Additional Funds in full-width page-section--gray with standard container/row/column. Contributions sentence is its own non-italic appreciation paragraph using existing smiley style. Six fund entries/text/links preserved apart from source whitespace; no broad copy/formatting sweep.
- ANTH build passed (51 pages/11 redirects); rendered shared grid, appreciation markup and gray funds placement verified. An accidental npm run build in shared reported no script before running the correct successful ANTH build. Local only, no commit/push/deployment.

## November 15: Graduate image pool visible in hero labels

- Review unit hero entries now label graduate-pool images Graduate Featured or Graduate Supporting based on image path. General-pool labels remain Featured/Supporting, existing colors/weights retained. Assignments/grouping unchanged.
- Review built29 pages; pool/label matching checked for ANTH/SOC/ES/PUBA and live ANTH labels verified. Local only, no commit/push/deployment.

## November 15: Anthropology hero review grouped by page priority

- ANTH-only order: General: Primary Pages12, Secondary Pages15, Graduate Pages6, Faculty Landing Pages3, Faculty Profile Pages13, Privacy and Policies2. Home first then alphabetical; undergraduate degree overview pages primary, MA/PhD and other graduate pages graduate; AGSA explicitly secondary per user example. Existing final faculty/universal groups retained. ANTH has no current404 source page, so universal group contains existing privacy/policies only; no department page invented during this grouping-only task.
- Review build passed; all51 hero entry HTML fragments match the pre-change baseline exactly, including image, name, link, count and Featured/Supporting markers. All entries appear once; live group order verified. Other units' grouping code unchanged. Local Review script/shared handoff only, no commit/push/deployment.

## November 15: Review secondary navigation uses standard section wrappers

- Corrected shared Review shell: secondary nav now has its own page-section > container content-section > row > col-12 inside site-main, before the separate H1/content section. Reuses normal spacing and diagnostics; no new CSS. Supersedes prior placement outside main.
- Review build passed; actual localhost ANTH page DOM verified for all standard wrapper ancestors. Applies through shared shell to all Review section navigation. Local only, no commit/push/deployment.

## November 15: Review secondary navigation moved above content

- Shared Review shell now places its existing secondary button navigation immediately below the primary header/navigation and outside main page content, before H1. Applies to Heroes, Redirects/404s and Rules, with exactly one secondary nav per section page. ANTH added to current-review group; alphabetic first group ANTH/ES/PUBA/SOC/SSRI, existing gap before remaining units retained.
- Review built29 pages; checked five representative generated routes for primary/secondary/H1 order and unit group order. Actual localhost8090 ANTH Heroes and Code Formatting pages verified. No server restart or document-content changes. Local only, no commit/push/deployment.

## November 15: Documentation organized by purpose and unit

- Moved66 existing documents into docs/rules, docs/units/UNIT, docs/shared, docs/reports and docs/templates. Root now contains only README.md (plain-English map), project-conventions.md and work-status.md. Unit report/migration filenames retained; no document deleted. Code Formatting source is now docs/rules/code-cleanup.md; its content was not rewritten for this organization task.
- Updated Markdown links and explicit paths in shared working instructions, scripts, consuming SOC/PUBA READMEs and Review reader/watch target. Historical records remain records; this is not a claim that all older instruction conflicts were audited or resolved. Existing Rules categories have not been expanded.
- Shared validation passed; all local Markdown document links resolved. Review built29 pages. Isolated local server rendered relocated rules; touching the moved file triggered its watcher and a0.28s rebuild without changing contents. Temporary server stopped. Local changes only, not committed/pushed/deployed. Review server already running before this configuration move needs one normal go restart to load the relocated reader/watch target; ordinary document saves thereafter use the established watcher.

## November 15: Rules renderer reads fresh source on every render

- Replaced codeFormattingRules global data with a readRuleDocument filter in ../review/eleventy.config.js; generated Rules template invokes this read-only filter directly for docs/rules/code-cleanup.md, then existing Markdown rendering. Source content is not cached in global page data. Removed only the fixed Code Formatting H1 from rendered body, not arbitrary first lines. No document content changes retained.
- Tested two consecutive append/remove cycles of invisible unique comments against the actual local HTTP page with the server running; all four updates appeared without restart/manual build (watch rebuilds0.45–0.88s). Removed only each test marker, never restored an old whole-file snapshot. Source SHA256 matched before/after. Stopped server, ran exact go clean/dev again, verified source hash unchanged and Rules HTTP page correct with no markers.
- Temporary verification server stopped afterward; port8090 left for user terminal go. Local runtime/doc handoff changes only, no commit/push/deploy. No recovery search performed. These tests establish current behavior, not the cause or recovery of previously reported missing edits.

## November 15: Review terminal ownership restored

- Identified agent-started Review process still listening on8090 after prior watch tests; this was separate from the user's Terminal session. Stopped that confirmed process. No startup-command change was needed: user's existing go alias is npm run clean && npm run dev, and Review dev is Eleventy serve on8090.
- Ran the exact alias in a foreground interactive zsh/PTTY: clean/build succeeded, printed Local server: http://localhost:8090/, Rules page HTTP200. Sent Ctrl-C to that foreground session and confirmed no listener remained on8090. Did not claim to test macOS Terminal Command-Q itself. Port deliberately left free for user go; no background test server retained.
- No runtime files changed this turn. Shared handoff/build rules updated locally; no commit/push/deployment.

## November 15: Review rules save-and-refresh repaired

- Rules now render docs/rules/code-cleanup.md at Eleventy build time through the existing Eleventy Render plugin; removed generated Markdown snapshot, replacing it with a template calling renderContent. Shared watch targets now consistently use sibling-relative paths, correcting the observed missed document/config updates from the earlier absolute-path setup.
- Restarted only the confirmed Review server on8090. Verified a document save while it stayed running: watcher logged css-shared/docs/rules/code-cleanup.md and rebuilt in0.46s; HTTP page showed new text without manual build/restart. Removed temporary probe and verified a second automatic HTTP update. Document restored byte-for-byte to its pre-test contents. Review still uses npm dev/Eleventy on8090; no new server or dependencies.
- Local only; no commit/push/deployment. Editable source remains docs/rules/code-cleanup.md; generated Review files are output, not editable rule sources.

## November 15: Review Rules and Code Formatting

- Added Rules as the last shared Review primary-nav item at /rules.html, with the existing button submenu linking to /rules/code-formatting.html. Kept all image galleries and existing nav items. Review generator renders shared docs/rules/code-cleanup.md directly through Eleventy's Markdown support; no duplicated rule content. Watches the document for local updates.
- Consolidated formatting instructions in docs/rules/code-cleanup.md with plain-English rules, an example, preservation exceptions and verification expectations. Project conventions now point there instead of repeating the list; AGENTS.md explicitly requires it for HTML/Nunjucks formatting. This does not consolidate accessibility/SEO/voice rules yet or run a site-wide formatting sweep.
- Review built29 pages. Actual local Rules and Code Formatting routes, active submenu, retained image nav and escaped example verified; desktop/mobile Chrome layout checked. Local only, not committed/pushed/deployed. Review remains outside Git.

## November 15: SSRI fiscal service label aligned

- Fiscal & Compliance now replaces Fiscal/Compliance in ../ssri/src/support/fiscal-compliance.html H1/front matter, shared SSRI navigation and current migration label. Existing searchTitle already matched. Formal FOCUS name and page URL unchanged; OENAS official conjunction retained.
- SSRI build passed; rendered H1/title/navigation and retained formal office name verified. Review refreshed. An unnecessary shared npm run build attempt reported no build script; shared is a source repository, and consuming SSRI build succeeded. Local only; no commit/push/deployment.

## November 15: Review headings expanded without bullets

- ../review/scripts/build.py now lists each page in three lines: linked actual H1, visible source folder/HTML filename, actual rendered head title. Removed list bullets and indentation; shared review.css applies the former small-path text size consistently to all three lines. Existing unit columns/order retained.
- Review build passed (27 pages); output and actual localhost:8090/headings.html both verified136 entries,136 paths and136 head titles, no missing titles. Local only; no commit/push/deployment. Review is not a Git repository.

## November 15: Unit publishing changed to manual-only

- Removed push and hourly schedule triggers from all ten ../UNIT/.github/workflows/deploy.yml files (ANTH/ES/GEO/POLS/PSY/PUBA/SCI/SOC/SSRI/WGSS). workflow_dispatch remains; deployment jobs and local development commands are unchanged. Shared validation workflow is unchanged.
- Verified all ten trigger blocks are manual-only and the entire permissions/job portion is byte-for-byte unchanged. No site rebuild needed for trigger-only edits. No GitHub run started.
- Local changes only, not committed/pushed/deployed. Existing GitHub schedules continue until each workflow change is pushed to its default branch. After source pushes, manually use Actions > Build and publish UNIT > Run workflow. Push shared changes first when needed; manually rebuild affected units afterward. Daily scheduling remains a future option, not enabled.

## November 15: GitHub deployment failure diagnosis

- Public SOC Actions API: latest30 runs contain28 successes and2 failures (runs43722908266 and43680359679). Both fail at Deploy with missing github-pages artifact; latest failed run passed shared validation, install, build and upload. API confirms its unexpired github-pages artifact actually exists. This supports an intermittent artifact-discovery problem at deployment; precise backend cause remains unconfirmed.
- All ten unit deploy workflows schedule hourly at minute23, in addition to pushes/manual runs. This produces up to240 scheduled deployment attempts daily across ten units and amplifies failure notifications. Hourly scheduling exists to pick up shared-source changes; do not remove it without preserving an agreed refresh strategy.
- Read-only diagnosis; no workflow changes, reruns, commits, pushes or deployments. Superseded next step: user chose manual-only publishing below; no retry mechanism added. Do not characterize website builds as failing when the failure is deployment-only.

## November 15: Live preview crawler/indexing diagnosis

- Read-only inspection: ES/SOC/PSY/PUBA/SSRI/GEO all have indexingEnabled:false and shared shell emits noindex,nofollow. Confirmed all six live GitHub homepages return HTTP200 with that meta directive and no X-Robots-Tag header; cssweb-stack.github.io/robots.txt returns404 (no domain-root robots exclusion file observed). Siteimprove documentation explicitly says it ignores noindex/nofollow for crawl discovery; these settings do not explain the three selective scan failures. Actual Siteimprove crawl-error details/IP-level behavior remain unknown.
- Python HTTPS check initially failed due local certificate-store configuration; system curl verified TLS and all responses successfully. No indexing/code/settings changed; shared handoff note only.

## November 15: SSRI Home/Directory heroes finalized

- Home and Directory now Saunders05. Contact and Jack remain07. SSRI built; all four rendered assignments verified. Review rebuilt. Local only, not committed/pushed/deployed.

## November 15: SSRI Research section aligned

- Changed only Research landing hero from Saunders02 to01; all four research children already used01 via the existing default. SSRI built; all five rendered Research heroes verified01. Review rebuilt. Local only, not committed/pushed/deployed.

## November 15: Remaining SSRI Support heroes selected

- Fiscal Compliance now uses Saunders02; Research Services uses Saunders06. Grant Development/Boilerplate04 and Support ordering unchanged. SSRI built; both rendered assignments verified. Review rebuilt. Local only, not committed/pushed/deployed.

## November 15: SSRI Grant Development and Boilerplate aligned

- Both pages now use Saunders mural04.webp. Added explicit reviewOrder metadata so Support begins Grant Development then Boilerplate, adjacent, followed by other support pages. Other hero assignments unchanged.
- SSRI and Review builds passed; both rendered hero paths and live Support order verified. Local only, not committed/pushed/deployed.

## November 15: SSRI hero review grouped by section

- SSRI-only gallery order is now Support (four pages), Research (five), Other Pages (three), followed by existing Faculty Bio Pages and Privacy and Policies. Alphabetical within each group; frequency sections omitted for SSRI. Existing image assignments and other unit groupings unchanged.
- Review build passed; live /heroes/ssri.html checked for requested order, correct route membership, all16 entries exactly once. Review remains outside a Git repository; shared handoff updated locally. No commit/push/deployment.

## November 14: H1 review shows source paths

- Added always-visible relative src file paths beneath all136 headings, using small text and safe wrapping; kept four columns. No source URLs renamed. Review rebuilt; live page checked for136 visible paths. Local only, not committed/pushed/deployed.

## November 14: Four-unit H1 review page added

- Added /headings.html (Page Headings) and shared navigation link. Four responsive columns in requested order SSRI/SOC/ES/PUBA. Reads actual rendered H1s, follows clickable primary/dropdown navigation order Home→Contact, then lists all remaining source-defined content pages alphabetically under Other Pages. No titles/H1s edited; generated redirects excluded.
- Review built27 pages. Inventory check confirms each of 136 pages exactly once (SSRI16, SOC60, ES29, PUBA31), no missing H1, correct first/last nav destinations. Live desktop/mobile layout/nav checked; four columns at desktop, no horizontal overflow. Local only, not committed/pushed/deployed.

## November 14: SOC homepage intro unified

- Merged welcome, former tagline sentence and following prose into one standard opening paragraph on ../soc/src/index.html, preserving wording and removing tagline styling. SOC build passed; rendered opening paragraph contains all three parts and no tagline class. Local SOC source/output only, not committed/pushed/deployed.

## November 14: Three PUBA heroes selected; unique-image gallery added

- Applied only requested PUBA assignments: homepage graduate Featured57, Nonprofit Management certificate42, Public Policy certificate54. Default and other page selections unchanged. PUBA built and all three rendered hero paths checked.
- Added /heroes/puba-images.html (Current PUBA Images) and PUBA Images primary-nav link. Gallery deduplicates the effective current hero paths, showing one original-proportions image per file with filename/folder. Uses shared Review presentation. Review rebuilt; live route/nav, unique images and assets verified. Local only, not committed/pushed/deployed.

## November 14: Graduate gallery restored for PUBA selection

- Restored /heroes/graduate-images.html and Graduate Images navigation link. Shared presentation shows three Featured and five Supporting images in separate H2 sections, filenames and native proportions. General Featured gallery retained. No PUBA assignments changed.
- Review built25 pages; live gallery/menu and eight image files verified. Local only, not committed/pushed/deployed.

## November 14: ES Support and Certificate heroes selected

- Support ES uses General Featured60; Certificate ES uses General Featured55. ES built and both rendered hero paths verified; Review rebuilt. Local only, not committed/pushed/deployed.

## November 14: Eight ES Featured hero selections applied

- User selections applied: homepage48, News41, BA17, BA outcomes25, BAM51, Contact26, Double Majors20, Courses24, all General Featured bank. Default now follows homepage48. Existing other heroes and universal mural assignments unchanged.
- ES build passed; all eight rendered hero paths/copied files verified. Review rebuilt. No broad editorial/a11y recertification claimed. Local shared mappings/outputs only, not committed/pushed/deployed.

## November 14: General Featured gallery replaces completed galleries

- Removed Graduate Images and General Supporting Images generation/output/nav entries. Added /heroes/general-featured.html with all19 General Featured files, filenames and original image proportions, using shared Review shell/styles. Primary nav now links General Featured Images. No unit assignments changed; user will select ES replacements next.
- Review built24 pages. Live gallery/nav and all19 image files verified; removed gallery outputs absent. Local only, not committed/pushed/deployed.

## November 14: Final SOC24/32 adjustment

- User requested24 replace32 and32 remain Supporting/unused on SOC. Minor Concentrations now24. Because24 had been on Support SOC, assigned previously unused General Supporting22 there to preserve unique selection and leave32 unused. No bank files moved (32 was already Supporting). SOC build and both rendered hero paths checked; Review rebuilt. Local only, not committed/pushed/deployed.

## November 14: SOC graduate/general image cycle completed

- User requested42 to Applications and34 to the former42 page. Applied full cycle: Graduate Applications42, Sakihara Scholarship34, Support SOC24. Reclassified34 from General Supporting to Graduate Supporting, updating ANTH/SOC paths. Graduate bank is eight again; General Featured19/Supporting25. No new reuse introduced.
- ANTH/SOC builds and shared check passed; three rendered SOC hero paths verified. Review rebuilt. Local only, not committed/pushed/deployed.

## November 14: Image24 moved to General Featured

- User confirmed moving24.webp from graduate/supporting to general/featured. Updated ANTH/SOC/PSY/SCI references while preserving which pages display it. Graduate pool now seven (three Featured, four Supporting); General Featured19. SOC Graduate Applications still displays24 and needs a newly selected unique graduate replacement; no reuse proposed or automatic substitute chosen.
- Four affected site builds/shared check passed; Review rebuilt. Local only, not committed/pushed/deployed.

## November 14: Image60 corrected to General Featured

- User clarified60.webp is Featured. Moved general/supporting/60 to general/featured/60 and updated ANTH/SOC/PSY/POLS references; current SOC assignment remains faculty landing (Courses is51). Four builds passed; Review rebuilt to remove60 from Supporting gallery and show Featured label. User’s intended action for24 remains an open clarification; no24 changes made. Local only, not committed/pushed/deployed.

## November 14: General Supporting image review page added

- Added /heroes/general-supporting.html and shared navigation link General Supporting Images. Shows all 27 general/supporting files in filename order at natural proportions using shared Review shell/styles. No assignments/categories changed. User rejected reusing another graduate image as a substitute for finding an additional unique selection; do not propose that workaround again.
- Review built 25 pages; live route/nav and all 27 assets verified. Local only, not committed/pushed/deployed.

## November 14: Graduate heroes classified

- User explicitly selected Graduate Featured57/54/42. Moved those three to graduate/featured and other five (02/14/24/28/38) to graduate/supporting, preserving assignments and updating six units’ paths. 38 remains Supporting because its upgrade was tentative; 24 remains graduate pending a decision about its possible general/undergraduate use. No additional approved graduate reserve identified.
- Six affected builds and shared check passed; Review rebuilt with red Featured labels and Supporting labels on graduate selection page. Local only, not committed/pushed/deployed.

## November 14: Eighth SOC replacement completed

- User added Supporting37; replaced it with remaining unused Featured47 on BA Concentrations. SOC built and rendered hero path verified; Review rebuilt. All 17 General Featured images are now used by SOC. Local only, not committed/pushed/deployed.

## November 14: Seven SOC Supporting assignments replaced

- User identified seven Supporting images for replacement on SOC, not deletion: 43→26,09→27,18→31,56→25,21→36,07→39,19→40. Used seven previously unused General Featured files, preserving unique assignments. Shared Supporting files remain available. SOC rebuilt; seven rendered paths verified. Review rebuilt. Local only, not committed/pushed/deployed.

## November 14: Review classification labels emphasized

- Removed New swap-in output and obsolete SOC mapping flags. Featured labels now use shared Review CSS red #aa0000 and weight600; Supporting labels use explicit weight600. No hero choices changed. Review rebuilt. Local only, not committed/pushed/deployed.

## November 14: General classification finished; graduate selection page added

- Moved all 17 remaining unclassified general images to supporting, updating six unit mappings. General bank now has 17 Featured and 27 Supporting images. Graduate bank remains eight images awaiting classification. Removed Extra Student Images generation/output/nav link; added /heroes/graduate-images.html and Graduate Images nav link using shared Review presentation and natural image sizes.
- Six affected site builds and shared check passed; Review rebuilt. No individual hero choices changed, only paths/categories. Local only, not committed/pushed/deployed.

## November 14: Ten extra images approved as Supporting

- Moved 22,23,29,30,44,45,46,50,58,62.webp to students/general/supporting. Updated assignments in ANTH/POLS/PSY/SCI/WGSS; Sociology selections unchanged. Review labels Supporting and excludes both classified general folders from Extra Student Images, leaving no unreviewed extra candidates. Other SOC-selected general images remain unclassified until directed.
- Five affected site builds and shared check passed; all ten files exist and former active JSON paths absent. Review rebuilt. Local only, not committed/pushed/deployed.

## November 14: Approved Featured images removed from candidate review

- Extra Student Images now excludes all students/general/featured files in addition to images already used by SOC. Files/assignments retained; only candidate display filtered. Review rebuilt and checked ten remaining candidates with no Featured image paths. Local only, not committed/pushed/deployed.

## November 14: Nine SOC general selections marked Featured

- User approved 41,10,48,04,51,17,61,20,55.webp. Moved these nine to students/general/featured and updated all active references. General Featured now contains 17 approved files. Regular hero review labels now identify Featured images as well as the extra-image page; graduate assets unchanged.
- Six affected builds, shared check and SOC verifier passed. No active JSON retains former paths. Review rebuilt with Featured labels. Local only, not committed/pushed/deployed.

## November 14: Eight extra general images marked Featured

- User approved 25,26,27,31,36,39,40,47.webp as Featured. Moved only those eight to students/general/featured and updated existing assignments in ANTH/POLS/PSY/SCI; other images remain unclassified. Extra Student Images discovers nested folders, retains filename order and labels these Featured. Rejected-file guard covers any nested bank category.
- Four affected site builds and shared check passed; Review rebuilt. Local asset moves/data/Review changes only, not committed/pushed/deployed.

## November 14: Review missing menu item corrected live

- User screenshot and live HTTP confirmed the old three-item menu despite new page existing. Moved primary navigation to shared data/common/review-navigation.json, read dynamically and watched with resetConfig. Restarted only confirmed Review process PID57557. New preview session94781 serves port8090. Live HTTP now contains four links including Extra Student Images; its page returns200. No user restart required. Local only, not committed/pushed/deployed.

## November 14: Student hero bank split; extra-image review added

- Moved all 52 remaining student heroes into graduate (8:02/14/24/28/38/42/54/57) and general (44), based on current approved SOC graduate assignments. No image edits or quality classification. Updated six units’ active hero data and migration bank discovery to nested paths; removed old generated flat copies. Rejected-image guard now checks nested banks too. Updated hero-bank README to supersede obsolete pool/profile guidance.
- Added /heroes/extra-students.html and primary nav link Extra Student Images using shared Review shell/styles. It lists exactly 18 images not selected by Sociology, keeping original proportions; other-site use is explicitly noted. Review now builds 24 pages.
- Six affected site builds, shared check and SOC verifier passed. Scanned active JSON and affected output for old flat paths: none. Each new referenced student asset exists. Local shared/Review changes only, not committed/pushed/deployed. Featured/supporting split remains for the next user review.

## November 14: SOC top-ten hero selections applied

- Applied user choices: Home17, WhyStudy61, BA20, Faculty60, ResearchAreas04, BAM56, Minor55, Courses51, Applications24, Contact41 (students bank). BA archived requirements shares20. Seven other existing holders received displaced images through reciprocal swap chains, avoiding new duplicate assignments. Default follows homepage17. MA54/PhD57 and universal mural settings unchanged.
- SOC build and verifier passed; all 18 changed rendered hero paths checked. Review rebuilt. Local shared mapping/Review output only, not committed/pushed/deployed.

## November 14: SOC graduate/undergraduate student hero swaps

- Swapped students-bank pairs bidirectionally in SOC: 07↔28, 32↔02, 37↔14. Six assignments changed: academic planning/student organizations, minor/graduate course categories, Why Study/applications-admissions. No image files renamed; shared Saunders constants unchanged. SOC build passed and all six rendered hero paths checked. Review rebuilt. Local only, not committed/pushed/deployed.

## November 14: Universal Saunders bio and shared-page heroes

- User superseded Hawaiʻi Hall selections: Saunders mural 07.webp for every faculty bio; 06 privacy; 03 policies/procedures; 02 404. Common page-heroes.json owns facultyBio plus shared URL choices. Shared hero/attribution includes use the common bio assignment when personSlug is present; shell displays it even when other heroes are off. Current faculty-heroes records and explicit known bio mappings normalized. Faculty landing-page assignments untouched. Review honors these same common settings.
- Ten unit builds, shared checker and Review build passed. Verified rendered heroes for all 129 faculty bios and 24 existing policy/privacy/404 pages across ten sites. Inspected supplied images and set descriptive mural alt. Shared checker protects all four constants. No new 404 source pages or asset deletions. Local shared/Review changes only, not committed/pushed/deployed.

## November 14: SOC hero review split by page audience

- Sociology only: main heroes split into General Pages, Undergraduate Pages, Graduate Pages (H2), with duplicate-frequency groups retained as H3s. Faculty Landing Pages, Faculty Bio Pages, Privacy and Policies remain separate afterward. Undergrad covers undergraduate/ plus Alpha Kappa Delta; graduate covers graduate/; mixed-audience funding/prize/Courses remain General. BAM remains undergrad by its section/applicant route. No images or source page content changed.
- Review built; all 60 SOC entries retained exactly once (15 general, 10 undergraduate, 17 graduate, one faculty landing, 14 bios, three shared). Live localhost headings confirmed; ES retains existing grouping. Local only, not committed/pushed/deployed.

## November 14: Three more rejected student heroes deleted

- Deleted students/05.webp, 06.webp and 11.webp plus obsolete generated copies. Replaced 14 assignments across ANTH, POLS, PSY, SCI, SOC and WGSS with remaining images not already assigned within each site. Added new-swap markers to all three SOC replacements (News 18, BA outcomes 19, Courses 21). Expanded the existing rejected-image guard to seven filenames. All active shared JSON and affected built HTML scanned: no rejected references.
- Six affected builds, shared check and Review build passed. Local only, not committed/pushed/deployed. Original historical migration evidence not rewritten.

## November 14: SOC replacement heroes marked in Review

- Added reviewNewSwapIn flags to the four SOC replacement assignments (minor, BA outcomes, health research area, Courses). Review displays * New swap-in beside their labels; no production visual change. Rebuilt and checked exactly four marked SOC entries and none in other unit pages. Local only, not committed/pushed/deployed.

## November 14: Four rejected student heroes deleted

- User explicitly authorized deletion of students/03.webp, 49.webp, 53.webp and 59.webp. Deleted source assets and obsolete generated copies. Replaced 12 stored assignments across SOC, POLS, WGSS and ANTH with other bank images unused in each site; left selected graduate 54/57 unchanged. Shared checker rejects reintroduced files or data references. No other similarly numbered hero banks touched.
- All four affected site builds passed; SOC verifier passed; scanned affected built HTML for rejected paths with none remaining. Shared check passed. Review rebuilt after removing stale copies. Local deletions/mappings only, not committed/pushed/deployed.

## November 14: Universal Hawaiʻi Hall policy/privacy/404 heroes locked

- Common page-heroes.json now enforces Policies and Procedures → hawaii-hall/hero-01.webp, Privacy → hero-02.webp, 404 → hero-03.webp for all consuming sites. User renamed/supplied those files; inspected hero-03 and supplied descriptive alt. Updated PUBA references to renamed assets; common settings override per-unit choices. Review now prioritizes the common assignment even if a unit’s built page is older. Shared checker explicitly validates all three paths/files. Updated the existing convention and superseded the pending 404 selection.
- All ten unit builds and Review build passed. Verified all 24 existing policy/privacy/404 output pages use their correct shared image with copied assets; missing 404 sources on unfinished sites were not invented. Running ES Review displays the new names. Shared check and SOC verifier passed. ES broader preservation verifier separately flags Our History, Our Way source-body wording differing from its historical snapshot; no content modified or blanket ES pass claimed. Not caused by hero mapping; leave for editorial reconciliation.
- Local shared/Review changes only; no commit/push/deployment performed in this task.

## November 14: Hero review grouped for duplicate inspection

- Main images now group by frequency descending (Triple Use, Double Use, Single Use, or numbered Uses above three), with matching image paths adjacent and titles alphabetized within each image group. Each H2 has an HR. Faculty Landing Pages lists directory before associated pages, separate from Faculty Bio Pages (duplicate image groups adjacent). Privacy and Policies is last and includes privacy, policies/procedures and 404. Existing 404 image retained pending user’s shared replacement.
- Counts now compare within each of those four categories, excluding intentional shared pages from main-page duplication. This supersedes the whole-unit count below: ES homepage/News hero-04 show (2) together under Double Use, while 404 is separately (1) under Privacy and Policies. Tooltips state count scope. Review rebuilt all 23 pages; verified current four units’ section orders, HRs, nine ES bios, two ES landing pages, all 29 ES entries retained and correct scoped counts. Local only, not committed/pushed/deployed.

## November 14: Review group gap and actual image-use counts

- Group-gap selector now outranks the shared li margin reset, preserving 1.5rem between current/remaining units. Hero counts now count actual rendered unit page uses of each full image path, including inherited defaults, across all hero groups. Supersedes JSON-literal reference counting: ES hero-04.webp is used by homepage, 404 and News, so all show (3). Tooltip states pages using image in this unit. Review rebuilt. Local only, not committed/pushed/deployed.
- Desktop Chrome confirmed 24px group margin. Running watch process continued overwriting newer labels with cached content; added standard watch-mode cache opt-out and restarted only the confirmed Review server (old PID 57041). New preview session 88548 serves localhost:8090; HTTP response confirms three hero-04.webp (3) labels. This server remains running. No other site server stopped.

## November 14: Duplicate Review index navigation removed

- Removed Current review/Remaining sites bullet lists from both section indexes. One shared grouped button navigation remains, retaining the current-unit-first order and gap. Review rebuilt; both output indexes checked for exactly one button navigation and absence of duplicate lists. Supersedes the index-list portion of the grouping change below. Local only, not committed/pushed/deployed.

## November 14: Review units grouped by current work

- Shared data/common/review-units.json records current units ES/PUBA/SOC/SSRI. Both section indexes show Current review and Remaining sites; unit submenus show those four alphabetically first, followed by a visible gap and remaining units alphabetically. Gap becomes vertical on phones. Shared degree-navigation gets optional groupStart metadata; existing degree navigation unchanged without it. This is review grouping, not certification of deployment/completion.
- Review built all 23 pages; verified order ES, PUBA, SOC, SSRI | ANTH, GEO, POLS, PSY, SCI, WGSS and one group gap. Shared check passed (860 files). Local only, not committed/pushed/deployed. No additional unspecified page created.

## November 14: Hero review labels use visible H1

- Review hero labels now read the rendered page’s first H1, falling back to source H1 then metadata title. Alphabetical sorting uses that heading too. Rebuilt all 23 pages and confirmed PUBA shows Why Study Public Administration? with its question mark. Unit page content unchanged. Local only, not committed/pushed/deployed.

## November 14: Review heroes show original image proportions

- Replaced fixed-height/cover/background/overlay previews with plain img.review-hero-image. Shared Review CSS uses max-width:100%, width:auto, height:auto: shrink to container, retain native ratio, never enlarge smaller images. Applies to all unit hero review pages; production hero treatment untouched. Review rebuilt. Local only, not committed/pushed/deployed.

## November 14: Review converted to shared presentation

- Review now renders through shared layouts/review/shell.njk and bundles shared css/review.css importing common.css. Reuses Bootstrap/shared containers, typography, unit navigation and degree-navigation submenu. Removed standalone generated review styling. Full-width shared blue banner says CSS Review; shared university gray bar contains Home, Redirects and 404s, Heroes. Heroes and redirect pages offer ten unit submenu links. No UH brand header/footer. Shared nav adds opt-out showUHLinks:false for Review; default department behavior unchanged.
- Kept explicit .html addresses, hero labels/counts and all 23 pages. Shared check passed (859 files). All 23 output pages have one H1 and resolving local links/assets. Chrome at 1440/320px confirmed blue #354d67, nav #f7f7f7, Inter, working mobile menu, three primary links, ten submenu items, 29 ES heroes and no horizontal overflow. Running localhost:8090 reviewed; no fresh full axe certification claimed. Screenshots /tmp/review-shared-1440.png and /tmp/review-shared-320.png.
- Local Review/shared changes only, not committed/pushed/deployed. Future Review content still prepares from unit records; presentation is shared, not an independent theme.

## November 14: Review hero filenames and JSON reference counts

- Hero labels now show page name · linked page path · image basename (count). Count is exact image-path references in the supplying JSON, including a defaultHero reference if present, not a claim of total runtime page uses. Hover text identifies the JSON filename. Applied to all ten unit hero pages; existing explicit .html routes preserved. Build passed; checked all 29 ES labels and all ten unit outputs; running ES Review page serves updated labels. Local only, not committed/pushed/deployed.

## November 14: Plain-English website build rules recorded

- Added docs/rules/website-build-rules.md covering established Eleventy/go workflow, actual startup URL, explicit .html filenames, no unnecessary per-page folders, about/root Courses conventions, editable source ownership, shared reuse and concrete route verification. Retained intentional existing section-index exceptions. Linked from project conventions and AGENTS.md so future build/routing work must read it. No website code changed in this task; documentation checked for consistency with the agreed workflow. Local only, not committed/pushed/deployed.

## November 14: Review explicit HTML routes repaired

- Eleventy default directory URLs had turned heroes/es.html into heroes/es/index.html while links retained .html. Added computed permalinks preserving every prepared HTML filename. Rebuilt all 23 pages; verified the user’s exact localhost:8090/heroes/es.html returns HTTP 200 and all local page/image links resolve. Local only, not committed/pushed/deployed.

## November 14: Review startup restored to Eleventy model

- Replaced custom Python server/launcher with standard npm clean/build/dev and Eleventy --serve --port=8090. Python now only prepares content under ignored _generated; Eleventy renders 23 HTML pages and copies CSS/media. Installed cached dependencies with the same Eleventy/Nunjucks setup as unit sites; removed scripts/dev.py. Startup callback visibly prints actual localhost URL after listening.
- Tested Eleventy on temporary port 8091 because the user-owned old Python server still holds 8090: all 23 pages generated, HTTP 200, explicit Local server: http://localhost:8091/ output confirmed. Agent test server stopped. User must Ctrl+C their old server then run go for standard 8090 startup. Supersedes previous custom-server fixes. Local only, not committed/pushed/deployed.

## November 14: ES editorial gaps corrected and review claims qualified

- Courses H1/front-matter title expanded from ES Courses to Ethnic Studies Courses; concise searchTitle Courses remains intentional. Shared associated-faculty template now uses colon-space before descriptions, replacing literal hyphens; optional links use semicolon instead of em dash. Other consumers receive this template correction on rebuild.
- Added ES verifier assertions for exact full-subject Courses H1 and colon separators for all 13 associated faculty descriptions. Prior text/SEO reports now explicitly acknowledge the coverage gaps: mechanical clean scans and zero SEO errors did not enforce these rules. Earlier accessibility and code evidence retained with scope qualifications. Local only, not pushed/deployed.

## November 14: About folder standardized across sites

- Renamed suffixed About folders in SOC, GEO, POLS, PSY, ANTH and WGSS to about. ES already corrected; PUBA already uses about. SSRI/SCI/UHERO/style-guide have no About folder to rename. Updated active source paths/permalinks, navigation, heroes, original redirect destinations, current URL inventories, approved title inventories and migration scripts. Historical migration reports and original preservation snapshots retained unchanged.
- Added 37 direct redirects from the previous suffixed paths (SOC 9, GEO 5, POLS 8, PSY 1, ANTH 11, WGSS 3). GEO’s older build now invokes the existing shared redirect generator. No template/CSS redesign.
- Six clean builds passed; all 37 redirect files and target pages checked. SOC full verification passed (60 content pages, 73 redirects); shared check passed (857 files). Review rebuilt. Local edits only, not committed/pushed/deployed.

## November 14: ES About folder shortened

- Renamed ../es/src/about-es to about; updated navigation, hero mappings, permalinks, current URL inventory, editorial mapping and title inventory. Original preserved-content snapshot untouched; verifier maps its old keys. Added four old about-es URL redirects directly to new pages, alongside updated original WordPress destinations. Clean ES build and verification passed: 29 pages, 31 redirects, nine bios, 21 preserved bodies. Review rebuilt. Local only, not committed/pushed/deployed.

## November 14: ES statement anchor landing fixed

- Added existing page-jump-target class to all three statement headings. Reuses shared measured sticky-header offset and load-time bookmark correction; no new CSS/JavaScript. ES rebuilt. Chrome followed all three old URLs locally: each heading landed at 251px, 16px below the 235px sticky header. Local only, not pushed/deployed.

## November 14: ES 404 quick link correction

- Removed misleading Academic programs quick link, which pointed only to the BA page. Remaining recovery links are homepage, Faculty and Contact. ES rebuilt locally; no commit/push/deployment.

## November 14: Review go workflow corrected

- The user's go command runs clean then dev. Updated ../review/package.json so dev builds first, then serves _site on port 8090. Clean removes only generated _site. Rebuilt the pages and verified the existing server returns HTTP 200 at localhost:8090; the user can refresh without restarting.
- Supersedes the earlier assumption that go runs build separately. Local changes only; no commit, push or deployment performed.

## November 14: Minimal Review site delivered and ES URL mapping implemented

- Created sibling ../review with zero-dependency Python build, package scripts and two review sections: redirects-404s and heroes. Ten active shared units each have one page in both sections, plus indexes (23 HTML pages). Redirects/retired paths use plain bullet links to GitHub unit previews; units without mapping files are explicitly marked. Heroes show page title/path and supplied images, grouped main/faculty/policy/privacy and alphabetized by name. Images copied into generated output; no paid service or interaction layer. Existing style-guide unchanged. README explains rebuild/test destination.
- Review built successfully and all local links/image files checked. Local server running on port 8090 (session 19759), HTTP 200 verified with network-permitted request. No GitHub repository creation, commit, push or deployment performed.
- ES now has shared custom 404 source/quick links and url-migration.json. Compared all 33 published original URLs in the user-supplied November 14 WXR: 26 moves (including three statements to retained policy anchors), six retired news stories approved for genuine 404, one unchanged homepage. Added interim /courses/ → /courses.html redirect, for 27 generated redirects total. Source Courses remains root-level; only generated legacy redirect uses the old directory. All decisions recorded in exports/es/ES-url-migration-2026-11-14.json; original exports/workbooks untouched.
- Shared redirect generator now accepts and validates anchored internal destinations; canonical excludes fragment while refresh/fallback retain it. ES verifier distinguishes 29 real pages from 27 generated redirects and validates every destination/anchor plus absence of retired outputs. Local missing-path request returned genuine HTTP 404. Final ES verification passed. Production/preview redirect clicks remain user-review work after upload.
- Local changes span ../review, ../es and css-shared. No synchronization claimed. User rejected overbuilding: keep future Review work to simple lists/hero images. Next: user visual Review and GitHub preview checks after publishing; no further utility features required.

## November 14: Instagram profile embed experiment

- User paused 404/redirect work before any mappings or 404 sources were changed, then requested an Instagram trial using the account already in ES social.json. Restored ../es/src/department-news.html as a new News and Updates test page, sourcing https://www.instagram.com/uhm_ethnicstudies/ from social.links. Uses official embed.js/profile blockquote plus permanent plain fallback link. Not added to navigation pending user test; no retired-story redirects changed.
- Fresh logged-out Chrome session loaded embed.js and profile iframe with HTTP 200, showing the account card and six post thumbnails. Confirmed visually. This proves display in this test, not universal availability or guaranteed future refresh behavior. No paid widget, Meta app or access token used.
- Instagram's injected 326px minimum initially overflowed at 320px viewport. Added opt-in instagram-profile wrapper/styles in shared images.css overriding only injected iframe/block width/min/max. Retest: desktop iframe 540px, phone iframe 288px, no document overflow; profile content remains visible. Scoped style does not affect other components.
- ES build/28-page verification passed. Evidence exports/es/ES-instagram-test-2026-11-14.json. New page added to current title inventory; existing hero fallback applies pending hero approval. Broader final-review reports describe the preceding 27-page baseline and do not certify the third-party widget.
- Local ES source/shared CSS/report/docs only; not committed/pushed/deployed. Local ES server confirmed listening on port 8088 for user review at /department-news.html. 404/redirect task remains paused; recommend genuine 404s for retired stories without content replacements, and eventual statement redirects to retained policy anchors. Hero review site still pending.

## November 14: ES final text/code/accessibility/SEO passes

- Completed authorized whole-ES text/voice review: nine institutional paragraphs revised; named courses use colon-space; run-in career/benefit/fund labels use bold plus colon; corrected whitespace and known Hawaiian characters; preserved all nine authored bios and three dated statements. User resolved ES 318 as Asian America and ES 370 as Literatures of Hawaiʻi, applied to both academic lists. All 106 named course-list items pass separator check; academic code/credit counts and source href/src destinations unchanged. BAM nav/tile labels corrected to cover MEd/MPA routes. One diacritic candidate (personal name Willy Kauai) intentionally retained; no required copy decision remains.
- Code: new report-only-by-default scripts/code-cleanup.py reviewed 28 unit HTML/Nunjucks sources and formatted 12. All 27 rendered outputs preserve tags/attributes/text through formatting. Rescan proposes zero edits. Original exports/snapshots/workbooks unchanged. Updated text-cleanup tool to stop obsolete em-dash rewriting; ES reference/editorial-text-replacements.json explicitly records authorized narrative replacements for the preservation verifier.
- Accessibility: Chrome/axe 4.14.0, zero violations on 27 mobile pages and eight representative desktop pages. H1/main/alt/eager-image checks, keyboard/skip/disclosure states, eight mobile text-spacing cases and seven tablet/small-desktop reflow pages passed. Color contrast/frame rules retain incomplete results; external maps, full screen-reader/zoom testing and comprehensive Siteimprove review remain outside this pass. No shared accessibility fix was needed.
- SEO: replaced 25 placeholder descriptions; all 27 approved titles/social metadata checked; self-canonicals use existing production ES origin. Audit zero errors, ten intentional title/H1 wording notes. Preview indexing remains off and guides remain on for review. No live-search/rank claims.
- Final ES build/27-page verifier, shared 850-file checker, text/code rescans, registry-link scan and whitespace checks passed. Reports: docs/units/es/es-text-cleanup-report.md and docs/units/es/es-final-review-2026-11-14.md; measured evidence under exports/es, exports/accessibility and exports/seo.
- Local ../es and css-shared changes only, not committed/pushed/deployed. Preserve unrelated edits and user Excel lock file. Next release tasks: hero approval/review tool, old/new URL mapping/custom 404/redirects, publishing decisions, then live checks/Siteimprove. Do not claim those launch tasks complete.

## November 14: ES Courses final supplied photos

- Replaced Courses placeholders in order: Lower Division uses /media/units/es/courses/course-01.webp; Upper Division uses course-02.webp. Visually inspected both supplied photos, set actual 600x600 dimensions and descriptive alt text without inventing identities/event details. Shared image-row treatment unchanged.
- ES build/27-page verification and whitespace checks passed. Local ES source/shared handoff only, not committed/pushed/deployed. No Courses image placeholders remain.

## November 14: Compact ES requirement subgroup dividers

- Certificate/BA now use existing hr.my-3 above Introductory Course(s), Group 1 and Group 2, reducing divider margins from 2rem to 1rem per side. Other dividers/content unchanged. No CSS added.
- ES build completed. Initial verifier raced generated media availability and reported George Hall/temporary image paths missing; files were present immediately afterward and rerun 27-page verification passed. Source assertions confirmed three compact dividers per page. Whitespace checks passed. Local ES source/shared handoff only, not committed/pushed/deployed.

## November 14: Faculty H1 expanded; hero-review proposal

- ES faculty landing H1 and source title now Ethnic Studies Faculty. Retained approved HTML title Faculty | Ethnic Studies | UH Mānoa, ES Faculty dropdown label, URL, intro and directory content. ES build/27-page verification and whitespace checks passed. Local ES source/shared handoff only; not committed/pushed/deployed.
- User proposed the next review tool: separate lightweight review site with one page per unit, small page-name labels and each page's assigned hero displayed consecutively for quick visual approval. Recorded as upcoming proposal; not built/published and no hero assignments changed. Finish current page review first; use actual mappings/crops when implemented rather than a generic image pool.

## November 14: Run-in label separator agreed

- Recorded cross-site standard: bold, sentence-case explanatory label followed by colon/space. ES BAM advantage label-periods and Why Study career italics/dashes are pending cleanup to that pattern; no website source changed during current page review.
- Updated text-cleanup procedure, including correcting its stale spaced-em-dash instruction to match the existing superseding no-prose-dashes agreement and approved welcome exception. No broad punctuation/italics replacement authorized; preserve headings, protected originals and real sentence punctuation.
- Documentation whitespace check passed. No builds/tests needed for docs-only change. Local shared docs only; not committed/pushed/deployed.

## November 14: ES Courses sections and readable source

- Rebuilt ../es/src/courses.html using existing shared sections/imageTextRow: H1/current intro on white, Lower/Upper Division rows in full-width gray with temporary 500x500 shared images on left and HR between, shared course resources on white below. Preserved the user's current three course-description paragraphs verbatim. No new CSS or invented imagery; placeholder images use empty decorative alt.
- Source is flush-left, no blank lines, one structural opening/closing tag per line; include/import/call directives each on their own line. Removed chained divs and stray indentation, following existing code-cleanup agreement. Broader code sweep remains pending.
- ES build/27-page verification passed. Source assertions checked formatting, two shared image rows, section ordering and widget position. Whitespace checks passed. No new browser check; existing shared image-row layout reused unchanged.
- Local ES source/shared handoff only, not committed/pushed/deployed. Two Courses images remain intentional placeholders for user replacement.

## November 14: ES Courses moved to root

- Moved ../es/src/courses/index.html to ../es/src/courses.html, published /courses.html. Removed now-empty source directory and stale generated /courses/index.html/directory. Updated shared ES navigation, assigned hero mapping (hero-15 unchanged) and current approved title inventory source path. Original workbook/history evidence retained unchanged; final redirect matching must account for any temporary /courses/ links if published previously.
- Generalized the established root-level Courses convention across unit sites; no unrelated unit relocation. ES verifier now explicitly enforces root source/output path and absence of courses folders to prevent recurrence.
- ES build/27-page verification and whitespace checks passed; active source/config scan has no /courses/ or courses/index references. Local source/verifier/shared data/docs only; not committed/pushed/deployed.

## November 14: Unit-bar acronym matches full-name styling

- Updated only shared header.css .unit-short-name to inherit color/weight as well as size, preserving parentheses. Both full name and acronym now use 600 and the same color; supersedes the visually separate gray/400 trial. No unit text/visibility changes.
- ES build/27-page verification, SOC build/60-page/64-redirect verification and PUBA/SSRI builds passed. Chrome checked four sites at phone/desktop widths: same size, weight 600, inherited color, no overflow. Whitespace checks passed. Local shared CSS/docs/rebuilt output only; not committed/pushed/deployed.

## November 14: Unit-bar acronyms in parentheses at full size

- Shared unit-name template now renders (ES), (SOC), (PUBA), (SSRI), etc. where existing showShortName is enabled. Header CSS short-name size inherits from full unit name instead of 0.875em. Retained existing #555 gray/400 weight, full name 600, and all other typography/layout. Visibility flags/footer/search unchanged.
- Recorded parenthetical same-size convention; current lighter color/weight remains available for user visual reassessment. ES/SOC builds and verifiers passed; PUBA/SSRI builds and 847-file shared checker passed.
- Chrome checked all four homepages at 320/1800px (eight cases): exact parenthesized acronyms, same font family/size (24px phone, 32px desktop), gray/400 treatment, no horizontal overflow. Whitespace checks passed.
- Local shared template/CSS/docs plus rebuilt local outputs only; not committed/pushed/deployed. Other consuming sites receive the shared treatment when rebuilt.

## November 14: Why Study dropdown question marks

- Shared ES/SOC/PUBA navigation labels now read Why Study ES?, Why Study SOC?, Why Study PUBA?. Verified existing H1s already spell out Ethnic Studies, Sociology and Public Administration with question marks; no page copy/H1 edits needed. URLs and unit-name-bar acronym styles unchanged.
- Recorded short acronym navigation/full-subject H1 convention. PUBA build, SOC build/60-page/64-redirect verification, ES build/27-page verification passed; rendered nav labels checked on all three homepages. Whitespace checks passed.
- Local shared navigation data/docs and regenerated local output only; not committed/pushed/deployed.

## November 14: ES learning outcomes moved to dedicated academic page

- Created ../es/src/undergraduate/student-learning-outcomes.html, H1 Student Learning Outcomes, with all six original outcomes and their introductory wording retained exactly. Added BA Student Learning Outcomes | Ethnic Studies | UH Mānoa title, descriptive metadata, and the BA page's assigned hero. BA introduction now ends with a sentence linking the outcomes. No additional nav/dropdown item or legacy redirect needed.
- Why Study ES now has Skills and Knowledge in full-width gray, Job Prospects in a separate white section below; all nine skills/eight career entries retained. Removed redundant HR at the new section boundary. No CSS change.
- User approved placing outcomes with BA based on their likely major-specific scope. Formal scope remains unverified and should be confirmed with the unit; no universal rule that every SLO applies only to a major was adopted. Original outcome claims were not rewritten.
- Updated ES verifier to check every relocated outcome text chunk on its new page; original snapshot unchanged. Added new academic page to approved title inventory. ES build/27-page verification passed; assertions confirmed six outcomes, 17 skills/career entries and section order. Whitespace checks passed. No browser layout check rerun.
- Local ES source/verifier/shared hero/title inventory/docs only; not committed/pushed/deployed. Final SEO/redirect inventory must include this new page; existing final-review items remain.

## November 14: BAM bottom course resources

- Added the existing shared ES course-resources section below BAM advising, directly above footer, matching Certificate/BA/Double Majors. Uses the configured ES catalog destination (ent_oid=702), class availability and course descriptions with ES prefix note. No new CSS/data duplication.
- ES build/26-page verification passed; rendered placement/catalog assertions and whitespace checks passed. Local ES source/shared handoff only; not committed/pushed/deployed.

## November 14: ES BAM page structure and cross-program advising

- Generalized BAM intro to cover Ethnic Studies paired with education or public administration, eligible double-counting, undergraduate tuition rates and potential completion in about five years, qualified by pathway. All three existing pathway descriptions retained, third credential corrected to Master of Public Administration. Intro/pathway list remain white; obsolete Contact Us/course shortcuts/Additional Details removed.
- Gray full-width BAM Pathway Advantages lists Save money, Save time, Gain a competitive advantage with concise third-person descriptions; removed guaranteed job-placement/quantified savings rhetoric. White BAM Pathway Requirements follows; retained existing application timing, three eligibility bullets and all three ES course alternatives. Replaced Education-only application-review attribution with instruction to confirm procedures/deadlines with the offering graduate program, avoiding incorrect routing for PUBA. Requirements/application timing still merit unit confirmation in final review.
- Added ES BAM advising variant: Ethan and Monisha for undergraduate guidance, Dawn last for general education; intro directs students to the offering graduate program for graduate admission/requirements/advising. No external program advisors duplicated. Existing default advising variants elsewhere unchanged. No new CSS or added BAM course bar.
- ES build/26-page verifier and shared 847-file checker passed. Source/rendered assertions confirmed section order, legacy removal, three-advisor order and graduate-host guidance. Explicit source verifier retains checks on all pathways, education links and eligibility details while recognizing approved copy replacements. Whitespace checks passed. No new browser test.
- Local ES source/verifier/shared advising data/docs only; not committed/pushed/deployed.

## November 14: Double Majors intro and embedded advising

- Replaced weak second-person intro with a concise third-person opening The 30-credit Ethnic Studies major can be paired with a second major…; mentions Ethnic Studies once and uses lowercase major throughout prose. Retained disciplines, interdisciplinary/community focus and qualified source financial-aid sentence. Removed unsupported distinct advantage/aligns smoothly claims and trailing advisor-prompt paragraph. Full-site text review remains pending.
- Intro and advising now share one white page-section/container/column, separated by standard HR. Added optional advisingEmbedded wrapper suppression to the existing shared widget; identity/content/grid unaffected and default standalone behavior remains for Certificate/BA/SOC. Bottom course resources remain separate. No CSS changes.
- ES build/26-page verifier and SOC shared-template regression build/60-page/64-redirect verifier passed. Parsed rendered ancestry confirms H1 and advising share a single content-section. Original snapshot retained; verifier explicitly recognizes the rewritten two-paragraph source body. Whitespace checks passed. No new browser layout test.
- Local ES source/verifier/shared template/docs only; not committed/pushed/deployed.

## November 14: Certificate/BA group-label consistency

- Compared both Group 1 and Group 2 descriptions word for word. Group 1 differed only in case/trailing period; Group 2 was identical on both pages. No substantive differences found.
- Both pages now use identical sentence-case descriptive paragraphs, no final periods, and and instead of &. H3 group labels, course lists and six/twelve-credit distinctions unchanged. Recorded ES group-label convention and updated source verifier's narrow case/punctuation normalization.
- ES build/26-page verification and whitespace checks passed. No layout/CSS changes or browser test needed for these text-only edits. Local ES source/verifier/shared docs only; not committed/pushed/deployed.

## November 14: BA four-year plan catalog destination

- Replaced obsolete program-sheets paragraph with third bullet beneath Degree Requirements: Ethnic Studies, B.A. Four-year Plan, linking to the user-supplied https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1735&returnto=1018. Actual href uses HTML-escaped ampersands. Existing two requirement bullets unchanged.
- Retrieved catalog destination but received JavaScript anti-bot verification, so page contents were not independently verified; used user's supplied destination/label. Updated explicit source-verifier exception and new-link check. ES build/26-page verifier and whitespace checks passed. Local source/verifier/shared handoff only, not committed/pushed/deployed.

## November 14: ES BA page rebuilt to certificate structure

- BA H1/two intro paragraphs now occupy their own white section with one merged paragraph and unchanged sentence wording. Removed obsolete Contact Us/contact data/course shortcuts/Additional Details. Gray requirements section has H2 Degree Requirements and HR-separated H3 Introductory Courses, Group 1, Group 2, General Education Designations. Group descriptions use strong paragraphs followed by 12-credit instructions and shared two-column course lists. Preserved all courses/credits and program-sheets URL, explicitly left for user correction. Removed duplicate inline UH Catalog link in favor of bottom widget.
- Compared BA Skills and Knowledge/Job Prospects against material already moved to Why Study: same substantive nine skills/eight career entries, only capitalization and skill versus skills differ. Removed BA duplicates without adding another copy. Verifier checks their original text against Why Study with only those normalizations.
- Added separate white Declaring an Ethnic Studies Major section immediately before Undergraduate Advising, matching certificate/SOC pattern and existing common Kuali form destination/login-required notice. Existing advising and bottom course resources retained. No new CSS; semantic subgroup headings stay H3 under requirements H2.
- ES build/26-page verifier passed. Source assertions confirmed intro, heading sequence, duplicate removal, two list modifiers, retained program-sheets link and declaration order. Chrome at 320/768/992/1800px confirmed shared heading styles, one/two-column transition at 992px, no overflow. Whitespace checks passed. Course punctuation/diacritics and source title discrepancies remain for later text review.
- Local ES source/verifier/shared handoff only; not committed/pushed/deployed.

## November 14: Certificate requirements heading hierarchy

- Certificate Requirements remains H2 with the existing three general-requirement bullets immediately below. Standard HRs now introduce H3 Introductory Course, Group 1, Group 2 and General Education Designations. Each group has its existing full description in a strong paragraph below the short H3, then the six-credit requirement and unchanged two-column course list. Introductory ES 101/301 content retained. Used Designations rather than Requirements because DH/DL/DS are definitions, not additional requirements.
- Removed redundant inline UH Catalog paragraph; bottom ES-specific catalog/resource widget remains. No new CSS or course/credit changes. Source verifier recognizes explicit group-description/credit reordering and catalog paragraph removal, retaining all substantive source checks.
- ES build/26-page verification passed. Source assertions confirmed H3 sequence, group pattern, two column lists and duplicate catalog removal; whitespace checks passed. No browser review rerun. Local ES source/verifier/shared handoff only; not committed/pushed/deployed.

## November 14: Shared heading hierarchy revised

- Changed only src/css/typography.css at runtime: H1/H2/H3 now 28/24/20px, weight 500; H4 remains 18px/500. Phones below 576px use H1 26px/H2 22px, H3/H4 unchanged. Removed superseded tablet-only H1 breakpoint. Body remains 18px/400; unit-name responsive 24–32px/600 and existing margins/line-height unchanged. No page markup/layout edits in this task.
- Reviewed W3C WAI heading guidance; chosen numeric scale is a design choice, while heading levels retain semantic structure. Updated shared typography documentation/conventions, superseding prior defaults.
- Shared checker passed (847 files). ES build/26-page verifier, SOC build/60-page/64-redirect verifier, PUBA build, SSRI build passed. Chrome tested representative content pages on each site at 320/768/1200/1800px (16 cases), confirming all generic heading/body sizes/weights, unit-name weight and no horizontal overflow. Evidence exports/heading-scale-2026-11-14.json. No full accessibility audit or browser zoom test performed.
- Local shared CSS/docs/report plus local regenerated outputs only; not committed/pushed/deployed. Shared consumer styles change on rebuild; other sites not rebuilt in this task. User visual review remains next before returning to ES undergraduate work.

## November 14: PUBA approved titles applied

- Applied approved 31-page PUBA title list via searchTitle plus Public Administration | UH Mānoa unit suffix. Removed three superseded full-university seoTitle overrides. Preserved full credential H1s on MPA/certificate pages; clarified Why Study Public Administration? and MPA Practicum Placements H1s. Remaining H1s, nav, URLs and copy retained. Shared typography unchanged.
- Saved exports/seo/puba-approved-titles-2026-11-14.json and puba-titles-2026-11-14.json. PUBA build passed. All 31 reviewed pages' exact rendered HTML/social titles and single H1s passed explicit checks. Whitespace checks passed.
- Full SEO scan also includes existing development-only hero-review.njk, currently emitting /hero-review.html despite older audit documentation saying disabled. Its nine metadata errors and one canonical note are isolated to that utility, not the reviewed 31 pages; retained its source/config untouched pending user review. Eight title/H1 wording notes on current pages reflect approved labels. Do not claim full SEO audit clean. Preview indexing remains off.
- Local PUBA source/shared settings/docs/reports only; not committed/pushed/deployed. Existing homepage welcome/local program changes preserved. Next: shared H1/unit-name visual hierarchy, then ES undergraduate review.

## November 14: SSRI titles applied; PUBA list pending

- Applied approved 16-page SSRI title inventory using searchTitle plus SSRI | UH Mānoa unit suffix. H1s/content, URLs, descriptions and nav unchanged; no H1/unit-bar typography changes. Retained HAM/HCRI/OENAS and compact TASI/PHIDC as explicitly approved. SSRI working tree was clean before this task.
- Saved exports/seo/ssri-approved-titles-2026-11-14.json and ssri-titles-2026-11-14.json. SSRI build passed, SEO audit zero errors/four intentional title-H1 shortening notes. All 16 exact rendered titles and one H1/page checked. Preview indexing remains off; whitespace checks passed.
- PUBA's 31-page source inventory read and proposed title list supplied for approval; its previous local changes preserved. No PUBA title conversion or shared typography change performed. Local SSRI source/shared settings/docs/reports only; not committed/pushed/deployed.

## November 14: ES titles approved and both H1 inventories reviewed

- Applied all 26 approved ES titles with Ethnic Studies | UH Mānoa suffix, removing four superseded full-university seoTitle overrides. Saved exports/seo/es-approved-titles-2026-11-14.json and measured exports/seo/es-titles-2026-11-14.json. Existing page title/frontmatter and navigation labels otherwise retained.
- Reviewed all rendered SOC/ES pages' single H1s, including shared profile/policy/404 headings. Earlier degree H1 expansions remain. Clarified SOC Why Study Sociology?, Graduate Annual Review, Graduate Applications & Admissions, Current MA and PhD Students, Graduate Student Organizations, BA Student Learning Outcomes. ES Why Study Ethnic Studies? and Our History, Our Way replace abbreviated/dash versions. Full research H1s, faculty names and approved homepage H1s unchanged.
- ES build/26-page verifier and SOC build/60-page/64-redirect verifier passed. Exact-title/single-H1 assertions passed on all 86 current pages. Whitespace checks passed. ES SEO audit is NOT clean: 25 placeholder descriptions plus duplicate-description error; 26 canonical review notes and nine intentional H1/title wording notes. These existing ES final-SEO tasks were surfaced, not silently waived. Preview indexing stays off.
- Local ES/SOC source, ES verifier, shared unit settings/docs/reports only; not committed/pushed/deployed. PUBA title conversion not performed. No broader SEO completion claimed.

## November 14: SOC approved title inventory and SEO process correction

- Applied all 60 approved SOC title labels, using Policies & Procedures and Graduate Applications & Admissions and retaining conjunctions in research titles. Unit titleSuffix Sociology | UH Mānoa composes with each page's searchTitle. Removed SOC's five superseded full-university seoTitle overrides. H1s, URLs, nav labels and descriptions unchanged. Shared shell supports searchTitle/titleSuffix while preserving legacy defaults/overrides for unconverted units.
- Saved approved inventory exports/seo/soc-approved-titles-2026-11-14.json and measured audit exports/seo/soc-titles-2026-11-14.json. All 60 rendered titles exactly match the approved list. SOC build/60-page/64-redirect verification passed. SEO audit: zero errors, 15 intentional title/H1 wording-review notes corresponding to approved shortenings/context/credential labels. Preview indexing remains off.
- Corrected SEO workflow gap: require complete plain title-list review, unit/campus suffix consistency and semantic/length review; metadata presence alone is insufficient. Shared SEO checker now understands configured suffixes and flags missing suffixes instead of misreporting every composed title/H1 pair. Conventions updated to supersede earlier full-university program-title exception.
- Shared shell regression: ES build/26-page verification passed without converting its titles yet. Proposed ES list supplied in chat for approval. No PUBA title conversion performed. Whitespace checks passed. Local source/shared data/template/checker/docs/reports only; not committed/pushed/deployed.

## November 14: Academic H1 and university-qualified search titles

- ES: expanded four overview H1s to Undergraduate Certificate in Ethnic Studies, Bachelor of Arts in Ethnic Studies, Double Majors in Ethnic Studies, Combined Bachelor’s and Master’s Pathways in Ethnic Studies (BAM). Broad BAM label covers the supplied education/public administration pathways without calling them all MA degrees.
- SOC: expanded Minor, BA, BAM, MA and PhD overview H1s to credential/subject names. PUBA's three existing full program H1s retained. Across all 12 overviews, page-level seoTitle adds at the University of Hawaiʻi at Mānoa. URLs/nav labels unchanged; subpages not swept.
- Shared shell supports optional seoTitle consistently in HTML/social titles; existing title-plus-site-name fallback remains for other pages. Updated naming convention/SEO procedure. ES verifier handles approved source H1 replacements; original source snapshot unchanged.
- ES and SOC builds/verifiers passed; PUBA build passed; shared-source readiness check passed. Rendered assertions verified all 12 exact university-qualified titles, single H1s and matching available social titles. Whitespace checks passed. No ranking claims or live-search verification; no browser typography check in this pass. Existing ES placeholder descriptions remain for final SEO review.
- Local ES/SOC/PUBA source, ES verifier, shared shell/docs only; not committed/pushed/deployed. Existing unrelated changes retained.

## November 14: Certificate career content moved to Why Study

- Moved certificate Skills and Knowledge and Job Prospects sections, retaining all nine skill and eight career entries/wording, to a new white section at the bottom of Why Study ES. Standard HR separates their H2s. Existing learning outcomes remain gray.
- Certificate gray block now ends after requirements/designations/catalog note. Separate white declaration section directly precedes shared Undergraduate Advising. Heading Declaring an Ethnic Studies Certificate and concise wording follow SOC's Declaring a Sociology Major/Minor pattern; existing Kuali destination and login-required notice retained, advisor guidance points conceptually to the widget below instead of general faculty directory.
- Updated verifier to check every moved source chunk on Why Study rather than Certificate, and declaration heading/form destination. ES build/26-page verification and whitespace checks passed. No browser check rerun. Local ES source/verifier/shared handoff only, not committed/pushed/deployed. Equivalent legacy material still on BA page pending its review.

## November 14: Certificate delivery paragraph and course columns

- Merged Course Delivery Options into one paragraph without wording changes; added standard HR before Certificate Requirements. Applied existing list-columns-two to Group 1 and Group 2 long course lists only. Short requirements/introductory/nested lists unchanged. No new CSS.
- ES build/26-page verification passed. Chrome at 320/768/992/1800px confirmed both H2s have identical 20.4px/600 styles, long lists use one column below 992 and two above, and no document overflow. Existing break-inside avoid keeps each course item together; names wrap within their columns. Initial temporary browser script syntax error corrected before successful run. Whitespace checks passed.
- Local certificate source/shared handoff only; not committed/pushed/deployed.

## November 14: Certificate intro and gray program details

- ../es/src/undergraduate/certificate-es.html has H1 and merged single-paragraph intro in its own white section. Intro sentence wording retained. Removed obsolete Contact Us/email/phone, old ES Courses shortcuts and generic Additional Details heading; existing shared advising/resource widgets supply the current contacts/course links.
- Course Delivery Options starts a full-width gray section through How to Apply, ending before white Undergraduate Advising. Promoted existing Course Delivery Options, Certificate Requirements, Skills and Knowledge, Job Prospects and How to Apply labels to H2; requirements, course lists, credit counts and supporting content retained. Standard section/row/column wrappers, no CSS added.
- ES build/26-page verification passed with explicit exceptions for only the approved obsolete sidebar labels/contact data. Source assertions confirmed one intro paragraph, gray boundaries and advising placement. Whitespace checks passed. Local source/verifier/docs only; not committed/pushed/deployed.

## November 14: SOC degree palette and foreground layout guides

- SOC homepage degree tiles now use blue undergraduate, purple graduate and blue/purple BAM, retaining Jigsaw artwork and all links/geometry. Research-photo fallback palette unchanged.
- Extended existing diagnostic foreground-guide technique from photo tiles to main-content Bootstrap columns and all program tiles. Pointer-transparent ::after with z-index 100 draws red guides above image/tile surfaces; relative column positioning anchors the overlay, without dimensions/padding changes. Only diagnostics.css changed; existing per-site toggle remains respected (SOC guides remain off). Updated diagnostics documentation.
- SOC build/60-page/64-redirect verification and ES build/26-page verification passed. Chrome checked ES homepage at 320, 768, 1200 and 1800px: all 11 column/tile overlays present, pointer-events none, no viewport overflow, identical measured geometry when overlays hidden/shown. Whitespace checks passed.
- Local SOC source/shared CSS/docs only; not committed/pushed/deployed. Other unrelated site work retained.

## November 14: Blue/purple academic tile palette

- ES homepage Certificate, BA and Double Majors tiles now use existing shared tile-blue. BAM uses new reusable tile-split-blue-purple modifier with existing brand color tokens. No geometry, typography or link changes.
- Updated academic tile palette convention: blue undergraduate, purple graduate, blue/purple combined; supersedes teal because of visual competition with UH green. Other teal components unchanged. SOC/GEO not edited in this pass; their existing palette remains pending review/update.
- ES build and 26-page verifier passed; whitespace checks passed. Local ES source/shared CSS/docs only, not committed/pushed/deployed.

## November 14: ES academic-program row completed

- ES homepage gray Academic Programs row now starts with a col-lg-4 introduction, followed by the existing four col-lg-2 tiles. This fills the desktop row at one-third text/two-thirds tiles without enlarging tiles. Intro stacks above tiles below 992px; existing four/two/one tile breakpoints retained. Standard Bootstrap grid only, no CSS added.
- Added concise description: Flexible pathways connect undergraduate study in ethnic studies with diverse academic interests and opportunities for graduate study. Links, colors and tile labels unchanged.
- ES build and 26-page verifier passed; whitespace checks passed. No new browser layout check. Local homepage/docs edits only; not committed/pushed/deployed.

## November 14: Sociology H1 approved

- User approved SOC: Understanding Society, Inspiring Change for the homepage H1, subject to later department review. Applied to ../soc/src/index.html; welcome, existing tagline, page metadata and remaining content unchanged. Updated conventions to supersede the pending-H1 note.
- SOC build and 60-page/64-redirect verifier passed; whitespace checks passed. Local source/docs only; not committed/pushed/deployed. Unrelated Support edit preserved.

## November 14: Sociology homepage welcome and tagline order

- ../soc/src/index.html now has the standard E komo mai — Welcome to the Department of Sociology within the College of Social Sciences at the University of Hawaiʻi at Mānoa. Existing tagline follows that welcome; subsequent paragraph starts Sociology connects to avoid immediately repeating the university name. Other text/layout unchanged.
- Suggested SOC: Understanding Society, Inspiring Change in chat as a candidate H1; not adopted pending user choice. Current H1 retained. Existing unrelated Support edit preserved.
- SOC build and verifier passed (60 content pages, 64 redirects, internal links/anchors, image alt attributes/CSS). Whitespace checks passed. Local SOC homepage/shared handoff only; not committed/pushed/deployed.

## November 14: PUBA homepage welcome

- ../puba/src/index.html now uses E komo mai — Welcome to the Public Administration Program (PUBA) within the College of Social Sciences at the University of Hawaiʻi at Mānoa. A full stop precedes This innovative graduate-level program is dedicated to the enhancement of public service and institutions. Changed our program to the program in that opening paragraph; other homepage content/layout retained.
- PUBA Git status was clean before this edit. Build passed; rendered exact opening/sentence boundary and whitespace checked. No wider text/accessibility/browser audit rerun. Local PUBA source/shared handoff only; not committed/pushed/deployed.

## November 14: Approved bilingual homepage welcome

- ES homepage intro now starts E komo mai — Welcome to the Department of Ethnic Studies within the College of Social Sciences at the University of Hawaiʻi at Mānoa. Remaining content/layout unchanged.
- Updated existing homepage convention: bilingual welcome approved, superseding tentative/English-only versions. User-specified em dash is an explicit exception to the prose-dash rule. No other sites edited.
- ES build/26-page verification and whitespace checks passed. Local source/verifier/docs only; not committed/pushed/deployed.

## November 14: Homepage welcome opening

- ES homepage paragraph now begins Welcome to the Department of Ethnic Studies within the College of Social Sciences at the University of Hawaiʻi at Mānoa. The next sentence begins The department provides a home; remaining copy/layout unchanged.
- Updated the existing institutional-intro convention to begin Welcome to, superseding its earlier declarative example. E komo mai remains tentative while the user investigates; not inserted or adopted as a standard. Other sites unchanged.
- ES build/26-page verification and whitespace checks passed. Local source/verifier/docs only; not committed/pushed/deployed.

## November 14: ES homepage institutional identification and voice

- ES opening paragraph now starts with The Department of Ethnic Studies within the College of Social Sciences at the University of Hawaiʻi at Mānoa. Converted remaining our/we/you references in that paragraph to third-person departmental/student wording, preserving its existing claims. H1 and layout unchanged.
- Recorded full unit/college/university identification as the shared homepage-intro convention for future review. No other unit homepage changed; SOC catchline remains pending.
- ES build and 26-page verifier passed with explicit approved identity/voice substitutions; whitespace checks passed. Local source/verifier/docs only, not committed/pushed/deployed.

## November 14: Final ES homepage H1 choice

- Changed ../es/src/index.html H1 to ES: What World Do You Want to Make? and removed the separate tagline. Intro, logo and program tiles unchanged. Recorded the approved ES-specific acronym/purpose heading and supersession in conventions.
- Updated original-content verification for the relocated/title-cased question. ES build and 26-page verification passed; whitespace checks passed. Local source/verifier/docs only, not committed/pushed/deployed.

## November 14: ES homepage introduction and academic tiles

- Homepage H1 now Ethnic Studies at the University of Hawaiʻi at Mānoa. Existing question What world do you want to make? is a separate tagline paragraph. Remaining original introduction retained. Shared profile-page provides 80/20 wide-desktop text/logo layout with supplied 633x633 es-history-logo.png, visually checked and given descriptive alt.
- Added gray Academic Programs section with Certificate, Major (BA), Double Majors, BA/MA Pathways (BAM) links in academic progression order. Reused program-tile/tile-style, teal undergraduate and split teal/purple BAM. Bootstrap col-lg-2 makes each tile one-sixth of the desktop row rather than one-quarter, leaving deliberate open space; tablet four across, small screens two, narrow phones one. No custom CSS or duplicated grid system.
- ES build and 26-page verifier passed, preserving original introduction text with approved H1 exception. Whitespace checks passed. Browser layout review remains pending; tile sizing is a first visual pass for user review. Local source/verifier/docs only, not committed/pushed/deployed.

## November 14: Why Study ES voice and outcomes section

- Recast ../es/src/about-es/why-study-es.html intro into third-person departmental voice, retaining its existing claims and single-paragraph structure. Removed four degree/program link paragraphs. Intro stays white; unchanged Student Learning Outcomes heading, introductory sentence and all six outcomes now occupy a separate full-width gray section using standard wrappers. No new CSS.
- Outcome applicability to BA versus other programs remains unconfirmed; no BA-only label added. Existing outcome wording/typography retained for later text review.
- ES preservation verifier allows the specific approved voice substitutions/link removals and still checks all outcomes. Build and 26-page verification passed; whitespace checks passed. No new browser test. Local source/verifier/docs changes only, not committed/pushed/deployed.

## November 14: ESSA intro/logo and photo section

- Rebuilt ../es/src/about-es/ethnic-studies-student-association.html with full name/acronym in H1, ESSA opening the intro, and unused ES acronym removed. Otherwise existing intro and closing wording retained. Shared profile-page places supplied ESSA logo right at 80/20 wide desktop and stacks on mobile.
- Separate full-width gray section contains supplied essa-01/02/03 photos in order across three desktop columns, stacking below 768px, then closing paragraph and plain Find us on Facebook. info link. No promotional Facebook graphic or archive/activity disclaimer. Reused Bootstrap/shared styles; no new CSS.
- Inspected all three photographs visually and supplied descriptive alt text; logo has full-name alt. Actual dimensions 900x506 photos and 300x207 logo retained.
- ES build/26-page verifier passed with explicit approved acronym exception; original evidence untouched. Rendered assertions checked photo order, closing-copy placement and acronym cleanup; whitespace checks passed. No new browser layout test. Local source/verifier/docs only, not committed/pushed/deployed.

## November 14: Island Connections archive links grouped

- Added standard HR below the info sentence, followed by Episodes and Archives H2 and two bullets: Visit Island Connections on YouTube, then View the show archive. White layout and right logo retained; no gray box. Host attribution remains omitted following the preceding simplification; current host was not verified.
- Preservation verifier recognizes approved link-label/order changes and explicitly checks both original destinations remain present. ES build and 26-page verification passed; whitespace checks passed. Local source/verifier/docs only, not committed/pushed/deployed.

## November 14: Island Connections viewing-information link

- Added user-supplied https://www.hawaii.edu/its/uhcable/ to the existing Island Connections info sentence: Friday schedule for broadcast times, UH Cable viewing information for channels/service providers. Retrieved the ITS page and confirmed its purpose. Provider names/channel numbers remain maintained at UH, not duplicated locally.
- ES build and 26-page verification passed; whitespace checks passed. Local source/docs only, not committed/pushed/deployed.

## November 14: Island Connections simplified

- ../es/src/about-es/island-connections.html uses the shared profile-page 80/20 wide-desktop layout with the supplied branding/island-connections.png in the right sidebar. Logo visually inspected; actual 360x172 dimensions and descriptive alt supplied. No CSS added.
- Retained a concise program introduction, archive and YouTube links. Replaced Oceanic/QAM channel list, named-host and recurring airtime/rebroadcast details with an info link to https://www.uhonline.hawaii.edu/cablefriday. Retrieved UH Online page lists the show but is dated August–December 2025; no current schedule claimed locally.
- Updated preservation verifier only for the approved removed legacy intro/schedule/list, retaining original snapshot evidence. ES build and 26-page verification passed; rendered logo/alt/schedule destination and absence of Oceanic checked. Whitespace checks passed. No browser layout test. Local edits only; not committed/pushed/deployed.

## November 14: Our History, Our Way logo/sidebar

- ../es/src/about-es/our-history-our-way.html now uses the existing profile-page 80/20 wide-desktop layout, stacking on mobile, with the supplied ES branding logo in the right sidebar. Preserved history wording and destination; visit sentence now uses shared info/icon-text treatment. No new CSS.
- Inspected the logo visually, used its actual 666x668 dimensions and descriptive alt text Department of Ethnic Studies logo. Alt-text review remains part of accessibility checks; no user clarification needed for this identifiable logo.
- ES build and 26-page verifier passed, including preserved source text and asset checks. Whitespace checks passed. No new browser test performed. Local source/docs changes only; not committed, pushed or deployed.

## November 14: ES undergraduate advising and course resources

- Added shared advising widget and bottom course resources to Certificate, Major (BA), and Double Majors in ../es/src/undergraduate/. Reused existing templates and CSS; existing academic content retained, empty headings removed. BAM unchanged.
- ES advising data references Ethan Caldwell and Monisha Das Gupta from people.json, then Dawn Nishida last as General Education Advisor. Added Dawn to common advisor data using her existing shared photo/email and user-supplied office/phone. GEO's older staff record remains unchanged.
- ES catalog configuration uses the existing common ethnicStudies destination (ent_oid=702) and ES prefix. The bottom resource bar follows advising directly above the footer on all three pages.
- ES build and 26-page verifier passed. Rendered assertions checked advisor ordering, Dawn contacts, catalog destination and resource/footer placement on all three pages. No browser check or live external-link verification in this pass. Local changes only; not committed, pushed or deployed.

## November 14: ES news removed

- Removed ../es/src/department-news.html and stale generated output, plus the homepage Department News heading and empty Find us on label. No active news routes/menu links remain in source/unit data. Kept the homepage introduction, shared footer social links and all three statements under Policies & Procedures. Original export and annotated worksheets unchanged.
- Verifier excludes the expressly retired news snapshot and recognizes the removed homepage labels without altering original evidence. ES build/verification passed: 26 pages, nine biographies, 21 preserved active content bodies, links/assets/anchors, metadata/heroes. Whitespace and statement-anchor checks passed.
- Final old-URL/404 work must account for the retired news landing/remaining posts and the three statement moves; no new redirect decision implemented in this task. Local ES source/verifier and shared docs changes only; no commit/push/deployment.

## November 14: Center for Oral History linked name and logo

- Linked Center for Oral History in its opening paragraph to the existing center URL, removed unused (COH) and the separate Visit paragraph. Other introductory copy retained. Applied the shared profile-page biography/sidebar layout with the supplied /media/units/es/coh/coh-logo.svg on the right (80/20 wide desktop, 67/33 intermediate, stacked mobile). No new CSS.
- SVG inspection: valid 666x666 viewBox, vector circles/paths only, no scripts, event attributes, external resources, embedded files, DOCTYPE or entities. Artwork unchanged. Logo has full-name alt text and explicit dimensions.
- Added general acronym-usefulness checks to conventions, text-cleanup procedure and report template, with exceptions for established labels/branding/credentials/quotes. ES verifier recognizes the approved abbreviation/CTA changes while preserving original evidence.
- ES build/27-page verification and whitespace checks passed. Rendered name link/logo/no redundant CTA checked. Chrome verified SVG decoding and standard column ratios/stacking at 320, 768, 1200 and 1800px without overflow. Local ES source/verifier and shared asset/docs edits only; not committed/pushed/deployed.

## November 14: Targeted ES grid consistency check

- Confirmed Support uses reverse imageTextRow, Contact uses shared unit-contact plus people-grid, and ES Faculty uses shared faculty-directory/people-grid; no local grid CSS.
- Chrome checked each page at 320, 768, 992, 1200, 1600 and 1800px (18 cases). Support: 75/25 text/logo desktop, 67/33 tablet, stacked phone. Office/map: 20/80 at 1600+, 33/67 tablet/smaller desktop, stacked phone. People grids use standard 5/4/3/2/1 columns with five contacts and nine faculty. All stayed within viewport; no document overflow.
- No layout corrections needed. Evidence: exports/es/ES-grid-check-2026-11-14.json. Local report/handoff edits only; no website source edits, rebuild, commit, push or deployment in this check.

## November 14: Support ES intro and Available Funds

- Rebuilt Support ES with the shared reverse imageTextRow: H1, unchanged intro and appreciation on white, linked Foundation logo on the right. Separate full-width gray section starts with Available Funds and contains all four fund descriptions/links at equal list weight, alphabetized by displayed title. No featured fund in the intro. No new CSS.
- Preserved all four link/description records; verifier allows the approved alphabetical fund order while checking source text remains. ES build/27-page verification and whitespace checks passed. Confirmed rendered intro/gray boundary, logo row and four list entries.
- Local ES source/verifier and shared documentation changes only; no commit/push/deployment.

## November 14: SOC and ES support appreciation

- SOC Support's closing italic sentence and ES Support's We sincerely appreciate sentence now use the exact separate paragraph Contributions of any size are sincerely appreciated., with shared appreciation/icon-text classes for the smiley icon. No new CSS. Other support copy, fund links and images retained.
- Recorded the common support-page treatment. ES verifier recognizes the explicitly approved wording replacement without editing the preserved source snapshot. ES/SOC builds and verification passed; both rendered paragraphs checked for exact wording, structure and no italics. All whitespace checks passed.
- Local SOC/ES source, ES verifier and shared docs changes only; no commit/push/deployment.

## November 14: Associated Faculty and policy dividers

- Added standard HR above ES Affiliate Faculty using an optional dividerBefore group flag in the shared associated-faculty include. Other units do not receive new listing dividers unless configured.
- Shared policy core now uses nine compact my-3 item dividers and one standard divider between Tobacco Products Policy and Graduate Division. ES's two statement separators also use the compact treatment. Reused existing HR styles; no CSS or wording changes.
- Shared/whitespace checks passed; ES build/27-page verification and PUBA regression build passed. Checked rendered separator counts and exact placements on both policy pages and ES Associated Faculty. Local shared template/data/docs edits only; not committed/pushed/deployed.

## November 14: Associated Faculty intro and gray listings

- Added one ES-specific intro paragraph grounded in the existing keywords: humanities/social sciences, race/ethnicity, Indigenous cultures, political economy, social justice and Hawaiʻi/beyond. H1/intro occupy white; existing listings now occupy their own full-width gray section.
- Kept Emeritus/Retired Faculty first, Affiliate Faculty second as requested. Alphabetized members by surname; all 13 member records, emails and research descriptions unchanged. Deferred dash/diacritic editing. ES verifier checks associated source text presence without imposing the superseded legacy list order; other source preservation checks remain ordered.
- Shared check, ES build/27-page verifier and whitespace checks passed. Confirmed section placement, group order and 13 retained names. Local ES source/verifier and shared listing-data/docs edits only; no commit/push/deployment.

## November 14: Shared buildings folder and George Hall

- Renamed src/media/shared/other to src/media/shared/buildings, retaining all three files and their bytes: george-hall.webp, sakamaki-hall.webp, saunders-hall.webp. Updated common buildings.json, POLS unit override and its migration helper; no active old-path references remain in shared source/scripts or consuming sources. Historical path-map evidence retained.
- Common George Hall now uses the supplied george-hall.webp (300x162) with correct alt text instead of the Saunders placeholder. Removed ES's empty buildingPhoto override so its Contact page inherits the real building image. Existing addresses/maps unchanged; other building selections retained.
- Shared check and whitespace checks passed. ES build/27-page verifier passed; POLS and PSY builds passed. Verified ES/POLS/PSY contact photo URLs resolve to copied buildings assets, with ES using George Hall. No browser/layout change needed for a path/photo assignment.
- Local shared assets/data/helper/docs changes only; no commit, push or deployment. Earlier ES edits and workbook preserved. Consuming builds generated ignored output only.

## November 14: ES Contact Key Contacts

- Added the shared mixed five-person people grid below Contact's office/map: Aga, Caldwell, Danico, Das Gupta and Hasager, in surname order. Preserved existing titles and roles (including academic advising, department chair, oral history and civic engagement) and contact details. Moved Aga off the faculty page; no staff section remains there.
- Merged the existing nine faculty plus one staff record into ES people.json; showInKeyContacts selects the five contacts and showInFacultyDirectory selects nine faculty. Removed old faculty.json/staff.json to avoid duplicate identity records. Biographies still resolve the loader's derived faculty collection. ES verifier follows that same selection.
- Contact uses the agreed three-section layout: white intro, gray office/map, white contacts. No new CSS. Shared checks, ES build/27-page verifier and whitespace checks passed; exact roster/order, below-map placement and staff exclusion from faculty verified. Chrome verified five contacts with loaded portraits, one across at 320px and five across at 1800px.
- Local ES source/verifier and shared people/docs changes only; no commit, push or deployment. Existing hero assignments and workbook remain untouched.

## November 14: Courses and Why Study ES hero swap

- Applied chat override to the workbook assignment: Courses now uses ES hero-15.webp; Why Study ES uses hero-14.webp. Updated applied-mapping evidence; original workbook unchanged.
- ES build passed; checked both rendered hero URLs. Local shared data/evidence/handoff changes only; not committed/pushed/deployed.

## November 14: ES workbook hero assignments applied

- Read the reviewed workbook USE column without altering it. Assigned all 15 selected non-profile pages to the supplied media/heroes/es/hero-01.webp through hero-15.webp files. Core Faculty workbook label resolves to ES Faculty /faculty/. Double Majors' hero-08.avif entry resolves to the supplied hero-08.webp. All 15 assets exist; supplied files retain their names/bytes.
- Assigned nine biography heroes from the seven Saunders mural images using a shuffled selection saved in faculty-heroes.json; choices do not vary at runtime/build. Kept common Policies 01 and Privacy 02. Default is ES hero-04; Department News is N/A in the workbook and uses the fallback while awaiting removal. Other old posts remain unmapped/no new pages created.
- Updated ES verifier to include common hero precedence, unit fallback and current source-page count instead of hard-coded 26. Root and /es/ builds/verification passed: 27 pages, nine bios, 22 preserved content bodies, internal links/assets/anchors, metadata and heroes. All 26 explicit/common assignments match rendered image URLs and real copied files. Shared and whitespace checks passed. No new visual/browser audit in this data-assignment task.
- Evidence: exports/es/ES-applied-heroes-2026-11-14.json. Reviewed workbook unchanged. Local shared data/assets/docs/evidence and ES verifier edits only; no commit, push or deployment. Existing ES page and portrait work preserved.

## November 14: Shared Privacy Policy hero

- Added /privacy.html to common page-heroes.json with /media/heroes/hawaii-hall/02.webp, alongside Policies & Procedures using 01.webp. Existing shared hero precedence enforces it across unit sites and shows it even where other heroes are disabled; no per-unit assignments needed. Style guide's separate /privacy/ reference information page is not the shared policy.
- Shared checks and representative ES/SOC builds passed; both built privacy pages use 02 while policies use 01. Local shared data/docs edits only; not committed/pushed/deployed. Other sites receive it when rebuilt.

## November 14: ES statements below shared policies

- Extracted three complete dated statements from the supplied November 14 export into src/includes/units/es/policies-procedures.njk, selected only by ES policies-procedures.json. They appear on white below shared gray university policies: Atlanta/anti-Asian violence (March 22, 2021), Black Lives Matter/racial justice (June 4, 2020), and anti-Asian/Chinese racism/COVID-19 (April 2, 2020). Newest-first is intentional for dated historical statements. Each title is H2 with a stable anchor and date; two HRs separate statements.
- Body wording, attributions, paragraphs and all 11 resource links preserved; removed WordPress wrappers/classes and source attribution italics. Further Resources is subordinate H3; resource list retained. Preservation evidence: exports/es/ES-statements-preservation-2026-11-14.json. Source date/context and first-person institutional wording remain historical, not freshly rewritten policy claims.
- Earlier analogous appendix is Anthropology's Position Statement on Race and Racism. Shared core/template mechanism unchanged; PUBA regression build confirms no ES statements leak into other units. ES build/shared/whitespace checks passed; built page checked for three titles/dates, order and rules.
- User intends to remove department news; this task preserves the statements independently first. Other news posts and the empty Department News placeholder were not imported or removed here; their route handling remains for the later full migration/404 review. No worksheet overwritten. Local shared content/data/docs/evidence edits only, not committed/pushed/deployed.

## November 14: ES Faculty label

- Changed Core Faculty to ES Faculty in the ES dropdown and faculty landing title/H1. Confirmed source ../es/src/faculty/index.html and existing /faculty/ permalink; no route or redirect change. Existing links and hero mapping keys remain valid. Review workbooks left untouched while open for annotation.
- Shared check, ES build and whitespace checks passed; verified built dropdown/title/H1. Local shared and ES changes only, not committed/pushed/deployed.

## November 14: ES original hero filename checklist

- Created exports/es/ES-page-checklist-with-heroes-2026-11-14.xlsx as a new copy, preserving the original two-column workbook and its row order/names. Added only column C, Original hero image. One worksheet, 39 rows including headers/separators; original-side blank means hero blank for new-only pages.
- Resolved thumbnail IDs to attachment filenames for all 33 published page/post entries in the supplied November 14 export. Used exported GeneratePress template rules to distinguish actual heroes from featured portraits: nine Faculty-category pages use DSC0922-jpg.webp; nine ES Post entries use hero-directory2-jpg.webp; remaining pages use their featured images through the dynamic Hero template. Original Directory supplies the source filename for both new faculty listing rows.
- Saved original featured and hero filenames together in exports/es/ES-original-image-map-2026-11-14.json for later remapping. Recorded ES's unit-specific hero exception. No downloads, image renaming, hero assignment changes, content edits, redirects or builds in this task.
- XLSX ZIP/XML, exact three-column contents, original two-column preservation and template/attachment resolution checked. Mapping reflects export configuration, not a live-site visual audit. Local shared workbook/evidence/docs edits only; not committed, pushed or deployed. Earlier portrait changes preserved.

## November 14: ES supplied faculty and staff portraits

- Renamed all ten supplied WebPs in shared src/media/units/es/faculty-staff to lowercase person slugs, removing jpg suffixes and inconsistent naming. Actual image bytes preserved. Nine faculty.json photo assignments now feed all biography and directory views; nine portraits are 333x333, Ty Tengan is 300x300. Staff portrait is 333x333.
- Added central staff.json for ʻAnoʻilani Aga and replaced the old inline Staff text on ../es/src/faculty/index.html with the shared people-grid/profile-card treatment, preserving her title/contact details. No new biography route. No active temp.jpg references; user-deleted placeholder stays removed.
- Shared check and ES build passed (27 pages); targeted source checks confirm ten assignments and all nine biography references. Existing full ES verifier still fails on its stale 26-page assumption and missing hero assignment for the pre-existing Policies & Procedures page; observed before portrait edits. Do not claim that full verification passed. Chrome verified all ten directory portraits and all nine biography portraits decode at their recorded dimensions and fit at 320px and 1800px (20 page/width checks).
- Local shared and ES edits only; no commit, push or deployment. Other user edits preserved; Contact was not edited in this task.

## November 14: Simple Ethnic Studies review sheet

- Created exports/es/ES-page-checklist-2026-11-14.xlsx from the supplied November 14 WordPress export and 27 current ES source pages. One worksheet, two name-only columns. Matched pairs first (25 rows covering 24 original pages; Directory maps to Core Faculty and Associated Faculty), followed by nine unmatched published news posts and two new-only pages (ES Courses, Policies & Procedures). Blank separators only; no URLs, notes, status fields, filters, dropdowns or additional tabs.
- Excluded drafts, attachments, theme/plugin entries and custom-field definitions. All 33 published page/post entries and all 27 new pages accounted for. No content, redirects or 404 changed. Fuller migration comparison deferred until after review.
- Shared workbook writer now supports optional compact rows, header-only freeze and disabled filtering; checked existing defaults remain intact. Validated XLSX ZIP/XML, one sheet/two columns, exact names/group order and no extra fields. Whitespace check passed. Local shared artifact/docs/helper edits only; no commit, push or deployment. ES repository unchanged.

## November 14: Security architecture added to services draft

- Added an eighteenth service to the private portfolio Page and its estimating prompt: intentional platform simplification and attack surface reduction through static publishing. Preserved the distinction between new static output and legacy WordPress exposure until retirement; no claim of a security audit, certification or quantified savings. Recorded this durable objective in project-conventions.md.
- Private Page edits confirmed by readback. Documentation only; no website source/security settings changed, no builds needed. Local documentation changes, not committed or pushed.

## November 14: Private portfolio services draft

- Prepared and read back a private Pages draft with a portfolio services checklist and neutral external-cost estimating prompt. Counted 10 implemented unit codebases containing 405 HTML sources, plus a 17-source style guide and shared system. Counts include utility pages and incomplete material; not 10 completed launches or 405 rewritten pages. Excluded configuration-only units.
- Distinguished shared work charged once, incremental unit work, completed versus outstanding scope, and documented accessibility/SEO passes versus inherited shared improvements. No dollar estimate, price research, meeting invitation or reminder created. No website source changes in this task.
- Private draft: https://chatgpt.com/space/page_269823331584819198b855e432d09d1b. Saved content read back successfully; no visual Page preview tool used. This handoff edit is local, not committed/pushed.

## November 14: Graduate Division outbound URL replacements

- Saved all five user-supplied old/new pairs in src/data/common/url-replacements.json: committee composition, research/publication, fellowships/scholarships, financial support and academic progress. New scripts/link-replacements.py provides unit-scoped report/apply modes and recognizes HTTP/HTTPS and www variants. Added it to conventions and link-review guidance for future sites.
- Updated five links in five SOC sources: funding, MA requirements/thesis, PhD requirements/dissertation. The other two supplied mappings have no current SOC matches but remain saved. Link labels and surrounding copy unchanged; other units and original exports untouched.
- Helper fixtures passed for report-only behavior, four scheme/host variants, trailing slash, query/fragment retention, unrelated paths/hosts and repeat runs. SOC replacement scan now finds zero old links. Shared checker passed. SOC build/verify passed (60 content pages, 64 redirects); both whitespace checks passed. These replacements are user-confirmed, not a fresh live external-availability audit.
- Local changes only for this task; not committed, pushed or deployed. Earlier local commits and saved dismissal documentation preserved.

## November 14: Saved crawler dismissal wording

- Saved the reusable Siteimprove crawler-blocked link dismissal in project-conventions.md under Reusable Siteimprove dismissal text. Retrieval phrases include no crawl dismiss forever text and dismiss forever. Return the exact provider-neutral wording for manually verified links blocked to crawlers.
- Also saved the approved hostname-resolution dismissal and a separate false-404 statement for links repeatedly verified manually. Retrieval phrases include hostname dismiss forever text and false 404 dismiss forever text.
- Documentation only; whitespace check passed. Local changes, not committed or pushed.

## November 14: Final review complete; GitHub authentication blocks upload

- User confirmed News uses department X link/email only, old Undergraduate Advising goes to Contact, and old Colloquia Archive goes to News and Events. Implemented all three. Migration now has 64 immediate HTML redirects: 55 original WordPress URLs plus nine intermediate routes. Two original URLs unchanged, no unresolved/retired routes. Historical archive content remains in the original export, not on the new news page.
- Final local review: 60 content pages, 64 redirects; source cleanup, text/course/voice spot checks, shared checks, root/project-prefix builds, internal links/anchors/assets and SEO pass. Focused axe/reflow passed 30 cases; contrast incomplete remains manual follow-up. SOC helper lines off, preview noindex retained. Full report: soc-final-review-2026-11-14.md.
- Known content follow-up: three Courses images, three Why Study images, Le Lin's unfinished ending. External funding links are deferred to Siteimprove. News fallback is complete and approved.
- Local commits: SOC e95feff; shared fb8ba4e plus final routing/handoff follow-up. Both git push attempts failed with GitHub HTTPS authentication unavailable (could not read Username). No pushes, deployments, live 404/status validation or Siteimprove scan occurred. Origins were fetched before commits and were aligned; local branches now contain unpublished commits. Push shared main first, then SOC main using an authenticated Git client; SOC workflow builds with /soc/ preview prefix. No other consuming source repository committed.

## November 14: Final SOC review and preview preparation

- Completed focused final review after page-by-page approval. Full report: soc-final-review-2026-11-14.md. Formatted 48 SOC sources and one shared include; all 60 HTML sources now flush-left without blank lines. Before/after parsed content and markup preserved on all 67 then-existing outputs.
- Fixed remaining documented punctuation, diacritics, inline spacing and TMS definition issues; retained Le Lin's unfinished ending pending his reply. Courses/Why Study each retain three placeholder images. News now has the real Sociology X link and email-list contact, with the broken XDevelopers test removed; this conservative fallback was announced while optional preferences were pending.
- Added shared-standard SOC 404 and 63 static HTML redirects (not HTTP 301). Undergraduate Advising goes to Contact; former supplementary faculty bios go to the restored Faculty listings. Colloquia Archive is the sole unresolved old route; export content preserved, no silent retirement. Original review workbook untouched.
- Updated stale SOC verifier to use current source permalinks/redirect configuration. Root and /soc/ preview builds, internal links/anchors/assets, SEO (zero errors), shared checks and whitespace checks passed. Focused axe/reflow: 15 pages at 320/1800px, zero violations/overflow; contrast incomplete remains manual follow-up. SSRI/PUBA/GEO regression builds passed; their unrelated source edits preserved.
- SOC guides disabled with its existing per-unit flag; other sites retain their settings. Noindex/nofollow retained. Two benign SEO notes (full Asia/Pacific title, shortened Courses title) preserved. Funding external-link work remains for Siteimprove.
- Fetched shared and SOC origins successfully; both were on main with no pre-existing ahead/behind commits. Current changes prepared locally for GitHub preview; commit/push/deployment follow below when verified. No Siteimprove access or scan run claimed.

## November 14: Sakihara Scholarship requirements

- Moved Requirements and its five-item list to the bottom of ../soc/src/graduate/funding-sources/sakihara-scholarship.html in a separate full-width gray section using standard container/row/col-12 wrappers. Requirements is now H2. Selection committee paragraph follows the list inside the gray section, restoring its original order after clarification; substantive text retained. Touched source uses flush-left consecutive lines and separate list wrappers.
- SOC build passed (59 pages, 8 existing redirects). Local source/documentation edits only; no commit, push or deployment.

## November 14: Source formatting rule and pending cleanup

- Recorded shared HTML/Nunjucks formatting rules in project-conventions.md and new rules/code-cleanup.md: flush-left with no indentation or blank source lines; structural tags on separate lines; ul/ol wrappers and each li on consecutive separate lines. Public GitHub readability and future manual editing are explicit reasons. Preserve inline word spacing, whitespace-sensitive content, front matter and template semantics.
- Added the separate code-cleanup pass to final-review guidance in text-cleanup.md. SOC sweep remains pending the user's review phase (requested for roughly 20 minutes later); no sweep, scheduling, page edits or builds performed for this documentation task. Local documentation changes only, not committed/pushed/deployed.

## November 14: Emeritus and affiliate faculty restored

- Added simple Emeritus Faculty and Affiliate Graduate Faculty lists below the gray directory band on ../soc/src/faculty/index.html. Retained all four supplied names, emails and research interests; no photos, redundant rank titles or italics. Emeritus entries sorted by surname. Used the requested dash separator for these directory entries only.
- Current navigation already has no separate emeritus/affiliate item; no new page/menu item created. Faculty anchors emeritus-faculty and affiliate-graduate-faculty provide potential migration targets. The old Hagen Koo, Patricia Steinhoff and Yean-Ju Lee URL decisions can now be reviewed against this restored content; workbook and redirects unchanged pending review.
- SOC build passed (59 pages, 8 existing redirects); whitespace checks passed. Local changes only; no commit, push or deployment.

## November 14: Degree navigation bottom spacing

- Corrected component selector specificity in buttons.css so generic content UL/LI margins no longer override the navigation's zero margins. Flex gap alone now controls button separation; no negative margins or diagnostic changes.
- SOC build passed. Chrome verified both degrees at nine widths from 320 to 1800px: list/item margins zero, navigation bottom gap zero, desktop single-row fit and responsive wrapping preserved. Local shared changes only; not committed, pushed or deployed.

## November 14: Annual Review navigation correction

- Annual Review now uses one two-item navigation linking to Master’s (MA) and Doctorate (PhD) overviews, with exact dropdown labels. Supersedes the two full MA/PhD menus. Added SOC annualReview navigation data; shared include/CSS and standard col-12 diagnostic wrapper retained.
- SOC build, shared checks and whitespace checks passed. Verified the built page has one navigation with exactly these two overview links. Previous responsive component checks apply to the unchanged shared styling.
- Local shared/SOC changes only; no commit, push or deployment.

## November 14: MA and PhD navigation styling

- Styled the shared degree-navigation include with reusable classes in buttons.css: subtle gray rounded boxes, white hover/focus and current-page treatment, compact spacing, 44px minimum targets. Removed the former utility-only list treatment and extra nav top margin. Degree destinations and labels retained.
- SOC build passed (59 pages, 8 existing redirects). Headless Chrome checked MA/PhD at 320, 390, 576, 768, 992, 1024, 1200, 1400 and 1800px: one row from 1200px, natural tablet wrapping, full-width rows below 576px, no navigation overflow, one current item per overview. Shared checks and whitespace checks passed.
- Local shared changes only for this task; no commit, push or deployment. Ready for visual review across degree subpages.

## November 14: Academic Planning links

- In ../soc/src/undergraduate/academic-planning.html, updated the Law and Society certificate link to the supplied Political Science URL. Linked Minor and Certificates labels to the supplied catalog programs page and removed both trailing complete-list sentences. Other copy retained.
- SOC build passed (59 pages plus 8 existing redirects); whitespace checks passed. Local edits only, not committed, pushed, or deployed. Funding page accepted as consolidated; external-link review remains for Siteimprove after publication.

## November 14: AKD membership contact

- In ../soc/src/alpha-kappa-delta.html, replaced the obsolete Sociology Undergraduate Advising label with contact the Department of Sociology, retaining the general contact-page destination. No specific AKD recipient is confirmed; routing can change when the unit supplies one.
- Added the shared photo-style class to the AKD sidebar logo for the standard border, radius, and shadow treatment. No new CSS.
- Local source edits only; no commit, push, or deployment. Verified the link and image class in source and whitespace checks.

## November 14: SOC earlier BA requirements review

- Updated only the gray section in ../soc/src/undergraduate/major/requirements-fall-2022-and-earlier.html: Course Requirements heading now includes the 30 upper-division SOC credit requirement; removed the redundant sentence. Converted numbered labels to unnumbered H3s, removed label colons, and added shared my-3 dividers above Prerequisites and Additional Notes. Course lists and academic requirements retained.
- SOC build passed (59 pages and 8 existing redirects). Local source changes only; not committed, pushed, or deployed.

## November 14: Shared profile Online heading

- Renamed shared Website/Websites section Online. Ashley Rubin's Twitter entry
  now labeled X and moved into websites after Website; existing URL retained.
  SOC Website/CV label spaced Website / CV. SSRI Jack Barile's Faculty Website
  label simplified to Website; Research Lab unchanged. No link destinations removed.
- SOC, SSRI and PUBA builds passed. Checked Ashley's ordered Online links and
  preserved X URL; SSRI Online heading present; PUBA profiles have no affected
  website section. Shared/whitespace checks passed. Earlier unrelated SSRI/PUBA
  changes preserved; no source edits in those consuming repositories this task.
- Local css-shared changes only for this task; no commit/push/deploy. Commit/push
  shared alongside existing SOC work and rerun SOC and SSRI deployments to publish
  shared heading; PUBA rebuild passed with no affected profile heading.

## November 14: SOC Courses layout during page review

- Separated H1/intro into its own white section. Lower/Upper/Graduate Division
  now use three shared image-left rows in an independent full-width gray band,
  with shared decorative placeholders pending images. Course-resource widget and
  its preceding sentence are in a separate white section below. All copy retained.
- SOC build and whitespace checks passed; verified three rows, one gray band,
  one H1 and unchanged paragraphs. Local soc/css-shared handoff only; no push or
  deployment. Existing Excel workbook untouched so user review notes are safe.

## November 14: Sociology final review workbook ready

- Compared new WordPress export with saved November 10 source: same 57 published
  page IDs/titles/URLs and raw page bodies; 242 total items, no posts. Matched
  against 59 current local content pages. Updated stale destination proposals,
  checked local targets/fragments and recorded known merges/splits/editorial
  changes. No new content/media imported and no website source edited in this task.
- Excel: exports/soc/SOC-page-review-2026-11-14.xlsx. Five tabs: Page Review (59
  current pages, From/To local and GitHub links, status dropdown, notes), Old URLs
  (57), URL Decisions (7), Route Changes (8 existing plus Courses proposal), Read Me.
  Decisions: three unmatched faculty bios, colloquia archive, News, Events and
  Undergraduate Advising. No retirement assumed. News page still has XDevelopers
  diagnostic; advising functions are distributed, so primary target needs review.
- Old URLs: 2 unchanged, 40 moved proposals, 8 merged proposals, 7 undecided.
  All 57 originals and 59 current pages accounted for; all nonblank proposed paths/
  anchors resolve. SOC build, workbook ZIP/XML/rows/dropdown/360 hyperlink checks
  and both whitespace checks passed. Report docs/units/soc/soc-page-review.md; machine plan,
  CSV, workbook data and validation in exports/soc. Not a fresh factual-content,
  text/voice, accessibility or SEO audit; live preview freshness not verified.
- User reviews workbook first. New 404/redirect edits deferred; existing eight
  mappings unchanged. No 404 created. Follow with agreed decisions and final audits.
  Local css-shared artifacts/docs only for this task; earlier soc/shared work
  preserved. No commit/push/deploy; no synchronization claimed. Keep annotated
  workbook intact. Eventually commit/push soc and css-shared, rerun SOC deployment.

## November 14: Shared Jigsaw degree-tile overlay

- User approved 96px repeat size; reduced Jigsaw opacity to 0.1 for subtler
  linework. SOC rebuild passed. Local only; no commit/push/deploy.
- Scaled Jigsaw to 96×96px and repeated it at user request. Existing shared
  overlay now accepts size/repeat/opacity variables with original fallbacks;
  Jigsaw modifier owns these settings (opacity 0.2). GEO defaults unchanged.
  SOC build/shared and whitespace checks passed; no new browser pass for this
  size adjustment. Local only, no commit/push/deploy.
- Inspected supplied src/media/shared/backgrounds/jigsaw.svg: one black path,
  no background rectangle/image/script; thin filled line geometry left intact.
  Added reusable tile-pattern-jigsaw modifier setting existing --tile-background;
  applied only to SOC's five academic tiles. Existing filter makes black paths
  white at 20% overlay opacity, retaining teal/purple/BAM split colors.
- SOC build/shared and whitespace checks passed. Browser verifies all five
  computed background URLs/opacity and SVG transparent pixels; photo tiles and
  GEO's local contour asset unchanged. Local soc/css-shared only, no commit,
  push or deployment. Commit/push both and rerun SOC when ready.

- Homepage first paragraph after H1 now uses existing shared tagline class.
  Copy unchanged; SOC build passed. Local only, no commit/push/deploy.

## November 14: Health research description finalized for review

- User accepted life course sentence; retained lowercase. Added closing sentence
  about medical sociology as an established academic specialization and its ASA
  scholarly community, explaining section in ordinary language. Avoided unverified
  current growth/largest ranking; ASA membership form confirms topical groups.
- Removed both resolved Health review excerpts/reasons. No research-area review
  blocks remain. Courses/faculty unchanged. SOC build/whitespace checks passed.
  Local soc/css-shared notes only; no commit/push/deploy. User review of closing
  wording next; department approval not implied.

- Race research description: changed second-sentence opening from Research
  addresses to Areas of inquiry include, removing adjacent repeated openings.
  Topics unchanged; SOC build passed. Local only, no commit/push/deploy.

## November 14: Nationalism research description approved

- User approved the revised Nationalism, Globalization, and Sustainability
  description. Kept its wording and removed the resolved Material for Review
  excerpt/reason. Courses, faculty intro and grid unchanged. Health's two review
  excerpts remain unresolved; Nationalism meaning review is complete.
- SOC build and whitespace checks passed. Local soc/css-shared notes only;
  no commit, push or deployment.

## November 14: Crime research field clarification

- Added “the fields of” before the three named specializations and a brief
  Punishment and Society definition between the other two explanations, at user
  direction. Generic field context supported by SAGE handbook description;
  not attributed to department source text or additional faculty capabilities.
  Retained capitalization. Notes in docs/units/soc/soc-research-descriptions.md.
- SOC build and whitespace checks passed. Courses, faculty intro and memberships
  unchanged. Local soc/css-shared notes only; no commit, push or deployment.
  Department review of edited description remains pending.

## November 14: Sociology institutional voice cleanup complete

- Revised News, Contact, Courses, Faculty landing, Admissions, Hörmann Prize and
  Honors Track to third-person institutional prose. Courses' promotional commands
  now have third-person subjects; revised intro spells out the university name.
  Personal biographies, original review quotes, shared policy/instructions and
  external titles unchanged. No academic requirements or numeric facts changed.
- Rebuilt SOC and rescanned 59 rendered pages: no targeted institutional pronoun
  issues remain. Candidate blocks 67 to 57; remaining matches classified as
  intentional/contextual or Roman numeral/name false positives. Verified tags,
  attributes/links/templates/numbers unchanged on seven edited pages and preserved
  biography/quote content against baseline. Shared and whitespace checks pass.
- Report docs/units/soc/soc-voice-review.md; after evidence in exports/voice. No new browser,
  accessibility or SEO audit. Local soc/css-shared changes only; no commit/push/
  deployment. Commit/push both and rerun SOC deployment when ready; course-title
  discrepancies and remaining research-review statements still await decisions.

## November 14: Sociology voice scan

- Reviewed 59 rendered main-content pages and corresponding source; searched
  shared SOC JSON. Found 11 actionable first-/second-person blocks on seven
  department pages: News, Contact, Courses, Faculty, Admissions, Hörmann, Honors.
  Homepage/Why Study/research descriptions are consistent; Courses needs the
  clearest paragraph-level alignment. No website copy changed.
- Separated personal faculty biographies, shared Privacy, procedural guidance,
  external title and retained review quote; excluded Roman-I/name false positives.
  Report docs/units/soc/soc-voice-review.md; evidence exports/voice/soc-voice-2026-11-14.json.
  Voice review already belongs in text cleanup; documented dedicated scan option
  and contextual/manual limitations. Course-format check remains in checklist.
- Diff whitespace check passed. Read-only website task; no build/accessibility/
  SEO rerun. Local css-shared report/evidence changes only, no commit/push/deploy.
  Next: user-directed institutional-copy cleanup; preserve personal author voice.

## November 14: Research faculty introduction polish

- Revised five Research Area Faculty introductions using the main faculty page's
  contextual-opening pattern: Drawing on, Across, Using, From, Through. Kept
  third-person institutional prose and original expertise/method/publication/
  geographic claims, without repeatedly opening with Faculty. Main faculty page
  untouched; its supplied first-person model informed structure, not a global
  voice change. Retained claims were not independently reverified.
- SOC build/shared checks and whitespace checks passed. Source comparison proves
  only the five intro paragraphs changed; research descriptions, review items,
  courses and faculty grids/memberships unchanged. Local soc/css-shared records;
  no commit/push/deploy. Refresh locally for copy review.

## November 14: Research Areas landing image rows

- Added one source-grounded institutional intro to Research Areas landing and
  moved all five entries into a separate full-width gray band. Reused shared
  imageTextRow with the same 600×600 images as homepage, empty decorative alt,
  linked headings and unchanged short descriptions. Alphabetical order retained.
  No new local CSS. Detail pages, memberships and course lists unchanged.
- SOC build/shared checks and whitespace checks passed; verified five resolved
  shared images, original summaries/links, one H1 and balanced independent bands.
  Chrome checked 1800, 992, 768, 390 and 320px: image-left/stacked layouts fit
  and all five images load.
  Local soc/css-shared records only; no commit, push or deployment.

## November 14: Sociology direct catalog destination

- Changed SOC catalog settings to catalogKey sociology, reusing the shared
  direct entity link (catoid=4, ent_oid=707) already stored in uh-catalog.json.
  Replaces legacy category URL; Course Descriptions remains the separate main
  course-search destination with SOC prefix guidance. User approved stored URL.
- SOC build/shared checks and whitespace checks passed; built course-resource
  links verified. External catalog fetch returned 403, so destination contents
  were not verified. Local css-shared change; no commit, push or deployment.
  Commit/push css-shared with existing soc work, then rerun SOC deployment.

## November 14: Sociology course-format sweep completed

- Swept all 59 HTML sources and checked shared SOC JSON for course text. Fixed
  57 missing colons, three additional named-course prose references, two Honors
  code-description separators, three BAM trailing commas and S0C typo. Removed
  60 credit counts from all five research-area lists; academic credits retained.
- Rescan finds no confirmed missing named-course colons. Combined-lab, cross-list
  and Alpha notation retained; conflicting academic titles unchanged for review.
  Report: docs/units/soc/soc-course-format-review.md. No new course names/codes inferred.
- SOC build/shared checks and whitespace checks pass. Verified HTML structure,
  attributes/links/template code and academic credit annotations unchanged.
  No browser rerun for text-only changes. Prior shared/site work preserved.
- Local soc/css-shared changes; no commit, push or deployment. Commit/push both
  and rerun SOC deployment when ready. Academic-title discrepancies still need
  source verification; not a blocker to the completed punctuation sweep.

## November 14: Sociology course-format scan

- Read-only course-title list scan across 59 SOC HTML sources, with contextual
  review. Confirmed 57 missing-colon entries across five pages (Crime 17, Race 19,
  BAM 11, BA concentrations 5, minor concentrations 5). Most entries use colons.
- Separate issues: variant titles for same codes, lab/cross-list/Alpha notation,
  inconsistent credit display, BAM trailing commas and S0C typo in Honors prose.
  No academic titles or credits verified/changed; scan is not exhaustive of all
  prose/tables/shared JSON. Report: docs/units/soc/soc-course-format-review.md.
- Recorded SUBJECT NUMBER: Course Title convention and added report-only course
  review to text-cleanup checklist/template. No SOC edits for this scan; no build
  needed. Shared docs local only, no commit/push/deploy. Next: punctuation cleanup
  if requested; academic-title reconciliation remains a separate review.

## November 14: Research-area course-list layout

- Added HR before Related Courses on all five SOC detail pages. Added shared
  list-columns-two utility using footer-style CSS multicolumn flow: two equal
  columns at 992px+, one below, 3rem gap, no splitting individual list items.
  Course text and source order verified byte-identical apart from UL class.
- SOC build, shared checks and whitespace checks pass. Local soc/css-shared
  changes only; no commit, push or deployment. Existing review notes retained.
  Chrome verified all five lists at 1800, 992, 991, 390 and 320px: expected
  column counts, visible divider element and viewport containment pass.

## November 14: Photo-tile diagnostic guides

- Fixed missing red helper outlines on research photo tiles: image/label layers
  covered the parent inset shadow. Added a foreground, pointer-transparent guide
  in diagnostics.css only, following the existing navigation-guide approach.
  These guides indicate grid geometry, not validation failures. Production tile
  styling and the diagnostics toggle remain unchanged.
- Chrome verified all five foreground guides, no pointer interception, and
  identical geometry for all ten tiles with the new guides enabled/disabled.
  SOC build/shared checks and whitespace checks passed. Local css-shared change;
  no commit, push or deployment. Rebuild consuming sites to see the guide fix.

## November 14: Research-area faculty introductions

- Renamed all five grid headings Research Area Faculty and added one introduction
  based on each area's existing faculty material. All five have source material;
  no missing-introduction placeholders. Moved related upper review statements
  into faculty intros, retaining original expertise/accomplishment claims.
- Asia: area/language expertise, comparative strengths and Hawaiʻi/Oceania
  commitment; Crime: named expertise; Health: methods and publications; Nationalism:
  local-to-global research settings; Race: theoretical/methodological depth/breadth.
  Faculty-focused methods/scales removed from upper prose where relocated.
- Remaining upper review items: Health major-advances and field-size/growth claims;
  Nationalism sustainability-premise meaning check. Each retains its own reason.
  These are field-level/interpretive issues rather than department faculty intros.
- SOC build, shared checks and both whitespace checks passed. Verified all five
  intros, unchanged course sections and unchanged membership/card markup. No new
  browser pass for text relocation. Claims retained, not independently verified.
- Local soc/css-shared changes only; no commit, push or deployment. User reviews
  remaining three excerpts next. Commit/push both and rerun SOC when ready.

## November 14: Sociology research-description source reset

- User rejected the repetitive and subsequent subject-led short-description
  drafts. Rebuilt five short/long descriptions fresh from supplied soc-areas.txt.
  Alphabetical landing summaries use third-person present-tense openings: Explores,
  Examines, Investigates, Studies, Traces; each names source research topics.
  This supersedes the -ing trial. User delegated selection of grammatical form
  to the editor; corrected the earlier misattribution of that choice to the user.
  Long paragraphs use institutional third-person prose and preserve source scope.
- At that stage nine original source sentences were retained for review; faculty
  claims have since moved under Research Area Faculty as recorded above. Each remaining excerpt
  now has its own specific reason, identifying reputation/capability claims versus
  research subjects, unsupported time-sensitive prominence claims, or the precise
  sustainability-premise ambiguity. No generic blanket explanation. Removed
  duplicate criminal-justice topic only; no new academic claims or topics.
- SOC build, shared checks and both whitespace checks passed. Verified original
  excerpts against supplied text, individual reasons, consistent short openings,
  alphabetical landing order, third-person long paragraphs and no prose dashes.
  Course sections and subsequent faculty-grid markup byte-identical to pre-reset
  sources. No new browser pass for this text-only revision; prior layout checks
  remain documented below. Review guide: docs/units/soc/soc-research-descriptions.md.
- Local only in soc/css-shared; no commit, push or deployment. Prior unrelated
  work preserved. User review of new descriptions and retained claims is next.
  Commit/push both repositories and rerun SOC deployment after copy is settled.

## November 14: Sociology research-area faculty grids

- Replaced inline faculty lists on all five detail pages with shared people-grid
  cards in separate full-width gray bands after descriptions/courses. Existing
  prose/course markup preserved exactly. Cards use central people.json names,
  photos, titles and contacts, sorted by surname; no duplicated identity data.
- Added SOC-only research-areas.json membership references: Asia/Pacific 9,
  Crime 3, Health 3, Nationalism 5, Race 8. Shared optional loader resolves slugs
  to original people objects, rejecting duplicate/unresolved memberships. Canonical
  names replace inconsistent spellings in old inline lists. No roster additions.
- SOC build/shared checks pass; verified all memberships/order, portrait/profile
  targets and exact preservation of nonfaculty prose/courses. Browser checked all
  five pages at 1800, 1200, 768, 390 and 320px: directory column counts, viewport
  containment, separate gray sections and unique IDs pass. Uses established people
  grid breakpoints (five from 1600px), not homepage tile breakpoints.
- Local only in soc and css-shared; prior homepage/Why Study/Courses changes
  preserved. No commit, push or deployment. Commit/push both repositories then
  rerun SOC deployment when ready. Membership currency awaits unit review;
  current implementation faithfully follows existing page assignments.

## November 14: Sociology homepage, Why Study and shared tile review

- Moved SOC Courses source from about-soc/soc-courses.html to root courses.html,
  updated permalink, shared navigation and preserved hero assignment. No redirect
  added. Historical import report/importer retain initial route as evidence.
  SOC build/shared checks and whitespace checks passed; verified root output
  and navigation, removed stale local old-route output. Local only, not deployed.
- Alphabetized homepage research tiles by full displayed name: Asia/Pacific,
  Crime, Health, Nationalism, Race. Images and destinations travel with each tile.
  Degree progression retained as an explained exception. Recorded alphabetical
  default across college sites. SOC build and whitespace checks passed.
- Homepage has source-grounded third-person introduction, research photo grid on
  gray and academic tile grid on white. Programs: minor/BA teal, BAM split
  teal/purple, MA/PhD purple. Old comparison content/video link removed. Five
  supplied research images are shared assets; user still selecting final photos.
- Why Study has one-paragraph introduction, undergraduate/graduate image-left
  rows on gray and Career Directions image-left row on white. Three decorative
  shared placeholders remain. Original comparison removed; study anchor IDs kept.
  Career wording uses broad categories from supplied ASA 2008 bachelor's report
  and department graduate copy, without outcome statistics or guarantees.
- Shared grid-five uses one below 768px, three from 768–1399.98px, five from
  1400px. Middle-range centering rules are isolated to prevent implicit mobile
  columns. Shared photo-tile CSS reuses framing, interaction and grids; no local
  styles or Sociology-specific selectors. docs/shared/photo-tiles.md documents reuse.
- Labels use one 0.5rem padding control, two-line minimum bands, 400 weight,
  stable rem sizing and 80% black background (worst-case white-text contrast
  12.63:1). Final review found 200% text clipping with outer aspect ratio; square
  sizing track now allows enlarged label content to expand the tile. No forced
  line clamp. Earlier full-overlay, fixed-height and container-font trials retired.
- SOC and GEO builds, shared checks and both edited-repository whitespace checks
  passed. Chrome checks: both SOC grids at ten widths 320–1800px have expected
  5/3/1 counts and contained tiles. Photo labels checked at ten widths with 16px
  and 32px root text: no clipping, equal four-side padding, weight 400. Keyboard
  focus and reduced-motion checks passed. Not a comprehensive accessibility audit.
- Local changes in soc and css-shared; no commit, push or deployment. Existing
  unrelated GEO work preserved; GEO build output regenerated for verification.
  Commit/push soc and css-shared, then rerun SOC deployment when approved for
  publication. Other grid-five consumers inherit updated breakpoints on rebuild.

## November 14: Sociology X timeline trial

- User screenshot confirms XDevelopers follow button renders successfully.
  Current page replaces that button with the user's XDevelopers timeline test:
  dark theme, 666px width/height, in the full-width gray section, one loader at
  platform.x.com/widgets.js. SOC rebuild and output/whitespace checks passed.
  Timeline browser result pending; working follow button confirms the browser
  can render some X widgets despite earlier Sociology timeline HTTP 429 failures.
- User requires an entirely free ongoing solution. SociableKIT's current X page
  explicitly limits free updates to manual sync; automatic sync requires upgrade.
  Recommendation: stop that provider trial rather than add manual upkeep. Bluesky
  is under discussion; no migration or account creation authorized yet.
- User Console screenshot confirms widgets.js runs but X syndication returns
  HTTP 429 even after login. Login alone did not solve it; cause of the upstream
  rate limit is unknown. Grammarly warnings are separate. No successful live embed.
- Applied user-supplied widget variant: one light 600px timeline, noborders,
  correct Sociology profile/script URLs, shared white 500px-wide container with
  UH green top border and 600px minimum height to make its location visible.
  Removed duplicate old widget and malformed user-added script/profile URLs.
  This remains an embed trial, not a confirmed fix for post retrieval.
- Public legacy `/news/` inspection succeeded without login: Smash Balloon Pro
  2.11.1 renders 20 post cards directly into HTML, including text, original post
  links and image URLs. First card matches the supplied Terrell Carver screenshot.
  Public JS uses WordPress AJAX for pagination/background work. Broken settings
  export is not needed to read already-published posts. No private credentials read.
- A build-time fetch/parser could bridge these posts into static cards, retaining
  the last good snapshot on fetch failure. Not implemented or scheduled: continued
  updates would depend on the legacy WordPress installation/license remaining
  reachable at a known address after launch; this is not independent X access.
- Replaced News and Events feed placeholder with the official async X timeline
  for `@UHM_Sociology`, 700px high, with do-not-track requested and the separate
  direct account link retained. No Smash Balloon export or credentials needed.
- At user request, isolated the Sociology timeline in its own shared gray section
  below the introductory content, labeled “Posts from UHM Sociology”; removed
  the user-added XDevelopers test and extra loader. Rebuild and output checks pass.
  Corrected section nesting afterward: intro and gray band are sibling sections,
  with the gray background outside the intro container for full-width display.
- SOC build passed; generated HTML checked for timeline, one script loader,
  persistent profile link and removed placeholder. Both diff whitespace checks
  passed. Public oEmbed returned account markup; timeline endpoint returned HTTP
  429. These responses do not establish whether visitors can see live posts.
- User browser screenshot shows both Sociology and XDevelopers as plain fallback
  links, with no rendered timelines. Browser control unavailable here; script/network
  failure cause remains unconfirmed. Recheck the isolated Sociology feed. If it fails,
  investigate a supported static-site feed service before selecting a provider.
- Local changes only in soc and css-shared; no commit, push or deployment.
  Commit/push both repositories and rerun SOC deployment to test the hosted page.

## November 13: Sociology SEO cleanup and Open Graph diagnosis

- Completed 59-page metadata review. Replaced 57 placeholder descriptions with
  distinct content-based summaries; preserved two good descriptions, all titles,
  H1s, URLs and page bodies. Verified edited-body hashes unchanged.
- Added production self-canonicals in shared SOC settings; indexing remains off.
  Root and /soc/ preview builds/checker pass: zero errors, one intentional long
  research-area title advisory. Shared checks and diff whitespace checks pass.
  Restored root build for local preview after prefix verification.
- Confirmed live Open Graph bug: GitHub preview advertises production host plus
  /soc/ image path, returning HTML (HTTP 200), while correct GitHub image returns
  JPEG (HTTP 200), matching local export. Added SITE_ORIGIN to SOC deploy build;
  all 59 prefix-build social page/image URLs verified correct. Not deployed yet.
- Report: `docs/units/soc/soc-seo-audit.md`; before/after/prefix/live evidence in exports/seo.
- Tomorrow: final text/accessibility/SEO sweeps after edits and Le Lin’s reply;
  recheck deployed social tags, URL migration/custom 404/live HTTP behavior, fix
  stale migration verifier inventory, and retain manual contrast/map follow-up.
  No indexing launch, sitemap, Search Console action or cache refresh performed.
- Local soc and css-shared changes; earlier cleanup/audits preserved. No commit,
  push or deployment. Commit/push both, then rerun SOC deployment. Local ignored
  `_remove/` archive needs manual transfer if wanted on another machine.

## November 13: Sociology accessibility scan

- Local axe review complete: 59 content pages at 320/1800px, zero confirmed
  violations in 118 scans. All have one H1/main, language, image alt attributes,
  no duplicate IDs, no observed broken eager images and no page overflow.
- Keyboard skip/main focus, desktop dropdown keys/hover/Escape, mobile menu/search
  and three open-state axe checks passed. Text spacing passed on eight pages;
  768/1200px reflow passed on seven representative pages. Both timeline tables
  retain scoped column headers and valid accessible labels.
- Report: `docs/units/soc/soc-accessibility-audit.md`; measured evidence under
  `exports/accessibility/soc*-2026-11-13.json`. Axe contrast remains incomplete
  in 118 scans; external map/frame review incomplete in two. No full screen-reader
  session, comprehensive conformance claim or Siteimprove run.
- SOC build and shared check passed; no accessibility source changes needed.
  Stale migration verifier remains as previously recorded. SEO next, then live
  Open Graph diagnosis/final launch and accessibility follow-up after edits.
- User contacted Le Lin about incomplete paragraph; may receive reply November 14.
  Wait for supplied wording; no further action needed from user for this scan.
- Local css-shared report/evidence/handoff changes only for this task; prior
  SOC/shared folder-cleanup and text-audit work preserved. No commit/push/deploy.

## November 13: Sociology working-folder cleanup

- Audited SOC source/root files, image references across local/shared active source,
  build copy rules and scripts. Moved all 42 unused imported images, the retired
  downloader and four Finder metadata files to local ignored `../soc/_remove/`.
  Original paths/hash manifest preserved; user can move the folder out intact.
- No local source media remain. Active shared images unchanged. Kept source pages,
  WordPress XML, migration/URL evidence, build/deploy/check scripts, dependency
  files and Git metadata. Updated SOC README and accepted cleanup convention.
- Clean pre/post builds passed: all 582 retained generated files byte-identical;
  42 imported images absent from output. All 485 checked local HTML/CSS asset
  references resolve; quarantine not published and confirmed ignored by Git.
  Moved-file SHA-256 hashes verified; both repositories’ diff whitespace checks pass.
- Inventory: `exports/soc/folder-cleanup-2026-11-13.json`; topic notes in
  `docs/units/soc/soc-migration.md`. Stale full verifier remains as previously reported;
  no accessibility/SEO/live Open Graph scan performed in this folder task.
- Local changes in soc and css-shared; prior text report/artifacts preserved.
  No commit, push or deployment. Commit/push both repositories and rerun SOC
  deployment after syncing shared. `_remove/` is local only and will not sync.

## November 13: Sociology whole-site text scan

- Scanned 59 current HTML sources and 15 shared SOC JSON files; standard tool
  proposed zero mechanical patches and found zero heading wrappers. Saved measured
  findings and text extracted from all 67 rendered HTML pages (eight redirects).
- Report: `docs/units/soc/soc-text-scan-2026-11-13.md`. Flags two missing inline spaces,
  Le Lin’s apparently truncated sentence, prime/missing diacritics, one repeated
  research topic, TMS wording, and voice/degree/department naming for review.
  No source copy edited; naming suggestions are not accepted conventions.
- SOC build passed. `npm run verify` stops on stale missing graduate/gssa.html
  inventory; remaining verification did not complete. Checker update remains.
- Accessibility, SEO, live Open Graph diagnosis and final scans remain next, per
  user’s choice to start with text only. No claim about GitHub/cache cause.
- Local css-shared report/artifacts/handoff only; no commit, push or deployment.
  Both repository working trees were clean at start; remote sync not checked.

## November 13: Research summaries moved to Research Areas

- Replaced Research Areas landing page’s bare link list with the five original
  linked H2s and descriptions from Why Study SOC, preserving all wording/order.
- Removed the About Sociology/research block and Department History link from
  Why Study SOC. Both undergraduate/graduate overviews remain for the planned
  new intro and image/text grid treatment; no new copy or images chosen yet.
- Local ../soc edits only; no builds/tests, commit, push or deployment.

## November 13: Why Study graduate overview restored

- Restored Graduate Study H2 and its two original introductory paragraphs/degree
  links after clarifying the intended cutoff. Old graduate image/link blocks remain
  removed. Undergraduate overview and AKD navigation unchanged. Column/table
  treatment remains pending. Local ../soc edit only; no builds/tests, commit,
  push or deployment.

## November 13: Why Study SOC reduction and AKD access

- Removed everything beneath the Undergraduate Study overview paragraphs on
  Why Study SOC, including old images/link blocks and duplicate graduate overview
  material already represented on degree pages. Existing upper research material
  and undergraduate explanation remain unchanged.
- AKD remains linked from Graduate > Student Organizations. Added direct Alpha
  Kappa Delta link after Honors Track in Undergraduate navigation so both audiences
  can reach it after removing the old Why Study links.
- Local soc/css-shared edits only; no builds/tests, commit, push or deployment.

## November 13: Honors-only course widget prefix

- Removed the standalone HON Class Descriptions link. Honors Track alone now
  sets courseResourcesPrefix: SOC or HON. Shared course widget uses that optional
  override, falling back to unit prefix everywhere else; buttons unchanged.
- Recorded the page-specific override in project-conventions.md. Local soc and
  css-shared edits only; no builds/tests, commit, push or deployment.

## November 13: Honors semester labels

- Changed Semester 1/2 labels beneath HON 496 to regular paragraphs, removing
  italics and using spaced em dashes. Wording/course lists unchanged.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: Honors course group labels

- Converted the four bold paragraph labels beneath Honors and Sociology Courses
  to plain H3s, each preceded by the existing smaller my-3 HR. Label text and course
  descriptions unchanged; semester italic labels left for separate review.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: Honors intro sidebar logo

- Added shared media/units/soc/undergraduate/honors-program.png (283x391) to the
  Honors Track intro’s right column, matching the narrow AKD sidebar grid.
  Uses the user-requested classic photo-style border/shadow treatment and
  descriptive logo alt text; original intro prose unchanged.
  Removed the duplicate imported bottom logo instance; media file not deleted.
- Local ../soc edit only; inspected image dimensions; no builds/tests, commit,
  push or deployment.

## November 13: Honors Track intro/gray split

- Read Honors Track and separated its H1/three opening overview paragraphs into
  the white intro. Gray starts at Participation and Requirements and includes
  Honors and Sociology Courses plus the existing image/HON descriptions link.
  Removed the leading HR at that boundary; course widget remains separate below.
- Wording and other markup unchanged. Further heading/voice cleanup deferred.
  Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: Funding white sections combined

- Combined undergraduate and graduate funding into one continuous white section,
  with a standard HR before Graduate Funding Opportunities. Existing audience
  headings and all content unchanged. Later funding topics remain in that section.
- User accepts the consolidated resource-directory approach for now. Local ../soc
  edit only; no builds/tests, commit, push or deployment.

## November 13: Funding descriptions generalized

- Rewrote root funding list entries as concise name — purpose/resource summaries,
  as authorized. Removed named contacts/mailto links, amounts, deadlines, award
  years, quotas, GPA/credit thresholds and detailed application/benefit claims.
  Native Hawaiian items describe resources rather than recurring deadlines.
- Shortened Graduate Assistantships and Student Employment separately; intro
  directs readers to providers for current terms and availability. Broad audience
  distinctions retained; listed resources and detail pages preserved. Provider
  URLs were not audited and current availability is not asserted.
- Recorded the general-directory convention and updated soc-funding-text-cleanup.md.
  Local soc/css-shared edits only; no builds/tests, browser review, commit, push
  or deployment.

## November 13: Funding Sources focused text cleanup

- Standardized award/resource entries to name — description; cleaned obvious
  punctuation, range formatting and Hawaiian-character issues. STAR is one linked
  General Funding Resources bullet; removed its extra section, application prose
  and JTB example. Other specifics retained for the next editorial pass.
- Recorded entry format in project-conventions.md and focused findings in
  soc-funding-text-cleanup.md. Flagged stale 2023 award/deadlines, named contacts,
  EPIC’s our website wording, uncertain details and remaining naming differences.
- Local soc/css-shared edits only; no full-site script, builds/tests, browser audit,
  commit, push or deployment. Next: simplify descriptions and review stale details
  with the user; no current eligibility verification claimed.

## November 13: Undergraduate funding landing page retired

- Undergraduate menu now points to /funding-sources.html, matching Graduate.
  Deleted ../soc/src/undergraduate/funding-sources.html; updated Why Study links
  and removed the obsolete fragment. Removed old hero assignment, configured
  old-URL redirect and removed stale generated page to permit redirect output.
- Both former funding landing sources are retired. Combined page awaits cleanup.
  Local soc/css-shared edits only; no builds/tests, commit, push or deployment.

## November 13: Final undergraduate funding section moved

- Moved Specialized Funded Programs Affiliated with UH, all six entries unchanged,
  beneath Student Employment on root Funding Sources with a standard HR.
  Audience/dated content review remains pending; no eligibility claims added.
- Old undergraduate source now only retains its intro; its navigation/retirement
  remains pending approval. Local soc/css-shared edits only; no builds/tests,
  commit, push or deployment. Next: cleanup/reconciliation of the combined page.

## November 13: Funding shared/STAR/native moves and Hörmann merge

- Study Abroad Center scholarships moved to General Funding Resources; STAR is
  a dedicated H3 at the bottom of gray, combining its general resource description
  and former STAR example content. Removed duplicate general STAR listing.
- Moved Native Hawaiian Funding unchanged below graduate funding, before Student
  Employment. Merged Hörmann descriptions into one concise departmental entry,
  preserving core award/history facts and dedicated-page link; removed old copy.
- Old undergraduate source now retains only Specialized Funded Programs and its
  intro (six entries pending review). See units/soc/soc-funding-consolidation.md for details.
- Local soc/css-shared edits only; no builds/tests, commit, push or deployment.

## November 13: Graduate funding landing page retired

- Deleted ../soc/src/graduate/funding-sources/index.html after consolidation.
  Graduate navigation and Why Study funding links now use /funding-sources.html.
  Removed its old hero assignment and configured an old-URL redirect; removed
  stale generated index to permit redirect output. Sakihara detail page retained.
- Undergraduate funding page/menu remain pending review of uncertain leftovers.
  Local soc/css-shared edits only; no builds/tests, commit, push or deployment.

## November 13: Graduate funding staged move

- Added Graduate Funding Opportunities to the root funding page, with Graduate
  Assistantships first and Scholarships and Financial Support second. Moved the
  remaining graduate resources and GA prose intact from the old graduate source.
- Split hourly Student Employment into its own H2, preserving the two original
  sentences/SECE link rather than conflating jobs with graduate assistantships.
- Old graduate page now holds only its intro; old undergraduate uncertainties
  remain flagged in soc-funding-consolidation.md. Navigation/redirects unchanged.
  Local soc/css-shared edits only; no builds/tests, commit, push or deployment.

## November 13: Undergraduate funding staged move

- Added a white Undergraduate Funding Opportunities section to the root funding
  page, grouped into scholarships/support, research/travel/study abroad, paper
  awards. Moved twelve entries from the old undergraduate page; combined its two
  UROP descriptions without losing listed services. Combined duplicate general
  Financial Aid Services entries as separately authorized.
- Mixed/unclear audience material remains on the old undergraduate page for review
  (including JASC/FLAS/Boren, Native Hawaiian programs, and alternate Hörmann copy).
  See units/soc/soc-funding-consolidation.md for exact moved/remaining topics.
- Dated 2023 paper-award copy retained for review; no eligibility/deadline audit.
  Both old pages/navigation remain. Local soc/css-shared edits only; no builds/tests,
  commit, push or deployment. Next: classify remaining shared material and move
  the clearly graduate section, then reconcile and review before retiring old URLs.

## November 13: Root Funding Sources staged consolidation

- Created ../soc/src/funding-sources.html with white intro and gray Residency,
  Departmental Funding Sources, General Funding Resources. Moved shared/broad
  material out of both old pages; consolidated near-identical departmental Hörmann
  and residency copies, retaining WUE and original prose. Both FAS summaries remain
  for review. See units/soc/soc-funding-consolidation.md for moved/remaining inventory.
- Old undergraduate/graduate pages remain with their unmoved material. Navigation
  and old URLs unchanged; full merge/retirement deliberately deferred per steering.
  Added the new page’s hero assignment. No eligibility audit or substantive rewrite.
- Local soc/css-shared edits only; no builds/tests, commit, push or deployment.
  Next: review new gray section and progressively reconcile remaining content.

## November 13: Undergraduate funding color split

- Applied white intro, gray Residency/Departmental Funding, then white from Other
  Scholarship Opportunities through Paper Awards. No leading divider at the new
  white section. Existing funding descriptions unchanged.
- User flagged duplicate Hörmann Prize entries; both retained pending choice of
  description/consolidation. Local ../soc edit only; no builds/tests, commit,
  push or deployment.

## November 13: Undergraduate funding duplicate opening removed

- Removed the opening HRs, Additional Undergraduate Funding/Undergraduate Funding
  headings and duplicate financial-assistance sentence. Funding Sources H1/intro
  now lead directly to Residency for Tuition Purposes. Remaining text unchanged.
- Suggested gray Residency/Departmental Funding, white from Other Scholarship
  Opportunities; color-section split not yet implemented pending user choice.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: Undergraduate funding reordered

- Moved the appended undergraduate funding block (Residency for Tuition Purposes,
  Departmental Funding Sources and Other Scholarship Opportunities) above STAR.
  Existing block headings/intro and all wording retained for subsequent cleanup.
  Page now ends with the final Paper Awards item. No other restructuring.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: Academic Planning intro and gray section

- Separated H1/new cohesive intro into white; everything from Planning Tools
  through Career Planning is gray. Removed the leading HR at that section boundary;
  later dividers retained. Intro summarizes tools, advising, degree combinations,
  study abroad, internships and careers. All supporting content unchanged.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: Academic Planning replaces Advising & Support

- Replaced Undergraduate navigation’s Advising & Support with Academic Planning.
  Moved the page to ../soc/src/undergraduate/academic-planning.html and preserved
  the remaining ASA careers-article link under Career Planning. Existing planning
  copy unchanged, including outdated links pending later review.
- Retired the old Advising & Support landing source; mission/services were already
  incorporated into the shared BA/Minor advising intro. Updated Why Study planning
  links; remaining contact-oriented advising links now point to Contact.
- Moved hero assignment and configured old landing/planning URLs to redirect to
  the new page; removed stale generated files that could collide with redirects.
- Local soc/css-shared edits only; no builds/tests, commit, push or deployment.

## November 13: BA/Minor advising introduction

- Added shared default advising intro beneath Undergraduate Advising on BA/Minor,
  encouraging work with advisors toward graduation and preserving the service
  topics from the Advising & Support mission paragraph: courses, requirements,
  planning, careers, graduate school, declarations, minor verification and paperwork.
- Existing template supplies HR before the two people. Services remain collective,
  not assigned to either advisor; BAM’s separate introduction is unchanged.
  Advising & Support page remains pending retirement. Local css-shared edit only;
  no builds/tests, commit, push or deployment.

## November 13: BAM intro approved and admissions label standardized

- Applied the approved BAM intro presenting teaching as one possible career path.
  Standardized Applications & Admissions in the BAM H2/link and MA/Why Study links;
  page title/H1/global navigation already used that form.
- Recorded the Sociology page-label convention in project-conventions.md.
  Local soc/css-shared edits only; no builds/tests, commit, push or deployment.

## November 13: BAM application section streamlined

- Replaced duplicated application-component explanation with the approved short
  paragraph linking Applications and Admissions, retaining January 15 junior-year
  deadline and fall admission timing. Three bullets cover notification, dual
  enrollment/double-counted tuition, and temporary advisor/Plan A or B choice.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: BAM advising introduction relocated

- Removed the final second-person advising paragraph from the BAM intro. Added
  a general explanation under the advising widget H2 about coordinating
  undergraduate, graduate and general education advising across both degrees,
  followed by an HR. Stored as BAM’s optional JSON intro; BA/Minor unaffected.
- Local soc/css-shared edits only; no builds/tests, commit, push or deployment.

## November 13: Advisor wording unified

- Undergraduate Chair uses the same undergraduate course selection, program
  requirements and planning description on BA, Minor and BAM. Graduate Chair
  uses the equivalent graduate wording on BAM. Removed SOC; Jason unchanged.
- Supersedes the prior general-SOC/default versus BAM-specific wording distinction.
  Local css-shared edits only; no builds/tests, commit, push or deployment.

## November 13: Advisor descriptions generalized and BAM variant

- Default BA/Minor chair description now says For guidance on SOC course
  selections, program requirements and planning, without declaration ownership.
- Added BAM JSON variant with Undergraduate Chair, Graduate Chair, then Jason.
  First two use undergraduate/graduate SOC guidance descriptions respectively;
  Jason unchanged. Shared loader resolves both chairs by role from people.json;
  same widget and typography/layout, two chairs first desktop row, Jason second.
- Local soc/css-shared edits only; no builds/tests, commit, push or deployment.

## November 13: BAM intro flow and terminology

- Merged existing career paragraphs into the opening paragraph; added Program
  features and planning considerations include before the bullets. Lowercased
  students/master’s, clarified Sociology BA/MA program links, expanded UHCC to
  University of Hawaiʻi Community Colleges, and corrected Kaʻieʻie/UH Mānoa.
- Other instructions and requirements unchanged. Local ../soc edit only;
  no builds/tests, commit, push or deployment.

## November 13: BAM double-counted course headings

- Replaced the three selection lead-ins with H3s: Undergraduate Course (select
  one), Quantitative or Qualitative Methods (select one), and Sociological Theory
  (select one). Course lists and selection requirements unchanged.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: BAM plan labels aligned

- Renamed the tracks heading Plan A: Thesis or Plan B: Research Report, matching
  the MA page labels/colon punctuation. Catalog Plan B link now also says
  Plan B: Research Report. Other text unchanged. Local ../soc edit only;
  no builds/tests, commit, push or deployment.

## November 13: BAM catalog plan links

- Removed the obsolete Sample Five-Year Plans link/page-bottom note from
  double-counted courses. Added the two catalog links at the end of the tracks
  section: Plan A Thesis poid=1843, Plan B Non-Thesis poid=2105, as confirmed
  by the user. Catalog content blocked automated viewing; mapping is user supplied.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: BAM dividers and direct plan links

- Added standard HRs before the three later gray-section H2s, none before
  Eligibility Requirements. Linked Plan A/Plan B at the start of their detailed
  bullets to the existing MA thesis/research-report pages and removed the redundant
  details-of-these-tracks sentence. Intro’s brief plan-choice bullet retained.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: BAM intro and gray sections

- Kept BAM H1 through the paragraph before Eligibility Requirements in the white
  intro. Eligibility Requirements through the remaining pathway content now sits
  in a separate gray section. Advising and course widgets remain separate below.
- Wording unchanged. Local ../soc edit only; no builds/tests, commit, push
  or deployment.

## November 13: BAM section headings and footer cleanup

- Converted Eligibility Requirements, Application and Admission, Plan A Thesis
  or Plan B Non-Thesis Tracks, and Options for Double-Counted Courses to H2s.
- Removed the bottom For more information/contact paragraph, image, standalone
  Undergraduate Advising link and surrounding HRs. Shared advising/course widgets
  and other content remain unchanged. Local ../soc edit only;
  no builds/tests, commit, push or deployment.

## November 13: Graduation guidance consolidated on BA

- Added a final BA Graduation Requirements bullet linking the full phrase
  step-by-step guidance on the graduation process to the existing CSS graduation
  resource, with concise College of Social Sciences attribution.
- Removed Preparing for Graduation, its preceding HR, Jason’s old photo/details,
  and everything below from Advising & Support. Its intro and early links remain
  pending the user-directed eventual retirement; page not yet deleted.
- Local ../soc edits only; no builds/tests, commit, push or deployment.

## November 13: BAM advising widget

- Inserted the same shared advising widget directly above the course widget on
  ../soc/src/undergraduate/bam.html. Reuses central identity/role/appointment data;
  no other BAM content changed. Local soc/css-shared edits only;
  no builds/tests, commit, push or deployment.

## November 13: Major Concentrations intro aligned

- Replaced the awkward Optional, our opening with a Minor-style explanation of
  optional topic-based course groupings, example areas, and career/graduate-school
  preparation. Retained the link to the BA overview within the introduction.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: BA catalog terminology updated

- Replaced the outdated Program Sheet/STAR paragraph with a catalog reference
  grounded in the user-supplied transition notice: from 2025–26 onward, program
  requirements and sample four-year plans are in Undergraduate Programs A–Z.
  Retained the supplied direct Sociology catalog destination. Did not reproduce
  the old webpage’s archive notice as though it described this new site.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: BA program link and naming review item

- Replaced the BA Graduation Requirements Program Sheet destination with the
  supplied catalog.manoa.hawaii.edu program URL. Visible wording unchanged.
  Research browser encountered the destination’s JS/anti-bot screen, so its
  program content was not independently verified.
- Recorded a Sociology-only department/degree naming inventory in rules/text-cleanup.md
  and the SOC cleanup report. Context-specific recommendations require review;
  no canonical naming or bulk changes adopted, and inventory not yet run.
- Reviewed Graduation Requirements prose: consistent third-person voice; some
  wordiness and potentially outdated Program Sheet terminology flagged to user,
  without rewriting. Local soc/css-shared edits only; no builds/tests, commit,
  push or deployment.

## November 13: BA graduation footer clutter removed

- Removed the image, standalone outcomes/advising links, both HRs, and Related
  Resources list beneath Graduation Requirements. Graduation prose/links remain
  unchanged, followed by declaration, advising widget and course widget sections.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: BA repeated credit sentence removed

- Removed the redundant 30-credit/introductory-course sentence above Required
  Courses. Credit total remains in H2; introductory-course requirement remains
  in the list. Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: BA requirement headings and notes

- Removed the superseded intro bullets and HR. Current requirement heading now
  matches Minor: Course Requirements (at least 30 credits). Earlier-requirement
  link is an info paragraph followed by my-3 HR; credit sentence is regular text.
- Required, methods/statistics and elective labels are plain unnumbered H3s without
  trailing colons. Prerequisites and Additional Notes are H3s with smaller dividers.
  Requirement wording otherwise preserved. Local ../soc edit only;
  no builds/tests, commit, push or deployment.

## November 13: BA outcomes intro link

- Added the approved final intro sentence linking Student Learning Outcomes and
  explaining its purpose. Other BA content unchanged. Local ../soc edit only;
  no builds/tests, commit, push or deployment.

## November 13: BA concentrations intro sentence

- Added the Minor-matching final intro sentence describing optional major
  concentrations as suggested topic-based course groupings for career and graduate
  school preparation, linked to Major Concentrations. Other content unchanged.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: BA introduction grounded in course descriptions

- Replaced the generic BA intro/advising sentence with a general description of
  social relationships/institutions, required theory/research foundations, methods
  and statistics choices, and example upper-division elective topics.
- Read the supplied SOC.docx descriptions for SOC 100, 300, 321, 475, 476/L and
  478; elective themes draw on the previously reviewed 300/400-level descriptions.
  Wording presents options/examples rather than promising every topic or method.
- Local ../soc edit only; requirements untouched; no builds/tests, commit, push
  or deployment.

## November 13: Current BA course requirements gray section

- Wrapped the Spring 2023-and-later BA course requirements through their final
  additional note in a gray page section, including the earlier-requirements link.
  Intro content stays white; Graduation Requirements begins a separate white
  section. Other content and wording unchanged. Graduation requirements describe
  broader degree completion, not only the current Sociology course-credit block.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: Earlier BA requirements separated

- Moved the complete Fall 2022-and-before major requirements unchanged into
  ../soc/src/undergraduate/major/requirements-fall-2022-and-earlier.html, titled
  BA Requirements: Fall 2022 and Earlier. White intro/back-link, original content
  in gray, separate standard course widget. Uses the existing BA hero.
- Main BA page links to the new page beside current requirements; retained its
  section-2 anchor on the notice for old bookmarks. Graduation requirements and
  all other existing BA content unchanged; intro revision remains pending.
- Local soc/css-shared edits only; no builds/tests, commit, push or deployment.

## November 13: Minor Concentrations quick links

- Added the same Explore the Concentrations heading, explanation and seven
  vertical jump links between the intro and gray content on Minor Concentrations.
  Existing H2 IDs use page-jump-target for the shared sticky-header offset.
- Content and course lists unchanged. Local ../soc edit only; no builds/tests,
  commit, push or deployment.

## November 13: Concentration jump destinations and label

- Added Explore the Concentrations H2 and a short explanation above the jump list.
  Link fragments match the existing seven H2 IDs. Targets now opt into
  page-jump-target scroll spacing to clear the sticky header.
- Shared site.js measures header height with ResizeObserver (resize fallback),
  and corrects incoming bookmarks after load. Layout CSS provides measured header
  offset plus 1rem, with a no-JS fallback. Other targets/pages are unaffected.
- Local soc/css-shared edits only; source inspected, no browser verification,
  builds/tests, commit, push or deployment. User to confirm landing positions.

## November 13: Major Concentrations quick links trial

- Added a vertical list of seven concentration jump links in its own white section
  between the intro and gray content. Each targets the existing H2 ID; content
  stays visible and unchanged. No new CSS or accordion behavior added.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: Major Concentrations course resources

- Retained the last Research Methods and Statistics elective notes (four/five
  substantive-area courses depending on admission date). Removed the following
  image and plain availability/description links; added the shared course widget
  in its own white section below gray. Local ../soc edit only;
  no builds/tests, commit, push or deployment.

## November 13: Major Concentrations info notes and dividers

- Converted each concentration’s two admission-date elective bullets into separate
  info/icon-text paragraphs, preserving wording. Removed the following HR so the
  elective course lists follow directly. Added standard HRs before concentration
  H2s 2–7, with none above the first concentration.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: Major Concentrations initial structure

- Separated H1/existing opening paragraph into a white section; remaining content
  is gray. Shortened all seven description openings to Designed for.
- Converted numbered italic core/methods/statistics/electives labels to plain H3s,
  without numeric prefixes or trailing colons. Lists, elective rules, nested notes
  and remaining footer content unchanged; further elective work deferred.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: BA declaration moved

- Removed Declaring a Sociology Major from Advising & Support and added it in a
  standalone white section immediately above the BA advising widget. Reworded to
  match the Minor’s online-form/academic-plan approach; retained both declaration
  routes and the original expectation of meeting an advisor before the form.
- Local ../soc edits only; no builds/tests, commit, push or deployment.

## November 13: BA advising widget

- Inserted the existing shared advising widget directly above the course widget
  on ../soc/src/undergraduate/major/index.html. Same central data and layout as
  Minor; no other BA content changed. Minor accepted as done for now by the user.
- Local soc/css-shared edits only; no builds/tests, commit, push or deployment.

## November 13: Minor advising scope clarified

- Changed Jennifer’s widget description to SOC Course Selections as requested.
  Declaration advice covers sociology course choices and now ends with how the
  minor fits into their overall academic plan, per the user’s final wording.
- Course-widget button labels untouched. Local soc/css-shared edits only;
  no builds/tests, commit, push or deployment.

## November 13: Advisor widget approved and shortened

- Removed the old Advising block and preceding HR beneath the Minor declaration
  paragraph. Shared widget remains in its own section above course resources.
- Shortened Jennifer/Jason role descriptions as approved, omitting repeated titles.
  Jason’s help line now reads Learn how to schedule an appointment, with the same
  link. No further changes to advising responsibilities were inferred.
- Local soc/css-shared edits only; no builds/tests, commit, push or deployment.

## November 13: Reusable advisor widget on Minor

- Added shared layouts/profiles/advising-widget.njk and SOC advising-widget.json;
  inserted the widget directly above the Minor course widget, in its own section.
  Existing advising content remains intact for comparison as requested.
- Chair resolves by role from SOC people.json (currently Jennifer Darrah), using
  existing office/email/phone rendering. Jason Higa resolves from new common
  advisors.json, with the shared 215x215 photo and exact three appointment
  instruction paragraphs/links from Advising & Support; no phone/email displayed.
- Layout-only CSS in layout.css: desktop 20/30/20/30, stacked advisor groups on
  tablet/mobile. Existing profile.css name rule extended to H3; existing profile
  typography/contact/frame styles reused. Legacy GEO advising loader unchanged.
- Recorded role-order/data conventions in project-conventions.md and component
  documentation in advising-widget.md. Local soc/css-shared edits only; no build,
  tests, browser review, commit, push or deployment. Next: user comparison before
  removing old advising text or adopting elsewhere.

## November 13: Advising & Support footer resources removed

- Removed the plain SOC Class Availability/Class Descriptions links and the entire
  Related Resources section through Alpha Kappa Delta. Earlier content preserved.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: Minor declaration wording modernized

- Described the Kuali declaration as an online form, removed the processing/STAR
  explanation, and explicitly encouraged advising before submission. Form link
  and declaration requirement unchanged. Local ../soc edit only;
  no builds/tests, commit, push or deployment.

## November 13: Minor declaration placement refined

- Moved declaration content out of the gray course section into the white section
  immediately before Advising, with an HR between the two H2s. Removed the former
  course/declaration divider. Tightened declaration/form/STAR wording and retained
  the recommendation to meet an undergraduate advisor for course planning.
- Supersedes the preceding gray-section placement. Local ../soc edit only;
  no builds/tests, commit, push or deployment.

## November 13: Minor declaration moved into degree page

- Moved Declaring a Sociology Minor H2 and its original paragraph/form link from
  Advising & Support into the Minor page’s gray section below course requirements,
  separated by a standard HR. Removed that section from Advising & Support.
- Local ../soc edits only; no copy rewriting, builds/tests, commit, push or deployment.

## November 13: Minor requirement headings

- Added Course Requirements (at least 15 credits) H2 and removed the repeated
  credit minimum from the lead-in. Required Course, Four Elective SOC Courses,
  Prerequisites and Additional Notes are plain H3s without numbering or colons.
- Used existing my-3 dividers before Prerequisites and Additional Notes.
  Course requirements otherwise unchanged. Local ../soc edit only;
  no builds/tests, commit, push or deployment.

## November 13: Minor page section structure

- Minor now has separate white intro, gray coursework/prerequisites/notes,
  white Advising, and white course-widget sections, in that order.
- Removed the bottom image, Related Resources/concentrations link and its HR.
  Existing text and course labels retained; heading/style refinements deferred.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: Minor concentration description openings

- Shortened all seven description openings to Designed for students interested
  in, including the existing Thus typo. Remaining descriptions unchanged.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: Minor Concentrations leading divider

- Removed the HR before the first Criminology H2; dividers between subsequent
  concentration sections remain. Local ../soc edit only; no builds/tests,
  commit, push or deployment.

## November 13: Minor Concentrations course resources

- Removed the bottom image, standalone Undergraduate Advising and plain SOC
  availability/description links. Added the standard course-resources widget in
  its own white section beneath the gray concentration content.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: Minor Concentrations sections

- Separated H1/new approved-scope introductory paragraph into a white section;
  remaining content is gray. Intro links minor in Sociology to the Minor page
  and describes the optional topic-based course groupings and preparation purpose.
- Added HR before each concentration H2; converted numbered italic Core Course
  and Electives labels to unnumbered plain H3s. Existing course lists, concentration
  descriptions and footer content preserved.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: Minor concentrations intro link

- Added a final intro sentence describing optional minor concentrations as
  suggested topic-based course groupings for career/graduate-school preparation.
  Linked the existing concentrations page and removed the superseded standalone
  promotional bullet and extra HR. Other content unchanged.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: Minor intro and advising

- Replaced the Minor intro with the exact approved research/elective summary.
  Moved its advising purpose to a new Advising H2 near the bottom, distinguishing
  Sociology coursework/minor guidance from general education/degree planning.
  Undergraduate Chair links to Contact; declaration/graduation guidance links to
  Advising & Support. Existing requirements and other structure remain untouched.
- Read Geography’s advising examples and SOC Advising & Support as references.
  Local ../soc edits only; no builds/tests, commit, push or deployment.

## November 13: Undergraduate landing-page course resources

- Added the shared Sociology course-resources include as a standalone final white
  section on Minor, Major, BAM and Honors Track, outside existing content columns.
- Removed superseded plain SOC availability/description links; retained Honors
  course-description link and all other content. Local ../soc edits only;
  no builds/tests, commit, push or deployment.

## November 13: History decorative sidebar photo

- History now uses the same 10/2 desktop, 9/3 tablet, stacked mobile columns as
  Alpha Kappa Delta. Moved the photo to the right column and switched to shared
  media/units/soc/history/hawaii-hall.webp (240x446), with photo-style and empty
  alt for decoration. Original prose and white-only section retained.
- Local ../soc edit only; read shared image dimensions; no builds/tests, commit,
  push or deployment. Old imported history image remains unused in local media.

## November 13: Application checklist capitalization

- Capitalized the six lowercase checklist openings on Sociology Applications &
  Admissions, including linked Official TOEFL. Other wording unchanged.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: Student Organizations AKD description

- Kept the linked Alpha Kappa Delta H2 and replaced its duplicate body link with
  a sentence about academic recognition, travel awards and paper competitions,
  grounded in the existing AKD page. Local ../soc edit only; no builds/tests,
  commit, push or deployment.

## November 13: AKD introduction and narrower logo column

- Added the requested student membership introduction immediately below H1,
  before the attributed quote. Defines AKD and identifies the honor society.
- Switched intro to the existing Bootstrap 10/2 desktop, 9/3 tablet grid,
  stacked on mobile. Shared 200px logo uses img-fluid to avoid enlargement.
  No new CSS. Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: Alpha Kappa Delta sections

- Replaced the italic intro with the exact purpose text supplied by the user,
  in a semantic blockquote with a visible homepage attribution. Shared AKD logo
  now occupies the intro’s right column using the existing Foundation-row pattern.
- Removed the repeated founded-in-1920 sentence and bottom image; existing
  membership paragraph and links moved to gray under Membership Benefits.
- Local ../soc edit only; no CSS changes, builds/tests, commit, push or deployment.

## November 13: Student organization order

- Reordered the two Student Organizations rows: Alpha Kappa Delta first, GSSA
  second. Content and image treatment unchanged. Local ../soc edit only;
  no builds/tests, commit, push or deployment.

## November 13: Student organization image treatment

- Applied the existing photo-style class to both Student Organizations images
  for the standard border/shadow treatment. Removed the GSSA Facebook sentence
  at the user’s request; no replacement text or CSS added.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: Shared student organization logos

- Student Organizations now uses both 200x200 PNGs from shared
  src/media/units/soc/student-organizations/. Updated AKD and Why Study SOC image
  references too, including Why Study’s old GSSA destination.
- Permanently deleted all four imported GSSA/AKD image copies from
  ../soc/src/media/content/ at the user’s request. Other media preserved.
- Local soc/css-shared changes only; inspected source references and shared image
  dimensions; no builds/tests, commit, push or deployment.

## November 13: Degree overview intros simplified

- Merged the two intro paragraphs on MA and PhD overview pages. Removed the five
  individual research-area links while preserving their wording; each combined
  paragraph ends with See Research Areas linking to /about-soc/research-areas/.
- Local ../soc edits only; no builds/tests, commit, push or deployment.

## November 13: Degree navigation separated from intros

- Moved shared degree navigation out of the intro on all five MA and six PhD
  pages. Each now has a separate white page-section/container/row/column between
  the intro and gray content section. Navigation markup/styles/content unchanged.
- Local ../soc edits only; no builds/tests, commit, push or deployment.

## November 13: Sociology TMS check recorded

- Added a Sociology-only cleanup item: spell out Theory, Methods, and Statistics
  or define TMS on first use on each page. Recorded in rules/text-cleanup.md and the
  SOC cleanup report; no site-wide scan or content changes performed this turn.
- Local css-shared documentation only; no tests, commit, push or deployment.

## November 13: MA timeline readability

- Matched the PhD pattern: existing opening sentence, two guidance bullets, and
  Graduate Course Categories as a separate sentence. All wording/table retained.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: PhD timeline readability

- Broke the example-progress paragraph into its original opening sentence and
  six bullets. Only the approved acceleration/advisor wording was rewritten into
  third person; conservative-plan qualification and all other details retained.
  Graduate Course Categories is a separate sentence after the list; table unchanged.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: PhD split implemented

- Split ../soc/src/graduate/doctorate-phd.html into doctorate-phd/index.html plus
  requirements, timeline, qualifying-review, comprehensive-exam and dissertation.
  See units/soc/soc-phd-pages.md for the content map and migration details.
- Preserved substantive prose; added short intros, plain H3s, gray content bands,
  shared PhD navigation ending in the existing Annual Review, and separate white
  course-resource sections. Timeline retains all twelve semesters in the shared
  responsive table. No CSS changes.
- Updated global/Why Study links and hero assignments; configured old PhD URL
  and fragment redirects. Corrected two Phase I links from advising to Coursework.
- Local soc/css-shared changes only; no build, tests, browser review, commit,
  push or deployment. Next: user review, then MA/PhD cross-check; old SOC verifier
  inventory still needs separate upkeep when verification is requested.

## November 13: MA overview course resources placement

- Moved the MA overview’s course-resources include out of the prose column into
  its own white section beneath the content, matching Annual Review placement.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: Annual Review course resources

- Added the shared Sociology course-resources include in its own white section
  beneath Annual Review’s gray content section. Existing prose unchanged.
- Local ../soc edit only; no builds/tests, commit, push or deployment.

## November 13: Student Organizations

- Moved GSSA content unchanged to ../soc/src/graduate/student-organizations.html,
  with a white intro and gray shared image/text rows for GSSA and Alpha Kappa Delta.
  Added a short AKD introduction linking to its unchanged root-level page.
- Added Graduate navigation item after Funding Sources, updated the PhD resource
  link, carried over the GSSA hero, and configured the old GSSA URL redirect.
  Removed the MA Related Resources section and its leading HR; standard course
  resources remain. Local soc/css-shared changes only; no builds/tests, commit,
  push or deployment.

## November 13: MA overview refinements

- Final section title is Degree Options (supersedes Programs of Study); used existing my-3 HR spacing
  before Plan B and Choosing a Plan. Full divider before PhD admission retained.
- Standardized the PhD admission heading/first sentence to MA; replaced deadline
  and external application guidance with a local Applications and Admissions link.
  Removed the image and standalone Annual Student Review link. Annual Review
  remains in degree navigation and Related Resources.
- Local ../soc source edits only; no builds/tests, commit, push or deployment.

## November 13: MA overview plan headings

- Renamed the overview section Programs of Study (Plan A and Plan B).
  Separated its introductory paragraph from Plan A’s description and added
  H3s: Plan A, Plan B, Choosing a Plan. Existing prose and anchors preserved.
- Local ../soc source edit only; no builds/tests, commit, push or deployment.

## November 13: Graduate Division policy group

- Added Graduate Division H2 with linked Academic Progress and Conduct Code H3s
  and short source-based summaries in the shared Policies & Procedures body.
  Read both official pages; retained existing university-wide policy entries.
- Replaced Annual Review’s three inline external policy links with one local
  Policies & Procedures link; existing policy references and prose preserved.
  Local css-shared/soc edits only; no builds/tests, commit, push or deployment.

## November 13: Annual Review navigation and sections

- Added Annual Review last in the shared MA navigation, linking to the existing
  /graduate/annual-review.html. Reuse that destination in the future PhD page
  navigation; the unsplit PhD page does not yet have a degree-navigation block.
- Annual Review now has a white H1/first-sentence intro, followed by gray Review
  Process and Outcomes starting at “Although students.” Converted manual A/B/C
  labels to ol type=A; remaining wording/links preserved.
- Local soc/css-shared edits only; no builds/checks, commit, push or deployment.

## November 13: Degree overview research-area links

- Added the approved research-area paragraph as a second paragraph below the
  existing MA and PhD intros. Five research areas link to their existing pages.
  Original degree intro text and navigation placement preserved.
- Possible future navigation column is a user idea, not implemented or locked in.
  Local ../soc edits only; no build/checks, commit, push or deployment.

## November 13: TMS defined on first use

- Added (TMS) after Theory, Methods, Statistics in the Graduate Course Categories
  intro. Other text unchanged. Local ../soc edit only; no build/checks,
  commit, push or deployment.

## November 13: Graduate Course Categories sections

- White H1/existing intro; all category listings and explanations in gray.
  Theory, Research Methods, Statistics and Substantive Courses are plain H2s.
  Added HRs before Research Methods/Statistics; retained the existing standard
  HR before Substantive Courses. No wording or course-list changes.
- Local ../soc edit only; no build/checks, commit, push or deployment.

## November 13: Graduate Course Categories renamed

- Renamed ../soc/src/graduate/course-identification.html to
  graduate-course-categories.html; title/H1/permalink use Graduate Course Categories.
  Body content and structure unchanged.
- Updated six links: MA overview/requirements/timeline and three on the existing
  PhD page. No other PhD content changed. Preserved hero assignment; configured
  old URL redirect and removed stale local generated output to permit its rebuild.
- Local soc/css-shared changes only; no builds/checks, commit, push or deployment.

## November 13: MA Back to top links removed

- Removed Back to top links and their now-unused page-top H1 IDs from all five MA
  pages. Top degree navigation and bottom course-resource includes retained.
  Supersedes the immediately prior back-link treatment; conventions updated.
- Local source edits only; no builds/checks, commit, push or deployment.

## November 13: MA bottom navigation simplified

- All five MA pages retain degree navigation at top only. Replaced the bottom
  repeat with SOC’s existing course-resources include and one Back to top link,
  targeting an explicit page-top H1 ID. Existing SOC catalog settings reused.
- Removed the overview’s duplicate old availability/description links; other
  content retained. No new CSS. Local soc/css-shared edits only; no build/checks,
  commit, push or deployment.

## November 13: Advising subsection divider tightened

- Applied the same my-3 HR spacing between Temporary Advisor and Formal Advisor
  on MA requirements. Major-section dividers unchanged. Local ../soc edit only;
  no build/checks, commit, push or deployment.

## November 13: Coursework Notes divider tightened

- Added existing my-3 spacing utility to the HR before Coursework Notes: 1rem
  above/below instead of 2rem. Line width/style and major-section dividers
  unchanged. No new CSS. Local soc/css-shared edits; no builds/checks,
  commit, push or deployment.

## November 13: MA requirements headings refined

- MA Coursework → Coursework; Advisor → Advising; Coursework notes: → Coursework
  Notes. Removed trailing colons on requirements-page H3s. Candidacy, Human
  Subjects and all body text retained. User-approved heading edits only.
- Local ../soc edit only; no build/checks, commit, push or deployment.

## November 13: MA timeline explanatory wording

- Applied the user-approved gray-section lead-in: one possible sequence, not a
  required schedule; strongly encouraged first-year Theory/Methods/Statistics
  and relevant Substantive coursework. Original intro and third-semester thesis
  proposal recommendation retained. Table unchanged.
- Local ../soc edit only; no build/checks, commit, push or deployment.

## November 13: MA navigation wording and pathway punctuation

- Removed visible “(current)” from shared degree navigation; aria-current retained.
  No button styling added. Standardized MA Plan A/Plan B gray H2 labels to colons,
  matching page titles/navigation; dashes were inherited from the original source.
- No new Plan B lead-in copy inserted; user asked for advice only on that point.
  Local soc/css-shared edits; no builds/checks, commit, push or deployment.

## November 13: MA subsection headings made plain H3s

- Converted the 11 inherited italic paragraph labels into proper, unformatted
  H3s across MA requirements, thesis and research-report pages. Removed italic
  wrappers from any MA H3s; text and other content preserved. PhD untouched.
- Local ../soc edits only; no builds/visual checks, commit, push or deployment.

## November 13: SOC MA split into five pages

- Created ../soc/src/graduate/master-ma/ with index, requirements, timeline,
  thesis and research-report HTML pages. Existing section blocks moved intact;
  only new subpage intros/navigation labels and approved timeline-table markup
  added. Original overview intro and resource content retained. PhD untouched.
- One gray section per page: overview outcomes; timeline responsive table; other
  pages their assigned requirements/procedures. Overview Plan A/B explanation
  and MA-to-PhD information follow outcomes in white supporting content.
- Shared degree navigation appears top/bottom with current-page indication.
  Updated MA global menu and BAM/Why Study links, saved the same MA hero for all
  five routes. Old master-ma.html URL plus section-1…10 mapped through generated
  redirects; shared engine supports validated fragmentTargets for split pages.
- Source edits only; no build/visual checks or broad verification. Old fixed SOC
  verifier inventory predates this split; update separately when checks requested.
- Local soc/css-shared only; no commit/push/deployment. Full map and preservation
  details: soc-ma-pages.md. User reviews locally; PhD remains for a later task.

## November 13: SOC degree-page layout planning

- Reviewed MA/PhD source pages; user remains in planning stage. No degree pages
  split or rewritten. Discussed overview, requirements, timelines and completion
  stages, with consistent navigation between a degree’s pages.
- User’s standing layout rule: tables go in gray; prefer one gray section beneath
  each short white intro. Degree overview gray sections hold outcomes; timeline
  tables should have their own pages/gray sections. Recorded in conventions.
- Documentation only; no builds/checks, commit, push or deployment. Next: agree
  final page map/navigation before moving content or converting timeline lists.

## November 13: SOC admissions intro simplified into four bullets

- Retained the competitiveness/research-fit sentence as the short intro. Moved
  undergraduate-degree and MA/PhD information intact into two bullets before
  existing Fall-deadline and no-Spring-admission bullets. Four bullets total;
  all qualifications and gray-section content preserved.
- Local ../soc source edit only; no build/checks, commit, push or deployment.

## November 13: SOC admissions intro merged

- User authorized merging the opening and two General Requirements paragraphs.
  One paragraph now retains competitiveness/research fit, no required sociology
  BA, required make-up coursework beyond usual requirements, no MA prerequisite
  for PhD, encouragement to apply directly, and eligibility for an en-route MA.
- Removed redundant General Requirements H2/HR and conversational “On a similar
  note.” Existing deadline/no-Spring bullets follow, unchanged. Gray content intact.
- User accepted HRs above the two H3s; no special H3 CSS needed.
- Local ../soc edit only; no build/checks, commit, push or deployment.

## November 13: SOC application subsection dividers

- Added an HR immediately before each application H3 (Graduate Division and
  Sociology). Semantic hierarchy and existing H3 styling retained; optional
  special heading treatment deferred until the user reviews the dividers.
- Local ../soc edit only; no build/checks, commit, push or deployment.

## November 13: SOC application heading hierarchy

- Added Application Requirements H2 and the approved two-part application lead-in
  sentence in gray. Graduate Division and Sociology headings now H3s, with the
  redundant 1)/2) removed. All other text preserved.
- Local ../soc edit only; no build/checks, commit, push or deployment.

## November 13: SOC admissions sections

- Moved General Requirements H2 and both paragraphs from the bottom into the
  opening white section. Application steps 1) UH Mānoa Graduate Division and
  2) Department of Sociology, including all contents, now in full-width gray.
- Wording, links, lists and emphasis preserved. No copy rewrite. Local ../soc
  edit only; no build/checks, commit, push or deployment.

## November 13: Graduate funding intro and capitalization review

- Rewrote only the requested SOC graduate Funding Sources opening paragraph:
  retains departmental encouragement and summarizes scholarships, awards,
  assistantships, student employment, and travel/development support.
- Added report-only institutional-name capitalization review to cleanup procedure,
  report template and conventions. No Department/department policy imposed or
  site-wide capitalization edits made.
- Local soc/css-shared edits only; no build/checks, commit, push or deployment.

## November 13: Professional travel/development funding entry

- Expanded the SOC graduate Funding Sources inquiry entry using approved draft:
  possible departmental travel/development funds via Contact SOC, plus the CSS
  Travel Award for Professional Development in Research, administered by SSRI.
- User supplied the Kuali application URL; award name links there with UH login
  required noted. No attempt to inspect or submit the authenticated form.
- Local ../soc edit only; no build/checks, commit, push or deployment.

## November 13: SOC graduate Funding Sources restructured

- White H1/existing intro; gray Residency and Departmental Funding; white External
  Funding with no leading HR. Added Graduate Assistantships and Student Employment
  H2 above the unchanged jobs paragraph. Removed Department Travel Funds through
  the old page end, including detailed procedures and redundant related links.
- Departmental entries now Sakihara, Hörmann, then travel inquiry. Replaced the
  obsolete travel availability summary with the supplied inquiry wording linked
  to Contact SOC. Remaining copy/links preserved. No separate travel page made.
- Local ../soc change only; no rebuild/visual checks, commit, push or deployment.

## November 13: Role inquiry routing and graduate funding plan

- Added rule/checklist/report item: role-based inquiry prose links to unit Contact,
  not named chair emails/bios. Personal contact links on bios/cards remain valid.
- Read SOC graduate Funding Sources for requested plan only. Proposed white intro;
  gray Residency/Departmental Funding; white External Funding, followed by proposed
  Graduate Assistantships and Student Employment H2 over existing jobs paragraph.
  User wants Department Travel Funds through page end removed; page edits paused
  under explicit “don’t change anything yet.” No new travel page to be created.
- Existing short travel summary still claims funding availability; recommend
  inquiry-only Contact link when approved. No page text/link changes made here.
- Documentation only; no builds/checks, commit, push or deployment.

## November 13: Original-site backup workflow agreed

- Every migrating WordPress site needs a downloaded full backup (database/files)
  plus an All content WXR/XML export, labeled by unit/date/source and kept off-host.
  Check scope/recoverability before retirement; refresh if the original changes.
- Recorded as a durable migration requirement. No backups created or verified
  in this discussion; existing exports do not establish full-backup coverage.
- Documentation only, local; no build/checks, commit, push or deployment.

## November 13: Voice check added to text-cleanup checklist

- Added report-only pronoun/voice review to rules/text-cleanup.md and its report template:
  flag mixed institutional voice, distinguish intentional biographies/quotations,
  and consult before any rewrite. No website copy or cleanup script changed.
- Documentation only; no builds/checks, commit, push or deployment. Applies to
  future requested cleanup passes; no site-wide voice audit performed here.

## November 13: Hörmann Prize remaining bold removed

- Removed remaining strong/b wrappers from the prize page, retaining all words,
  headings, lists and journal-title italics. Local edit only; no build/visual
  checks, commit, push or deployment.

## November 13: Hörmann Prize item 3 readability

- Kept item 3’s opening sentence, then nested its seven remaining sentences as
  bullets. Removed bold/italic wrappers within item 3 and fixed the missing space
  after Mānoa by separating the sentences into list items. Word order and wording
  preserved exactly; only markup and whitespace changed. Other items unchanged.
- Local source edit only; no build/visual checks, commit, push or deployment.

## November 13: Hörmann Prize section split

- White H1/first-paragraph intro; remaining content in gray with approved H2s:
  Awards, Eligibility and Submission, Selection and Publication. Corrected only
  the approved Monitary → Monetary typo. Remaining paragraphs/list preserved.
- User supplied the LCH family tribute identifying Bernhard as the UH sociology
  professor, then approved Hörmann throughout this page. Updated visible surname
  and prize/committee references; /hormann-prize.html unchanged.
- Recorded explicit consultation-before-copy-rewriting rule in conventions.
  Local soc/css-shared edits only; no build/checks, commit/push/deployment.

## November 13: Graduate-student profiles consolidated

- Moved cohort row/photo CSS into profile.css and deleted graduate-students.css
  and its import. Ownership guard now requires student profile rules there too.
- Shared student template reuses faculty profile-name, profile-titles/job-title,
  profile-detail, email/contact-link and divider classes. Names 20px/600, program
  16px/600, research/advisers 16px/400. Faculty office uses the same detail class.
- Name/detail/divider spacing tokens centralized in profile.css. Student roster,
  field text, links, portraits and responsive row proportions preserved.
- Source edits only; no builds, visual checks, commit/push/deployment. Changes
  apply to all consumers of the shared student-directory template when rebuilt.

## November 13: Hawaii Hall heroes and universal policy pages

- Renamed shared media/heroes/faculty → hawaii-hall; main.webp → 01.webp and
  associated.webp → 02.webp. Updated PUBA directory references without changing
  their actual pictures. Common page-heroes.json centrally assigns 01 to every
  /policies-procedures.html; hero and attribution use that assignment first.
- Shared footer link default enabled. Added local policy pages where absent in
  ../es, ../geo, ../pols, ../psy, ../soc, ../ssri, ../sci, ../wgss, ../uhero;
  ../anth and ../puba already had them. All include the shared body. Existing
  Anthropology appendix retained; its old per-unit policy hero removed.
- Policy hero remains visible even on a site with other heroes disabled. Other
  saved heroes, heights, overlays, and GEO satellite assignments unchanged.
- Source edits only; no builds/visual checks, commit/push/deployment. Shared and
  consuming-site changes must be published together. Future scaffolds still need
  their own local policy metadata page; the shared assignment/footer is ready.

## November 13: Universal Policies & Procedures direction

- User wants the shared university policy page on all sites, including college
  and research units, linked from every page’s footer, with one common hero image.
- Initial discussion identified partial adoption. Completed above: selected
  Hawaii Hall 01 and added current-site page/footer adoption.
- Recorded scope in conventions. Image selected and current-site implementation completed above.

## November 12: Sociology site-wide text cleanup

- Standard mechanical cleanup across 50 HTML sources and shared SOC text fields:
  38 HTML files edited; 32 intro classes, 85 NBSPs, 30 ʻokina variants, one full
  university-name correction, one Mānoa correction, four repeated spaces.
  No heading-formatting wrappers or empty paragraphs found; shared JSON unchanged.
- Preserved links/attributes (except intro), tables, templates, original exports,
  and existing local layout edits. Eight visible missing-diacritic candidates
  left for optional editorial review; permalink watchlist false positive ignored.
- Report: units/soc/soc-text-cleanup-report.md; findings: exports/soc/text-cleanup-2026-11-12.json.
  No build, visual audit, broad checks or second scan, per user workflow.
- Local soc/css-shared edits only; no commit/push/deployment.

## November 12: Sociology faculty list removed

- Removed the redundant text-link list and its wrappers below the shared faculty
  grid in ../soc/src/faculty/index.html. Grid and opening content retained.
- Local only; no build/checks, commit, push or deployment.

## November 12: Sociology Support layout

- Support SOC now uses the established reverse imageTextRow: heading/paragraph
  left, shared Foundation SVG right. Removed the old inline figure. Preserved
  donation copy and destination. Local ../soc edit; no build, visual check,
  commit, push or deployment, per user’s requested editing workflow.

## November 12: Profile CSS ownership finalized

- profile.css owns faculty/person cards, office/building cards/maps, profile-page
  columns, profile photos and profile contact-link styling. Main Office now has
  an explicit office-card class instead of borrowing generic sidebar-group rules.
- layout.css retains structure/containment; typography.css retains fundamental
  text rules. Header title, global focus, HR and section-surface rules moved to
  their owners. Generic sidebar-group rules relocated unchanged to sidebar.css;
  broader sidebar audit/design remains deferred. Cohort rows moved unchanged to
  graduate-students.css. Ownership checks enforce these source boundaries.
- Before the user stopped further checking: seven builds passed and 24 before/
  after browser cases had zero computed-style differences. No further checking
  requested; do not repeat visual audits for routine edits without instruction.
- Local css-shared changes; no commit/push/deployment. Earlier profile typography
  settings remain: name 20px/600, title 16px/600, subtitle 16px/500. Footer acronym
  800 and decorative 404 mark 900 remain explicit graphic exceptions.


## November 12: Final regular-copy hierarchy and graphic exceptions

- User clarified cap scope: regular headings/paragraphs/bullets/profile text never
  exceed 600. Profile names 20px/600; academic titles 16px/600; role subtitles
  16px/500. Supersedes 18px title/role trial and 700-weight names.
- Restored footer acronym 800 and decorative 404 display 900 after explicitly
  rejected broad cap. These are graphic exceptions; white/no-shadow footer and
  approved tablet arrangement preserved. No other graphic changes authorized.
- Shared guard exempts only those exact selectors/weights; ordinary footer and
  404 copy remain capped. Source rules remain centralized in profile.css.
- Shared checks and SOC/PUBA/SSRI builds passed; built weights/sizes and restored
  graphic exceptions verified. Prior seven-site 48-case browser check measured
  final 16px titles/roles and 600 names before restoring graphic exceptions.
- Local only; no commit/push/deployment. Publish css-shared and rebuild consuming
  sites to apply online. Existing SOC contact/data migration remains local too.

## November 12: Shared profile typography audit (earlier size trial superseded)

- Final user hierarchy: paragraph 400, academic/job title 600, administrative
  subtitle 500; both title lines use the same paragraph-size token (1.125rem).
  Name headings retain 1.25rem/700. Supersedes the prior academic-weight-500 trial.
- Consolidated typography into one token-controlled block near the top of
  src/css/profile.css. Removed duplicate smaller-role rules and obsolete unused
  name/chair typography variants. Shared identity markup remains universal.
- Added shared CSS ownership guard; negative fixtures prove competing/duplicate
  role/title typography is rejected. Updated existing conventions rather than
  retaining conflicting size/weight instructions. Audit: profile-style-audit.md.
- Seven builds passed: SOC/PUBA/SSRI/PSY/POLS/GEO/SCI. Shared checks and existing
  SOC/POLS verification passed. Chrome computed-style checks: 16 pages × three
  widths = 48 cases, zero typography failures or horizontal overflow. Evidence:
  exports/accessibility/profile-typography-2026-11-12.json.
- New audit changes local to css-shared; no commit/push/deployment. Existing SOC
  contact/data migration edits remain separate. Other units’ source edits preserved.
  Publish shared changes and rebuild consuming sites before evaluating live output.

## November 12: Profile academic titles softened (superseded)

- Shared profile-job-title weight reduced 600 → 500; retained 1.125rem paragraph
  size. Applies to academic titles in contact/directory cards and bio sidebars.
  Name heading styling unchanged. Decision recorded in conventions.
- Shared checks and SOC build/50-page verification passed; built CSS confirms
  weight 500. Local css-shared change; no commit/push/deployment.

## November 12: Sociology contact page shared layout

- White Contact SOC/hours section, gray full-width shared Main Office/Saunders
  Hall photo/map, then white shared contacts grid. Address starts Saunders Hall;
  email/phone use icons and links; fax and legacy inline portraits removed.
- SOC migrated to one shared people.json: existing 14 faculty records retained,
  plus Lisa’s existing staff details/photo. Portraits centralized in faculty-staff;
  bios/directories/contact now use the same records. Existing shared faculty
  office/phone values remain authoritative over older Contact text.
- User clarified Ashley only; there is no additional Ashlyn/Ashland contact.
  Four contacts confirmed, sorted Darrah, Nhomi-Koza, Rubin, Steger. No fifth
  card pending; earlier fifth-person clarification is superseded.
- Shared checks and 50-page SOC build/verification passed. Verification excludes
  Contact’s intentionally replaced imported prose from its old-text comparison;
  targeted rendered checks cover the new content. Browser verified all three
  sections, four cards/order, shared image paths, address/map, no fax, and reflow
  at 320/390/768/1200/1800px. Main-content axe reported zero violations (external
  map contents excluded). A fresh final build resolved transient stale output
  during the data-file transition; final verification passed.
- Local css-shared and ../soc changes only; no commit/push/deployment. Prior SOC
  phone formatting edits preserved. Other local imported images remain untouched.

## November 12: PUBA course availability note

- Added the user’s final wording after the Courses opening paragraph, before
  course groups: “The information below provides an overview of typical course offerings;
  specific courses and topics offered vary by semester based on scheduling and
  instructional resources.”
- PUBA build passed before this final wording adjustment; final source wording
  and diff whitespace checked afterward.
- Local ../puba content change only; no commit/push/deployment.

## November 12: SSRI deploy artifact lookup failure

- Inspected run 43348253584/job 131632734036 via public GitHub API. Shared checks,
  install, site build, Configure Pages, and Upload site all succeeded; Deploy alone
  failed. Three error annotations report the same missing-artifact lookup.
- Run API lists unexpired github-pages artifact 14003280181 (13,768,777 bytes),
  created 15:54:14 HST; deploy failed at 15:54:15. Upload was not missing. Suspect
  artifact-service visibility/timing, not a confirmed workflow version mismatch.
  Node20 deprecation and Ubuntu migration annotations are separate warnings.
- No workflow changes made on this evidence. Next: rerun failed job and verify
  live footer; if recurrent, inspect deploy artifact lookup/logs before changing
  workflow. Existing terminal authentication limitation still prevents triggering
  reruns here. This documentation update is local only.

## November 12: Live footer deployment mismatch identified

- Verified local/remote main revisions match: css-shared 4adf9eb, PUBA 2b36564,
  SSRI 440364a. Shared white/no-shadow and tablet layout changes are pushed.
- Direct live CSS checks: PUBA has tablet folding but #c4d1cb; SSRI has old tablet
  layout and #c4d1cb. Neither live stylesheet contains the current white token.
- GitHub API: last successful PUBA run 43346360609 at 15:38 HST and SSRI run
  43344973587 at 15:26 HST predate shared commit 4adf9eb at 15:45 HST. Both unit
  workflows use css-shared/main; this is a deployment lag, not separate templates.
- Terminal GitHub credential helper unavailable; no workflow dispatched. GitHub
  connection suggested. Next: run existing deploy.yml workflow for PUBA and SSRI,
  verify successful runs and live CSS/markup. Other consumers also need a rebuild
  to pick up shared changes. No additional CSS/template changes made in this check.

## November 12: Footer abbreviation changed to white

- User requested solid white; shared --footer-abbreviation is now #ffffff.
  No acronym opacity or text shadow; approved tablet layout unchanged. Supersedes
  the previous pale-color experiment; conventions and footer documentation updated.
- Shared checks and PUBA/SSRI builds passed; white token verified in both bundles.
  Local only; no commit/push/deployment. Publish css-shared and rebuild consuming
  sites, then request a fresh Siteimprove scan; no cleared warning claimed.

## November 12: Footer acronym shadow removed

- Removed only the shared acronym text-shadow declaration. Retained #c4d1cb,
  no text opacity, existing background, text trimming, and approved tablet layout.
  Shadow token remains defined but unused; no unrelated shadow cleanup.
- Shared checks and PUBA/SSRI builds passed; both output acronym rules verified
  shadow-free with the original color token. Local only; no commit/push/deploy.
- Next: publish css-shared, rebuild PUBA/SSRI, and rerun Siteimprove. Whether the
  shadow caused its contrast-review warning remains unconfirmed pending scan.

## November 12: Footer acronym overlap corrected

- User explicitly approved the improved tablet arrangement as the shared standard;
  recorded in project conventions.

- Shared tablet footer now gives the acronym its own row, with identity/contact
  in halves below (576–991.98px). Replaces equal thirds that allowed PUBA to
  overlap its program name. Existing font sizes, colors, shadow, and phone /
  desktop arrangement preserved; no solid acronym backdrop added.
- Shared checks and PUBA build passed. Chrome verified no acronym/identity
  overlap or horizontal page overflow at 320/390/575/576/700/768/991/992/1200/1800px.
- Local css-shared change only; no commit/push/deployment. Publish shared change
  and rebuild consuming sites to apply remotely. Hero-review change remains
  separate in ../puba.

## November 12: PUBA hero review restored

- Restored ../puba/src/hero-review.njk output at /hero-review.html after the
  user reported the preview URL returned 404. Remains noindex/nofollow and
  excluded from collections/navigation. Supersedes its audit-time exclusion.
- PUBA build passed; generated review heading, hero assets, and noindex checked.
  Local only; no commit/push/deploy. Push puba and rerun its publishing workflow
  to restore https://cssweb-stack.github.io/puba/hero-review.html remotely.

## November 12: PUBA news URL decision

- Preserve existing published post URLs/slugs when migration resumes; no historical
  slug-shortening pass or resulting redirects needed. Future articles receive
  concise descriptive slugs independent of headline length; check uniqueness.
- Recorded in project conventions. News import remains deferred. Documentation
  only for this decision; diff whitespace check passed. No commit/push/deployment.

## November 12: PUBA audits and launch preparation

- User confirmed all current pages reviewed/approved; news migration explicitly
  deferred. Inspected Posts export: 54 published posts matching the pending URL
  inventory, two drafts, 74 attachment records. No posts imported or retired.
- Accessibility: corrected shared long-email wrapping, footer utility target
  height, redundant directory portrait alt, and skip-link focus. 31-page mobile /
  desktop axe recheck passed; five-width reflow and targeted keyboard/mobile /
  text-spacing checks passed. Color-contrast/frame incompletes remain manual
  coverage limits. POLS build and 51-page verification passed for regression.
- SEO: 28 page descriptions replaced; production canonicals enabled, guides off,
  development hero page unpublished. Canonical computation handles false URLs.
  31-page SEO checks: zero errors/notes. Indexing remains off pending host choice.
- URL/404: standard 404 plus 26 verified generated redirects; root and /puba/
  builds passed 2,980 internal-reference checks. News landing + 54 posts deferred;
  Academic Program and GCERT Public Service Leadership still unresolved. Preserve
  existing WordPress archive access for any production switch.
- Reports: units/puba/puba-accessibility-audit.md, units/puba/puba-seo-audit.md, units/puba/puba-url-comparison.md;
  measured evidence under exports/accessibility, exports/seo, exports/launch.
- Local changes in css-shared and ../puba only; no commit, push or deployment.
  Existing unrelated edits/workbook annotations preserved. Await destination:
  configured GitHub preview or production WordPress replacement. Next: publish
  to selected host, verify live redirects/HTTP 404, run live checks and request
  Siteimprove re-scan. No Siteimprove connection is available here.

## November 12: PUBA course images assigned

- Replaced the three course-row placeholders in `../puba/src/courses.html` with
  shared PUBA `courses/course-01.webp`, `course-02.webp`, and `course-03.webp`
  in page order. Actual dimensions are 600×600; decorative empty alt retained.
- PUBA build passed (31 pages); verified all three rendered image paths,
  dimensions, and copied assets. Text and layout preserved.
- Local only; no commit, push, or deployment. Repositories to commit/push:
  `css-shared` (including new course assets) and `puba`; rerun PUBA publishing
  workflow after both are available remotely.

## November 12: PUBA three course image/text rows

- Three user-authored course groups use shared imageTextRow square-image layout
  with shared 500x500 temp.jpg decorative placeholders. Text preserved. Course
  resources moved outside gray to separate white section below, per correction.
- PUBA build passed (31 pages); placeholder intrinsic dimensions checked and
  matched. Local only; no deployment.

## November 12: PUBA certificate gray requirements bands

- Both certificate pages now use white opening/sidebar, full-width gray Program
  Requirements content, then the existing separate white course-resource section
  below. Resource includes remain outside gray. No copy or grid changes.
- PUBA build passed (31 pages). Local only; no deployment.

## November 12: PUBA Courses section split

- H1 and opening paragraph remain white. Existing six course content groups and
  resource buttons now in second full-width gray section; first leading HR
  removed, later separators retained. Copy unchanged; course grid deferred until
  user supplies content. PUBA build passed (31 pages). Local only.

## November 12: PUBA homepage two-section trial

- White introduction through NASPAA-accredited MPA paragraph, with NASPAA logo /
  Requirements callout right. Gray supporting section has public-service question
  and list, separate ranking and program-action columns. Desktop 75/25 above,
  50/25/25 below aligns resource widths; below 1200 supporting text precedes two
  equal resource columns, below 768 all stack. Existing shared Bootstrap gutters,
  graphic callouts and button include; no new CSS. PUBA build passed (31 pages).
- Local only; visual trial awaiting user review.

## November 12: PUBA Why Study sections and accreditation

- White opening uses shared responsive main/right-sidebar layout, full University
  of Hawaiʻi at Mānoa name, and NASPAA accreditation mention plus existing logo /
  Requirements callout. Mission and Values moved intact into full-width gray;
  leading HR removed. PUBA build passed (31 pages). Local only; no deployment.

## November 12: PUBA Advisory Board sections

- White opening retains intro and purpose bullets. Advisory Board Members and
  alumni note now in full-width gray section; leading HR removed. Text unchanged.
- Local only; no deployment.

## November 12: PUBA Pi Alpha Alpha sections

- White opening retains H1, introduction and three purpose bullets. Membership
  and Additional Notes now in full-width gray section; removed leading HR before
  Membership, retained separator before Additional Notes. Text unchanged.
- Local only; no deployment.

## November 12: Policies page accepted for use

- User accepted shared policy page for current use. Removed visible In progress
  notice, PUBA draft metadata/flag; site-wide noindex setting remains unchanged.
- Shared core and optional Anthropology appendix remain; further POLS-specific
  material still deferred. Local only; no deployment performed.

## November 12: PUBA funding page section split

- Funding Opportunities H1/opening paragraph remain in white section. Scholarships
  and Graduate Assistantships now gray full-width section. Removed leading HR;
  retained divider between scholarship and GA groups. Text/URLs unchanged.
- Local only; no deployment.

## November 12: Certificate sidebar contact caption shortened

- Both certificate pages now pass programLabel GCert, rendering To discuss the
  GCert! MPA retains To discuss the MPA! No other sidebar content changed.
- Local only; no deployment.

## November 12: PUBA program grids updated and mobile 2x2 fixed

- Confirmed MPA and two certificate pages still used older content-sidebar /
  three-resources wrappers. Replaced with shared current profile-page 80/20
  wide-desktop, intermediate sidebar widths, and stacked mobile layout.
- Removed full-width grid-column from utility-link group: four ordinary action
  cells now form 50/50 + 50/50 below 768px; tablet/desktop actions remain stacked.
- Existing texts, destinations and compact internal link spacing retained.
- Shared checks/build passed. Fifteen browser cases across all three pages at
  1800/1100/700/390/320px verified desktop 80/20, single-column sidebar actions
  at tablet/desktop and exact 2x2 mobile cells; no horizontal overflow.
- Local only; no commit/push/deploy.

## November 12: Sidebar block consistency reassessment

- Found mixed grid/sibling spacing; SSRI home could combine Bootstrap gutter and
  legacy resource margin. Added one sidebar-stack / --sidebar-block-gap (1.5rem).
- SSRI home, GDO, OENAS, HAM, TASI and HCRI contacts now use shared stack. Contents
  retained. PUBA button groups use same block gap; utility links remain compact.
- Diagnostic rules now outline stack children and PUBA logical button/link groups.
  No production borders added; unit layoutGuides toggle still controls helper CSS.
- Shared checks and both builds passed. Eight browser cases at desktop/mobile
  verified 24px gap token, actual stacked gaps, outlines and no overflow. PUBA's
  existing two-column mobile button layout retained; its row gap uses same token.
- Local only; no commit/push/deployment.

## November 12: SSRI layout guides re-enabled for sidebar review

- Set SSRI layoutGuides true at user's request to inspect sidebar consistency.
  Other units/settings unchanged. Local review; no deployment.

## November 12: Duplicate funding references removed

- Removed final funding bullets from both certificate pages and MPA Additional
  Notes heading/paragraph/divider that contained only the duplicate funding link.
- Shared sidebar Funding Sources link remains on all three pages; funding page
  itself untouched. Local only; no commit/push/deploy.

## November 12: Compact PUBA sidebar deadlines and links

- Shortened shared caption to Deadlines: Apr 30 & Nov 1 (no redundant Application
  or forced break). Month names preserve quick date recognition.
- Testimonials/Funding Sources now one compact group with .125rem gap instead
  of separate grid items inheriting large button gaps. Touch targets retained.
- Local only; no commit/push/deploy.

## November 12: PUBA program sidebar labels and utility links

- Shared three-program sidebar removes forced line breaks: MPA contact reads
  To discuss the MPA! and info session caption reads Explore PUBA programs.
  Certificate contact captions retain their own program names; deadlines unchanged.
- Testimonials and Funding Sources links reuse special-text icon geometry/color
  with people.svg/cash-coin.svg; removed conflicting button-style testimonial rule.
- Enabled funding link on MPA and two certificates, not homepage. Existing inline
  funding references retained for content context. No commit/push/deploy.

## November 12: Main MPA second section gray

- Added page-section--gray to second main MPA section; text/layout unchanged.
- Local source change only; no deployment performed.

## November 12: PUBA practicum placements sections

- Added white lead-off paragraph describing sectors/service areas reflected in
  existing sites. Gray Selected Practicum Sites section holds original lead-in
  and unchanged placement list. Removed intervening HR.
- Original past-five-years claim retained pending user's content review; no
  placement currency verification or editorial list changes made.
- Local only; no commit/push/deployment.

## November 12: PUBA MPA learning outcomes sections

- Added concise general lead-in under H1 in white opening section. Gray section
  now contains Student Learning Outcomes H2, original linked lead-in and all ten
  original outcomes. Removed intervening HR; no leading rule.
- Outcome wording/order unchanged. Local only; no commit/push/deployment.

## November 12: SSRI layout review accepted

- User considers layout work complete. White lead-off emphasizes page purpose;
  gray bands group supporting detail. Individual bios always remain white.
- Gray heaviness may be revisited through shared color tokens later; no color
  adjustment requested now. Continue user's next task, not further layout polish.

## November 12: Conditional final gray-band spacing

- Shared CSS adds layout-section-spacing bottom margin only to a gray section
  that is the final direct child of site-main. Existing main bottom padding stays;
  white-ending pages and gray sections followed by more content are unchanged.
- Responsive gap uses existing token (3rem desktop, 2.25rem mid, 2rem phone).
- No empty spacer markup or unit-specific overrides. Local only; no deployment.

## November 12: Shared privacy page white lead / gray policy content

- Heading/date/intro remain white; Website analytics through remaining sections
  now in full-width gray band. Opening analytics H2 has no leading divider.
- Updated shared privacy body, so all university-template consumers inherit it.
  Policy wording, date and links unchanged. SSRI layout now 13 split/2 exceptions.
- Local work only; no commit/push/deployment performed.

## November 12: SSRI layout consistency sweep

- Reviewed all 15 built pages: 12 white opening/gray details; bio/privacy/404 are
  deliberate white purpose-specific exceptions. Directory extra white group valid.
- No legacy sidebar grid or leading section HR/H2 found. All pages one H1.
- Eight targeted desktop/mobile cases verified 80/20/stacking and no overflow.
- Report: ssri-layout-review.md. No site edits required, no deployment performed.

## November 12: Boilerplate page presentation

- Replaced prominent tagline/separate update paragraph with ordinary intro sentence
  describing grant-application use and full institutional names; final sentence
  retains Last updated October 2020. No date/content freshness claims invented.
- All reference content now in gray full-width section; no leading HR before first
  H2, later separators retained. Historical boilerplate text unchanged.
- Local only; no commit/push/deployment performed.

## November 12: TASI/PHIDC team wording corrected

- User directed removal of entire Key faculty include sentence (Victoria Fan and
  Yan Yan Wu). No replacement roster invented. Prior roster uncertainty closed by
  removing that sentence. Heading now TASI/PHIDC Team for combined program page.
- Local only; no commit/push/deployment performed.

## November 12: TASI/PHIDC section layout and stale team warning

- Entire opening H1/tagline/intro/list/certificate paragraph now white full-width.
  Gray shared 80/20 section starts at PHIDC Team, with Christina contact sidebar.
- Removed leading HR at PHIDC Team and outdated paragraph presenting Norman
  Okamura as current director, following user's confirmation he is deceased.
- User uncertain whether Victoria Fan remains involved: existing roster sentence
  still needs confirmation; do not repeat speculative employment allegations.
  Other project/program text remains unchanged and needs content-owner review.
- Local only; no commit/push/deployment performed.

## November 12: HCRI and HAM lower-section headings

- Added Mission and Impact above HCRI mission/history paragraphs and About Greg
  Chun above HAM biography. Both open gray content sections without a leading HR.
- Existing content/contacts unchanged. Local only; no deployment.

## November 12: HCRI two sections with upper logo

- First white shared 80/20 row holds H1/first intro paragraph and existing logo.
- Second gray shared 80/20 row holds remaining mission/history paragraphs and
  main office/Christina Higa/Charissa Minato sidebar. All original content retained.
- No new divider above opening content. No commit/push/deployment performed.

## November 12: OENAS and HAM white lead / gray details

- Moved each H1/first intro paragraph into white full-width section. Remaining
  content and existing contact sidebar occupy gray shared responsive 80/20 section.
- Removed leading HR before OENAS Professional and Experienced Staff. HAM lower
  section starts with Greg Chun biography prose; no heading/content invented.
- Original text, links, portraits/contact details and later dividers retained.
- Local review; no commit/push/deployment performed.

## November 12: SSRI homepage mobile callout icons

- Home graphics inherited 75% mobile portrait sizing after sidebar move. Marked
  both as sidebar-media--icon and capped stacked/mobile artwork at 6rem (96px),
  retaining centered labels and existing tablet/desktop sizing.
- Shared opt-in icon class leaves portraits/logos and other graphics unchanged.
- Local work only; no commit/push/deploy.

## November 12: SSRI homepage white lead / gray details

- Full-width white H1 and introduction; gray details section starts at
  Interdisciplinary Research without a leading HR. Extramural Grant Administration
  retains its separating HR. Shared responsive 80/20 profile-page geometry.
- Existing Travel Award/Funding Levels callouts moved with sidebar alongside
  details, stacked within right column; destinations/content preserved.
- No commit/push/deployment performed; local review.

## November 12: SSRI Grant Development section structure

- Full-width white opening section contains H1 and existing introduction.
- Priority through Boilerplate now in gray full-width section with shared 80/20
  main/contact-sidebar geometry; removed leading HR before Priority.
- Hanalei Abbott photo/details and Jonathan Massie details retained unchanged in
  right sidebar. Later main-content dividers retained. No deployment performed.

## November 12: SSRI leading section H2 dividers corrected

- Found four leading HRs across Directory (two page sections), Research Services,
  and Fiscal/Compliance. Shared people/service includes now pass divider=false
  for each loop's first group; later separators remain. No CSS hiding workaround.
- sectionHeading accepts explicit divider flag. Other content/prose, privacy
  headings, sidebar dividers and section background borders remain unchanged.
- Updated convention: no leading rule at a fresh section/band or bio column;
  retain rules separating later content groups. No deployment performed.

## November 12: UHERO fully detached

- User wants no literal css-shared connection. Copied Inter/fonts license locally;
  removed shared.config/bootstrap helpers/watch targets/CI checkout and hourly cron.
- Independent build verified, no shared imports. Local UHERO AGENTS/README/handoff
  now own its instructions. Earlier font-sharing notes superseded.
- No production deployment or other unit changes.

## November 12: UHERO scope corrected — independent design

- User clarified UHERO is standalone Bootstrap + Inter, not university-template
  based. Replaced initial starter in same uhero directory; no restart needed.
- Removed provisional central unit records. Only Inter assets shared; no university
  CSS/shell/header/footer/hero. Standalone Eleventy config and Bootstrap dependency.
- Next: bespoke header and slideshow direction, then stop. Earlier starter notes
  superseded. Guide: uhero-starter.md. No full-site migration/deployment.

## November 12: UHERO local starter

- Created lowercase sibling uhero with existing shared Eleventy generator, home
  and privacy HTML, local/shared settings, workflow and durable instruction pointer.
- Central uhero data: identity/contact from official site; home-only navigation,
  noindex, guides on, hero disabled pending slideshow, Open Graph awaiting asset.
- Shared UH logo temporary. No imported content/images, custom header/slideshow,
  Git remote, commits or deployment. Next: user's header/slideshow direction.
- Guide: uhero-starter.md. Local preview command uses port 8094.

## November 12: Solid footer abbreviation color

- Added --footer-abbreviation: #c4d1cb in master colors.css and replaced large
  footer acronym's .75 opacity with that solid color in shared footer.css.
- All units inherit the same editable token; other footer opacity rules unchanged.
- Local workflow; no commit/push/deploy.

## November 12: NASPAA Requirements opening sidebar

- Added homepage shared NASPAA SVG in right profile-sidebar of opening section,
  matching accreditation page's shared responsive profile-page geometry.
- Informative standalone image has descriptive alt text; no internal SVG title
  required when embedded through img. Lower gray section/tables unchanged.
- Local workflow; no commit/push/deployment performed.

## November 12: Ordinary blockquote visual treatment corrected

- NASPAA blockquote existed in source/output but border/indent styling was limited
  to testimonial wrappers. Extended common quote treatment to main-content
  blockquotes; reset nested testimonial quote border/padding to prevent doubling.
- Local workflow: user requested no repository handoff lists in responses until
  they switch back to remote workflow. No commit/push/deploy.

## November 12: NASPAA accreditation quotation semantics

- Wrapped middle accreditation quotation in blockquote; final paragraph remains
  ordinary prose. Text and links preserved.
- Repositories: puba; css-shared (handoff). No commit/push/deploy.

## November 12: PUBA NASPAA accreditation sidebar

- Accreditation uses shared profile-page geometry: main 80/right 20 at wide desktop,
  shared intermediate ratios and mobile stacking. Existing shared CSS, no overrides.
- Reused exact homepage NASPAA graphicCallout with logo/Requirements link; omitted
  Public Affairs badge and removed redundant closing requirements sentence.
- Repositories: puba; css-shared (handoff). No commit/push/deploy.

## November 12: Testimonial border softened

- Shared testimonial border now 6px var(--border-neutral), matching gray section
  borders. This supersedes the rejected white-border trial.
  Existing indentation, quote text and attribution styles unchanged.
- Repository: css-shared. No commit/push/deploy.

## November 12: PUBA support layout and appreciation treatment

- Replaced old content-sidebar layout with same reverse imageTextRow macro used
  by POLS, no lead photo; UHF logo stays right with common responsive sizing.
- Additional Funds moved into full-width gray section.
- Added reusable appreciation special-text class with shared 1em gray mask icon
  geometry, emoji-smile.svg and weight 500; text size unchanged. Existing smile
  treatment left intact for its other uses.
- Repositories: puba and css-shared. No commit/push/deploy.

## November 12: Contact band design approved, applied to SSRI

- User approved PUBA trial. Changed SSRI main office/map wrapper to gray; intro
  stays white. Recorded white intro / gray office-map / white people convention.
- Applied so far to PUBA and SSRI; other units checked during their reviews.
- Repositories for this change: ssri and css-shared. No commit/push/deploy.

## November 12: PUBA contact band trial

- PUBA only: main office/map section gray; Sarah/Helen shared people grid white.
  Heading/intro remain white. No shared CSS/template or SSRI changes.
- Trial for user review, not yet a universal contact-page convention.
- Repositories: puba; css-shared (handoff). No commit/push/deploy.

## Deferred follow-up: Political Science policies document

- Remaining Policies and Committees.docx material still needs POLS-specific
  restructuring and currency review. Not completed; resume when user returns to
  POLS. Review/inventory: pols-policy-content-review.md.
- Anthropology position statement safely stored at
  src/includes/units/anth/policies-procedures.njk and selected by its unit JSON;
  no need to divert from PUBA to inspect it now.

## November 12: Shared core policies with unit appendix

- Added Academic Integrity/Plagiarism and Consensual Relationships as linked H2
  topics in shared gray core; EP 1.203 verified, catalog fetch 403 noted in guide.
- Moved Anthropology statement to central units/anth/policies-procedures.njk,
  selected by anth/policies-procedures.json. Only ANTH gets that appendix; PUBA
  and other consumers get common core only unless explicitly configured.
- Recorded architecture in conventions/guide. Generalized draft notice; no POLS
  graduate rules or penalties promoted to universal policy.
- Shared checks/PUBA build passed; rendered both default and ANTH variants,
  verified nine core H2 topics and ANTH-only appendix after core.
- Repository: css-shared. No commit/push/deploy.

## November 12: POLS policy document reviewed, no site edits

- Read supplied Policies and Committees.docx. Shared-page candidates: Academic
  Integrity and Consensual Relationships; grievances already covered. University AI
  guidance may be a later candidate, but document calls EP 2.221 proposed and its
  actual graduate rules are department-specific. Verify before universalizing.
- Other sections belong in POLS graduate/faculty/governance resources; currency
  needs department review. Review saved in pols-policy-content-review.md.
- Repository: css-shared (review/handoff only). No website changes or deployment.

## November 12: Policy page heading/title follow-up

- Corrected shared H1 and PUBA metadata title to Policies & Procedures; prior
  edit had changed only footer label. Moved broad intro immediately under H1,
  before retained In progress notice. Gray consolidated section remains present.
- Confirmed PUBA reference section and duplicated Anthropology policies removed.
- Repositories: puba and css-shared. No commit/push/deploy.

## November 12: Policies footer label and gray policy section

- Footer label now Policies & Procedures, following navigation ampersand convention.
- Added broad university-community policy introduction; retained In progress notice.
- Consolidated policy list now occupies full-width gray section. Anthropology
  reference position statement remains in its own plain section below.
- Repository: css-shared. No commit/push/deploy.

## November 12: Policy EEO label standardized

- Checked current UH Institutional Equity heading: Equal Employment Opportunity
  (EEO). Kept consolidated EEO entry/current policy collection link; removed older
  duplicate Anthropology EEO/AA section. Only its position statement remains below.
- Terminology decision does not assert EEO/AA equivalence or eliminate obligations.
- Repository: css-shared. No commit/push/deploy.

## November 12: Policies reference sections reduced

- Removed entire PUBA reference block as directed. Below the consolidated policies,
  Anthropology now retains only its position statement and EEO/AA reference.
- Removed duplicated Anthropology responsibilities, grievances, conduct, records
  and tobacco sections. Consolidated policies remain unchanged and in progress.
- Repository: css-shared. No commit/push/deploy.

## November 12: Consolidated policies working set

- Added seven H2 policy topics above unchanged PUBA and Anthropology reference
  sections. Single-destination headings linked; grievances retains two body links.
- Retained In progress status; no universalized Anthropology position statement.
- Used current EEO collection, faculty responsibility page, FERPA page and tobacco
  guidance; replaced broken graduate grievance URL in working set only.
- Repository: css-shared. No commit/push/deploy. Source sections retained verbatim.

## November 12: Policies comparison draft exposed in PUBA/ANTH footers

- Existing central pages/policies-procedures.njk retains separate PUBA and ANTH
  sections; added explicit In progress comparison-draft notice under H1.
- Created PUBA local HTML shell at /policies-procedures.html, using same body as
  existing Anthropology page. PUBA draft marked noindex even if indexing enables.
- Shared footer opt-in policiesProceduresUrl added for PUBA and ANTH only, after
  Webmaster · Privacy Policy. No other units linked to unfinished policy content.
- Policy content/links retained for review, not legally or editorially validated.
  PUBA workbook's earlier unresolved policy-page note is superseded by this page;
  do not overwrite user's annotated workbook. Redirect still awaits final URL audit.
- Shared checks/PUBA build passed (31 pages); footer destination, draft notice,
  both source sections and PUBA noindex verified. ANTH build not rerun.
- Repositories: puba and css-shared. No commit/push/deployment performed.

## November 12: PUBA shared portrait folder renamed

- Updated all six faculty photo paths in people.json to faculty-staff; connected
  Sarah Amend's new sarah-amend.webp instead of the shared placeholder.
- Confirmed all seven referenced photos exist; Sarah dimensions measured 300×300.
  Shared checks and PUBA build passed. Recorded combined faculty-staff
  portrait-folder convention. User already renamed folder; no additional rename.
- Repository: css-shared. No commit/push/deployment performed.

## November 12: PUBA contact people grid

- Confirmed main office/map already uses shared unit-contact.njk.
- Added shared POLS people-grid below map in gray section, no heading, last-name
  order: Sarah Amend (source spelling, Program Manager), Helen H. Yu.
- Moved six faculty records into central PUBA people.json and added Sarah using
  saved directory details/shared placeholder. Faculty collection excludes Sarah;
  key_contacts selects only these two. No duplicated Helen record or new bio.
- Build/shared checks passed; contact card count/order/map position verified,
  staff excluded from faculty directory and Helen bio preserved.
- Repositories: puba and css-shared. No commit/push/deployment performed.

## November 12: PUBA associated faculty sections

- First plain section: Associated Faculty H1 plus one-sentence introduction.
- Second full-width gray section: all existing faculty lists; Cooperating Faculty H2
  retained with no HR above it. Lecturer/Emeriti headings and separators retained.
- Repositories: puba and css-shared (handoff only). No push/deployment.

## November 12: PUBA Faculty display name standardized

- Changed primary faculty dropdown label, H1 and page title from Core Faculty to
  PUBA Faculty. Kept /faculty/ URL and faculty/index.html source filename.
- Shared checks/PUBA build passed; rendered heading/title/menu verified.
- Recorded [UNIT] Faculty convention in project-conventions/faculty-directories
  for future builds/reviews; other units not swept.
- Repositories: puba and css-shared. No commit/push/deployment performed.

## November 12: PUBA duplicate faculty links removed

- Removed legacy six-name list and its row below shared core faculty directory.
  Faculty cards and their biography links remain intact.
- Repositories: puba; css-shared (handoff only). No commit/push/deploy.

## November 12: Core faculty filename locked down

- Recorded src/faculty/index.html → /faculty/ as the standard in project-conventions
  and faculty-directories. Existing exceptions need inventory/redirects when fixed.
- Documentation only; no unit files renamed or deployment performed.
- Repository: css-shared.

## November 12: Office divider on all shared people cards

- Removed bio-only condition: shared profile-contact now renders the existing
  profile-contact-divider between title/roles and office in directory/contact cards
  too. Email/phone already uses that exact class and remains unchanged.
- No office or preceding titles means no extra separator. Shared across all units.
- Shared checks/PUBA build passed; verified all six cards have identical office
  and contact divider classes.
- Repository: css-shared. No commit/push/deploy.

## November 12: Intro-class removal added to standard cleanup

- Updated procedure, report template and cleanup tool to remove intro tokens from
  parsed HTML element class attributes, retaining other classes and skipping code.
- Removed ten PUBA intro classes. Copy and other attributes preserved; global intro
  CSS retained for a separate retirement pass. Follow-up scan finds no changes.
- Shared checks passed; four optional diacritic candidates unchanged.
- Repositories: puba and css-shared. No commit/push/deploy.

## November 12: PUBA Excel content-review checklist and URL plan

- Saved original 84-URL export, machine-readable plan and four-tab Excel workbook
  under exports/puba. Main checklist covers 29 current pages including six bios,
  with preview/original hyperlinks, dropdown review status and blank notes.
- Counts: one unchanged, 26 proposed moves, three unresolved pages, 54 deferred
  blog/post candidates. No retired declarations, active redirects, or 404 added.
  News landing held for blog work; two new current pages included in checklist.
- Three decisions: Academic Program, GCERT Public Service Leadership, Policies
  and Procedures. User can review these in workbook; no need to block page review.
- Verified workbook ZIP/XML/counts/hyperlinks, destination coverage and byte-identical
  original export. Reusable writer refuses overwrite to protect annotated copies.
- Guide: puba-page-review.md. Repository: css-shared. No website source changes,
  no commit/push/deploy. Next: user page review; blog export/workflow later.

## November 12: PUBA standard text cleanup complete

- Updated 17 HTML pages: 59 NBSPs, 10 incorrect ʻokina, seven dash-spacing
  corrections, two doubled spaces; one extra hyphen after an em dash removed.
- No bold/italic inside headings found. Shared PUBA text records required no edits.
  Four possible missing diacritics left as report-only observations; no response
  required. User's page-by-page review is next; SEO/accessibility/URL audit later.
- Verified identical HTML structure/attributes/templates, unchanged table markup;
  second pass zero mechanical findings. Shared check and PUBA 30-page build passed.
- Report: units/puba/puba-text-cleanup-report.md; measured JSON in exports/puba.
- Repositories: puba and css-shared (documentation). Local only, no push/deploy.

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
  docs/rules/seo-review.md; report docs/units/ssri/ssri-seo-audit.md; metadata exports/seo/ssri-2026-11-12.json.
- Checker: 14 pages, zero errors, one reviewed title-length note. SSRI build and
  shared checks pass. Indexing deliberately remains off until launch. Next is
  original-URL comparison and shared 404 page when user supplies the URL export.
  Repositories: ssri and css-shared; local changes only, no commit/push/deployment.

## November 12: SSRI accessibility review

- Completed red-flag accessibility review; scope narrowed with user: Siteimprove
  owns comprehensive scans, focused shared fixes are authorized. Audit report:
  docs/units/ssri/ssri-accessibility-audit.md; compact evidence exports/accessibility/ssri-2026-11-12.json.
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
  flagged. Report: docs/units/ssri/ssri-diacritics-review.md. No content changed in this review;
  shared checks pass. This update: css-shared only; prior SSRI edits preserved.

- Standard SSRI text cleanup complete: 24 incorrect Hawaiʻi ʻokina characters
  corrected across five HTML pages (including HCRI metadata/H1). Scanned 14 HTML
  pages and 11 unit JSON files. No NBSP, extra-space, empty-paragraph or other
  mechanical fixes proposed. Repeat scan zero patches; attributes/links/tables,
  template/code text and prior intro removal independently verified unchanged.
  SSRI build (14 pages) and shared checks pass. Optional ʻāina quote/dash-label
  observations retained in docs/units/ssri/ssri-text-cleanup-report.md; no user action needed.
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
  removed space before a comma in Andrew Wertheimer's text. See units/sci/sci-migration.md
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
  changes. Updated units/wgss/wgss-text-cleanup-report.md with this follow-up and clear
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
  2 repeated spaces and 3 empty paragraphs. Report in units/wgss/wgss-text-cleanup-report.md;
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
  validation are saved in docs/units/anth/anth-text-cleanup-report.md. User wants a findings
  report at the end of future cleanup sweeps as well.
- Standard text cleanup completed on 34 ANTH HTML/shared-data files plus the
  shared policies body ANTH renders: 312 accidental NBSPs replaced, 37 Hawaiʻi
  backtick/apostrophe variants corrected, 2 institution-name/kahakō corrections,
  6 em-dash spacing corrections, 3 repeated spaces and 1 space before punctuation.
  No invisible characters or empty paragraphs required removal. HTML attributes
  compared before/after; URLs and original exports unchanged. Source table
  structure preserved. Ambiguous sentence hyphens left for editorial review.
- Added reusable rules/text-cleanup.md checklist and house style. Repositories changed:
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
  GitHub remote not supplied. See docs/units/es/es-migration.md.
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
  See `docs/units/pols/pols-migration.md`; local POLS Git repository initialized on main;
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
- Canonical rules: `docs/shared/faculty-profiles.md` and project conventions. Earlier
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
- Editing/reference notes: `docs/shared/faculty-directories.md`. If changing a portrait,
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
  Detailed accepted structure and source handling: `docs/units/soc/soc-migration.md`.
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
