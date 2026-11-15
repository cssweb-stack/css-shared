# Ethnic Studies text and code cleanup

November 14, 2026. Initial editorial and formatting pass completed locally, with two coverage gaps found afterward. No required user decision remains: the user supplied the catalog titles for ES 318 and ES 370.

## Scope and editorial review

Reviewed all 27 current pages, ES people/associated-faculty/advising/navigation records, and the unit-owned policy appendix. Recast nine institutional paragraphs across the homepage, faculty introduction, Why Study, history, oral history center, student association, Support and Contact into consistent third-person prose. The homepage retains the approved bilingual welcome and the department, college and university names, while avoiding repeated “the department” sentence openings. Reduced unsupported promotional phrasing without adding programs, outcomes, services or employment promises.

Nine authored faculty biographies retain their first-person voice and wording, apart from explicit whitespace/punctuation and Hawaiian-character corrections. The three attributed, dated policy statements retain their original prose and first-person stance. Functional labels such as Find us on Facebook and the approved homepage question are intentional exceptions to third-person narrative. Did not rewrite academic requirements or official learning-outcome wording.

## Measured corrections

| Correction | Count | Example |
|---|---:|---|
| Institutional paragraphs edited | 9 | Our faculty brings… → Ethnic Studies faculty bring… |
| Accidental nonbreaking spaces | 23 | Ordinary prose now wraps normally |
| Hawaiʻi character variants | 19 | Hawai‘i → Hawaiʻi |
| Other known Hawaiian-character variants | 7 | O‘ahu → Oʻahu; ʻAha/Kūaliʻi/Waialeʻe character fixes |
| University-name spelling | 1 | University of Hawaii at Mānoa → University of Hawaiʻi at Mānoa |
| Repeated spaces | 2 | Removed accidental doubled prose spaces |
| Spacing before inline punctuation | 7 | Closing link followed by a detached period → attached period |
| Named-course separator corrections | 54 | ES 101 - … → ES 101: …; added missing cross-listed separator |
| Topic-marker placement | 2 | ES 455: (B) … → ES 455 (B): … |
| Italic course notes standardized | 3 | Parenthetical substitution/credit-limit notes |
| Career-category labels | 8 | Italic label and dash → bold label and colon |
| BAM benefit labels | 3 | Save money. → Save money: |
| Fund-link labels | 4 | Linked fund name and dash → bold linked name and colon |

Counts are individual measured operations. Earlier paragraph replacements absorbed additional source whitespace, so these are not a sum of every character difference. The formatting-stage changed-file count below is separate.

Applied the user-confirmed course titles on both academic pages: ES 318: Asian America and ES 370: Literatures of Hawaiʻi. Kept all course codes, cross-listings, credits, topic letters and grade requirements; before/after code and credit-token counts match. A final structural scan confirmed all 106 named course-list items use colon-space separators. The former title differences are resolved. Links supplied by the user: [ES 318 catalog](https://catalog.manoa.hawaii.edu/preview_course_nopop.php?catoid=4&coid=70179) and [ES 370 catalog](https://catalog.manoa.hawaii.edu/preview_course_nopop.php?catoid=4&coid=70191).

Removed the unused SLOs parenthetical abbreviation from the outcomes introduction. Corrected ES homepage/nav BAM labels to generic bachelor’s/master’s wording or BAM Pathways, since the actual graduate routes are MEd/MPA rather than MA. Retained established branding/credential acronyms and the full names in page H1s.

No retired intro classes, empty paragraphs or heading bold/italic wrappers required removal. No role-based email rerouting was needed. No obsolete links were found by the shared replacement-registry scan.

## Preserved and deferred

- Willy Kauai is a personal name, not an automatically correctable geographic reference. Preserved its supplied spelling; it is the mechanical scan’s sole remaining diacritic candidate.
- Authored bio/book/publication typography and course-title punctuation are distinct from institutional prose separators. Preserved them, including meaningful hyphens and original course-title dashes. Official outcome wording/assessment parentheticals remain for the unit to revise, rather than silently rewriting requirements.
- BA scope of the relocated outcomes, BAM application timing and pathway-specific eligibility, and the certificate’s original accreditation/online-approval wording still warrant unit confirmation. These are source-content ownership observations, not blocking copy decisions or independently verified current requirements.
- “E komo mai — Welcome to…” retains the user-approved em dash. General run-in explanatory labels use bold plus colon.
- No original WordPress XML, source-preservation snapshot, review workbook or user Excel lock file was edited.

## Source formatting

Reviewed 28 editable HTML/Nunjucks sources: 27 ES pages and its shared policy appendix. Twelve needed formatting changes. Source is flush-left with no blank lines, structural wrappers on individual lines, list wrappers/items on consecutive lines, and inline links/emphasis/punctuation kept with their text. Front matter and whitespace-sensitive code are protected. Shared generic templates, JSON indentation, generated HTML and vendor code were not swept.

The new report-only-by-default `scripts/code-cleanup.py` asserts parsed source-event equivalence before writing. After applying and rebuilding, compared parsed rendered tags, attributes and text with the pre-format build: all 27 outputs are identical apart from insignificant source whitespace. A second formatter run proposes zero edits.

## Verification and status

- ES build and 27-page verifier passed, including nine faculty biographies and 21 original-source bodies with explicit reviewed transformations.
- All source page href/src destinations retained during editorial cleanup. All nine authored biography word streams match after the approved character normalization. Course-code/credit counts match on Certificate and BA.
- Standard text rescan proposes zero patches; one personal-name observation remains. Removed the tool’s obsolete em-dash-spacing rewrite so it follows the current documented rule.
- Original evidence remains intact. `../es/reference/editorial-text-replacements.json` records the exact nine-paragraph/node replacements used by the preservation verifier; narrow character/course/label normalizations are explicit in the verifier.
- Shared checker and whitespace checks passed. Accessibility and SEO results are recorded in the [final review](es-final-review-2026-11-14.md).

Evidence: [text counts and preservation](../exports/es/ES-text-cleanup-2026-11-14.json), [code formatting](../exports/es/ES-code-cleanup-2026-11-14.json).

Changes are local in `../es` and `css-shared`. Not committed, pushed or deployed by this pass.

## Follow-up: editorial coverage gaps

The initial pass left the Courses H1 as ES Courses and retained a shared-template hyphen between associated faculty names/contact details and research descriptions. Neither was an approved exception. The source-formatting pass covered unit pages and the ES policy appendix, not all shared templates; the SEO audit recorded the H1 without rejecting its acronym. Zero proposed mechanical text patches did not establish full editorial consistency.

Corrected Courses to Ethnic Studies Courses and changed the shared associated-faculty description separator to colon-space. Added rendered-output assertions to the ES verifier for that H1 and all 13 associated-faculty descriptions. The shared template correction applies to its other consuming sites when rebuilt. Earlier reports remain evidence of checks actually run, not proof every editorial rule was enforced.
