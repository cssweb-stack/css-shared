# Sociology accessibility review

November 13, 2026 (Pacific/Honolulu). Local red-flag review complete.
**Result:** Zero confirmed axe violations across 59 content pages at 320px and
1800px (118 page/viewport scans). No accessibility source changes required.
**Action needed from the user:** None for this scan. SEO is next; live follow-up
and Siteimprove remain for after publishing/final edits.

## Checks completed

- Built current SOC sources successfully; shared `npm run check` passed
  (801 shared files and 13 unit records checked).
- Chrome 157.0.8103.52 with axe-core 4.14.0: WCAG A/AA tags through 2.2 plus
  best practices, across every current content page. Eight generated migration
  redirect documents excluded; they are not ordinary content pages.
- All 59 pages have one H1 and one main landmark, an HTML language declaration,
  no duplicate IDs, alt attributes on all images, and no observed broken eager
  images. Below-viewport lazy images are not claimed fully load-tested.
- No horizontal document overflow at 320px or 1800px across the 59 pages.
  Additional 768px/1200px reflow checks passed on seven representative pages:
  Home, Contact, Faculty, Current Cohort, MA and PhD timelines, Major Concentrations.
- Actual keyboard checks passed: first Tab reveals the skip link; Enter transfers
  focus to main; desktop Enter opens a dropdown; Arrow Down enters its links;
  Escape closes and restores focus. Pointer-hover opening and Escape dismissal pass.
- Mobile navigation opens; mobile search reports expanded correctly. Open desktop
  dropdown, mobile menu and mobile search each have zero axe violations.
- Text-spacing overrides (line height 1.5, letter spacing .12em, word spacing
  .16em, paragraph spacing 2em) cause no document overflow at 390px on eight
  representative pages: Admissions, Contact, Faculty, both timelines, Major
  Concentrations, Le Lin biography and Current Cohort.
- Both timeline tables have explicit column-header scopes and valid heading-based
  accessible labels; repeated mobile visual labels are hidden from assistive
  technology. No academic content or table structure changed.
- Interaction artifact records 34 successful assertions, including open-state axe
  checks, keyboard behavior, text spacing and representative reflow.

## Limitations and follow-up

Zero confirmed automated violations does not establish comprehensive WCAG
conformance. Axe returned incomplete color-contrast results in all 118 scans and
frame-tested results in two scans (Contact at both widths). These remain manual
review items, not automated passes. Pseudo-element/pattern surfaces in the shared
shell can require manual contrast inspection; no incomplete result was silently
reclassified as passing.

Analytics/Tag Manager and Google Maps requests were blocked during the audit.
The host map iframe has a descriptive title; the third-party map interface was
not reviewed. Bootstrap loaded from the declared CDN and its controller was
verified present on every scanned page. Existing development layout-guide CSS
was retained. Reduced-motion preference was enabled for stable interaction checks;
this does not establish full animation behavior under every preference.

No full screen-reader session, exhaustive alt-text editorial review, visual review
of every focus state, external PDF/form audit or live Siteimprove run was performed.
A final accessibility scan is still needed after remaining edits/publication.
The stale original-migration `npm run verify` inventory reported by the text scan
remains separate; it was not rerun or repaired by this audit.

SEO, live Open Graph diagnosis, custom 404/launch checks and production-domain
behavior are not established by this local accessibility review. Le Lin has been
contacted by the user about his unfinished paragraph; wait for his supplied text.

Evidence: [page scans](../exports/accessibility/soc-2026-11-13.json),
[interaction checks](../exports/accessibility/soc-interactions-2026-11-13.json).

**Repository to commit/push for this audit:** `css-shared` (report/evidence/handoff).
SOC was rebuilt locally but its source was not changed by this scan. Existing
folder-cleanup changes remain in both repositories. No commit, push, deployment
or remote synchronization check performed.
