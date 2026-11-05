# College of Social Sciences shared website source

One source for shared styles, templates, public assets, and unit JSON. GEO reads this repository directly during its build. Shared files are not mirrored into GEO's src directory.

## Source map

| Folder | Contains |
| --- | --- |
| src/assets/fonts | Inter fonts and license |
| src/assets/js | Shared browser JavaScript |
| src/css | Shared CSS; common.css imports the other stylesheets |
| src/data/uh | header.json, footer.json, languages.json |
| src/data/units/geo | GEO's site, navigation, hero, event, people, advising, and homepage JSON |
| src/includes/base.njk | Complete page assembly |
| src/includes/layouts/branding/header | UH bar, department name/search, navigation |
| src/includes/layouts/branding/footer | Main footer and subfooter |
| src/includes/layouts/hero | Hero and attribution |
| src/includes/layouts/events | Event displays and date formatter |
| src/includes/layouts/profiles | Profiles, contacts, cards, directories, advising |
| src/includes/layouts/social | Social feeds |
| src/includes/layouts/content | Buttons, callouts, course resources, grid macros |
| src/media/branding/logos | UH, college, and unit SVG logos |
| src/media/branding/backgrounds | Shared UH background graphics |
| src/media/branding/favicon | Shared favicons |
| src/media/icons | Shared SVG icons and license |
| src/media/heroes | Shared hero-image collection, ready for approved images |

Names are lowercase with hyphens. Code and JSON are flush-left. YAML front matter and workflows retain required indentation.

## Department data

Select a department with `unit` in the consuming site's shared.config.json. The GEO build loads its actual records from data/units/geo and exposes the established template variables. Filename improvements do not require renaming existing template fields:

| JSON file | Template data |
| --- | --- |
| site.json | site |
| navigation.json | navigation |
| heroes.json | heroes |
| faculty-heroes.json | faculty_heroes |
| events.json | events; lectures is the existing lecture-page alias |
| faculty.json | faculty |
| graduate-students.json | graduate_students; students is the existing directory alias |
| advising.json | advising |
| home.json | home |

No staff.json was created because there was no staff dataset in the supplied source. Staff content already on pages remains intact. Add a real staff record when it is needed. A new JSON filename is discovered after restarting development preview or reloading its configuration.

Shared UH records are exposed as uh.header, uh.footer, and uh.languages. The shared footer privacy and webmaster settings now contain the verified values migrated from GEO. They are no longer repeated in GEO's site.json. Each unit must still supply the privacy page at the common /privacy/ URL; this migration did not rewrite the GEO policy into a generic college policy.

## Images and heroes

Unit logo configuration points to `/media/branding/logos/<name>.svg`, with alt, width, and height supplied in site.json. Add new approved logos to that folder; the college/unit logo collection was not included in the supplied archive.

Hero records use full site-relative image paths. Shared photographs and unit photographs can both be assigned:

- Shared image: css-shared/src/media/heroes/<filename>.
- GEO satellite image: geo/src/media/heroes/<filename>.
- Configuration for both: css-shared/src/data/units/geo/heroes.json or faculty-heroes.json.

Both collections publish under /media/heroes/. Use distinct filenames. The consuming build rejects public asset collisions before copying.

Each hero can provide alt, location, position, and credit. GEO's existing accessible descriptions are preserved explicitly in its JSON. Credit defaults to the unit's heroes.credit; use an individual credit object (source and url) to override it or `credit: false` to suppress that attribution. Shared hero images do not have to be satellite imagery.

The contour graphic belongs to GEO at geo/src/media/backgrounds/contour-lines.svg. Shared tiles accept the optional --tile-background property; GEO sets it in its own stylesheet.

## Build integration

The repositories sit beside each other by default: css-shared and geo. SHARED_SOURCE can select a different checkout. GitHub Actions uses GEO's ignored .shared-source directory for its shared checkout; no public source paths change because of that.

GEO resolves page layouts from the shared includes directory, loads inline SVGs from shared media, and keeps biography includes local. Only public assets and rendered pages reach _site. CSS is bundled into geo.css, with source-relative asset URLs rewritten to copied public paths. The font preload matches the copied font URL; fonts are not duplicated into hashed bundle paths.

Shared configuration/data/template edits are watched during preview. Record structure validation and reference checks run before every build. npm run shared:check in GEO verifies the selected shared source without copying files into src. A generated .shared-state.json receipt records the shared commit and content hash for CI; it is ignored by Git.

## Commands

Run `npm run check` here. Run `npm run build` or `npm run dev` from GEO. Shared changes require a consuming-site rebuild before publication. Rebuild fan-out across other departments is not added by this migration.

The footer grid, breakpoints, typography, and rendered page content were preserved. The style-guide footer showcase and responsive visual review remain separate work. For multiple footer instances, pass a distinct footerId to each include so language heading IDs stay unique.

The old buttons patch, one-time GEO adoption/synchronization/retirement scripts, unused photo importer and hero-gallery data helper were removed after reviewing the actual consumer. See docs/consumer-migration.md and docs/validation.md.
