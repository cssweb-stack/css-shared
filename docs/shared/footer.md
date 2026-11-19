# Shared footer

The footer is rendered by `src/includes/layouts/branding/footer/footer.njk`, with
`subfooter.njk` for the legal text. Styling lives in `src/css/footer.css`, ordered
by surface, base links, layout, acronym, identity, contact, social, university
links, languages, and subfooter. Component media rules sit beside their component.

## Selectable footer templates

The four-column template is the default for every site using the shared footer.
Set `site.footerTemplate` to `classic` to select the classic template explicitly.
Both share unit-details.njk, data and subfooter.

The optional footer has one university-link ul and one language ul. On mobile,
each has two equal columns. The option uses one --footer-gap: 48px for
column gaps and spacing between major rows, superseding shared responsive gaps
for this footer option only. University links flow down columns
using CSS grid auto-flow: column; --footer-link-rows-mobile: 11 gives 11/11.
From 1200px, department details occupy one of four equal cells and the university
list spans the other three. --footer-link-rows-desktop: 8 gives 8/8/6 links.
Those two central CSS variables control the counts without reordering HTML or
creating separate lists. Adjust counts with the total link count in mind.
Languages use CSS column flow: two columns below 1200px, eight above (two rows
for 16 languages). Every second language column aligns with an upper four-column
edge because both layouts use the same overall width and 48px gap. Source order remains unchanged.
This supersedes the experimental four separate lists and one-column phone lists.

## Editable typography and detail groups

Acronym font sizes are three adjacent media rules: phone 4rem, tablet 4.667rem,
desktop 4rem. These are fixed values with no JavaScript fitting. Native text-box
trimming removes leading where supported. Older browsers may retain that leading.
The acronym uses solid `--footer-abbreviation: #ffffff`, no text opacity, and
no text shadow (removed at user request to isolate the contrast-review warning).

The identity column has three groups with a single 0.625rem inter-group gap:

- Unit name: 1.0625rem / weight 600.
- College/university links: identical white 0.9375rem / weight 400.
- Address: separate paragraphs, 0.875rem / weight 300.

Parent links and address share a 0.25rem detail gap and 1.6 line height. Phone and
email share the parent-link size, a 0.5rem internal gap, and 1.25rem after their
group. Their icon spans alone have opacity 0.8. Webmaster/privacy remains 0.75rem.

Local controls on `.footer-unit-column`:

- `--footer-unit-group-gap: 1.25rem`.
- `--footer-unit-identity-gap`: half that value.
- `--footer-detail-gap: 0.25rem`.
- `--footer-secondary-font-size: 0.9375rem`.

Social accounts come from each unit's `social.json`; blank URLs are omitted.
The existing compact icon sizes, wrapping, labels and focus treatment are retained.

## Subfooter

The subfooter outer has no margin/padding; its inner container has 1rem top/bottom
padding. A standard row/col-12 contains centered legal text, the explicit alignment
exception. Pink diagnostic borders on the main footer/subfooter inners meet with
no outside gap. Legal links keep inline wrapping and underlines.

## Configuration

Shared defaults are in `src/data/uh/footer.json` and language links in
`src/data/uh/languages.json`. Per-unit identity/contact/social data is loaded by
the existing shared loader.

- University links: default flat `footerLinks`; unit override `footer.links`.
  Legacy grouped `footer.columns` overrides are flattened for compatibility.
- Parent college/university links: `src/data/common/links.json`.
- Privacy and webmaster: `uh.footer.privacy` / `uh.footer.webmaster`.
- Backgrounds: unit `footer.background.desktopTablet` / `mobile`, falling back to
  shared values. Only public image URLs are emitted.
- Former `footer.language.showHeading` / `presentation` settings are inactive.
  The integrated language list has one presentation, no dark band or visible
  heading. Its navigation retains an accessible label and each link's lang tag.

## Earlier footer-only cleanup review — November 8, 2026

This records the earlier before/after cleanup, before the later spacing and
tablet acronym adjustments documented above. See `../reports/css-audit-2026-11-08.md` for
the current site-wide review.

The review preserves the approved SSRI design, organizes the stylesheet, removes
redundant focus/list/min-width rules, and replaces duplicate 1rem stack literals
with one shared layout token. Diagnostic extraction is complete; see `docs/shared/diagnostics.md`. Header work remains separate.
Validation results and any existing fixed-acronym fit limits are recorded in the
accompanying review export. Browser measurements use local Chrome and actual
Inter fonts; actual Safari/device review remains separate.

Review result: 168 paired before/after cases across 14 footer specimens and
12 widths, comparing 21,264 elements plus divider/background pseudo-elements
and keyboard-focus styling. No computed-style or geometry differences were
found; no footer overflow occurred. SSRI passed all tested acronym widths.
Existing fixed-acronym limits: ANTH, DURP, ECON, POLS, PUBA and WGSS at 576px;
WGSS also at 992px. These were identical before/after and were not restyled.
Results: `exports/footer-cleanup-review-2026-11-08.json`.

## Alternative unit-information grouping

Four-column option groups acronym, identity and college/university links
in the summary; address, phone/email, social and policy links in the other. These sit
side-by-side at576–1199px and stack otherwise. Acronym line-height1 and reduced
summary gap remove excess leading. The shared checker allows line-height 1 only
for this four-column display acronym. Policy links finish the contact group.
Classic structure stays unchanged; shared address/policy partials prevent copies.

Latest grouping: policy links follow social links at the bottom. Logical information groups use one --footer-info-gap, equal to the existing
--footer-unit-identity-gap, between department, parents, address, contact, social
and policy groups. This supersedes the temporary zero stacked gap. Social icons have a visible Social: label for one
account, Socials: for multiple; the group is omitted when no accounts exist.

Both optional footer sections sit in one standard Bootstrap row with two stacked
col-12 wrappers inside the shared container, matching hero-credit/subfooter
outer alignment. Internal four-column and language-list arrangements stay intact.
