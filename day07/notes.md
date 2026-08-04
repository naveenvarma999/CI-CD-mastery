# Day 7 — Foundation Review and Local CI

## Local CI pipeline

The local pipeline performs:

1. Check required tools
2. Create a virtual environment
3. Install dependencies
4. Run code-quality checks
5. Run automated tests
6. Validate YAML
7. Create a build artifact

## Why exit codes matter

- Exit code 0 means success.
- A non-zero exit code means failure.
- CI/CD systems use exit codes to decide whether a job passed or failed.

## Why use `set -euo pipefail`?

It makes Bash scripts stop when commands fail, undefined variables are used or commands inside a pipeline fail.

## Why test locally?

Local CI provides quick feedback before code is pushed. Remote CI still provides an independent and repeatable check in a clean environment.

## Artifact

The pipeline creates a compressed package inside the `dist` folder. This package is the output of the build process.

## Pipeline flow

```text
Source code
→ install
→ lint
→ test
→ validate
→ package
→ artifact