# SSRI URL comparison — November 12, 2026

Compared the supplied WordPress URL export against the current SSRI page destinations.

- 15 original URLs: 5 unchanged, 9 moved, 1 unmatched.
- All 14 current regular pages are accounted for; the custom 404 page is new.
- Nine confirmed replacements now appear on the 404 page, plus four general quick links. No redirect stub pages were created.

## Confirmed moves

| Original path | Current path |
| --- | --- |
| `/privacy-policy/` | `/privacy.html` |
| `/grant-development/` | `/support/grant-development.html` |
| `/fiscal-compliance/` | `/support/fiscal-compliance.html` |
| `/research-services/` | `/support/research-services.html` |
| `/hcri/` | `/research/hcri.html` |
| `/tasi-phidc/` | `/research/tasi-phidc.html` |
| `/oenas/` | `/research/oenas.html` |
| `/ham/` | `/research/ham.html` |
| `/boilerplate/` | `/support/boilerplate.html` |

## One decision remains

The [RTRF FY2019 report](https://ssri.manoa.hawaii.edu/rtrf-fy2019/) has no matching current page. It contains historical Research and Training Revolving Fund financial tables. Decide whether to retain/archive that report or retire it. No replacement was invented, and it has not been marked retired.

## Saved inventory

- [Original export](../exports/ssri/original-urls-2026-11-12.json), preserved byte for byte.
- [Comparison CSV](../exports/ssri/url-comparison-2026-11-12.csv).
- [Comparison JSON](../exports/ssri/url-comparison-2026-11-12.json), including source checksum and per-URL status.

For another unit: preserve its original export, compare against built page URLs, classify each original URL, verify real replacement content, and populate only confirmed recovery links. Flag unresolved pages for a decision. A recovery list does not automatically redirect old URLs.

Local build and shared checks passed. Live hosting must still be checked after publication.
