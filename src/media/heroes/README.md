# Shared hero images

Add approved shared hero images here. Unit heroes.json records reference them with an explicit path such as /media/heroes/shared-campus.webp. This is a naming example, not an installed image. Keep shared hero filenames distinct from unit hero filenames because both publish under media/heroes/. Each shared/unit public asset collision is rejected before building.

Set alt for the image description. Set location when relevant. Set credit to false when no imagery attribution should be shown, or to an object with source and url to override the unit credit. GEO satellite imagery remains in GEO/src/media/heroes/.

## Student and faculty collections

`students/` contains the general student image bank (59 WebP files at initial
assignment). Use these for non-profile pages, including faculty directory landing
pages. Default description: “Students at the University of Hawaiʻi at Mānoa.”

`saunders-mural/` contains seven mural images used for individual faculty profiles.
For Psychology and Sociology, `heroes.json` owns non-profile assignments and
`faculty-heroes.json` owns individual profile assignments in each shared unit data
directory. Keep the URL keys disjoint; the template reads `heroes.json` first.
Random selection happens once during assignment, and the selected image paths are
saved. Do not randomize at runtime or reshuffle existing pages without a request.
Use each bank image once per site before repeating; balance mural reuse across
profiles. Existing hero height/overlay settings remain in `site-settings.json`.
These banners are currently decorative and hidden from screen readers.

`faculty/main.webp` and `faculty/associated.webp` are fixed directory banners,
currently assigned to PUBA only. GEO retains its satellite imagery. Do not include them in the random student or
mural pools. Before removing a bank image, update every referencing assignment.
