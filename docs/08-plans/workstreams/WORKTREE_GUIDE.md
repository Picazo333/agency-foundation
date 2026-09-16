# Worktree Guide

When multiple coding agents work simultaneously, prefer isolated branches/worktrees so each worker has its own filesystem state. Suggested local pattern:

```text
agency-foundation-main/
agency-foundation-codex/
agency-foundation-jules/
agency-foundation-antigravity/
```

Each worktree maps to a distinct branch. Integrate through PR review rather than shared uncommitted state.
