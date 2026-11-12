# SSRI accessibility red-flag review

Date: November 12, 2026 (Pacific/Honolulu).

**Result:** Two shared accessibility issues found and corrected. No remaining
confirmed violations in the targeted recheck. Ready to proceed to the SEO audit.
**Action needed from you now:** None. Refresh Siteimprove after publishing for
the comprehensive scan; its previous 98% score describes an older crawl.

## Shared fixes

| Issue | Correction | Verification |
|---|---|---|
| Desktop dropdown remained visible after Escape, despite aria-expanded=false | Bootstrap now controls visual visibility and aria-expanded together. Desktop pointer hover uses that same controller; Escape dismisses hover-opened menus too. Keyboard focus alone no longer silently opens a collapsed menu. | Enter opens, Arrow Down reaches links, Escape closes and returns focus; pointer hover reports expanded=true and Escape hides it |
| Mobile Search button text contrast was 4.37:1 on #f7f7f7, below 4.5:1 | Shared search-submit text uses the existing dark text token; hover styling retained | 15.71:1 measured from computed colors; opened mobile search passes axe |

Both fixes live in `src/css/header.css` and `src/assets/js/site.js`. All unit
sites inherit them when rebuilt. No SSRI page content was edited by this audit.

## Checks completed

- Current local SSRI build: 14 pages, checked at 1800px and 390px with axe-core
  4.14.0 / Chromium 157.0.8103.52, using WCAG A/AA tags through 2.2 plus best
  practices. Those 28 initial page/viewport checks had no confirmed violations.
  Opening the mobile search exposed the additional contrast issue above.
- Targeted browser recheck after fixes: desktop dropdown open, mobile navigation
  open and mobile search open all report zero confirmed axe violations.
- Real keyboard actions checked: visible first-Tab skip link, navigation into
  main content after activation, visible link focus, desktop/mobile disclosure
  buttons, Arrow Down and Escape behavior. Hover-opened Escape also verified.
- All pages have one H1 and one main landmark. Every image has an alt attribute;
  intentional decorative empty alt remains valid. Human judgement of every alt
  description is outside this quick pass. Lazy-loaded images below the viewport
  were not treated as broken images.
- Reflow at 320, 768 and 1200 CSS pixels, plus prescribed text-spacing overrides
  at 390px: 56 checks, no horizontal page overflow. This does not establish that
  every possible zoom/font combination has been manually inspected.
- Reduced-motion dropdown transitions report zero duration.
- SSRI build, shared structural checks and JavaScript syntax check pass. POLS
  build and 51-page verification pass as a shared-component regression check.

## Scope and remaining manual coverage

Siteimprove remains the primary comprehensive scanner. This review is a major
red-flag check, not a WCAG conformance certification or a replacement score.

Development guide CSS was disabled only in the temporary audit stylesheet; the
working site's helper lines/settings were preserved. Bootstrap 5.3.3 was served
from the exact cached package during the audit to remove CDN variability.

Some navigation/footer contrast checks remain marked *incomplete* by axe because
the design uses pseudo-element surfaces and a patterned footer. They are not
automated passes. Basic source-color checks support the intended contrast:
even the footer's 75%-opacity white text against a worst-case 10% white pattern
over UH green has a conservative 5.44:1 contrast bound. This is not a complete
pixel-by-pixel visual review of every state.

The external Google Maps frame's internal interface was excluded. Its host iframe
has a descriptive title. A full screen-reader session and third-party-content
review were not performed. No blanket false-positive dismissals were applied.

Page-title copy, descriptions and indexing remain for the next SEO audit.
The 404 page and original-URL comparison remain subsequent work.

Evidence: [measured audit results](../exports/accessibility/ssri-2026-11-12.json).
Reference criteria: [W3C WCAG 2.2 quick reference](https://www.w3.org/WAI/WCAG22/quickref/).
Tool reference: [axe API](https://github.com/dequelabs/axe-core/blob/develop/doc/API.md).

**Repository to update for this audit:** `css-shared` only. Existing SSRI content
changes from earlier tasks remain separate. No commit, push or deployment made.
