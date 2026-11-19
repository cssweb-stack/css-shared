# Unit SEO review

Request: **“Run the quick SEO review for [UNIT].”**

An SEO review is an editing task. A request to do it authorizes the page-by-page
work below, including clear corrections to titles and descriptions. Do not merely
run a script, report metadata presence, or postpone obvious title edits as
“cosmetic.” Read this checklist and put the full editorial work in the task plan
before starting. “Quick” means focused work, not omitted editorial work.

1. Read every current page's primary content, using rendered output for shared
   includes. Inventory all pages so none are silently skipped. Understand each
   page's purpose before writing its metadata. Do not claim a full review after
   reading only a sample. Preserve academic facts and protected authored voice;
   ask about genuinely uncertain meanings rather than inventing them.
2. Review and finish the complete title/heading list together:
   - Read each visible H1, HTML search title, navigation label and filename.
   - Edit every search title for clear, specific, natural wording that accurately
     represents its page. Use the established Page name | Unit name | UH Mānoa
     suffix. Remove unnecessary repetition between the page portion and suffix;
     do not call this optional cleanup after declaring SEO complete.
   - Use page searchTitle for a concise search label while retaining a descriptive
     visible H1 where appropriate. Navigation can be shorter; the subject,
     credential and option must remain consistent across all representations.
   - Contact-page visible H1s use Contact [full unit name], never an acronym.
     The search-title page label is Contact; the full unit name is supplied
     once by the suffix. Navigation stays Contact.
     Check every unit contact page; the H1 and title need not be identical.
   - Donation/support pages use Support [full unit name] in the H1 and
     /support.html as the ordinary filename/route. The search-title label is exactly
     Support; contact pages use exactly Contact. No unit name or acronym before
     the first pipe on either page. This supersedes earlier support title choices;
     check navigation, internal links, hero mappings and redirects together.
     Respect explicitly deferred sites; do not rename their routes during review.
   - Graduate degree subpages use Degree: Topic identically in the visible H1
     and title label before the first pipe. The title suffix supplies the unit.
     Filenames match Topic in lowercase dash-separated form (ampersands and
     parentheses omitted); Overview uses index.html. Example: MA: Plan A (Thesis)
     uses plan-a-thesis.html. Preserve actual program topics, not another unit's
     curriculum. Update current links/hero keys; create no development redirects.
   - When an approved program/option name changes, update navigation, H1,
     frontmatter title, searchTitle and overview references in the same task.
     Check the whole family, not just the page currently open.
   - Check every source filename and permalink against `website-build-rules.md`,
     including root `courses.html` without a unit prefix and root `support.html`.
     Apply already-approved naming corrections and update navigation, links, hero
     mappings and current route records together. Do not create redirects for
     development-only names on non-indexed previews; preserve actual legacy public
     URL mappings. Ask about genuinely unapproved route changes.
   - Before claiming completion, compare the actual source and rendered route list
     with these naming rules; metadata presence alone does not cover filenames.
   - After editing a title, H1 or source filename being reviewed, build the
     affected unit and rebuild Review before reporting the change visible there.
     Use Review npm run refresh:headings -- UNIT for title/H1/filename edits; it
     rebuilds affected unit(s) and naming pages without unrelated inventories.
     Verify the exact changed value in Review output; source edits alone are not
     enough because Review reads built HTML.
   - Read the complete final rendered title list before handoff. Long titles are
     prompts for editorial judgment, not automatic truncation failures. Preserve
     useful specificity, research-area names and personal names. Use familiar
     ampersands in compact administrative labels where approved.
   - Homepage exception: every reviewed unit uses exactly Full Unit Name
     (ACRONYM) | UH Mānoa, implemented with the existing homepage-only seoTitle
     override. Never replace it with Home or a repeated acronym suffix. This
     supersedes the earlier blanket instruction to remove seoTitle overrides.
   - Locked ordinary-page suffix: | Full Unit Name | UH Mānoa, with one space
     on either side of each pipe. Never use SSRI/WGSS or another acronym as the
     unit suffix. Do not add Department of or Program. Social Science Research
     Institute is the full institute name, not a department/program prefix.
     Exact names live in src/data/common/title-standards.json; unit settings must
     match them. searchTitle owns only the page-label segment. The existing
     read-only SEO checker independently validates settings AND rendered titles,
     including full name, suffix spacing and campus. Existing pipes inside authored
     news headlines do not change the final two suffix segments. No unit exception.
     Homepage-only titles retain their separately approved pattern above.
   - Final prefix-removal scope, November18: strip the full unit name only when
     it is a redundant leading prefix in the search-title page label. Do not
     remove matching words later in titles. Preserve full organization names:
     Anthropology Graduate Student Association (AGSA), Anthropology Undergraduate
     Student Association (AUSA), Ethnic Studies Student Association. These exact
     protected labels are recorded in title-standards.json. This supersedes the
     earlier anywhere-in-label repetition check. Keep discipline/credential/topic
     names intact, including Medical Anthropology, Applied Cultural Anthropology,
     Master of Public Administration and named professional organizations.
     This changes searchTitle only, not visible H1s or filenames. Why Study uses
     the separately approved acronym label; do not strip that acronym.
   - Before editing, compare equivalent pages across the established units on
     Review (all eight must be listed). Review is evidence, not permission to copy
     an outlier: apply the accepted majority model and documented rules. If the
     intended model is unclear, ask before changing it. Verify all eight homepage
     titles against the exact homepage pattern before declaring SEO complete.
