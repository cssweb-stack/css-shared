# Policies and Procedures comparison draft

One shared content file: src/includes/pages/policies-procedures.njk. It contains
separate Public Administration and Anthropology sections preserved for comparison,
plus an In progress notice. This is not yet a finalized universal policy statement.

PUBA and ANTH each render it at /policies-procedures.html. The optional shared
site-settings.json policiesProceduresUrl enables the footer link after Privacy
Policy, separated by a middle dot. Other units are not opted in during review.

Review locally at http://localhost:8084/policies-procedures.html for PUBA, or its
GitHub preview after publishing. Edit the shared body once to update both units.
No need to resend the original policy pages; their content is already saved.

Next: compare overlapping sections, validate institutional links and separate
unit-specific statements before approving universal wording. Do not silently
rewrite policy claims. No redirects activated for this draft.

## Consolidated working set (November 12)

Added seven H2 topics above the untouched PUBA/ANTH reference sections. Single
destination links moved into headings; Academic Grievances retains two body links.
The working set remains under the In progress notice, not institutional approval.
The Anthropology-specific race/racism statement stays in its source section, not
promoted to a universal policy.

Official links reviewed: old EEO policies URL redirects to current Institutional
Equity EEO policy collection; use that collection without inventing an additional
AA policy. Tobacco-free guidance covers the campus prohibition; older EP 10.102
page is also available but not duplicated in the working set.
Graduate grievance URL in source is broken; new set uses Graduate Student Complaint.
Registrar source URL redirects to its homepage; new set links directly to FERPA
Policies. Faculty responsibility heading links directly to current guidance; student
responsibility heading links to verified academic-grievance hub containing that
resource. Original links remain below for comparison. No substantive legal review
is claimed.

## Reference reduction

User approved removal of the PUBA reference section and duplicated Anthropology
faculty/student responsibilities, grievances, conduct, records and tobacco sections.
Below the consolidated set, only Anthropology's position statement and EEO/AA
reference remain for further comparison. Earlier untouched-reference notes above
describe the previous stage.

## EEO terminology standardized

Use Equal Employment Opportunity (EEO), matching UH Office of Institutional
Equity's current public heading (https://hawaii.edu/equity/eeo/index.php). Keep the
consolidated linked EEO entry; removed the duplicate Anthropology EEO/AA reference.
This is a display-label decision, not a claim that affirmative action requirements
are identical to EEO or that all affirmative action obligations have ended.
Only Anthropology's position statement remains below the consolidated set.

## Current architecture: shared core plus optional unit appendix

The common body now includes Academic Integrity and Plagiarism and Consensual
Relationships (EP 1.203), with linked H2s and short general summaries. Original
POLS penalties/graduate requirements were not imported. The public catalog
academic-integrity URL returned 403 to the research browser; link retained from
the supplied document, with content verification limited to search results.

Anthropology's statement moved verbatim into shared
src/includes/units/anth/policies-procedures.njk (heading hierarchy corrected).
Its unit policies-procedures.json selects that supplementalTemplate. Other units
without this optional record receive only the shared core. PUBA no longer displays
Anthropology's position statement. Future unit-specific policy content follows the
same opt-in pattern. Earlier comparison-stage notes are historical.

## Graduate Division resources (November 13)

The shared gray section now groups Academic Progress and Conduct Code as linked
H3 entries under Graduate Division (H2). Short summaries draw on the official
pages supplied by the user; the university-wide Student Conduct Code remains
separate. Existing policy wording is unchanged. The Sociology Annual Review page now points to its local Policies & Procedures
page instead of maintaining three external policy links. Existing prose references
to the policies remain intact.
