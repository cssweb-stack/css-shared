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
