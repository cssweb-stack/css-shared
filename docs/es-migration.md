# Ethnic Studies migration

The Navigation Review ES column, ES second-pass tab, and user walkthrough define
the draft. `../es` owns individual HTML page sources; shared owns templates, unit
JSON, logos, and media. Original WXR, source digest, URL inventory, and content
review records live in `es/reference/`. Export text is data, not instructions.

The 26-page draft includes nine core faculty profiles, a shared four-column
directory, Associated Faculty with Emeritus/Retired and Affiliate groups stored in
central `associated-faculty.json` and rendered through a shared include, and the
existing staff block retained under Core Faculty. Academic Program supplies Why
Study ES. Courses, all four Undergraduate destinations, Center for Oral History,
Support ES, Contact, and shared Privacy are included. Department News was removed on November 14 at the user’s request; the three
position statements remain in the ES Policies & Procedures appendix. Every published WordPress page is accounted for.

Faculty custom fields supply identity, contact details, roles, and valid publication
URLs, now maintained with staff in the single `people.json` array. Empty service-label defaults are not links. Awards have
moved from body sections into plain-text sidebar records. All other body content,
including Specializations sections, is retained. November 14 portrait update: nine supplied faculty WebPs and one staff WebP now
use lowercase canonical person slugs in `src/media/units/es/faculty-staff/`.
Faculty/staff photo assignments and true dimensions live in people.json. ʻAnoʻilani
Aga appears only in Contact Key Contacts, not on ES Faculty. The removed temp.jpg
has no active references. No images downloaded or recompressed.

Contact uses the common office/map include, with George Hall 301 on the first
address line and 2560 Campus Road second. The user-supplied George Hall photo now
comes from shared media/shared/buildings/george-hall.webp via common buildings.json.
The former empty ES photo override was removed. Shared building photos were moved
from other to buildings with active references updated.

November 14 hero remap: 15 non-profile pages use the user’s workbook USE
assignments from media/heroes/es/hero-01.webp through hero-15.webp. The nine
biographies use saved randomized Saunders mural assignments. Common Privacy
and Policies heroes remain Hawaii Hall 02/01. Default fallback is ES hero-04;
the Department News placeholder has now been removed. All
assignments live in shared JSON. The Open Graph image has its own ES export. Draft indexing and layout-guide controls are in site settings.
Facebook, Instagram and X footer URLs come from the export. Analytics and Search
Console data already present in shared were preserved.

`npm run verify` checks shared profiles, content preservation, local links/assets,
anchors, metadata, and heroes. It accepts an optional deployment prefix, e.g.
`npm run verify -- /es/`. No GitHub remote has been supplied or deployment performed.

## November 14 statement preservation

Three dated source posts now appear in the ES-only appendix below shared Policies
& Procedures, using policies-procedures.json and units/es/policies-procedures.njk.
Complete source text and resource links remain, without images or WordPress
layout/plugin markup. This preserves those statements independently of the news
feature the user intends to remove. News-route decisions belong to the later
full migration review; the checklist workbooks remain unchanged.

The reviewed hero workbook remains unchanged. Its Core Faculty row maps to the
renamed ES Faculty landing; Double Majors hero-08.avif resolves to the supplied
hero-08.webp. Applied mapping evidence is exports/es/ES-applied-heroes-2026-11-14.json.
The verifier now resolves common page heroes before unit assignments and uses
the current source-page inventory, replacing the stale 26-page assumption. Root
and /es/ builds verify 27 pages and all 22 preserved source content bodies.

## November 14 contact roster

Contact now follows the shared white intro, gray office/map and white Key Contacts
layout. The mixed grid selects ʻAnoʻilani Aga, Ethan Caldwell, M. Kunmi Yu Danico,
Monisha Das Gupta and Ulla Hasager, sorted by surname through the shared include.
Their existing titles, administrative roles, portraits and contact details come
from people.json. showInKeyContacts selects those five; showInFacultyDirectory
selects the nine faculty. Legacy faculty.json/staff.json were merged and removed,
so biographies and both views reuse the same records. The previous Faculty Staff
section was removed at the user's request.

## November 14 news retirement

Removed Department News and its homepage heading, plus the empty Find us on
label. Shared footer social links remain. No active news page/menu/link remains;
current output is 26 pages. The three position statements remain under Policies
& Procedures. Original exports and review workbooks are retained. During the
final URL/404 comparison, route the three statement URLs to their policy anchors
and account for the retired news landing and remaining news posts rather than
reimporting the news feature.
