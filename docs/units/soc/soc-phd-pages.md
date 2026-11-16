# Sociology PhD page split

November 13, 2026. Local source changes; not built or published.

| Page | Original material |
| --- | --- |
| `/graduate/doctorate-phd/` | Existing introduction and research-area links; student learning outcomes in gray |
| `/graduate/doctorate-phd/requirements.html` | Coursework, notes, deficiencies, bypassing, advising, guidance committee, human subjects |
| `/graduate/doctorate-phd/timeline.html` | Existing example-progress explanation and all twelve semester sequences |
| `/graduate/doctorate-phd/qualifying-review.html` | Complete qualifying review, pass/fail procedures, MA en route and terminal MA provisions |
| `/graduate/doctorate-phd/comprehensive-exam.html` | Complete comprehensive exam preparation, administration and evaluation |
| `/graduate/doctorate-phd/dissertation.html` | Dissertation committee, proposal, dissertation, oral defense and graduation |

Every page has a white intro and shared degree navigation, one gray content
section, and the standard Sociology course-resources include in a separate white
section beneath the content. Short new subpage intros summarize the moved content.
Existing substantive prose, lists and external form links were preserved.
Former italic subsection labels are plain H3s, with my-3 dividers within a topic
and standard dividers between major topics. No new CSS was added.

The timeline uses the same responsive Semester / Coursework / Milestones table
as the MA. Every original semester item remains in its original semester. The
original explanation remains intact, including the six-year example and seven-year
limit; no requirement reconciliation or external link audit was performed.

Annual Review is the final PhD navigation destination and uses the existing
shared `/graduate/annual-review.html` page. Obsolete standalone image, review link,
course links and Related Resources footer were replaced by the standard navigation
and course resources, following the MA treatment. Student Organizations remains
available in Graduate navigation; Graduate Course Categories remains linked from
the relevant content.

Updated the global PhD navigation and Why Study SOC links. Original phd-1 through
phd-11 IDs remain on their moved sections. Configured the old doctorate-phd.html
URL and fragments through the existing redirect generator, as for MA. These are
build-generated HTML redirects, not HTTP 301s, and fragment routing requires JS.
The old generated page was removed locally to avoid a redirect output collision.
The two Phase I course-requirements links previously pointed to the advising
anchor; they now point to requirements.html#phd-4 (Coursework).
All six pages retain the original PhD hero assignment.

No build, browser review, or tests run, per the user's source-edit workflow.
Cross-checking MA and PhD remains the next requested review phase. Existing SOC
verification inventory predates both approved splits and requires separate upkeep
when verification is requested. Publish soc and css-shared together; no commit,
push or deployment performed here.

## Navigation placement update

The shared navigation now occupies its own white section and column between the
intro and gray content section on every degree page. Intro content and navigation
styling remain unchanged; visual treatment will be decided separately.
