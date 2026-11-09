# Foundation: one page-content parent

Every page has exactly one `<main id="main-content" class="site-main">`, supplied
by the shared base layout (or the style-guide comparison shell). It starts after
the hero/navigation and contains all page content before the footer/credit band.

At the top of `src/css/layout.css`, `.site-main` alone owns page-edge padding:

```css
.site-main {
  padding-block: var(--layout-content-spacing);
  background: var(--white);
}
```

`--layout-content-spacing` is 2rem on phones (<576px), 2.25rem on tablets
(576–1199.98px), and 3rem on desktop (1200px+). Change this variable to change
only the page's outside content spacing. Do not change section padding to do it.
The former minimum content height is removed so short pages cannot gain extra
bottom whitespace beyond the wrapper's padding.

`--layout-section-spacing` is a separate, independent control for internal bands
and existing footer/component spacing. Ordinary `.content-section` containers
have no vertical padding. Full-width `.page-section > .content-section` bands
retain internal padding; their first/last outer edges defer to `.site-main`.
A final page-section's outside margin is zero so it cannot add to the footer gap.
Section backgrounds/borders and internal group gaps are separate presentation.
Horizontal container width and Bootstrap column gutters are unchanged.

Earlier claims that content-section itself was the universal page wrapper were
incorrect and are superseded by this document. A multi-section page has multiple
section containers but only one site-main parent. No per-page edge-padding rule
is permitted.

## Verification — November 8, 2026

SSRI/GEO/style-guide builds and shared checks passed. Chrome checked 65 generated
pages at 375, 820, 1440px (195 cases). Each had one main parent and equal top/
bottom padding (32/36/48px). The test then changed only --layout-content-spacing
to 96px: both main edges became 96px while every internal section's padding stayed
unchanged. Measurements: `exports/page-wrapper-isolation-2026-11-08.json`.
Previous content-section padding audit exports describe the superseded model.
Safari visual review is still needed; these are structural/computed-style checks.
