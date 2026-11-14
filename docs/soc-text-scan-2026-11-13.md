# Sociology whole-site text scan

November 13, 2026 (Pacific/Honolulu). Complete with limitations below.
No response required tonight. Scan/report only; no source copy changed.

Follow-up: the user contacted Le Lin about the incomplete paragraph on November
13; a reply may arrive November 14. Keep the supplied copy until his wording arrives.

## Scope and results

Scanned all 59 current HTML sources and 15 shared SOC JSON files with the standard
text tool. Built the site and extracted text from all 67 generated HTML documents
(including eight migration redirects) so shared/generated text is retained in the
review artifact. This supersedes the old 50-page scope for this scan; the earlier
cleanup report remains a historical record. This is a text review, not factual
verification of academic requirements or a comprehensive language spellcheck.

- Zero proposed mechanical patches: no accidental nonbreaking spaces, repeated
  prose spaces, wrong apostrophe variants recognized by the tool, em-dash spacing
  corrections, invisible characters, retired intro classes or empty paragraphs.
- Zero embedded bold/italic heading wrappers; zero adjacent repeated-word matches
  in the source-text screen.
- Four automated diacritic candidates: three visible occurrences and one permalink
  false positive. Manual review found two additional prime-character occurrences.
- All corrections remain unapplied in this scan, including the items below.

## Concrete text findings

| Page | Finding | Suggested follow-up |
| --- | --- | --- |
| Faculty / Le Lin, line 36 | `Higher Education</em>and` renders as “Higher Educationand” | Insert a space after the closing emphasis tag. |
| Faculty / Le Lin, line 36 | Final sentence ends “Society for the Advancement of Socio-Economic” | Obtain the complete original wording; do not invent the missing ending. |
| Hörmann Prize, line 47 | `Hawai′i</em>or` renders as “Hawai′ior” | Insert a space after the closing emphasis tag. |
| Hörmann Prize, lines 13 and 47 | Two uses of U+2032 prime in `Hawai′i` | Geographic prose should use `Hawaiʻi`; review the journal’s official title separately. The automated apostrophe check misses this character. |
| Faculty / Wei Zhang, line 10 | Two uses of `Hawaii` in geographic research prose | Candidates for `Hawaiʻi`; preserved for review. |
| Academic Planning, line 40 | `Manoa Political Internships` | Verify the official program label before changing its diacritics. |
| Asia/Pacific research area, line 13 | “criminal justice” appears twice in the research-topic enumeration | Consider removing the duplicate after editorial review. |
| MA / Thesis, line 33 | Paragraph ends “provide it to the department” without final punctuation | Add a final period during cleanup. |
| Home, line 23 | “faculty - both in research and teaching -” | Sentence separators are candidates for spaced em dashes; no blanket hyphen replacement. |

The `hawaii` permalink candidate is an identifier: preserve its URL unchanged.
Academic Planning also retains hyphen separators after bold list labels; review
these as list punctuation rather than converting them automatically.

## TMS and academic naming

Only Graduate Course Categories uses TMS: two occurrences, at lines 13 and 51.
Its first use defines “Theory, Methods, Statistics (TMS)”; it is not undefined,
but lacks the agreed full wording’s “and.” Recommend “Theory, Methods, and
Statistics (TMS).” MA/PhD requirements and timelines generally spell the categories
out. Preserve “or” where it expresses a choice of course category.

Department naming variants include shared unit name “Department of Sociology,”
“Sociology Department” on Student Learning Outcomes, “our department” on Research
Areas, and “our Department” on Hörmann Prize. Full official names and generic
references need different treatment; no global capitalization rule was applied.

Degree variants include “Major (BA)” in navigation/H1, “Sociology BA” on Major/BAM,
“BA in Sociology” on Major/Concentrations/Student Learning Outcomes, “MA in
Sociology” and “PhD in Sociology” on Why Study, “Master’s (MA)” and “Doctorate
(PhD)” in degree-page H1s, and “MA degree in Sociology” / “PhD degree in Sociology”
in learning-outcome introductions. Faculty education credentials are a separate
context and should retain their supplied names.

Proposed convention for later approval: retain compact navigation/H1 labels;
prefer “BA in Sociology,” “MA in Sociology,” and “PhD in Sociology” on first formal
prose reference, then use the short degree/program name. Use “Department of
Sociology” for the official name and lowercase “the department” generically.
These are recommendations, not accepted project rules.

## Voice review

Institutional copy mixes third-person descriptions with first-person plural and
occasional direct address. Examples for later editorial review:

- Home: “You will find” / “our interconnected world.”
- Why Study: “Our sociology undergraduate program” / “We offer.”
- Applications & Admissions: “We do not accept Spring admissions” and “our program”
  alongside “Applicants must.”
- Honors Track: “our most talented” and “We recommend” alongside “students.”
- Research Areas and its five detail pages: “our faculty,” “we explore,” and
  “our focus” alongside descriptions of faculty and concentrations.
- Faculty directory: “our faculty”; Contact: “We are open”; News & Events:
  “our Twitter/X account”; Hörmann Prize: “our Department.”

Faculty first-person autobiographies/research statements are intentional personal
voice and were kept separate from institutional copy. The Alpha Kappa Delta
source title “Our Purpose” is an attributed title, not an institutional voice error.
Shared privacy and service instructions may reasonably address the visitor.
No pronouns or capitalization were rewritten; no global voice has been approved.

## Preservation, checks and next work

- `python3 scripts/text-cleanup.py soc`: completed, zero patches.
- Source screens: TMS, naming, voice, inline emphasis spacing, repeated words,
  placeholder/encoding markers; generated whole-site text extraction completed.
- `npm run build` in `../soc`: passed (59 generated files plus copied assets).
- `npm run verify` in `../soc`: failed before completion because its inventory
  references missing `src/graduate/gssa.html` after the Student Organizations move.
  This is a stale checker limitation, not evidence of a failed site build. The
  remainder of that verifier was not completed; update its migration inventory
  before the final verification pass.
- No links, HTML attributes, table structure, academic rules, original exports,
  portraits or shared content were changed. Build output is generated locally.
- Placeholder meta descriptions remain widespread and intentionally untouched;
  address them in the separately requested SEO review.
- Accessibility, SEO, live Open Graph diagnosis and final launch scans remain
  subsequent tasks; this pass does not establish whether GitHub/cache delay is
  responsible for the reported Open Graph problem.

Artifacts: [measured findings](../exports/soc/text-scan-2026-11-13.json) and
[complete rendered text](../exports/soc/rendered-text-2026-11-13.txt).

Repository to commit/push: `css-shared` (report, artifacts, handoff). `soc` source
unchanged. Local only; no commit, push, deployment or remote-sync check performed.
