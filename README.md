# aws-cipipe-core
The core infrastructure for an AWS powered build/deploy pipeline

## Goals of a good CI workflow
- **Flexible**: Should support building in multiple languages, with multiple deployment methods
- **Project Isolation**: The workflow should not be embeded within the application code itself.  When working with multiple applications, it will become tedious to update each applicaiton if a change in workflow is required
- **Configurable**:  The steps that one person or organizaiton requires will likely be different than every other person or organizaiton

## Architecture

A CI pipeline consists of two pieces:

1. **Steps**:  This is the basic unit of work: Compile your code, Run Security Analysis, Package in a Docker Image, Deploy to a K8s cluster, Deploy as an AWS Lambda etc.

1. **A workflow**:  This is what will connect the steps to gether to take a repository from source to deployment.

## On a personal note
- Want to put into practice and expand on my programming skills and AWS knowledge
