# Worktree Operating Guide

## What a worktree is
A Git worktree is a second local working directory attached to the same repository but checked out on a different branch. It lets multiple agents or tools work simultaneously without changing each other's files or branch state.

## Important distinction
Worktrees are a local Git mechanism. They are useful when multiple local/desktop agents share the same machine/repository. Cloud agents that clone or isolate branches remotely do not require the human to create local worktrees; branch isolation is enough.

## Current workstreams
- `plan/claude-master-agency`
- `asset/gemini-foundry-architecture`
- `tech/agent-foundation`
- `brand/naming-exploration` (managed from the Brand/ChatGPT workstream)

## Recommended local layout
From a parent folder:

```bash
git clone https://github.com/Picazo333/agency-foundation.git agency-foundation
git -C agency-foundation fetch --all

git -C agency-foundation worktree add ../agency-claude plan/claude-master-agency
git -C agency-foundation worktree add ../agency-gemini asset/gemini-foundry-architecture
git -C agency-foundation worktree add ../agency-tech tech/agent-foundation
```

Result:

```text
/agency-foundation   -> main/control
/agency-claude       -> plan/claude-master-agency
/agency-gemini       -> asset/gemini-foundry-architecture
/agency-tech         -> tech/agent-foundation
```

Do not point two local agents at the same worktree.

## If the tool works directly in the cloud
Do not create a local worktree just for that tool. Tell it the exact repository and exact branch. It should work only on that branch and finish with a PR to `main`.

## Operator rules
1. `main` is canonical; agents do not work directly on it.
2. One workstream/agent per branch or worktree.
3. Pull/fetch before starting a session.
4. Commit meaningful checkpoints rather than one giant final commit.
5. Do not merge agent PRs automatically without review.
6. If two branches need the same new canonical input, merge/update that input to `main`, then sync/rebase the branches deliberately.
7. Never store secrets in Git.
8. Generated/provisional work does not become canon merely because it exists in a branch.

## Daily inspection commands
```bash
git -C agency-foundation worktree list
git -C agency-foundation status
git -C agency-claude status
git -C agency-gemini status
git -C agency-tech status
```

## Cleanup after a branch is merged
```bash
git -C agency-foundation worktree remove ../agency-claude
git -C agency-foundation worktree prune
```

Use the same pattern for the other worktrees after their PRs are merged and branches are no longer needed.
