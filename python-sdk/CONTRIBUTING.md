# Contributing to VizDataService Python Client

Thank you for your interest in contributing to the VizDataService Python Client! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please read it before contributing.

## How to Contribute

### Reporting Bugs

- Use the GitHub issue tracker
- Include a clear title and description
- Include steps to reproduce
- Include expected and actual behavior
- Include relevant logs and screenshots
- Include your environment details

### Suggesting Features

- Use the GitHub issue tracker
- Include a clear title and description
- Explain why this feature would be useful
- Include any relevant examples

### Pull Requests

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

### Development Setup

1. Fork and clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Unix/MacOS
venv\Scripts\activate     # On Windows
```

3. Install development dependencies:
```bash
pip install -r test-requirements.txt
```

4. Install the package in development mode:
```bash
pip install -e .
```

### Code Style

We use:
- Black for code formatting
- isort for import sorting
- flake8 for linting
- mypy for type checking

Run all checks:
```bash
black .
isort .
flake8
mypy .
```

### Testing

- Write tests for new features
- Ensure all tests pass
- Maintain or improve test coverage
- Run tests with:
```bash
pytest
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

## Questions?

Feel free to open an issue for any questions about contributing. 