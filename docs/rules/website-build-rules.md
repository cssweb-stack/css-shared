# Website build rules

Agreed November 14, 2026. These rules cover how we organize and run websites.
They are separate from writing, accessibility and SEO rules.

## Keep the working setup

Use the established Eleventy setup and the standard clean, build and dev commands.
Do not replace a working setup with a different server or workflow without agreement.
The existing `go` shortcut runs clean, then dev. That sequence must build the pages,
start the local server and print its actual, copyable localhost address.
Never report a server as working merely because the build succeeded.
The user starts and owns local servers through their terminal with go. After an
agent starts a temporary verification server, stop that server and confirm its
port is free before handing control back, unless asked to leave it running.
Do not leave a competing server in a separate agent session.
When a page reads an editable shared document, saving that document must trigger
a local rebuild and update the served page without restarting or asking for a
manual build. Verify an actual edit and restoration through the running server;
a successful startup build does not prove the watcher works.

## Keep page addresses simple

An ordinary page uses a descriptive filename ending in `.html`.
Do not create a folder just to hold that page inside an `index.html` file.

- Correct: `/heroes/es.html`
- Incorrect for that same page: `/heroes/es/index.html` or `/heroes/es/`
- Correct: `/redirects-404s/soc.html`

Folders organize related pages. Do not add an extra folder for each individual page.
Set page addresses explicitly so framework defaults cannot silently change them.
This includes generated Review pages.

Existing, deliberately established section landing pages and the site homepage
may use `index.html`. This rule does not authorize a wholesale move of existing
faculty directories, degree sections or SCI program sections. Review those routes
separately before changing them; preserve working old addresses with redirects.

## Use consistent folders

The About folder is `about`, without a unit acronym. The main Courses page is
`courses.html` at the site root, not inside About or a Courses folder.
Use lowercase filenames and folder names, with hyphens between words where needed.
Do not create empty folders for sections that do not exist.

## Keep editable pages available

Department content pages must have identifiable HTML source files in the site's
`src` folder. Shared layouts and centrally maintained content remain shared;
do not duplicate them into every page. Review's generated listings are an explicit
exception: its generator assembles them from existing site records.

## Keep shared work shared

Reusable layouts, styles, assets and common records belong in `css-shared`.
Unit page sources belong in the unit site. Reuse established components rather
than inventing a separate implementation for each page or department.

## Verify the actual result

After changing routes or the build setup:

- Run the affected build and confirm expected output files exist.
- Check internal links and local image paths.
- For server changes, start the actual development server and request the exact
  address being given to the user. A different working page is not proof.
- For moved pages, update navigation, hero mappings and current route records;
  preserve old published routes with direct redirects.
- State whether changes are local, committed, pushed or deployed. Do not imply
  that a local fix is already live.

## Change a rule deliberately

Record an agreed change here or in its relevant topic rule, replacing the previous
instruction rather than keeping conflicting versions. Do not treat an experiment
or a framework default as an approved exception.

## Academic-program course resources

Every academic-program page, including degree, minor, certificate, combined-pathway and program subpages, ends with its unit’s shared course-resources widget directly above the footer. Use `layouts/content/course-resources.njk` inside the standard page-section/container/row/col-12 wrapper. The course widget always has its own dedicated container. Put advising/application callouts in a separate section/container above it. Keep catalog sections and other content before it. Check this when creating pages and during final review; ask if program scope is unclear.
