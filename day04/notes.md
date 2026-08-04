# Day 4 — Git Fundamentals for CI/CD

## Why Git matters in CI/CD

Git stores every version of the source code. CI/CD pipelines use Git events such as pushes, pull requests and tags to start automated workflows.

## Git areas

1. Working directory — files currently being edited
2. Staging area — changes selected for the next commit
3. Local repository — committed project history
4. Remote repository — repository stored on GitHub

## Main Git flow

```text
Edit
→ git status
→ git diff
→ git add
→ git diff --staged
→ git commit
→ git push
→ pipeline starts