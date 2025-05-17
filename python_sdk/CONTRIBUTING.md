# Contributing Guide For VizQL Data Service Python Client

This page lists the operational governance model of this project, as well as the recommendations and requirements for how to best contribute to the VizQL Data Service Python Client. We strive to obey these as best as possible. As always, thanks for contributing – we hope these guidelines make it easier and shed some light on our approach and processes.

## Salesforce Sponsored

The intent and goal of open sourcing this project is to increase the contributor and user base. However, only Salesforce employees will be given `admin` rights and will be the final arbitrars of what contributions are accepted or not.

# Getting started

# Issues, requests & ideas

Use GitHub Issues page to submit issues, enhancement requests and discuss ideas.

### Bug Reports and Fixes
-  If you find a bug, please search for it in the [Issues](https://github.com/tableau/VizQL-Data-Service/issues), and if it isn't already tracked,
   [create a new issue](https://github.com/tableau/VizQL-Data-Service/issues/new). Fill out the "Bug Report" section of the issue template. Even if an Issue is closed, feel free to comment and add details, it will still
   be reviewed. Please provide as much information as you can, including clear and concise reproduction steps, attaching any necessary files to assist in the reproduction of the bug. **Be sure to scrub the files of any potentially sensitive information. Issues are public.**
-  Issues that have already been identified as a bug (note: able to reproduce) will be labelled `bug`.
-  If you'd like to submit a fix for a bug, [send a Pull Request](#creating_a_pull_request) and mention the Issue number.
  -  Include tests that isolate the bug and verifies that it was fixed.

### New Features
-  If you'd like to add new functionality to this project, describe the problem you want to solve in a [new Issue](https://github.com/tableau/VizQL-Data-Service/issues/new).
-  Issues that have been identified as a feature request will be labelled `enhancement`.
-  If you'd like to implement the new feature, please wait for feedback from the project
   maintainers before spending too much time writing the code. In some cases, `enhancement`s may
   not align well with the project objectives at the time.

### Tests, Documentation, Miscellaneous
-  If you'd like to improve the tests, you want to make the documentation clearer, you have an
   alternative implementation of something that may have advantages over the way its currently
   done, or you have any other change, we would be happy to hear about it!
  -  If its a trivial change, go ahead and [send a Pull Request](#creating_a_pull_request) with the changes you have in mind.
  -  If not, [open an Issue](https://github.com/tableau/VizQL-Data-Service/issues/new) to discuss the idea first.

If you're new to our project and looking for some way to make your first contribution, look for
Issues labelled `good first contribution`.

### Development Setup
1. Fork and clone the repository
```bash
git clone https://github.com/tableau/VizQL-Data-Service.git
```

2. Create a virtual environment and install setup dependencies:
```bash
cd VizQL-Data-Service/python_sdk
python -m venv --system-site-packages venv
source venv/bin/activate  # On Unix/MacOS
venv\Scripts\activate     # On Windows

python -m pip install --upgrade pip # Upgrade pip
pip install -e .          # Required dependencies
pip install -e .[dev]     # Required and optional dependencies
```

3. Generate OpenAPI client:
If on a linux-based OS,
```bash
bash scripts/generate_stub.sh
```

If on Windows,
```bash
scripts\generate_stub.bat
```

See [OpenAPI Generated Models](docs/openapi_models.md) for detailed information about the generated model classes, their properties, and usage examples.

### Running Examples
```bash
# Running the existing examples synchronously and asynchronously
cd src/examples

python examples --help

# If `site` argument is left out, this will run against a default site that your token works for
# If `async` argument is left out, the default examples run synchrounously
# Auth using username and password
python examples.py --user "<username>" --password "<password>" --server "<server>"

# Auth using personal access token (PAT)
python examples.py --pat-name "<pat-name>" --pat-secret "<pat-secret>" --server "<server>" --site "<site-id>" -async

# Auth using JWT
python examples.py --jwt "<jwt-token>" --server "<server>" --site "<site-id>" -async
```

# Contribution Checklist

- [x] Clean, simple, well styled code
  - Black for code formatting
  - isort for import sorting
  - flake8 for linting
  - mypy for type check
  - Run all checks:
  ```bash
  black .
  isort .
  flake8 .
  mypy .
  ```
- [x] Commits should be atomic and messages must be descriptive. Related issues should be mentioned by Issue number.
- [x] Comments
  - Module-level & function-level comments.
  - Comments on complex blocks of code or algorithms (include references to sources).
- [x] Tests
  - Write tests for new features
  - The test suite, if provided, must be complete and pass
  - Increase code coverage, not versa.
  - Run tests with:
  ```bash
  pip install -e ".[dev]"
  pytest tests/ -v
  ```
- [x] Versioning
  - The major and minor numbers of the "version" in pyproject.toml must always be the same as the major and minor numbers of the "version" in VizQLDataServiceOpenAPISchema.json. If these values aren't the same, then the build pipeline will fail. Example: If VizQLDataServiceOpenAPISchema.json has a "version" value of "1.0", then the pyproject.toml "version" needs to be "1.0.x".
  - The patch number for the "version" in pyproject.toml must always be increased by 1 per pull request. This is to ensure proper versioning for publishing to PyPi. If this conventioned isn't followed, the publish to PyPi step will fail. Example: If pyproject.toml had a "version" value of "1.1.11", then the new pull request must have a new "version" value of "1.1.12".
- [x] Dependencies
  - Minimize number of dependencies
  - New dependencies need to have their licenses vetted and approved before merge
- [x] Reviews
  - Changes must be approved via peer code review
- [x] Documentation
  - Update README.md if needed
  - Add docstrings to new functions/classes
  - Update API Documentation
  - Add examples for new features

# Creating a Pull Request

1. **Ensure the bug/feature was not already reported** by searching on GitHub under Issues.  If none exists, create a new issue so that other contributors can keep track of what you are trying to add/fix and offer suggestions (or let you know if there is already an effort in progress).
2. **Clone** the forked repo to your machine.
3. **Create** a new branch to contain your work (e.g. `git br fix-issue-11`)
4. **Run** tests and linting
5. **Verify** that the major and minor numbers for the "version" in pyproject.toml are the same as the major and minor numbers for the "version" in VizQLDataServiceOpenAPISchema.json. If they aren't the same, the build will fail.
6. **Bump** the patch number for the "version" in pyproject.toml. This will trigger a new release to PyPi upon merge to main.
7. **Update** documentation (e.g. README.md) with details if needed.
8. **Commit** changes to your own branch.
9. **Push** your work back up to your fork. (e.g. `git push fix-issue-11`)
10. **Submit** a Pull Request against the `main` branch and refer to the issue(s) you are fixing. Try not to pollute your pull request with unintended changes. Keep it simple and small.
11. **Sign** the Salesforce CLA (you will be prompted to do so when submitting the Pull Request)
12. **Address** any review comments

> **NOTE**: Be sure to [sync your fork](https://help.github.com/articles/syncing-a-fork/) before making a pull request.

> **NOTE**: The Pull Request will be merged once at least one maintainer signs off and all tests pass

# Contributor License Agreement ("CLA")
In order to accept your pull request, we need you to submit a CLA. You only need
to do this once to work on any of Salesforce's open source projects.

Complete your CLA here: <https://cla.salesforce.com/sign-cla>

# Code of Conduct
Please follow our [Code of Conduct](CODE_OF_CONDUCT.md).

# License
By contributing your code, you agree to license your contribution under the terms of our project [LICENSE](LICENSE.txt) and to sign the [Salesforce CLA](https://cla.salesforce.com/sign-cla)