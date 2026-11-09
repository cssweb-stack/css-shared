# Shared sidebar layout — Bootstrap

Sidebars use the same nested Bootstrap row/column system as the footer.

```html
<aside class="col-12 col-lg-4 col-xl-3 sidebar-resources">
  <div class="row gx-0 gx-sm-5 sidebar-resources-grid">
    <div class="col-12 col-sm-6 col-lg-12"><!-- One group --></div>
    <div class="col-12 col-sm-6 col-lg-12"><!-- Another group --></div>
  </div>
</aside>
```

Groups stack on phones and in desktop sidebars, splitting equally at
576–991.98px. A single group keeps half-width on tablet. Footer groups use
col-sm-4 for thirds; the mechanism and gutter utilities are the same.
sidebar-resources-grid is now only a divider hook: it does not set
display:grid, template columns, or container queries. Bootstrap owns layout. There is no added gap between stacked sidebar columns,
matching the footer's nested row.

All six SSRI sidebar pages use this pattern. Diagnostic borders use the same
row > col rule as the footer, with no sidebar-specific border selectors.
Images use the shared 100%-width, auto-height rule. Sidebar-group owns internal
text spacing; graphicCallout owns the explicit centered graphic/link treatment.
Portraits, contacts and addresses remain left aligned. Outer content/sidebar
rows use gx-lg-5, never narrower than a 9/3 split (8/4 at lg on research pages).

Shared checks and SSRI build passed. Chrome verified all six sidebars at
375/820/1440px (18 cases): flex layout, correct column fractions, diagnostic
borders and no content overflow. Results: exports/sidebar-bootstrap-2026-11-08.json.
