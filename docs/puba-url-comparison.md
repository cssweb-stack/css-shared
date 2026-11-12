# PUBA URL migration review

November 12, 2026 (Pacific/Honolulu). Local URL/404 preparation complete;
production cutover still has deferred content.

The 84 original URLs are accounted for as one unchanged homepage, 26 verified
moves, and 57 deferred/unresolved URLs. No URLs are declared retired.

The active shared PUBA url-migration.json generates 25 previously inventoried
moves plus the original policies URL to the now-approved local policies page.
Each destination exists. The existing annotated workbook is preserved; its
earlier proposed mappings are historical review evidence, not deployment state.

Unresolved: Academic Program and GCERT Public Service Leadership were excluded
from import; no replacement or retirement has been confirmed. The other 55
entries are the news landing and 54 published news posts. Their import is
explicitly deferred. The inspected Posts XML matches all 54 pending post URLs;
two additional drafts remain unpublished. Preserve access to the existing
WordPress news archive when planning a production switch. Do not redirect its
landing to the introductory-only new news page or mark its posts retired.

Added the shared custom 404 with PUBA recovery links. It remains noindex and has
no canonical. Verified both root and /puba/ builds: 31 content/error pages plus
26 generated redirects, 2,980 internal references, no broken paths/fragments,
correct redirect refresh targets/canonicals, and no published hero-review page.
Redirects are immediate HTML meta refresh, not HTTP 301 responses.

Evidence: [root checks](../exports/launch/puba-root-2026-11-12.json) and
[preview-prefix checks](../exports/launch/puba-prefix-2026-11-12.json).
Actual host redirect navigation, genuine missing-URL HTTP 404 responses,
production archive handling, and live re-scan remain unverified. No commit,
push, or deployment performed.
