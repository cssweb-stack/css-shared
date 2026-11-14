# Shared photo tiles

Use the existing responsive grid, program-tile interaction, and tile-style frame.
The photo-tile modifier adds a decorative cover image and a bottom label band.
Styles live in src/css/tiles.css; this is not a Sociology-specific component.

```njk
<div class="grid-five grid-spaced">
<a class="program-tile photo-tile tile-style tile-teal" href="{{ '/destination/' | url }}">
<img class="photo-tile-image" src="{{ '/media/example.webp' | url }}" alt="" loading="lazy" decoding="async">
<span class="photo-tile-label">Destination name</span>
</a>
</div>
```

One variable, --photo-tile-label-padding, sets all four sides to 0.5rem.
The minimum band height reserves two text lines plus that padding, rather than
an arbitrary fixed height. One-line and two-line labels share the same band
height; longer labels may expand to remain readable on narrow screens or with
text enlargement. --photo-tile-label-lines can reserve more lines for another
grid when needed. Labels stay regular weight 400 with stable rem font sizing.

The band alone uses 80% black, with white text. Over even an all-white photo,
the calculated contrast is 12.63:1. Photos outside the band remain undimmed.
Empty alt text avoids repeating the visible link label when imagery is decorative.
Hover, focus, reduced-motion behavior and responsive columns use existing shared
rules. Check final label wrapping and image crops in the consuming page.

Grid breakpoints are one column below 768px, three from 768px through
1399.98px, and five from 1400px. Incomplete rows center only in the middle range.
A transparent square sizing track shares the label's grid cell: normal tiles
remain square, but the track can grow with enlarged labels instead of clipping
text. The absolute cover image fills the resulting tile. This replaces relying
on a fixed aspect ratio on the outer link, which clipped long enlarged labels.
