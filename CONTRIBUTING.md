# CONTRIBUTING

## Continuous Integration
Using GitHub Actions, this repository has a continuous integration setup that ensures the quaity and compatibility of its application. It does this by automatically running tests and protecting key branches for every code change. The details of these features are as follows:

1. #### Automated Test Execution:

  - **Triggers**: Tests are automatically run whenever any branch is pushed to or a pull request is made to the `main` branch.
  - **Enviroments**: The setup runs on `ubuntu-latest` and Python versions 3.8, 3.9, and 3.10
  - **Test Suite**: All unit and integration tests in the `test/` directory are executed with `pytest`.
  - **Static Code Analysis**: Installs and runs `pylint` on all Python files, excluding the `test/` directory.

2. #### Branch Protection Rules:

  - **Protection**: The `main` branch is protected with an "Active" enforcement status.
  - **Pull Request Approval**: Merging to the `main` branch requires a pull request which must have at least one approving review.
  - **Status Checks**: The workflow mandates `pytest` status checks must pass before merging.
