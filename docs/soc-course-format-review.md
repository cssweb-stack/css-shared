# Sociology course-reference formatting review

## Completed formatting sweep

User authorized the sweep November 14, 2026. Checked all 59 local HTML sources
and searched shared SOC JSON for course text (no matching shared course references).
Changed nine HTML pages: inserted 57 missing title colons, standardized three
additional named-course prose references, changed two Honors code-to-description
separators to colons, removed three trailing BAM list commas and corrected S0C 300.
Removed 60 credit counts from the five research-area Related Courses lists.
All academic-page numeric credit annotations were preserved exactly.

Rescan: no confirmed named-course colon omissions remain. Four matcher candidates
are valid combined-lab slash notation already followed by a colon; three Alpha
designators also retain their source notation and colon. Code-only references
remain unchanged. Course-title discrepancies listed below remain unresolved and
unchanged; no official title chosen by inference.

SOC build/shared checks and diff whitespace checks passed. Source comparisons
verified unchanged HTML tags/attributes, links, template code and academic credit
annotations. No browser rerun for punctuation-only changes. Local only in soc and
css-shared; no commit, push or deployment for this sweep.

## Original scan baseline

November 14, 2026. Read-only scan of 59 local SOC HTML sources, focused on
course-title entries in list items plus contextual review of requirements and
faculty pages. No course text changed. This is not a catalog-title verification
or an exhaustive inventory of every reference in prose, tables or shared JSON.

## Established pattern and punctuation findings

Named courses use SUBJECT NUMBER: Course Title. Most inspected entries already
follow this. Code-only references in prerequisites and prose remain code-only.

Confirmed 57 course-title entries lacking a colon on five pages:

| Page under src/ | Missing colons |
| --- | ---: |
| about-soc/research-areas/crime-law-social-control.html | 17 |
| about-soc/research-areas/race-ethnicity-gender-class.html | 19 |
| undergraduate/bam.html | 11 |
| undergraduate/major/concentrations.html | 5 |
| undergraduate/minor/concentrations.html | 5 |

Examples: SOC 218 Introduction to Social Problems (3); SOC 413 Economy and
Society, (BAM list). The latter also has a trailing comma; other BAM entries
have similar punctuation. Honors has two code-to-description hyphens (SOC 100A
and SOC 300A), rather than course titles. Do not count these as missing-title
colons. That section also contains S0C 300, with a zero instead of O.

## Academic content differences requiring separate review

- SOC 332: Sociology of Law / Survey of Sociology of Law.
- SOC 333: Criminology / Survey of Criminology.
- SOC 335: Drugs and Society / Survey of Drugs and Society.
- SOC 357: Japanese Society and Culture / Sociology of Japan.
- SOC 413: Economy and Society / Analysis in Economy and Society.
- SOC 431: Advanced Criminology, Advanced Criminology & Juvenile Delinquency,
  Criminology and Juvenile Delinquency, Analysis in Criminology/Juvenile Delinquency.
- SOC 478: Analysis in Field Research Methods / Field Research Methods /
  Analysis in Field Research.
- SOC 318: usually Women and Social Policy, but Myungji Yang's teaching list
  says Sociology of Korea. This may be historical or an error; do not guess.

These are observed variants, not determinations of current official titles.
Some could be historical teaching titles or variable-topic offerings.

## Special cases and credits

- SOC 476L and SOC 605L coexist with abbreviated SOC 476/L and SOC 605/L.
- SOC 455/REL 452 is a cross-listed entry; preserve both subjects/numbers.
- SOC 725 (Alpha): Seminar in Race and Ethnicity appears on three faculty pages.
- Credit displays vary: omitted, (3), and (4 credits), with other valid values.
  Do not fill in missing credits or assume all lists require credit information.
- SOC 495: Topics in Sociology* retains an asterisk needing contextual review.

The preliminary matcher returned 534 course-like list candidates on 31 pages:
467 colon entries, 62 apparent no-colon entries, 3 Alpha entries and 2 dash
descriptions. Manual classification removed four combined-lab notations and one
HON 491 explanatory entry from the apparent no-colon count, leaving 57 confirmed
course-title omissions. Candidate totals are not comprehensive course counts.

## Next step

Standardize separators/spacing without changing course names, credits or codes,
then separately resolve academic-title discrepancies against approved sources.
Added this distinction to the standard text-review checklist/report template.
No content rewrite, browser check, site build or deployment for this read-only scan.
