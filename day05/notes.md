# Day 5 — Git Branches and Pull Requests

## What is a branch?

A branch is an independent line of development. Developers use branches to build features and fix bugs without directly changing the stable main branch.

## Feature workflow

```text
main
→ create feature branch
→ make changes
→ commit
→ push
→ open pull request
→ run CI checks
→ code review
→ merge
→ update local main
→ delete feature branch
```

## Important commands

git branch lists branches.
git branch --show-current displays the current branch.
git switch branch-name changes branches.
git switch -c branch-name creates and switches to a branch.
git push -u origin branch-name pushes a new branch.
git merge branch-name merges a branch.
git branch -d branch-name safely deletes a local branch.
git fetch downloads remote information.