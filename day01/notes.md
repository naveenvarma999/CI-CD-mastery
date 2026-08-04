# Day 1 — CI/CD Foundations

## What is CI?

Continuous Integration means automatically checking code whenever developers push or merge changes.

Common CI tasks:

- Install dependencies
- Check formatting
- Run linting
- Run tests
- Build the application
- Scan for security problems

## What is Continuous Delivery?

Continuous Delivery means the application is automatically tested, built and prepared for release. Production usually requires manual approval.

## What is Continuous Deployment?

Continuous Deployment means every valid change is automatically deployed to production after all checks pass.

## Software environments

- Local: developer's computer
- Development: shared developer environment
- Testing: environment for quality testing
- Staging: production-like final testing environment
- Production: live environment used by customers

## Important terms

- Pipeline: complete automated workflow
- Stage: major section of a pipeline
- Job: group of work executed by a runner
- Step: individual command inside a job
- Runner: machine that executes pipeline jobs
- Build: process of creating a deployable output
- Artifact: output produced by the build
- Release: approved version of the application
- Deployment: running a release in an environment