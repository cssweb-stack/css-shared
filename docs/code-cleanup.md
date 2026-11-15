# Source code cleanup

Run as a separate final-review pass alongside text, voice, accessibility and SEO
checks. Applies to editable site HTML and shared HTML/Nunjucks templates. It is
not a CSS minification or generated-output cleanup.

- Flush-left source lines with no indentation.
- No blank source lines from top to bottom.
- Minimal, predictable formatting for public GitHub review and future manual editing.
- Structural opening and closing tags each start on their own line.
- List wrappers and each list item start on separate consecutive lines.
- Simple list items retain their content and closing li on the same line.
- Nested lists follow the same rule; no empty lines between items.
- Keep inline links, emphasis and punctuation with their surrounding text.
- Preserve whitespace-sensitive content, front-matter values and template logic.
- Preserve text, attributes, URLs, IDs, element order and rendered layout.
- Do not format generated output, exports, vendor assets or historical snapshots.

Example:

```html
<h2>Related Courses</h2>
<ul class="list-columns-two">
<li>SOC 305: Women and Health</li>
<li>SOC 341: Survey of Social Psychology</li>
</ul>
```

For a sweep, record files changed and any whitespace-sensitive exceptions. Build
affected sites and compare rendered content/structure before and after, allowing
only insignificant source whitespace changes. Check inline word boundaries and
template output; avoid a blanket regular-expression formatter that can alter
these. Report validation actually performed and preserve unrelated local edits.

The rule applies to new edits immediately. The SOC sweep was completed November 14, 2026; see
soc-final-review-2026-11-14.md for scope and preservation checks.

## Repeatable formatter

Run `python3 scripts/code-cleanup.py UNIT` for a report-only preview, then `--apply` within an authorized cleanup. Optional `--output PATH` records changed files. It reviews editable unit HTML/Nunjucks plus unit-owned shared includes, preserves front matter/preformatted code/comments, and asserts parsed source tags, attributes and text stay unchanged apart from insignificant whitespace. Still build and compare rendered output before/after: source equivalence alone is not a layout check. ES's 28-file pass on November 14 confirmed all 27 rendered outputs retained identical structure, text and attributes. Other units are not automatically swept.
