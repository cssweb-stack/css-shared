# Shared privacy policy

Edit `src/includes/pages/privacy.njk` to update the policy for all consuming sites.
Update its revision date when the policy changes. The contact comes from
`src/data/uh/footer.json` → `webmaster.email`.

`scripts/unit-site/privacy.mjs` registers two Eleventy virtual pages, using the
existing `base.njk` layout and each site's branding:

- `/privacy.html`: primary address, linked through the shared footer on every page.
- `/privacy/` (`privacy/index.html`): retained for existing links and bookmarks.

The shared unit-site configuration registers these pages automatically, including
for newly scaffolded departments. GEO and the style guide use older independent
configurations and explicitly register the same helper. Other independently
configured consumers must also register `configurePrivacy` from the helper.

Old local `src/privacy.html` and `src/privacy/**` templates are excluded by the
helper, so their previous text cannot override the central policy. They can be
removed when cleaning up those consumers. Do not create new local privacy pages.
The scaffold no longer creates a placeholder privacy page.

The footer URL passes through the existing `url` filter, including
`SITE_PATH_PREFIX` for subdirectory hosting. No separate CSS or tracking script
is included by the policy. This change does not enable Analytics or add consent
controls. Confirm the policy against actual collection practices and Analytics
settings when rolling out tracking; this policy does not replace any required
consent implementation.

Validation: shared checker and GEO, SSRI, and style-guide builds passed. Generated
root/legacy pages, shared content/contact, and homepage footer links were checked.
An SSRI build with `SITE_PATH_PREFIX=/ssri/` verified prefixed links and styles.
