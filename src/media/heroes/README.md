# Shared hero images

Add approved shared hero images here. Unit heroes.json records reference them with an explicit path such as /media/heroes/shared-campus.webp. This is a naming example, not an installed image. Keep shared hero filenames distinct from unit hero filenames because both publish under media/heroes/. Each shared/unit public asset collision is rejected before building.

Set alt for the image description. Set location when relevant. Set credit to false when no imagery attribution should be shown, or to an object with source and url to override the unit credit. GEO satellite imagery remains in GEO/src/media/heroes/.

## Student collections

Student heroes are split into `students/graduate/` and `students/general/`.
The first split follows the user's Sociology review: graduate contains 02, 14,
24, 28, 38, 42, 54 and 57.webp; the other 44 remaining images are general.
These are approved visual-use categories, not claims about pictured people's
actual ages or enrollment. Approved general Featured selections live under `students/general/featured/`.
All other general images have now been approved as Supporting and live under
`students/general/supporting/`. Graduate Featured images are 42, 54 and 57.webp in `graduate/featured/`;
the other four remain in `graduate/supporting/`. Image24 was reclassified as General Featured.

Keep filenames stable. When moving a file, update all active references before
removing the old path. Existing assignments are saved in shared unit heroes.json;
selection must not reshuffle on every build. Migration inventory scripts discover
both nested folders. The completed Extra Student Images candidate page was removed.
`/heroes/graduate-images.html` now displays the graduate bank for selection.

## Faculty and universal shared pages

`common/page-heroes.json` owns universal Saunders mural choices: faculty bios use
`saunders-mural/07.webp`; Privacy uses 06.webp; Policies and Procedures uses
03.webp; 404 uses 02.webp. These override individual unit assignments. Faculty
landing pages remain independently selected in unit heroes.json. GEO retains its
other satellite imagery. These shared banners are currently decorative and hidden
from screen readers; descriptive alt metadata remains available in the records.

The retired students-bank images 03, 05, 06, 11, 49, 53 and 59.webp must not be
restored or selected; the shared checker rejects them. Those exclusions apply only
to the students bank, not to similarly numbered Saunders mural images.
