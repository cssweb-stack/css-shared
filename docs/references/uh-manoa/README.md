# UH Mānoa CSS reference snapshots

The `2026-11-08/` folder contains unchanged copies of the base Total theme and
UH child-theme stylesheets linked from https://manoa.hawaii.edu/ when inspected.
`sources.json` records their original URLs, sizes and SHA-256 hashes.

Use these as a dated reference for typography, widths, breakpoints and footer
comparisons. They are not a university-wide design standard and do not represent
every UH website. Both files matter because the child theme builds on the base
and uses relative font sizes. Other page/plugin/inline styles may also affect a
live page; this is not a complete archive of the university website.

These files live under docs, outside published src. Do not import them into our
sites or copy whole sections over our shared rules. Preserve source notices.
When a fresh comparison is needed, capture a new dated folder and keep this
snapshot so changes remain traceable.

## Normal-paragraph comparison

Chrome fixtures using the captured base + child CSS produced 18.75px paragraph
text with 31.875px line height in Georgia/Times at 375px, 820px and 1440px.
Our Bootstrap + shared CSS produced 16px text with 25.6px line height in
Inter/Arial at those same widths. These are fixture measurements from the saved
stylesheets, not a claim that every live UH page has identical typography.
The base sets html to 62.5%; the child sets body to 1.5em and paragraphs to
1.25em. At the default 16px browser root, that yields 10 × 1.5 × 1.25 = 18.75px.
