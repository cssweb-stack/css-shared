# Shared image-and-text rows

Ask for: **“Use our shared image-and-text rows, like POLS Courses.”**

For text left and image right, ask for **“the reverse image-and-text row, like
Support POLS.”** Its desktop split is 75% text / 25% image from 992px upward;
at 768–991px it uses 67% text / 33% image. On mobile,
text comes first and the image follows at 75% width, left-aligned.

Use this for decorative graphics or illustrations beside headings and text.
This is distinct from people profiles; it retains the smaller 2/10 desktop image.
The layout is centrally maintained in `layouts/content/image-text-row.njk` and
`src/css/layout.css`. Page text stays editable in each unit's HTML source.

## Landscape image-and-text rows

Ask for **“the landscape 20/80 image-and-text row, like SSRI Research.”**
Use `landscape=true` on the same shared macro. It gives horizontal images more
space on wide desktop, while retaining every other standard breakpoint:

- 1600px and up: image 20%, text 80%.
- 992–1599px: image 25%, text 75%.
- 768–991px: image 33%, text 67%.
- Below 768px: stacked, image 75% width and text full width.

Images retain their original proportions. The default square-image course rows
keep their existing 17/83 wide-desktop layout; the reverse layout keeps 75/25.
The landscape modifier applies to image-left rows. There is one shared macro,
with an explicit variant, rather than unit-specific layouts or copied CSS.

```njk
{% call imageTextRow('/media/units/ssri/hcri.webp', 520, 280,
  'Hawaiʻi Coral Reef Initiative', false, '/research/hcri.html', landscape=true) %}
<h2>Hawaiʻi Coral Reef Initiative</h2>
<p>Editable page content.</p>
{% endcall %}
```

SSRI's seven research-list entries retain semantic article wrappers with
`image-text-item`; shared CSS provides standard 3rem between those wrappers.

## Responsive behavior

For a full **80/20 content-and-sidebar layout**, use the shared `profile-page`
row with `col-12 col-md-8 profile-biography` for content and
`col-12 col-md-4 profile-sidebar` for the sidebar. Content can come first for a
right sidebar. Shared profile.css controls 80/20 from 1600px, 67/33 at
768–1599px, then stacked below 768px. Sidebar groups stack vertically; images
using profile-photo or sidebar-media retain native proportions and use 75%
width on mobile. SSRI's HCRI, HAM, OENAS, TASI/PHIDC and Grant Development pages
use this pattern. The image-and-text macro's separate proportions follow below.

- 1600px and up: image 2/12 (about 17%), text 10/12 (about 83%).
- 992–1599px: image 25%, text 75%.
- 768–991px: image 33%, text 67%.
- Below 768px: stacked; image 75% of available width, left-aligned; text full width.

Rows use the shared grid gaps, with 3rem between consecutive image-and-text rows.
Recheck fit if the global UH content width changes.

## Page markup

```njk
{% from "layouts/content/image-text-row.njk" import imageTextRow %}

{% call imageTextRow('/media/units/pols/courses/course-01.webp', 600, 600) %}
<h2>Section heading</h2>
<p>Page content remains here.</p>
{% endcall %}
```

Arguments are image path, actual width, actual height, and optional alt text.
Optional fifth argument `true` reverses the row; sixth supplies an image link;
seventh supplies an image class (default `photo-style`, use `sidebar-media` for logos).
Optional `leadImage={src: '/media/...', width: 600, height: 400, alt: ''}` adds
a framed photo above the primary image/logo, with shared spacing and mobile sizing.
The default empty alt is appropriate only for decorative images; provide descriptive
alt text as the fourth argument when the image conveys information. No images or
text are duplicated into shared JSON just to use this layout.
