# Shared section spacing

`src/css/layout.css` defines `--layout-section-spacing`: 3rem at desktop widths
(1200px+), 2.25rem at tablet widths (576–1199.98px), and 2rem below 576px.
Both `.main-content` and `.page-section-inner` use it for inner block padding.
A `.page-section--gray` also uses it for outside bottom margin, ensuring a gap
between the gray bar and the following section or footer. This is shared across
consumers; it is not an SSRI research-page override.
