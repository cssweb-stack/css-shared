# SSRI URL comparison — November 12, 2026

Compared the supplied WordPress URL export against the current SSRI page destinations.

- 15 original URLs: 5 unchanged, 10 moved, 0 retired.
- All 14 current regular pages are accounted for; the custom 404 page is new.
- Ten confirmed replacements now use generated redirects; the 404 retains four general quick links. No redirect stub pages were created.

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

## RTRF reporting replacement

User confirmed the [College/SSRI Funding Levels dashboard](https://lookerstudio.google.com/reporting/3608bb1f-144f-463b-bcea-00fbf39fdfbc/page/p_m3uaggdjvc?s=vDHTIBnbeCM) replaces this
reporting. `/rtrf-fy2019/` now generates an immediate external redirect to it.
This supersedes the earlier retirement decision. No decisions remain.

## Saved inventory

- [Original export](../exports/ssri/original-urls-2026-11-12.json), preserved byte for byte.
- [Comparison CSV](../exports/ssri/url-comparison-2026-11-12.csv).
- [Comparison JSON](../exports/ssri/url-comparison-2026-11-12.json), including source checksum and per-URL status.

For another unit: preserve its original export, compare against built page URLs, classify each original URL, verify real replacement content, and populate only confirmed recovery links. Flag unresolved pages for a decision. A recovery list does not automatically redirect old URLs.

Local build and shared checks passed. Live hosting must still be checked after publication.
