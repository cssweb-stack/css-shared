# Google Analytics and Search Console

Configuration lives centrally in `src/data/units/<unit>/`:

- `analytics.json`: `googleTagId` and `allowedHostnames` (exact production DNS names).
- `search-console.json`: `verificationToken`, the content of Google's verification meta tag.

The shared `base.njk` places Analytics immediately after charset metadata near the
top of `<head>` and the Search Console meta tag later in the same head. Every
page using this layout inherits the configuration. Rebuild/deploy consumers when
settings change. No individual page edits or full embed strings are needed.

`GTM-` IDs load `/gtm.js` and initialize `gtag('js')`, matching the supplied
current Google installation snippets. `G-` and `GT-` IDs load `/gtag/js` and
initialize `gtag('js')` and `gtag('config', id)`. Only one ID is selected per
site. Do not install another tag for the same destination in local pages.

The inline initializer checks `window.location.hostname` before creating any
Google script or data layer. Only exact `allowedHostnames` matches load the tag;
localhost, GitHub previews, and other units' hosts do not. Missing production
hostnames on a configured tag fail the build. This gate depends on hostname,
not development/build mode or the indexing setting. Search Console verification
is static markup and stays present on previews without loading a service.

Existing `ga4MeasurementId` settings remain supported. Resolution order is unit
`googleTagId`, unit `ga4MeasurementId`, common `googleTagId`, common
`ga4MeasurementId`. Common defaults are in `src/data/common/analytics.json`;
production hostnames must also be supplied when enabling a common default.
A blank unit ID inherits the common default; all blank means no tracking.
`allowedHostnames` can be specified per unit or inherited from common settings.

## Supplied configuration (November 8, 2026)

ANTH, DURP, ES, POLS, SSRI, PSY, CSS, PUBA, SCI, SOC, and WGSS use their supplied
`GTM-` IDs. Geography uses the supplied `G-3HXB5SCJ66`. All 12 use the supplied
Search Console token. CSS's production hostname is taken from the existing
common college link: `socialsciences.manoa.hawaii.edu`. Other hostnames come
from the user's department URL list. Economics was subsequently supplied as `G-E6W6FPX085`, restricted to
`economics.hawaii.edu`. Its Search Console ownership is verified through Analytics
(per the supplied screenshot); no separate verification token was supplied.
Before replacing that live site, preserve/recheck its Analytics verification or
add an HTML verification tag. The hostname-gated dynamic loader has not been
validated for Search Console Analytics-based ownership verification. The earlier public-homepage audit is a historical
observation, not the source of these updated settings.

Validation: shared checker and GEO, SSRI, and style-guide builds passed. Isolated
JavaScript execution checked all 12 unit configurations on their production host
and four disallowed hosts (60 cases), including endpoints and initialization.
Generated homepage/privacy headers and verification tags were checked on GEO
and SSRI. The unconfigured style guide emits no Analytics tag.

These checks validate our integration, not Google-account destinations or actual
Analytics collection. Verify Analytics Realtime/Tag Assistant after production
deployment. Search Console ownership must be confirmed in Search Console. This
change does not add consent controls or change live sites.

References:
- https://developers.google.com/tag-platform/gtagjs
- https://support.google.com/webmasters/answer/9008080
