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

HCRI reuses this pattern with two group wrappers: logo and office/contacts.
Its outer Bootstrap columns now start at `lg` (992px), matching the homepage's
wrap threshold. Portrait tablet widths below that threshold put the sidebar
below the main content; landscape widths of 992px+ retain the right sidebar.
Within this component, `.sidebar-media` logos keep natural proportions and
are capped at 18rem, independently of viewport size.

HAM and TASI/PHIDC use the same two-track grid with a single contact wrapper:
at wide wrapped widths the unused second column stays empty, so the contact
does not expand across the entire row. OENAS uses one wrapper per contact,
placing Jack and Nancy side by side. Contact wrappers contain `.sidebar-group`
to preserve internal spacing without applying sibling-group top margins across
the grid. All four portraits use the shared `.sidebar-media` width/cap, so a
single-contact page has the same portrait sizing as a two-contact page. Phones
use one full-width track; portraits retain the same 18rem maximum.

## Tablet divider

Add `content-sidebar` to the outer Bootstrap row that holds the main column
and `sidebar-resources`. At 576–991.98px, the wrapped resource grid gets the
same 1px light-gray divider and 2rem spacing above/below as `.intro`. Both
use `--content-divider-border` and `--content-divider-spacing`, defined in
`special-text.css`. The tablet rule removes the row's sidebar top gutter and
the main column's trailing margin/padding so they do not add to that spacing.
The line stays inside the column gutters. Desktop and phone layouts retain
their existing spacing and have no added divider. All six current SSRI
sidebar consumers opt into this shared row pattern.

Within `.sidebar-group`, address paragraphs now use the same inherited 0.5rem
gap as headings, titles and email details, with default paragraph margins
removed. HCRI keeps Main Office, Christina and Charissa together as three
consecutive `.sidebar-group` blocks: each block separation is the existing
shared 1.5rem. In the wide wrapped layout, the logo is on the left and all
three information blocks are on the right, with Main Office above Christina.

## Required content/sidebar gutter

All content/sidebar rows use Bootstrap `gx-lg-5` (3rem horizontal gutter from
992px upward), across sites. No page-specific desktop gutter variants. SSRI's
homepage, HCRI, HAM, OENAS, TASI/PHIDC, and Grant Development now all use it.
Smaller-screen gutters and vertical component gaps remain separate settings.
