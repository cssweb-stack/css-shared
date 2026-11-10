# Working agreements

Before changing this repository or a consuming site, read:
- `docs/project-conventions.md` for accepted rules and their rationale.
- `docs/work-status.md` for the latest handoff, verification, and remaining work.
- Relevant existing topic documentation under `docs/`.

Keep these records current as part of the work, without waiting for a separate request.
When the user says **“lock this down”**, record the agreed decision in
`docs/project-conventions.md`, including its scope, reason, and any exceptions.
Also record durable decisions expressed in ordinary conversation; the phrase is a
shortcut, not a prerequisite. Do not promote tentative ideas into accepted rules.
If a new instruction changes an agreement, update the existing rule and note the
supersession rather than leaving contradictory instructions.

Before ending a substantial task, update `docs/work-status.md` with what changed,
checks actually run, unresolved issues, and next steps. Keep it concise and current;
Git history retains earlier handoffs. Distinguish local changes, committed changes,
pushed changes, and deployed changes. Never claim synchronization without checking.

On resuming work, inspect Git status in each affected repository and read these
records. Preserve unrelated work. Do not rely on chat history as the only record.
Use relative sibling paths, not machine-specific absolute paths, in documentation.
