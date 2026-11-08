# Shared footer configuration

All sites render `src/includes/layouts/branding/footer/footer.njk` and use
`src/css/footer.css`. The subfooter remains in `subfooter.njk`.

Shared defaults live in `src/data/uh/footer.json`:

- `language.showHeading`: `true` shows Free Interpretation Services and the
  About these services link; `false` removes that bar and gives the language
  navigation an `aria-label`. Every language link remains available.
- `language.presentation`: `enhanced` (default) or `uh`.
- `background.desktopTablet`: SVG URL used at **1200px and wider**.
- `background.mobile`: SVG URL used **below 1200px**. Replace this value alone
  to change the smaller-screen source. Both currently use the existing
  `/media/branding/backgrounds/uh-pattern-horz-white.svg`.

Each site can override those keys under `footer` in its
`src/data/units/<unit>/site-settings.json`. Omitted keys inherit the shared
values independently. For example:

```json
"footer": {
  "language": {
    "showHeading": false,
    "presentation": "uh"
  }
}
```

## Footer link list

The default A–Z Index through UH System links live in one flat `footerLinks`
array in `src/data/uh/footer.json`. A unit can override it with a flat
`footer.links` array of `{ label, url }` records in its site-settings.json.
Legacy `footer.columns` arrays are still accepted and flattened for compatibility.
The CSS no longer honors manually assigned column breaks.

The template emits one `<ul>` containing one `<li>` per link, in source order.
CSS multi-column flow handles balancing: two columns below 576px and three
columns from 576px upward. Links flow down a column, then into the next, with
`break-inside: avoid` keeping each item intact. No per-item layout styles or
separate HTML lists are generated. The outer identity/links Bootstrap layout
still changes at 992px; these are internal list columns.

Chrome verified 22 links exactly once, correct column count, matching container
geometry and no footer overflow across 32 width/language-mode cases. Results:
`exports/footer-list-columns-2026-11-08.json`. Builds for SSRI, GEO and the style
guide and the shared checker passed.

## Current content/footer alignment (2026-11-08)

This section supersedes the historical responsive layout and validation notes
below. UH reference comparison remains future work; these are our internal rules.

- Content, upper footer, language bands and subfooter all use the same `.container`
  from `layout.css`. Usable content max-width is 87.5rem (1400px at 16px/rem),
  with `clamp(1rem, 4vw, 3rem)` side gutters. At large widths the outer container
  caps at 1496px, including 48px padding per side. There is no footer-only width.
