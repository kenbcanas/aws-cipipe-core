# aws-cipipe-core
The core infrastructure for an AWS powered build/deploy pipeline

## Goals of a good CI workflow
- **Flexible**: Should support building in multiple languages, with multiple deployment methods
- **Project Isolation**: The workflow should not be embeded within the application code itself.  When working with multiple applications, it will become tedious to update each applicaiton if a change in workflow is required
- **Configurable**:  The steps that one person or organizaiton requires will likely be different than every other person or organizaiton

A CI pipeline consists of two pieces:

1. **Steps**:  This is the basic unit of work: Compile your code, Run Security Analysis, Package in a Docker Image, Deploy to a K8s cluster, Deploy as an AWS Lambda etc.

1. **A workflow**:  This is what will connect the steps to gether to take a repository from source to deployment.

## What CiPipe Core Provides

This project is intended to provide the underlying run time infrastructure to power the workflows and steps that are in related repositories.  This includes
- Compute Environment (Phase1)
- Temporary storage during the build process  (Phase1)
- Notification System (Phase1)
- API to trigger builds (Phase1)
    - Default hook for integration with Git (Phase1)
- Dashboard (WIP) (Phase2)
- DB for tracking (Phase3)
    - Scheduled builds
    - Dependency tracking for chaining upgrades

