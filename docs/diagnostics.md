# Toggle layout diagnostics

Normal sites have diagnostics OFF by default.

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

- Page parent: gold top/bottom lines.
- Section outer: lime top/bottom lines; Surface Gold except gray sections.
- Content inner: pink sides and Surface Pink.
- Footer inner containers: pink on all sides.
- Grid columns: Accent Warm; redundant footer row parents are excluded.

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
