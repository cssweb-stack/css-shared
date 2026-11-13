# Shared footer

The footer is rendered by `src/includes/layouts/branding/footer/footer.njk`, with
`subfooter.njk` for the legal text. Styling lives in `src/css/footer.css`, ordered
by surface, base links, layout, acronym, identity, contact, social, university
links, languages, and subfooter. Component media rules sit beside their component.

## Ownership of layout and spacing

| Responsibility | Owner |
| --- | --- |
| Shared max width and outside horizontal padding | `layout.css` → `.container` |
| Column widths, wrapping, horizontal gutters | Bootstrap row/col classes |
| Main content page-edge spacing | `layout.css` → `.site-main` / `--layout-content-spacing` |
| Upper footer top/bottom padding | `footer.css` → `.footer-inner`, using shared `--layout-section-spacing` |
| Desktop/phone stacked sidebar and footer group gaps | `layout.css` → shared last-excepted column rule, using `--layout-stack-gap: 1.5rem` |
| Desktop gap before the language row | `footer.css`, using shared `--layout-section-spacing` |
| Last element's bottom margin in unit-detail columns | Shared normalization in `layout.css` |
| Phone/tablet divider spacing | `footer.css` → half `--layout-section-spacing`, equal above/below |
| Identity/contact detail spacing | Footer-local variables on `.footer-unit-column` |
| Diagnostic overlays | `diagnostics.css`, toggle its import in `common.css` |

The footer does not redefine container width, Bootstrap column sizing, or page
content padding. Bootstrap `gx-0 gx-sm-5 gx-lg-5` is used for outer/nested rows:
zero horizontal gutter below 576px, 3rem from 576px. Continuous list column gaps
also use 3rem; these are internal list presentation, not another outer grid.

Shared section spacing is 2rem below 576px, 2.25rem at 576–1199.98px, and 3rem at
1200px+. The stack gap remains 1.5rem at all sizes where groups stack.

## Structure and breakpoints

One main `.container.footer-inner` contains a Bootstrap row:

- Unit block: `col-12 col-lg-3`.
- University links: `col-12 col-lg-9`.
- Languages: `col-12`, underneath both.

Within the unit block, acronym uses `col-12 col-sm-12 col-lg-12`;
identity/address and contact use `col-12 col-sm-6 col-lg-12`. At 576–991.98px,
the acronym occupies its own row, with identity/contact in equal halves beneath
and a 1.5rem row gap. This supersedes equal tablet thirds: fixed-size PUBA text
overflowed its third and overlapped the identity. Phones and desktop retain
stacked groups with a 1.5rem gap except after the last.

University links are one list: 2 visual columns below 576px, 3 above. Languages
are one list of 16 links: 2 columns below 576px, 3 at 576–1199.98px, and 8 from
1200px. Lists flow down each column before the next. All upper-footer text is
left aligned. Both dividers are visible below 992px and hidden at desktop;
spacing on each side is 16px on phones and 18px on tablets. Desktop row-gap uses shared section spacing: 2.25rem at 992–1199px and
3rem from 1200px. The background switches source at 1200px. No 525px/900px special layout
breakpoints or legacy language-band rules remain.

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
tablet acronym adjustments documented above. See `css-audit-2026-11-08.md` for
the current site-wide review.

The review preserves the approved SSRI design, organizes the stylesheet, removes
redundant focus/list/min-width rules, and replaces duplicate 1rem stack literals
with one shared layout token. Diagnostic extraction is complete; see `docs/diagnostics.md`. Header work remains separate.
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
