# SOC text-cleanup report

November 12, 2026. Scope: all 50 Sociology HTML sources and relevant shared SOC
JSON text fields. Mechanical cleanup complete; no response required.

## Corrections

38 HTML sources changed; shared JSON needed no mechanical changes.

| Finding | Corrections | Example |
| --- | ---: | --- |
| Retired intro classes | 32 | `<p class="intro">` → `<p>` |
| Accidental nonbreaking spaces | 85 | `Community[NBSP]Engagement` → `Community Engagement` |
| Incorrect Hawaiʻi ʻokina characters | 30 | `Hawai'i` → `Hawaiʻi` |
| Full university name | 1 | `University of Hawaii at Manoa` → `University of Hawaiʻi at Mānoa` |
| Mānoa spelling after university name | 1 | `Hawaiʻi at Manoa` → `Hawaiʻi at Mānoa` |
| Doubled spaces | 4 | Repeated prose spaces collapsed |
| Empty paragraphs | 0 | None found |
| Heading bold/italic wrappers | 0 | None found |
| Em-dash spacing / spaces before punctuation / invisible characters | 0 | No corrections proposed |

## Left for optional editorial review

The initial watchlist returned 12 candidates. Three were resolved by the mechanical
university-name corrections; one is the research-page permalink containing
`hawaii`, which is an identifier and must remain unchanged. Eight visible-text
candidates were preserved rather than guessing official labels or rewriting copy:

- Wei Zhang biography: two uses of `Hawaii` in research prose.
- Academic Planning: `Manoa Political Internships`.
- BAM: `UH Manoa`.
- Undergraduate Funding: `JTB Hawaii, Inc.`, the prize label ending in `Hawaii`,
  the phrase `religion in Hawaii`, and `UH Manoa STAR Scholarships`.

This finite watchlist is not an exhaustive Hawaiian-language spellcheck. Inline
spacing such as `Higher Education</em>and` is retained for editorial review rather
than changing markup boundaries automatically. Quotations and names are preserved.

## Preservation and work performed

The established source-preserving tool prepared patches and compared HTML
attributes, allowing only removal of the intro token. Proposed edits were read
before applying; source was checked against each prepared patch to preserve
intervening edits. Links, filenames, template expressions, table structure, and
original exports/reference snapshots were not edited. Existing support/faculty
page layout edits were preserved.

No rebuild, visual audit, broad validation run, or second scan was performed,
following the user's requested editing workflow. These are mechanical edits,
not a factual, SEO, or accessibility audit.

[Measured findings](../exports/soc/text-cleanup-2026-11-12.json).
Repositories changed: soc and css-shared (report/handoff). Local only;
no commit, push, or deployment.

## Next Sociology review: TMS

Check Theory, Methods, and Statistics references and every TMS occurrence.
Spell out the term or define Theory, Methods, and Statistics (TMS) on first use
on each page using the acronym. Recorded November 13; this check has not yet
been run across the current site. Scope is Sociology only.

## Next Sociology review: department and degree naming

Inventory department/degree naming variants, including formal prose, titles and
short navigation labels. Examples to compare: Sociology BA, BA in Sociology,
Major (BA), BA, and department-name/capitalization variants. Recommend consistent
forms by context for approval; no canonical choice or automatic replacement is
approved. Recorded November 13; full inventory not yet run.
