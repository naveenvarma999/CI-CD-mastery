# Day 3 — Linux and Bash Fundamentals

## Why Linux is used in CI/CD

Most CI runners, servers and containers use Linux. Bash commands are commonly used to install dependencies, run tests, build applications and deploy services.

## Important commands

- `pwd` shows the current directory.
- `ls` lists files.
- `cd` changes directories.
- `mkdir` creates directories.
- `touch` creates empty files.
- `cp` copies files.
- `mv` moves or renames files.
- `rm` deletes files.
- `cat` displays file contents.
- `grep` searches text.
- `find` searches for files and directories.
- `chmod` changes permissions.
- `export` creates environment variables.

## Important Bash operators

- `>` replaces file content.
- `>>` adds content to a file.
- `|` sends one command's output into another command.
- `&&` runs the next command only after success.
- `||` runs the next command only after failure.
- `$?` displays the previous command's exit code.

## Exit codes

- Exit code `0` means success.
- A non-zero exit code means failure.

CI/CD systems use exit codes to decide whether a pipeline job passed or failed.

## Safe Bash mode

```bash
set -euo pipefail