# PUBA accessibility review

November 12, 2026 (Pacific/Honolulu). Local review complete; live scan pending.

Four shared corrections:

- Long main-content email links wrap rather than overflow at 320px.
- Footer utility links have a minimum 24px height when their row wraps.
- Directory portraits have empty alt text because the same link includes the
  person's visible name. Individual biography portrait alt text is retained.
- Main has tabindex=-1 so activating the skip link transfers keyboard focus.

Verification: axe-core 4.14.0 in Chrome 157.0.8103.52 found zero violations on
31 pages (30 content pages plus custom 404), at 320px and 1800px, after the
first three corrections. All pages had one H1/main, image alt attributes, and no
observed broken eager images. Reflow passed at 320/390/768/1200/1800px.

After the skip-focus correction, targeted browser checks passed: first-Tab skip
link and main focus; desktop Enter/Arrow Down/Escape and pointer-hover Escape;
mobile menu/search disclosure and expanded states. Open desktop menu, mobile
menu, and mobile search had zero axe violations. Text-spacing overrides passed
on six representative pages. Shared checks and POLS build/51-page verification
passed as regression coverage.

Color-contrast and external-frame rules have incomplete results; these are not
automated passes. Analytics and Google Maps requests were blocked for this audit;
the external map's internal interface was not reviewed. No full screen-reader
session or comprehensive WCAG certification is claimed. Siteimprove remains the
comprehensive follow-up after publication; it has not been triggered here.

Evidence: [page scan](../exports/accessibility/puba-2026-11-12.json) and
[interaction checks](../exports/accessibility/puba-interactions-2026-11-12.json).
Changes local only; no commit, push, or deployment.
