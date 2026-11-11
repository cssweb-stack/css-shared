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
Support ES, Contact, and shared Privacy are included. Department News is retained
as a non-navigation page. Every published WordPress page is accounted for.

Faculty custom fields supply identity, contact details, roles, and valid publication
URLs in `faculty.json`. Empty service-label defaults are not links. Awards have
moved from body sections into plain-text sidebar records. All other body content,
including Specializations sections, is retained. Temporary portraits use the
user-supplied `src/media/units/es/faculty-staff/temp.jpg`; no images downloaded.

Contact uses the common office/map include, with George Hall 301 on the first
address line and 2560 Campus Road second. The common George Hall entry currently
contains a Saunders image, so ES explicitly omits that building photo until the
user supplies a George Hall asset. Its George Hall map and contact details work.

Non-profile heroes use stable student-bank selections; profile heroes use stable
Saunders murals, all stored in shared JSON. The Open Graph image temporarily uses
PSY's existing image. Draft indexing and layout-guide controls are in site settings.
Facebook, Instagram and X footer URLs come from the export. Analytics and Search
Console data already present in shared were preserved.

`npm run verify` checks shared profiles, content preservation, local links/assets,
anchors, metadata, and heroes. It accepts an optional deployment prefix, e.g.
`npm run verify -- /es/`. No GitHub remote has been supplied or deployment performed.
