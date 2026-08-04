# Day 6 — YAML Fundamentals

## What is YAML?

YAML is a human-readable configuration format. CI/CD tools use it to define triggers, jobs, runners, commands, variables and deployment configuration.

## Important rules

- Use spaces, not tabs.
- Use consistent indentation.
- Add a space after a colon.
- Use `-` for list items.
- Quote version values such as `"3.11"`.
- Quote text containing special characters.
- Never commit passwords or tokens into YAML files.

## Main structures

### Key-value pair

```yaml
environment: development