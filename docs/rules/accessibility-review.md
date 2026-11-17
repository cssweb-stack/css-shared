# Accessibility review

This is the current accessibility run sheet for shared components and consuming
unit sites. Read it before an accessibility review or accessibility-related code
change. It combines existing project practices with selected GitHub accessibility
auditor guidance. It does not install another scanner, certify compliance, or
authorize redesigning the sites. Historical audit reports are evidence of past
checks, not competing rules or proof that the current site passes.

## Scope and decisions before changes

- Identify the unit, current pages, shared components, intended WCAG version/level
  and automated checks available. Keep the approved target; report extra AAA or
  best-practice findings separately. A scanner score is not a conformance claim.
- Read the actual pages and rendered components. Automated findings support
  editorial and interaction review; running a checker alone is not completion.
- Preserve approved content, UH branding, centralized data, grid rules, typography,
  image ownership, routes and local-server ownership. Fix reusable problems in
  shared sources, not duplicated unit overrides or generated output.
- Existing authorization covers clear, low-impact corrections within the requested
  review, such as repairing a broken label reference or accessible control name.
  Do not invent alt descriptions, academic facts or captions when meaning is unclear.
- Before significant changes to layout, column order, navigation, keyboard behavior,
  heading structure, fonts/colors, content, media, forms or shared component contracts,
  explain the finding, evidence, proposed change, affected sites and alternatives.
  Ask the user to decide and wait before making that dependent change. Continue
  independent read-only review and already-authorized minor fixes while waiting.
- Do not add CI jobs, tools, dependencies, analytics changes, publishing actions or
  portfolio-wide migrations merely because an external checklist suggests them.

## First use of this merged run sheet

1. Start with read-only review of the selected site and its shared components.
   Map new recommendations to existing rules before editing; do not sweep all sites.
2. Separate confirmed defects, items needing human judgment, optional enhancements
   and checklist conflicts. A tool warning is a finding to investigate, not an order
   to rewrite working code. Review any proposed false-positive dismissal individually.
3. For each significant proposed change, give the user a concise decision item:
   what fails, how it was observed, what would change, and its shared-site impact.
   Do not silently batch such changes into routine fixes.
4. If the new run sheet itself suggests breaking a sound project rule or makes a
   disproportionate demand, flag and resolve that conflict first. Amend the rule
   deliberately; do not bypass it or manufacture a site defect to satisfy it.
5. After authorized fixes, check the affected behavior and representative shared
   consumer. Report actual coverage and remaining decisions. Do not declare an
   untested first run complete because an automated score is high.

## Known deferred component

User decision, November 17, 2026: homepage academic-program/degree tiles are
known unfinished across all sites. Exclude their layout, clipping and text-sizing
remediation from current review passes; record the known limitation without
reinvestigating or blocking the unit review. Resume tile work only when the user
explicitly requests it. This is a development deferral, not an accessibility pass.

## Page structure and accessible names

- Use meaningful native HTML elements for navigation, main content, articles,
  sections, headers and footers. Do not wrap every block in a landmark or add
  redundant roles; use semantic elements where their meaning fits the content.
- Use one descriptive H1 per page as our project convention. Use a meaningful
  H2/H3/H4 hierarchy without skipping levels when nesting sections. Do not add
  redundant headings merely for styling or automatically restructure approved
  content to silence a heading heuristic. Review what the section actually contains.
- Confirm unique IDs and valid label/description references. Repeated landmarks
  should be distinguishable when needed; headings and link names should make sense
  in context. Preserve standard full-name contact/support H1 conventions.
- Every img needs an appropriate alt attribute. Informative images describe relevant
  information; image-only controls/links describe their action or destination.
  Decorative or redundant images use alt="". Existing linked portrait/name pairs
  can legitimately use empty portrait alt text. Do not add duplicate spoken labels.
- Image review is a required completion check, not just an attribute-presence test.
  For each distinct image usage, identify its purpose: informative, functional,
  decorative, or redundant with adjacent accessible text. Review both nonempty and
  empty alt values; record the purpose and reason for intentional emptiness in the
  review evidence. Reused components can share a documented decision only when
  their usage/context is the same. Missing alt is a defect, never an implicit empty
  alt decision. An automated checker cannot certify that a description is accurate.
