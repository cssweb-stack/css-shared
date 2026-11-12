# Quick unit SEO review

Request: **“Run the quick SEO review for [UNIT].”**

1. Build the unit's current sources. Read each page's primary content, title, H1
   and description. Use rendered output for pages with shared includes.
2. Keep titles descriptive, unique and faithful to the H1. The shared shell adds
   the site-name suffix once; do not paste that suffix into local front matter.
   A shortened title can intentionally omit an acronym already covered by branding.
3. Replace description placeholders only when an SEO/copy pass is authorized.
   Write a specific summary supported by that page's content. Preserve good
   existing descriptions; do not copy one generic description across a unit.
4. Check canonical URLs, Open Graph/Twitter metadata, preview image availability
   and indexing directives. Confirm the intended production URL first. Existing
   shared `canonicalSections: ["/"]` can opt a unit into self-canonicals for all
   pages. This does not change the staging host or turn indexing on.
5. Run the shared read-only checker from css-shared:

   ```sh
   python3 scripts/seo-audit.py ssri --output exports/seo/ssri-2026-11-12.json
   ```

   Substitute the unit and report filename. It checks the built HTML without
   rewriting it. Semantic relevance still requires the review in steps 1–3.
6. Before launch, after final URLs and publishing are settled, run:

   ```sh
   python3 scripts/seo-audit.py ssri --launch
   ```

   This additionally catches disabled indexing. Keep indexing off while previewing.
   Check the custom 404 separately for its HTTP status and indexing behavior.

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
