# Toggle layout diagnostics

Normal production styling has diagnostics OFF. Diagnostics are currently ON
for header proofreading at the user’s request; comment out the import before
publishing the normal presentation.

At the bottom of `src/css/common.css`, enable proofreading by changing:

```css
/* @import url("./diagnostics.css"); */
```

to:

```css
@import url("./diagnostics.css");
```

Comment it again to switch off. Local dev rebuilds after common.css changes;
refresh the page. Published sites require rebuilding/deploying their consumers.
One switch applies to every site using the shared stylesheet. No page edits,
JavaScript, user-facing controls or special build flags are required.

The rules live only in `src/css/diagnostics.css`:

All helper lines are 3px thick. Container guides are pink; column guides are red.

- Header inners: pink side guides.
- Page parent and section outers: no helper lines.
- Content inners: pink on all four sides.
- Footer inner containers: pink on all four sides.
- Grid columns: red on all four sides.
- Redundant footer row parents are excluded.
- No diagnostic background fills; existing page backgrounds show through.

Helper lines use inset box shadows rather than real borders. Enabling them does
not add box dimensions, alter padding/margins, or move text. Borders, dividers and
photo frames that are part of the actual design remain in their component files.
The regular section bottom margin remains in layout.css, independent of this
switch. Diagnostic CSS must never introduce spacing or structural rules.

Validation: shared checker and SSRI/GEO/style-guide builds passed. Chrome
checked seven representative pages at phone/tablet/desktop widths (21 cases):
normal main/content/footer containers had no diagnostic borders; toggling the
helper stylesheet on and off moved/resized zero elements. Measurements:
`exports/diagnostics-toggle-2026-11-08.json`.

PUBA and SSRI page sources explicitly contain their section/container/row/column
structure and use `shell.njk`. The shell does not add content wrappers.

## Content-edge overlap correction — November 9, 2026

Removed cap-height and alphabetic-baseline text trimming from first headings and
last paragraphs, both directly inside content sections and inside primary
Bootstrap columns. Those trims placed the top ink at the box edge and allowed
descenders below it; 3px inset guides made the overlap visible. Normal line boxes
now provide top/bottom clearance without adding diagnostic padding or changing
helper geometry.

Chrome checked MPA and Associated Faculty at 375, 820, and 1440px. Text cleared
both inset guide edges in all six cases. Measurements are recorded in
`exports/puba-content-edges-2026-11-09.json`. The shared checker passed.