- Example: the linked Pi Sigma Alpha logo conveys the organization/destination;
  alt="Pi Sigma Alpha" is appropriate. A decorative hero may use alt=""; a news
  photo communicating an event needs relevant descriptive text. If removing the
  image loses information or an action's name, do not classify it as decorative.
  Ask the user when meaning/purpose cannot be established, rather than guessing.
- Treat captions/credits as visible content distinct from alt text. User owns image
  selection; use supplied assets and ask about unclear meaning, never source a new
  image to satisfy an audit. Complex charts need an equivalent explanation of their
  information, not just a visual description.
- Icons with adjacent text are usually decorative. Icon-only controls need names.
  Links must convey their destination or action; avoid unexplained Click here labels.
- Prefer native buttons, links and visible form labels. Use ARIA only when native
  semantics are insufficient, with accurate names, roles and synchronized states.
  Do not add role=menu to an ordinary website navigation merely to enable arrows.

## Keyboard, focus and assistive technology

- Actually navigate affected interfaces with Tab/Shift+Tab, Enter and Space as
  appropriate. Use arrow keys/Escape where the component's interaction pattern calls
  for them. Verify operation, logical focus order, no keyboard traps and sensible
  focus restoration when a panel closes. Do not add positive tabindex to force order.
- Verify the skip link is discoverable and moves focus to the real main target.
  Preserve the existing main ID/tabindex pattern; the sample #main is not a required
  literal ID. Check sticky headers and overlays do not hide focused controls.
- Keep visible, distinguishable keyboard focus. Our approved shared default is a
  2 CSS pixel outline with a 3px offset, controlled by --focus-outline-width and
  --focus-outline-offset in accessibility.css. Shared component focus rules reuse
  these variables, with colors appropriate to their backgrounds. Check the same
  standard on each site; report any intentional exception and its reason rather
  than accepting an unexplained component default. Thickness alone does not prove
  visibility/contrast or WCAG conformance; do not impose optional AAA redesigns.
- Check controls' accessible names and states, including aria-expanded for actual
  disclosures. Avoid contradictory hidden content and stale expanded states.
- Test a representative real task and unique interaction patterns with an actual
  screen reader, normally VoiceOver on Mac; NVDA is an alternative when available.
  Check landmarks/headings, reading order, links, controls and announcements. A DOM
  inspection, axe result or browser accessibility tree alone is not a screen-reader
  session. If unavailable, report this coverage as not tested and arrange follow-up.
- Announce relevant asynchronous status messages without unnecessary interruption.
  Prefer native/suitable status semantics or a targeted polite live region; reserve
  assertive alerts for genuinely urgent messages. Do not announce every content
  change, wrap whole pages in aria-live, or duplicate announcements/focus movement.

## Visual use, resizing and reflow

- Check normal text contrast at 4.5:1 and large text at 3:1. Large means at least
  18pt/24 CSS px regular or 14pt/about 18.67 CSS px bold; do not assume our 550-weight
  emphasis automatically qualifies for the bold exception. Check relevant states,
  actual backgrounds, opacity and overlays rather than source colors alone.
- Check necessary control/graphic information at 3:1 against adjacent colors where
  WCAG non-text contrast applies; account for its exceptions. Do not apply this to
  every decorative graphic or use it to recolor the brand without a decision.
- Information must not depend on color alone. Use suitable text, shapes, patterns or
  other cues where needed; not every status needs all of icon + color + text.
- Check text enlarged to 200%, plus reflow at 320 CSS px equivalent width (for
  example, 1280px at 400% zoom). These are distinct checks. Preserve information,
  controls and reading order. Necessary two-dimensional content such as maps/data
  tables can have scoped exceptions; ordinary text still needs usable wrapping.
- Check prescribed text-spacing overrides: line height 1.5 times font size,
  paragraph spacing 2 times font size, letter spacing .12em and word spacing .16em.
  Check clipping/overlap/hidden controls, not whether the design looks identical.
