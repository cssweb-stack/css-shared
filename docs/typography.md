# Body typography and UH reference comparison

The authoritative comparison snapshot supplied by the user is
`src/css/_uh-reference/styles.css`. It is not imported into our sites. Earlier
WordPress Total-theme snapshots under docs/references are a different UH theme
and must not be used to infer this reference's fonts or paragraph sizing.

## Reference findings

The supplied file defines ordinary paragraphs/lists at 0.875rem with 1.25rem
line-height below 1201px, increasing to 1rem/1.5rem at min-width 1201px.
Chrome fixtures using the complete supplied stylesheet confirmed 14px/20px at
320–1200px and 16px/24px at 1201px+. Plain and tw-prose paragraphs were checked.
These are stylesheet-fixture findings, not a claim about every live UH page;
page classes, extra styles and browser settings can change the live result.
The file contains Inter declarations; the earlier Georgia comparison does not
apply to it.

## Our deliberate readability setting

`src/css/typography.css` defines `--content-body-font-size: 1.125rem` (normally
18px). `.site-main` supplies that inherited size for reading content and lists;
the existing paragraph rule uses the same variable. Normal copy has the existing
unitless 1.6 line-height (28.8px at 18px). Nested lists inherit without multiplying.

This replaces the previous 16px paragraph size. We deliberately do not copy UH's
14px mobile reduction: the user reported difficulty reading 16px on an iPhone.
No new paragraph breakpoint is needed; the 18px reading baseline applies to
phone, tablet and desktop. Root/body sizing is unchanged, preserving rem-based
layout dimensions. Header/navigation/footer retain their existing explicit
component sizes. Existing heading, intro and other explicit component rules
remain in charge of those treatments. Content-area contact text using the normal
paragraph rule also benefits from the larger size.

## Verification

Shared checker and SSRI/GEO/style-guide builds passed. Chrome checked both the
complete UH reference and our built stylesheet at 320, 375, 390, 575, 576, 768,
991, 992, 1200, 1201 and 1440px (22 cases). Our normal paragraphs and first/nested
list items measured 18px, with paragraph line-height 28.8px and unchanged 16px
root/body sizing at every width. Measurements are in
`exports/body-typography-2026-11-08.json`. These are Chrome CSS checks; actual
reading comfort and Safari behavior still need the user's iPhone review after
refreshing the preview. No live deployment was made by this change.

## Unified intro

Only `intro` is used; `intro-nbrd` has been removed from the available source
pages/templates and CSS. Intro has no border or bottom padding. Normal paragraph
margin uses --content-paragraph-spacing (1rem); intro uses 1.5 times that (1.5rem).
Existing final-child margin normalization still removes trailing space when intro
is the last element of its primary column/section. Divider variables remain for
the separate wrapped-sidebar treatment, not for introductory text.

Intro trial adjustment: shared intro text is now 1.375rem (22px at the default
root), versus 1.125rem (18px) body copy. Bottom margin is twice normal paragraph
spacing: calc(2 * var(--content-paragraph-spacing)), normally 2rem. Existing
1.75 line height remains. There is still no border or bottom padding. This
supersedes the earlier 1.14rem/1.5-times intro values above.
