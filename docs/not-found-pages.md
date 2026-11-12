# Shared 404 page

Use `pages/not-found.njk` with the shared shell. SSRI is the first consumer;
other units can adopt the same template without copying its layout or CSS.

```yaml
---
layout: shell.njk
title: "404 Page Not Found"
description: "A short unit-specific recovery description."
permalink: "/404.html"
isNotFound: true
---
```

The HTML body contains `{% include "pages/not-found.njk" %}`. Local page metadata
remains in the unit repository. Shared content/layout is in the include and
`src/css/not-found.css`; unit links are in `src/data/units/<unit>/not-found.json`.

## Presentation

- Existing shared profile geometry: 20/80 at 1600px+, 33/67 at intermediate
  widths, stacked below 768px. No independent breakpoint system.
- Left: decorative 404, Inter variable font at its supported maximum weight 900,
  cool accent `var(--accent-cool)` (#006B8F). Text size follows the column width.
  It is aria-hidden because the right-column H1 supplies the full error message.
- Right: H1, brief explanation of the site update/moved or retired pages,
  navigation/search guidance, and unordered recovery/helpful links.
- Standard unit header, navigation, hero and footer retained. No new nav item.

## Unit links and URL comparison

`not-found.json` contains `quickLinks` with helpful primary destinations:

```json
{"quickLinks": [{"label": "Unit homepage", "url": "/"}]}
```

SSRI has four quick links. Moved-page lists were removed after introducing shared
build-generated redirects. Confirmed moves belong in url-migration.json; unknown
or retired URLs receive this 404. No manually maintained redirect source pages.
See [URL Migration Audit](url-migration-audit.md) and the saved
[SSRI comparison](ssri-url-comparison.md). Historical RTRF FY2019 redirects to the user-confirmed Looker Studio replacement.
The fallback for an unconfigured unit is a working homepage link.

## Hosting and SEO

The output must be root `404.html`; [GitHub Pages supports this custom error-page
convention](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-custom-404-page-for-your-github-pages-site).
Missing requests must retain HTTP 404, not redirect to a normal 200-status page.
Verify the live host after publishing; no hosting changes or deployment were made.

`isNotFound: true` forces noindex even after regular-site indexing is enabled and
omits canonical output. Do not canonicalize missing URLs to the homepage. The
shared SEO checker recognizes /404.html as an intentional error page rather than
treating its noindex/no-canonical state as a normal-page launch failure.

SSRI verification: local missing nested URL returned HTTP 404 with the custom
body; noindex and no canonical confirmed. Three viewport checks (1800, 1100,
390px) confirmed column proportions, Inter 900, cool accent, text fit and no
horizontal overflow. New 404 main content passed targeted axe checks. SSRI now
builds 15 pages; shared and SEO checks pass. Migration classification is complete: ten redirects and no retired reports.
The user confirmed live redirects and custom 404 behavior work.