3. Read and finish every meta description, not just placeholders. Write a unique,
   useful summary grounded in that page's actual content. Replace placeholders,
   generic repeated copy, misleading summaries and needlessly long descriptions;
   preserve descriptions that already work. Use relevant subject/research terms
   naturally without stuffing keywords or promising unsupported benefits. H1,
   title and description must describe the same page. SEO authorization includes
   these edits; do not wait for a second request to do them.

4. Check canonical URLs, Open Graph/Twitter metadata, preview image availability
   and indexing directives. Confirm the intended production URL first. Existing
   shared `canonicalSections: ["/"]` can opt a unit into self-canonicals for all
   pages. This does not change the staging host or turn indexing on.
5. Run the shared read-only checker from css-shared:

   ```sh
   python3 scripts/seo-audit.py ssri --output .local-notes/exports/seo/ssri-2026-11-12.json
   ```

   Substitute the unit and report filename. It checks the built HTML without
   rewriting it. This script supports the editorial work above; it does not perform it.
   Run the existing checker once after substantive edits, then recheck only actual
   fixes as needed. Do not substitute repeated validation for reading and editing.
6. Before launch, after final URLs and publishing are settled, run:

   ```sh
   python3 scripts/seo-audit.py ssri --launch
   ```

   This additionally catches disabled indexing. Keep indexing off while previewing.
   Follow [404s & Redirects](redirects-404s.md) for the custom 404, legacy mappings
   and their HTTP-status checks.

Completion means the page reading, title/heading review and description editing
are finished, the rendered results have been inspected, and any unresolved
questions are explicitly identified. A zero-error script result is not an SEO
completion grade. Never award an overall A based only on technical fields. If
editorial work remains, say the SEO review is incomplete and identify that work.
Do not reassure the user that unfinished requested edits are unnecessary merely
because the pages render or the user is tired. Do the authorized work.

Report corrections, intentional exceptions and launch-only items briefly. Use
length warnings as prompts, not arbitrary truncation rules. Google may generate
different title links and snippets; matching metadata cannot guarantee their
display. A sitemap and live Search Console checks belong to final publishing
after the URL inventory is settled. This pass does not perform keyword/rank
research, rewrite all page copy or replace the original-URL/404 comparison.

Metadata remains in each page's HTML front matter; shared shell/templates render
it into title, description and social tags. When content changes, review its
metadata too.

References: [Google title guidance](https://developers.google.com/search/docs/appearance/title-link)
and [description/snippet guidance](https://developers.google.com/search/docs/appearance/snippet).
