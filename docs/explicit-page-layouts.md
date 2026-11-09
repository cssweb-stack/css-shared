# Explicit page structure

PUBA and SSRI use one page-source convention, regardless of the number of sections.
Each content page uses `layout: shell.njk`. The shared shell supplies the document,
header, hero, main element, and footer. It never inserts sections or columns.

A simple page contains:

```html
---
layout: shell.njk
title: Example
permalink: /example.html
---
<div class="page-section">
<div class="container content-section">
<div class="row gx-0 gx-sm-5 gx-lg-5">
<div class="col-12">
<h1>Example</h1>
<p>Page content.</p>
</div>
</div>
</div>
</div>
```

For multiple sections, repeat the section/container structure in that same file.
Rows and columns are explicit too; includes such as unit-contact supply their own
rows and columns inside the visible section/container. Contact pages always use
a first section for the opening heading/text and a second for the office include.
No `fullWidthSections`, `hidePageTitle`, or automatic column setting is needed.

Shared privacy follows this same rule in `src/includes/pages/privacy.njk`.
The unit scaffolder and one-time PUBA importer now emit explicit page markup.
The obsolete ignored SSRI privacy placeholder was removed.

Older consumers may still use `base.njk`, a compatibility adapter that delegates
the document frame to `shell.njk` and its earlier wrapper behavior to
`legacy-content.njk`. This keeps GEO and existing style-guide examples compatible
without imposing source changes on those sites. The style guide forwards these
layouts to shared templates rather than copying the document shell.

Validation compares generated main-content structure and text before/after for
PUBA, SSRI, GEO, and the style guide. Ordinary pages remain unchanged; shared
privacy pages gain explicit columns where they previously lacked them. Results:
`exports/explicit-page-layouts-2026-11-09.json`.
