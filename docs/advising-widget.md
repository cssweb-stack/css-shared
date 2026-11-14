# Reusable advising widget

November 13, 2026. Local source implementation, not built or published.

Include `layouts/profiles/advising-widget.njk` above the course-resources section.
It supplies its own white section/container and heading. Currently included on the Sociology Minor, BA overview and BAM pathway pages
(../soc/src/undergraduate/minor/index.html, ../soc/src/undergraduate/major/index.html,
and ../soc/src/undergraduate/bam.html). The pre-existing advising section and its preceding HR were removed after
user review; the widget is now the sole advising section on the Minor page. BAM adoption was approved and implemented.

## Data ownership

- Unit `advising-widget.json` owns heading, role ordering, and advising descriptions.
- First Sociology entry resolves exactly one person with Undergraduate Chair in
  people.json roles. A chair change belongs in people.json, not each page.
- Jason Higa identity, shared photo, and appointment instructions live in
  src/data/common/advisors.json. The unit references his slug. No phone or email
  is shown: the shared template uses appointmentInstructions instead of contact
  details when those instructions exist.
- Jason’s appointment guidance and destinations came from Sociology Advising &
  Support. After review, the user approved shortening the second paragraph to
  “Learn how to schedule an appointment.” Other appointment wording is retained. That source page is
  unchanged. Future widget instruction changes belong in common advisor data.
- Loader support is isolated from the older GEO advising.json contract.
  Missing or ambiguous advisor references fail resolution.

## Presentation

Role order: Undergraduate Chair, then General Education Advisor; do not sort these
by surname. Desktop (1200px+) gives each advisor half the row, subdivided 40/60,
producing photo/text/photo/text proportions of 20/30/20/30 after gutters.
At 768–1199px advisor pairs stack, with 20/80 photo/text per row. On mobile the
photo and details stack; photos are capped at 200px or half the column width.
Photos use the existing photo-style treatment and descriptive person alt text.

All layout/grid declarations are in layout.css. Profile names, titles, roles,
contacts, and dividers reuse profile.css; the existing profile-name rule now also
supports H3 for advisor names under the widget H2. No new font size or weight rules.
Phone/email rendering uses the existing profile-contact include and icon links.

No build, browser review, or tests run, following the user's source-edit workflow.
The user approved this first placement and removal of the old advising copy.
BA and BAM adoption are implemented; adoption on other pages remains pending. Both soc and css-shared need publishing together.

## BAM-specific selection

SOC advising-widget.json now defines variants.bam: Undergraduate Chair, Graduate
Chair, then Jason Higa. BAM sets advisingWidget to advising_widget.variants.bam
before including the same template. BA/Minor use the default two-person group.
Both chairs resolve by their current role from people.json. Jennifer uses the same undergraduate course selection, program requirements and
planning description on BA, Minor and BAM. Ashley uses the equivalent graduate
description on BAM. Neither uses SOC or assigns declaration responsibilities.
Jason’s description and appointment instructions are unchanged. The existing
layout places both chairs in the first desktop row, Jason in the second.

BAM’s optional variant intro explains why students should coordinate undergraduate,
graduate and general education advising across the combined degrees. The shared
widget renders this paragraph under H2, followed by an HR; BA/Minor omit it.
The former second-person contact instruction was removed from the BAM page intro.

The default BA/Minor group now also has an intro beneath Undergraduate Advising,
summarizing the former Advising & Support mission/services paragraph and encouraging
close coordination toward graduation. An HR separates it from the people. Services
are described collectively; responsibility is not assigned to either advisor.
BAM retains its own cross-degree advising introduction unchanged.
