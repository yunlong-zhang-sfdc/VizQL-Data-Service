# Contributing to VizQL Data Service Python Client

Thank you for your interest in contributing to the VizQL Data Service Python Client! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please read it before contributing.

## How to Contribute
Contribution can include, but are not limited to, any of the following:

* File an Issue
* Request a Feature
* Implement a Requested Feature
* Fix an Issue/Bug
* Add/Fix documentation

## Issues and Feature Requests

To submit an issue/bug report, or to request a feature, please submit a [GitHub issue](https://github.com/tableau/VizQL-Data-Service/issues) to the repo.

If you are submitting a bug report, please provide as much information as you can, including clear and concise repro steps, attaching any necessary
files to assist in the repro.  **Be sure to scrub the files of any potentially sensitive information. Issues are public.**

For a feature request, please try to describe the scenario you are trying to accomplish that requires the feature. This will help us understand
the limitations that you are running into, and provide us with a use case to know if we've satisfied your request.

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

pip install -e .          # Required dependencies
pip install -e .[dev]     # Required and optional dependencies
```

3. Generate OpenAPI client:
```bash
bash scripts/generate.sh
```
See [OpenAPI Generated Models](docs/openapi_models.md) for detailed information about the generated model classes, their properties, and usage examples.


### Running Examples

```bash
# Running the existing examples synchronously and asynchronously
cd src/examples

# Auth using username and password
python sync_examples.py -u "<username>" -p "<password>" -s "<server>"
python async_examples.py -u "<username>" -p "<password>" -s "<server>"

# Auth using personal access token
python sync_examples.py -n "<pat-name>" -t "<pat-secret>" -s "<server>"
python async_examples.py -n "<pat-name>" -t "<pat-secret>" -s "<server>"
```

### Code Style

We use:
- Black for code formatting
- isort for import sorting
- flake8 for linting
- mypy for type check

Run all checks:
```bash
black .
isort .
flake8 .
mypy .
```

### Testing

- Write tests for new features
- Ensure all tests pass
- Maintain or improve test coverage
- Run tests with:
```bash
pip install -e ".[dev]"
pytest tests/ -v
```

### Documentation

- Update README.md if needed
- Add docstrings to new functions/classes
- Update API documentation
- Add examples for new features

### Commit Messages

- Use clear, descriptive commit messages
- Reference issues and pull requests
- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")

### Pull Request Process

1. Update the README.md with details of changes if needed
2. Update the documentation with details of any new features
3. The PR will be merged once you have the sign-off of at least one maintainer
4. The PR will be merged once all tests pass

## Development Workflow

1. Create a new branch for your feature
2. Make your changes
3. Run tests and linting
4. Submit a pull request
5. Address any review comments
6. Once approved, your PR will be merged