- Review target sizes/spacing for the selected WCAG version, reduced-motion behavior
  where relevant, and touch operation for interactive patterns. Existing device
  complaints warrant targeted checks, not an exhaustive viewport cross-product.
- Temporary red/pink layout guides are diagnostic overlays, not the site's intended
  palette. Assess published styling without them using a temporary test setup;
  preserve the user's actual guide setting and report how it was excluded.

## Forms, media and third-party content

- Prefer visible label elements associated with inputs; placeholders are not labels.
  Group related controls with fieldset/legend when appropriate. Preserve logical
  reading order; do not mandate above/left label placement where a different valid
  layout is already clear and accessible.
- Use native required for native controls when appropriate, and a visible required
  indication/instructions. Use aria-required where needed for custom controls;
  do not blindly duplicate native required on every field.
- Identify errors in text, associate relevant help/errors with aria-describedby,
  retain existing description references and set aria-invalid only when invalid.
  Make errors discoverable without color alone; check correction/submission flow.
  Do not force immediate validation or move focus on every keystroke.
- Video iframes need meaningful titles and usable keyboard controls. Check needed
  captions, transcripts/audio description according to the media and review target.
  A caption-query parameter or Analytics API parameter does not prove captions exist
  or are accurate. Report unavailable media review separately; do not invent captions.
- Review hosted maps, video players, externally linked forms and documents to the
  extent possible. Distinguish the accessible host iframe from the external content.
  Excluded third-party interfaces/PDFs are not passes; flag ownership and follow-up.

## Tools, evidence and stopping point

- Inventory all current pages. Run the existing axe-based/structural checks where
  available, with the chosen target and explicit exclusions. Review the findings
  and edit confirmed problems; tool output alone is not the deliverable.
- Siteimprove supplies a broad automated site scan, not a replacement for manual
  checks. Lighthouse may help investigate a gap but is not a required duplicate
  run on every page. Do not install CI/dependencies or build a new audit harness
  automatically. Reuse existing tools and stop when relevant checks pass.
- Inspect page-specific content and shared interaction/layout variants. Test shared
  behavior on representative pages, and expand only for a distinct pattern, failure,
  changed component or unresolved concern. Preserve the existing cost/stopping rule.
- Run the affected build after substantive source changes. Recheck the actual defect
  and likely regressions; do not repeat the whole audit after every small correction.
- Report: scope/pages, tools, manual tasks actually performed, corrections, remaining
  failures, items not tested and user decisions needed. Keep confirmed failures,
  tool-incomplete results, intentional exceptions and optional enhancements distinct.
  State local/committed/pushed/deployed status accurately. A sampled pass is not a
  whole-site pass, and 100/100 does not prove full WCAG compliance.

## Adaptations from the GitHub example

- Extended scope beyond an HTML-only applyTo glob: shared Nunjucks templates,
  CSS/JavaScript behavior, central data and rendered output also affect accessibility.
  Do not install the supplied Copilot front matter as a second rule system.
- Kept keyboard/semantic/contrast/screen-reader checks, qualified ARIA, decorative
  images, forms, live regions and focus guidance as described above. Added existing
  project protections, media review, text spacing and 320px reflow coverage.
- Rejected mandatory explanatory comments on every ARIA/semantic choice. Keep our
  concise code/comment style; explain non-obvious decisions only where useful.
- Did not adopt automatic axe CI installation or mandatory axe + Lighthouse duplicate
  sweeps. This checklist authorizes review, not new workflow/dependency changes.
- Significant-change consultation in this sheet supersedes earlier blanket wording
  allowing shared accessibility corrections without distinguishing their impact.

References: [GitHub example](https://docs.github.com/en/copilot/tutorials/customization-library/custom-instructions/accessibility-auditor),
[W3C ARIA principles](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/),
[decorative images](https://www.w3.org/WAI/tutorials/images/decorative/),
[focus appearance](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html),
[reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html),
[status messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html),
and [WCAG 2.2 quick reference](https://www.w3.org/WAI/WCAG22/quickref/).
