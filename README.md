# CSS shared website foundation

Authoritative shared styles, templates and public branding assets for College of Social Sciences unit sites.

Edit shared website files in `src`. Each unit build loads these files before Eleventy renders its own pages. Unit repositories retain local content, people/contact/navigation data, imagery, hero assignments and their local stylesheet.

| Shared location | Contains |
| --- | --- |
| `src/shell.css` | Header, navigation and footer styling |
| `src/common.css` | Typography, palette, layouts and components |
| `src/_includes` | Reusable templates and Bootstrap icons with their attribution/license |
| `src/_data/university.json` | Shared university links, interpretation services and legal footer data |
| `src/_media/branding` | University/unit logos, UH pattern variants, footer backgrounds |
| `src/_media/other/contour-lines.svg` | Shared contour pattern |
| `src/assets` | Common interface and optional Bluesky feed scripts |

Run `npm run check` to check basic package structure and JSON. GitHub runs the same check on pushes and pull requests. These basic checks do not replace visual or accessibility review.

A local GEO clone expects this repository beside it at `../css-shared`. Set SHARED_SOURCE to a different path when necessary. GitHub Actions checks out the repository into the unit workspace automatically.

Only reviewed changes belong on main because connected unit builds consume it. Commit changes through GitHub Desktop or GitHub's editor; there is no generated manifest to update after editing a footer, stylesheet or SVG. Newly added shared source files are discovered automatically.

Each connected unit must run a build to publish a shared change. The starter GEO workflow includes an hourly schedule and manual rebuild option. This repository is source, not a remotely executing HTML include server. It does not need its own GitHub Pages deployment.

The initial branding folder includes the supplied GEO logo and UH assets. Add other approved unit logos as those sites join. Existing fonts still load from Google Fonts; font family and typography rules are centralized in common.css. No font binaries were added in this phase.
