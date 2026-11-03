# College of Social Sciences website standards

These standards govern this authoritative shared repository and reusable components
consumed by GEO, SOC, WGSS, and other college websites. The GIS Certificate page in
`../geo/src/undergraduate/gis-certificate.html` is the reference implementation.
Apply the same standards to all future GEO page work, not just that page.

## HTML and component standards

- Keep HTML as simple and semantic as possible. H1, H2, H3, paragraphs, and lists
  have no classes unless a reusable role or necessary behavior requires one.
- Use `.tagline` for taglines and `.intro` for introductory paragraphs.
- Use `.callout` for common callout structure, padding, and spacing. Use
  `.callout-green`, `.callout-blue`, and `.callout-gold` for colors; color
  modifiers must not own layout or spacing.
- Use `.info-note`, `.text-note`, `.text-accent`, and `.action-link` only where
  their treatments are needed. `.info-note` is a paragraph with an automatic
  decorative icon; `.text-note` is an inline span.
- Use `.media-row` for every standard two-column photo or icon row. Its shared
  rule owns the 189px desktop left column, remaining-width right column, gap,
  top alignment, bottom spacing, and responsive stacking. Do not create
  page-specific grid variants or competing margin/width rules.
- Use `.grid-photo` only for image border/shadow treatment. Image sizing and
  aspect ratio belong to the shared grid structure. Preserve load-based fade-in
  and reduced-motion behavior. People/profile photos retain their own treatments.
- Retain the right-column element required to group its heading and content;
  omit redundant outer course/list wrappers and presentation-only classes.
- Do not introduce unnecessary IDs, spans, wrappers, or specialized classes.
  Preserve semantic labels, referenced IDs, accessible names, meaningful image
  alternatives, email/telephone links, and keyboard focus behavior.
- Preserve approved content, visual design, and responsive behavior. All text,
  including headings, controls, and generated text, must have line-height >= 1.5.
  Preserve larger values. Optical top trimming must not reduce multiline leading.

## Authoritative CSS and dependency cleanup

- Shared content/component CSS is authoritative in `src/common.css`; the shared
  site shell belongs in `src/shell.css`. Never edit generated copies in consumers.
- Each common component property has one authoritative declaration. Correct or
  consolidate the existing rule rather than adding another override. Prefer
  low-specificity semantic/structural selectors to classes on every text element.
- Every HTML cleanup includes its corresponding CSS cleanup. For each removed
  class, find its definition, every consumer, related overrides, and media rules.
  Move necessary styling into the approved shared component, then remove rules
  that are no longer used anywhere.
- Before deleting shared selectors, search GEO, SOC, WGSS, shared templates,
  JavaScript/data sources, and live style-guide examples. Distinguish owned source
  from generated shared copies and generated HTML; `rg` may omit ignored files.
- When consumers outside the task still need an old name, retain an explicitly
  documented compatibility selector grouped with the canonical rule. Do not
  duplicate declarations or silently break consumers. Remove that alias after
  its last consumer is migrated.
- Do not replace empty spacers with new spacers, inline styles, or site-specific
  overrides. Reuse shared component spacing.

## General lessons for subsequent cleanups

- A simple row needs a container, a visual, and one right-column grouping element.
  Style its plain heading and paragraphs through the shared structural rules;
  removing a text class must not silently replace compact component typography
  with a different global heading size, weight, or margin.
- Minimal markup is purposeful markup, not a zero-class or zero-span target.
  Keep the label span inside `.action-link` to isolate its underline from the
  generated chevron. Keep IDs used by `aria-labelledby`, fragments, or scripts.
- When consolidating selectors, compare specificity as well as declarations.
  Last-child resets can be necessary because a nested list has a stronger spacing
  rule. Group necessary legacy selectors into the authoritative declaration
  instead of discarding a reset or appending another override.
- New and cleaned pages use only canonical names. A compatibility alias exists
  for an unmigrated consumer, not as an alternative naming standard. Remove it
  once searches and rendered checks confirm its final consumer is gone.

## Verification and reporting

- Run `npm run check` here. Synchronize and build the affected site with its
  existing workflow; GEO uses `npm run shared:sync` and `npm run build`.
- Inspect generated HTML and compare computed styles at desktop and mobile widths.
  Confirm typography, spacing, image treatment, link destinations, accessible
  references, and missing-field behavior. For a grid-spacing change, verify all
  standard rows respond to editing the single shared bottom-margin declaration.
- Read-only inspections of sibling consumers are expected; avoid unrelated edits.
  Do not change macOS settings or run cleanup automatically during builds.
- Never commit or push automatically. A successful build does not publish changes.
- At the end of every coding task, check Git status and local commits ahead of
  upstream in css-shared, geo, soc, wgss, and style-guide. Report only repositories
  requiring action, shared first; distinguish task changes from pre-existing work.
  End with `Commit → Push origin:` and a numbered list of pending repositories,
  indicating COMMIT & PUSH for local changes or PUSH for commits awaiting push.
