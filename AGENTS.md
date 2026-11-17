# Working agreements

## Read the current records

Before changing this repository or a consuming site, read these documents. For
notes, prefer `.local-notes/<path>` when it exists; otherwise use the tracked
baseline at `<path>`:

- `docs/README.md`: documentation map and current rules versus historical records.
- `docs/project-conventions.md`: accepted decisions and their rationale.
- `docs/work-status.md`: current handoff, verification and remaining work.
- `docs/rules/website-build-rules.md`: before routes, folders, builds or servers.
- Relevant topic documentation under `docs/`.
- `docs/rules/accessibility-review.md` before accessibility reviews or accessibility-related changes; follow its first-run and significant-change decision safeguards.

Always read the tracked `docs/rules/code-cleanup.md` before editing or reviewing
HTML/Nunjucks/CSS formatting. It is the live rule sheet displayed on Review.

## Required rule check for every task

Use this category map to select the current rule sheets before starting:

| Category | Required rule sheet |
| --- | --- |
| SEO | `docs/rules/seo-review.md` |
| Accessibility | `docs/rules/accessibility-review.md` |
| File naming and routes | `docs/rules/website-build-rules.md` |
| Code formatting | `docs/rules/code-cleanup.md` |
| Text editing | `docs/rules/language-writing.md` and `docs/rules/text-cleanup.md` |
| 404s and redirects | `docs/rules/redirects-404s.md` |

The read, apply, check and maintain procedure below applies to every category.
Update the authoritative sheet when an agreed rule changes, including removals;
replace superseded wording and update references rather than adding competing rules.


Before editing, consult the applicable current rule sheets listed above. Reuse rules
already read in this active session unless they changed or the task enters a new
category. Identify and apply the specific rules governing the requested change;
a prior review is not proof that new edits satisfy them.

Before saying done, compare the actual edited sources and rendered result against
those specific rules. A successful build or automated check is not evidence that
naming, wording or layout agreements were applied. Fix clear violations within the
authorized scope. State any unchecked requirement or unresolved decision explicitly;
do not claim the whole task is complete while required work remains.

For page creation, renaming and SEO reviews, read website-build-rules.md and
seo-review.md and compare source filename, permalink, visible H1, rendered title,
navigation and internal references together. Standard main Courses is courses.html,
without a unit prefix. Development-only renames get no redirects; actual legacy
public URLs retain their approved mappings. Update shared mappings when needed. Queue affected Review listings for the next
review/publishing checkpoint; do not regenerate Review after each small text edit. Distinguish local results from published
results; do not report Review as updated without rebuilding it.

When a missed agreement is discovered, correct the implementation and strengthen
the applicable existing rule or this procedure in the same task. Do not substitute
an acknowledgment, another note, or repeated technical validation for the fix.

## Decision questions

Ask one distinct decision per question. Do not combine unrelated claims or edits
into a single yes/no choice, even when they appear on the same page.

## Fast path for small edits

This section takes precedence over routine startup, rendered-check and note-taking
requirements for consecutive small edits in the same active session.

- Read only relevant rule sections not already read this session. Do not reload
large convention logs, historical reports or the entire handoff for each edit.
On a fresh session, read the latest relevant handoff entries first; search older
records only when a specific unanswered question requires them.
- Simple copy edits and switches between existing grid classes use this fast path.
Edit the requested source and inspect its narrow diff; do not launch an audit,
browser session, separate build or Review refresh without a concrete reason.
- Batch independent file reads in one tool call. Keep output limited to relevant
lines or diffs; do not dump whole logs to find a small rule.
- Do not create per-edit notes, reports or checklist entries. Batch routine notes
at a substantial task, explicit handoff or publishing checkpoint.
- Complete straightforward edits directly. Omit plan recaps and repeated progress
messages; give a short result. Required tool-start commentary stays one sentence.
- Full code, language, accessibility, SEO and redirect reviews still follow their
complete category procedures when requested. Speed does not waive those reviews.

A small text, label or heading edit is not a new audit. Reuse applicable rules
already read in the active session. Edit the requested source and any directly
coupled metadata, then inspect the narrow diff. Let the user's running development
watcher rebuild the preview; do not start a server or run separate builds merely
for a simple text replacement. Do not refactor surrounding code or expand scope.
Batch Review regeneration and build checks at the next requested review or upload
checkpoint. Build immediately only for changed template logic, routes, structure,
CSS/behavior, or a concrete failure that requires it. Never claim an unperformed
build or a queued Review refresh is complete. Keep the response and routine notes
brief; batch handoff bookkeeping across consecutive small edits.

## Source document intake

Original site backups, WordPress XML, catalog PDFs and supplied reference/course
documents belong in `../CSS-Exports/<unit>/`, outside website repositories. Read
the Permanent source archives section of website-build-rules.md before intake.
Verify copies and preserve originals. Normal builds must not depend on the archive;
never claim external backup protection merely because the local archive exists.

## Keep routine notes out of GitHub Desktop

User decision, November 16, 2026: routine note-taking must not make css-shared
appear to need a website update. This supersedes earlier instructions to routinely
edit the tracked conventions, work-status, topic reports and other note files.

Continue keeping records, but write them beneath ignored `.local-notes/`, mirroring
the original path. For example, update `.local-notes/docs/work-status.md`, not
`docs/work-status.md`. Copy a tracked baseline there before its first local edit.
Treat the local version as current; the tracked baseline remains available for
fresh checkouts. Do not edit tracked documentation just to note ordinary work.
Put new reports, audit measurements and screenshots in `.local-notes/` as well.
Preserve existing tracked records and user-authored exports; do not hide tracked
changes with assume-unchanged or skip-worktree.

Keep website inputs tracked. In particular, `docs/rules/code-cleanup.md` and
`docs/rules/language-writing.md` power Review pages: substantive requested edits to
those documents are functional changes and belong in Git. Check actual consumers
before treating another Markdown file as a website input. Existing tracked notes
may be revised only when explicitly requested, rather than as task bookkeeping.

When the user says "lock this down", record the agreed decision in the local
project-conventions record, including scope, reason and exceptions. Also record
clear durable decisions expressed ordinarily. Do not promote tentative ideas to
rules. Replace superseded local rules instead of leaving contradictory guidance.

Before ending a substantial task, update the local work-status with changes,
checks actually run, unresolved issues and next steps. Keep it concise. Distinguish
local, committed, pushed and deployed work; never claim synchronization unchecked.
Do not mention routine note updates in user-facing handoffs or tell the user to
push/publish a repository solely because notes were updated.

On resuming work, inspect Git status in each affected repository and read the
current records using the local precedence above. Preserve unrelated work and use
relative sibling paths in documentation. Local notes are intentionally not pushed
or deployed and do not travel automatically between machines. At an explicit
machine handoff, arrange a separate copy of needed notes; do not promise Git sync
for ignored files. Chat history is not the only record.