- Bootstrap owns the upper footer's outer layout: `row gx-lg-5`, a `col-12
  col-lg-3` identity/contact column, and `col-12 col-lg-9` university-links column.
  Below 992px they stack; from 992px they sit alongside each other. Desktop
  gutter is the agreed 3rem, with no competing outer CSS grid.
- Shared `--layout-section-spacing` controls upper footer padding and the gap
  between stacked outer columns: 2rem below 576px, 2.25rem at 576–1199.98px,
  and 3rem at 1200px+. This matches content section padding. UH-language mode
  retains its existing deliberate bottom-padding removal before its language band.
- University links use two internal columns below 576px and three at 576px+.
  Column-first source/reading order is retained.
- Within the unit block, a nested Bootstrap row uses `col-12 col-sm-4 col-lg-12` for identity and `col-12 col-sm-8
  col-lg-12` for contacts: identity left/contact right at 576–991.98px, stacked below 576px
  and from 992px upward. Its horizontal gutter is 3rem. The outer footer
  still places the unit block alongside university links only at 992px+.
- Identity/contact and subfooter text are left aligned at every width. Language
  navigation retains its permitted centered treatment and existing presentation
  choices. The old 525px centering rule is removed.
- Enhanced languages retain 2 columns below 576px, 4 at 576–1199.98px, and 8
  at 1200px+. UH languages switch from two columns to inline links at 992px
  (previously 900px). Background and touch-target rules switch at 1200px.
- Bootstrap's 768px/1400px breakpoints introduce no special footer outer layout
  or container-size changes. The container remains fluid until its shared cap.

Validation: shared checker and SSRI, GEO and style-guide builds passed. Local
Chrome measured the built SSRI contact/footer markup with its actual styles and
Bootstrap across 320, 375, 575, 576, 767, 768, 899, 900, 991, 992, 1024, 1199,
1200, 1400, 1600 and 2330px, in enhanced and UH language modes (32 scenarios).
All footer containers matched the content container's x position, width and side
padding. Upper padding matched content section padding in enhanced mode; UH mode
retained only its intentional bottom exception. Outer columns stacked below
992px, shared the top edge above it, and footer content did not overflow.
Left alignment of identity and subfooter was verified at every width. Fixtures
used local styles and replaced the map iframe; no Analytics requests were made.
Measurements: `exports/footer-content-geometry-2026-11-08.json`. Safari/iPad and
keyboard/screen-reader verification were not repeated in this review.

## Historical responsive layout (superseded)


The supplied UH unit HTML and stylesheet define these values:

- Upper content: 5rem vertical padding; 3rem horizontal column gaps.
- At 900px+: four equal columns, with a 3rem top inset for the three university
  link columns. Below 900px: identity/contact share a two-column row and the
  university links split into two visual columns (11/11 for the default data),
  separated from the identity by 50px.
- At 525px and below: identity/contact stack and center. University links stay
  in two columns and remain left-aligned.
- Link spacing: 0.5rem between rows and natural 24px desktop link line boxes;
  44px mobile/tablet targets through 1199.98px
  intentionally exceed the reference's smaller targets.
- Shared container maximum widths remain unchanged. Only the upper footer and
  UH-mode language block use the reference’s local 2rem horizontal inset below
  1201px; global containers, enhanced languages, and the subfooter are unchanged.

University links are emitted once in their reading/tab order. CSS places the
same semantic list into three desktop columns or two smaller-screen columns.
The enhanced language mode retains the colored heading and language band,
with 8 columns at 1200px+, 4 at 576–1199.98px, and 2 below 576px. The `uh` mode
uses transparent bands over our retained green/SVG footer: centered inline
languages at 900px+ with 1rem right spacing and a 6rem upper gap; below 900px,
two column-first groups of eight, 3rem apart with 0.5rem row spacing and a 50px
upper gap. Both use the same `src/data/uh/languages.json` data unchanged.

Both modes retain the separate interpretation heading bar when enabled. The
reference has no heading bar, so use `presentation: "uh"` and
`showHeading: false` together to see its unheaded language arrangement.

## Validation (2026-11-06)

GEO and style-guide builds passed. Local Chrome checks covered 19 widths from
320px to 2330px, including 524/525/526, 899/900/901, and 1200/1201/1202. The GEO
page, all 13 comparison examples, four independent language/heading settings,
column override/fallback fixtures, and distinct QA-only background URLs were
checked: 171 page/viewport scenarios, 399 footer measurements, no footer
layout/overflow/configuration failures. Equal desktop tracks, 3rem gaps/insets,
5rem upper padding, natural 24px desktop link line boxes, and 44px smaller-screen
university/language targets were checked with computed browser measurements.
Keyboard Tab focus was visible at mobile, tablet, and desktop widths. Footer,
language, and subfooter focus styles and semantic link order were also checked.
Generated GEO/comparison markup has unique IDs and each shared university and
language link appears exactly once per footer. Both reference files, language
data, the SVG asset, and subfooter template remain byte-for-byte unchanged.

Known issues outside this change:

- The complete shared checker stops on the existing header rule
  `line-height: 1.5rem`, because its validator requires unitless line heights.
- Whole-page overflow remains outside the footer: UH branding navigation at
  1200px on GEO and the comparison page, and the comparison page's unit dropdowns
  at 1201–1202px. Header/global layout CSS was intentionally not changed.
- Browser verification used local Chrome; other browser engines and an actual
  screen-reader session were not tested.

## Footer identity and parent organizations

Each `src/data/units/<unit>/unit-details.json` now has a footer-only
`footerIdentity` object. Its `prefix` is present only for Department of / School
of, and `name` contains the remaining name. PUBA, SSRI, and CSS have no footer
prefix and keep their full names. The existing `name` and `prefix` fields used
by headers and other components are unchanged.

Parent organization labels/URLs are centralized as `college` and `university`
in `src/data/common/links.json`. All non-CSS units show both; CSS shows only the
university. The shared `.footer-unit-prefix`, `.footer-unit-name`, and
`.footer-parent-links` rules in `footer.css` control the 300/600 name weights,
smaller parent-link text, and spacing. Mobile/tablet parent links retain 44px
minimum targets.

## Social icon bar

Edit `src/data/units/<unit>/social.json`, in `links[].url`, to activate an
account. For example, WGSS Instagram is the `Instagram` record's `url` in
`src/data/units/wgss/social.json`. Keep `label` and `icon` as supplied. Every
unit has Bluesky, Facebook, Instagram, LinkedIn, Threads, TikTok, X, and YouTube
slots, in that order. Empty/whitespace URLs are not displayed; if none are
populated, the whole bar and its spacing are omitted. Existing URLs and GEO's
independent `bluesky` feed settings are preserved.

The usual unit loader exposes this same `social` record to the footer; the
style-guide `footerUnits` loader reads the same files. There is no second
account data source. The shared template sorts populated links alphabetically,
trims destination whitespace, and gives each link a unit/platform accessible
name. Decorative inline SVGs are hidden from screen readers.

All bar styling is grouped under the social controls comment in
`src/css/footer.css`: `.footer-social-bar`, `.footer-social-item`,
`.footer-social-link`, and `.footer-social-icon`. The actual populated-account
count sets `--footer-social-count`; the icon size ranges from 20–28px (one:
28px; eight: 22px) and gaps from 4–10px. Each link retains at least a 44×44px
click target and the left-aligned flex row wraps when needed. Eight targets
with the minimum gaps need 380px of available row width; narrower footer
columns wrap rather than shrinking the targets.

Official Bootstrap Icons v1.13.2 live in `src/media/icons/social/`, with their
MIT license and source information. They use `currentColor`, inheriting the
footer's white. Existing non-social icons are unchanged.

Social validation covered 81 local Chrome scenarios / 189 footer instances
at 320–2330px: no accounts, whitespace URLs, missing social data/entries, one
account, eight accounts (provided out of order), and an extra wide-row fixture.
Icon order, trimmed URLs, omission, actual-count sizing, 44px targets, white
fill, decorative SVG hiding, focus outlines, and wrapping passed. GEO and the
style guide rebuilt successfully; all eight SVGs are present unchanged in
both outputs. Synthetic URLs were used only in temporary QA fixtures, never
in unit data. The pre-existing full shared-check header line-height issue
remains as described above.

## Detail groups and tablet alignment (2026-11-08)

The tablet identity block is one-third width (`col-sm-4`), with contacts in the
remaining two-thirds (`col-sm-8`). This aligns the contact text with the second
column of the continuous three-column university link list. Both groups return
to full width at lg, and are full width below sm. Unit names wrap naturally.

Parent organization links and address paragraphs share one compact detail rule:
0.875rem text, 1.6 line-height, and `--footer-detail-gap: 0.25rem` between rows.
The former 44px minimum height on organization links below 1200px is removed;
their spacing no longer jumps between viewport sizes. Address paragraphs have
zero default margins. The abbreviation and unit name retain their own styles.
Phone/email and social groups use the existing shared 1.25rem block gap.
The Webmaster/Privacy divider and its obsolete spacing variables are removed.

Chrome checked 32 width/language scenarios: matching parent/address gaps, zero
organization-link minimum height, no divider, left alignment, matching contact
and second-list-column x coordinates on tablet, and no footer overflow. Results
are in `exports/footer-detail-spacing-2026-11-08.json`. All three builds and the
shared checker passed. Actual iPad refresh/review remains the next visual check.
