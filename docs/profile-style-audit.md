# Shared profile typography audit

November 12, 2026 (Pacific/Honolulu). Local implementation and browser checks complete.

## Final contract

| Content | Size at default root settings | Weight |
| --- | --- | --- |
| Normal paragraph | Shared body token, currently 1.125rem / 18px | 400 |
| Primary academic/job title | 1rem / 16px | 600 |
| Administrative subtitle/role | 1rem / 16px | 500 |
| Person name heading | 1.25rem / 20px | 600 |

Title and role sizes do not change at breakpoints. Names remain larger than title
lines. Regular page copy never exceeds 600; decorative footer acronyms (800) and
404 marks (900) are explicit graphic exceptions.
This supersedes the immediately preceding academic-weight-500 adjustment and the
older administrative-role size of 1rem.

## Ownership and findings

- `src/css/typography.css` owns the paragraph-size token and normal paragraph
  weight. `src/css/fonts.css` supplies Inter variable weights 100–900.
- `src/css/profile.css` is the only shared profile stylesheet. The problem was
  scattered rules inside that file, not different SOC templates: administrative
  role typography was declared twice, both explicitly smaller than paragraph text.
- Consolidated name/title/role typography near the start of profile.css, with named
  profile tokens. Titles and roles share one 1rem token rather than
  repeating independent size values. Preserved existing spacing and name treatment.
- Removed duplicate role declarations, an ineffective generic name-size rule,
  and obsolete anchor-name/chair-message typography variants with no source
  consumers identified in the workspace scan.
- Contact and faculty cards use profile-card.njk → profile-identity.njk; individual
  biographies use the same identity include through profile-sidebar.njk. No local
  title overrides were found in the inspected consuming source pages/styles.
- `scripts/check-shared.mjs` now enforces the three canonical title/role typography
  selectors in profile.css. Competing declarations elsewhere in shared CSS and
  repeated rules fail the shared check. Edit the tokens instead of adding overrides.
  This guard does not inspect future inline CSS or every consuming repository.

## Verification

SOC, PUBA, SSRI, PSY, POLS, GEO, and SCI builds passed. Shared checks and the
existing SOC 50-page/POLS 51-page verification passed. Negative checks in temporary
fixtures confirmed that duplicate title weights and competing stylesheet role-size
rules are rejected by the new guard.

Chrome 157 checked computed styles on 16 representative pages across those seven
sites, including contact cards, directories, and individual biography sidebars.
At 390px, 1100px, and 1800px (48 page/width cases), every rendered primary title
matched 16px/600, every role matched 16px/500, names retained
20px/600, and no horizontal page overflow was observed. These were local builds;
no live deployment or Siteimprove re-scan is claimed.

Evidence: [computed styles](../exports/accessibility/profile-typography-2026-11-12.json).
