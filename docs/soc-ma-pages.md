# Sociology MA page split

November 13, 2026. Implemented in local sources; not built or published.

| Page | Original material |
| --- | --- |
| `/graduate/master-ma/` | Original introduction; learning outcomes in gray; Plan A/B explanation, MA-to-PhD admission and existing resources below on white |
| `/graduate/master-ma/requirements.html` | Coursework and notes, advising, candidacy, human-subjects guidance |
| `/graduate/master-ma/timeline.html` | Original example-progress explanation and four-semester sequence, converted to a shared responsive table in gray |
| `/graduate/master-ma/thesis.html` | Complete Plan A thesis section, including committee, proposal, research, defense and graduation |
| `/graduate/master-ma/research-report.html` | Complete Plan B guidance committee and research report section |

New subpages have short content-grounded intro paragraphs, as explicitly approved.
Existing requirement/procedure sections, form destinations and wording were moved
intact. The timeline retains every course and milestone in its original semester;
its table uses Semester, Coursework and Milestones columns. No new CSS was added.

Each page includes one shared degree-navigation block at the top, with all five
destinations and aria-current on the selected item (no visible “current” word).
The bottom uses SOC’s standard course-resources include, with no Back to top link. Navigation data is
in shared SOC degree-navigation.json; markup is layouts/content/degree-navigation.njk.
The global MA menu and existing BAM/Why Study links now point to the new overview.
All five pages retain the original MA hero image through explicit assignments.

The old `/graduate/master-ma.html` URL is mapped to the overview through the
existing build-generated redirect mechanism. New fragmentTargets support sends
old section-1 through section-10 bookmarks to the corresponding page/anchor.
These fragment-specific routes require JavaScript; the normal meta-refresh and
visible fallback still reach the overview without it. This is not an HTTP 301.
Other units' redirect entries without fragmentTargets retain their existing output.

PhD page source was not edited by this split. Existing migration snapshots and
WordPress exports were preserved. The old generated MA output was removed locally
so the next build can generate its replacement redirect without a stale-file clash.

No builds, browser checks, or full-site verification runs were performed, following
the user's editing workflow. The SOC verifier's old fixed page inventory/source
comparison predates this approved split and still needs its separate maintenance
when verification work is requested. A local output directory is not evidence of
publication. Repositories to publish together: soc and css-shared.

## Navigation placement update

The shared navigation now occupies its own white section and column between the
intro and gray content section on every degree page. Intro content and navigation
styling remain unchanged; visual treatment will be decided separately.
