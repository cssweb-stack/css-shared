# Code Formatting

These rules cover editable HTML, Nunjucks templates and CSS, plus generated HTML across our websites. Code should be flush left, predictable and easy to edit by hand. This file is the single source displayed on Review; edit the rules here, not in generated pages.

## HTML & Templates

- Start every line at the left edge. Do not indent nested elements.
- Do not leave blank lines between elements, list items or template instructions.
- Put each structural opening and closing tag on its own line. Never join several div tags on one line.
- Keep each complete paragraph, heading and simple list item on one source line, including its opening and closing tags. Press Return after the complete element to start the next one.
- Long text may wrap visually in the editor without changing the file. This is soft wrap: do not insert Returns inside a sentence merely to fit the screen.
- Keep inline links, bold, italics, spans and punctuation with their surrounding sentence. Do not split them onto separate lines or introduce extra spaces before punctuation.
- Put ul and ol opening tags on their own lines, followed by each li on a new consecutive line, then the closing ul or ol on its own line.
- For a nested list, put the parent li and its text on one line, the nested ul or ol on the next, and each child li on its own line. Close the nested list and parent li on separate lines. Keep everything flush left, with no blank lines.
- Put standalone includes, loops and conditions on their own lines. An include or template expression that forms part of a sentence stays inline with that sentence. Do not add wrappers or extra markup to achieve formatting.

```html
<div class="content-section">
<h2>Related Courses</h2>
<p>Read the <a href="/courses.html">course list</a>.</p>
<ul>
<li>SOC 305: Women and Health</li>
<li>Additional options:
<ul>
<li>SOC 341: Survey of Social Psychology</li>
</ul>
</li>
</ul>
{% include "layouts/content/course-resources.njk" %}
</div>
```

### Whitespace

- In ordinary text, replace accidental repeated spaces with one normal space.
- Replace accidental nonbreaking spaces with normal spaces, including literal nonbreaking spaces and HTML forms such as `&nbsp;`. Keep an intentional nonbreaking space when words or values must stay together.
- Remove accidental trailing spaces before closing tags, such as `<p>Text. </p>`. Keep meaningful spaces around inline tags so adjacent words do not run together.
- Remove spaces before punctuation, including after links: `<a href="/contact.html">Contact</a>.`
- Preserve intentional spacing in preformatted text, code samples and other whitespace-sensitive content. Do not apply blanket replacements where they could change content or behavior.

## CSS

- Keep all lines flush left, including declarations and nested rules.
- Put each selector on its own line. For grouped selectors, retain the commas and put the opening brace after the final selector.
- Put each declaration on its own line. Put each closing brace on its own line.
- Leave exactly one blank line between rule blocks. Do not leave blank lines between declarations within a block.

```css
.example,
.example-link {
color: var(--link-color);
margin-bottom: 1rem;
}

@media (min-width: 768px) {
.example {
display: flex;
}
}
```

## Preserve Existing Behavior

- Keep text, links, attributes, classes, IDs, element order and page settings unchanged. A formatting pass does not authorize rewriting content, adding markup or changing layout.
- In CSS, preserve selectors, values, declaration order and rule order. Formatting must not change the cascade or appearance.
- Preserve meaningful whitespace inside preformatted text, code samples, scripts, styles and template strings. Do not remove whitespace where it changes content or behavior.
- Fix editable sources and shared generation code. Generated HTML must not accumulate blank lines from template instructions, loops, conditions or includes. Apply this centrally during generation, never by hand-editing built files. Raw exports, third-party code and historical snapshots remain unchanged.
- This sheet defines HTML/Nunjucks and CSS formatting only. JavaScript, JSON and Markdown keep their existing formats.

## Verification

- These rules are the default when creating, importing, generating or editing source files. Read this sheet before the work; do not postpone formatting until a final cleanup. Keep raw exports and historical snapshots unchanged, but format the editable source created from them.
- Check the affected files against these rules before marking a task complete. Fix formatting introduced by the current work and build/check the affected site as appropriate. Generators that produce editable source must produce this format. Generated HTML must also satisfy the no-blank-lines rule outside whitespace-sensitive content. Preserve embedded scripts, styles, preformatted text and textarea values exactly; their meaningful whitespace remains protected.
- Review all shared HTML/Nunjucks templates when checking shared formatting, not only the templates reached by one page. This includes shells, headers, footers, heroes, macros, profiles, shared pages and unit-specific includes. Use `python3 scripts/code-cleanup.py shared` to review that scope, with `--apply` to apply conservative formatting. Review template logic and whitespace-sensitive regions as well as the formatter results.
- Include a separate code-formatting check in final site reviews to catch older exceptions. Inspect rendered HTML as well as editable source; do not grade generated HTML as clean without reading it. Confirm template-only lines do not produce empty output lines.
- Build the affected site after cleanup. Verify that rendered wording, links, structure, spacing and layout remain unchanged, especially around inline links and templates.
- Default user feedback for a requested formatting cleanup is a brief before/after grade against this sheet, with build status and material exceptions. If no improvement was needed, say already clean. Base grades on actual checks; when a full pass is not verified, say so rather than inventing a grade. No separate report file unless requested.
- Formatting grades cover formatting only, not content, accessibility, SEO or overall functionality. Do not claim an entire site is clean after checking a few files.
- When an agreement changes, update this document rather than adding contradictory rules elsewhere. Unit reports record checks and exceptions; they are not alternative rule sheets.

- If another document conflicts with this sheet, flag the conflict rather than silently combining instructions. Resolve it with the user when the accepted decision is unclear. Once resolved, remove or update the obsolete instruction at its source so it cannot compete with this sheet again. Preserve historical records as history, clearly marked as superseded.
