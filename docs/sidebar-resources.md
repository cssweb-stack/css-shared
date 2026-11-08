# Responsive sidebar resources

Use the shared `sidebar-resources` container and `sidebar-resources-grid` inner
wrapper for a group of linked resources that should stack in a narrow sidebar
and form two equal columns when that sidebar moves below the main content.

```html
<aside class="col-12 col-lg-3 main-content sidebar-resources" aria-label="Resources">
  <div class="sidebar-resources-grid text-center">
    <div><!-- First image, link, and any supporting text --></div>
    <div><!-- Second image, link, and any supporting text --></div>
  </div>
</aside>
```

Rules live in `src/css/layout.css`. The inner group has one column by default
and two equal columns when the container's content width reaches 30rem (480px
at the default font size). The gap is 3rem, matching SSRI's existing spacing.
This depends on available component width, not device names or unit-specific
selectors. More items form additional rows; an unmatched last item stays in its
column. The outer page layout still decides when the sidebar moves below the
main content. Browsers without container-query support retain one column.

SSRI's homepage is the first consumer. Its images, destinations, link text,
image sizing, and source/tab order remain unchanged. No header, footer, or
people-directory rules are involved.

HCRI reuses this pattern with two group wrappers: logo/office and contacts.
Its outer Bootstrap columns now start at `lg` (992px), matching the homepage's
wrap threshold. Portrait tablet widths below that threshold put the sidebar
below the main content; landscape widths of 992px+ retain the right sidebar.
Within this component, `.sidebar-media` logos keep natural proportions and
are capped at 18rem, independently of viewport size.
