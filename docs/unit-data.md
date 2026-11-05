# Unit identity and social data

Each unit's records live in `src/data/units/<unit>/`.

| File | Contains |
| --- | --- |
| site.json | Unit name, abbreviation, primary address, phone, email, logo, and existing site configuration |
| social.json | Optional social links and optional Bluesky feed settings |

The social record uses `links` for footer accounts and `bluesky` for feed configuration. The shared footer reads social.links; the shared feed display reads social.bluesky. An empty links array or an absent social record produces no social links. Primary contact information remains independent.

Existing GEO accounts were moved to its social.json. Other units' social files contain empty links arrays because no accounts were supplied.

Each logo record supplies its public src, meaningful alt text, and intrinsic width/height. Horizontal white logos use `<abbreviation>-logo-horz-white.svg`; vertical white logos use `<abbreviation>-logo-vert-white.svg` in `src/media/branding/logos/`. Each unit-details.json exposes both as `logo.variants.whiteHorz` and `logo.variants.whiteVert`. The shared footer explicitly selects `whiteHorz`. Preserve the intrinsic dimensions recorded for each orientation rather than imposing one height on every unit.

These new unit records supply identity/contact/logo data only. Other units need their own pages, navigation, and build configuration when they are onboarded. GEO's existing records and build remain intact.

The supplied contact list used the same room (Saunders Hall 445) for GEO and Public Administration. This was retained pending confirmation.
