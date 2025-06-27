# Contributing to Wakatimer

Thank you for your interest in contributing to Wakatimer! This document provides guidelines for contributing to the project.

## Development Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/sukarth/Wakatimer.git
    cd Wakatimer
    ```

2.  **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install the package in editable mode with development dependencies**:
    This command installs the project and the dependencies needed for testing.
    ```bash
    pip install -e .[dev]
    ```

## Running Tests

All tests can be run using the `run_tests.py` script. This will execute the test suite with `pytest` and generate a coverage report.

```bash
python run_tests.py
```

Alternatively, you can run tests manually with `pytest`:

-   **Run all tests**:
    ```bash
    pytest
    ```

-   **Run tests with coverage report**:
    ```bash
    pytest --cov=wakatimer --cov-report=term-missing
    ```

Current test coverage: **98%**

## Code Quality

This project follows Python best practices:

- **PEP 8** style guidelines
- **Type hints** where appropriate
- **Comprehensive testing** (98% coverage)
- **Clear documentation**

### Linting and Formatting

```bash
# Check code style
flake8 wakatimer.py tests/

# Format code
black wakatimer.py tests/
```

## Making Changes

1. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and add tests for new functionality

3. Ensure all tests pass:
   ```bash
   python -m pytest tests/
   ```

4. Ensure code quality:
   ```bash
   flake8 wakatimer.py tests/
   black wakatimer.py tests/
   ```

5. Update documentation if needed

6. Commit your changes with a clear message:
   ```bash
   git commit -m "Add feature: description of your changes"
   ```

7. Push to your fork and create a pull request

## Pull Request Guidelines

- **Clear description**: Explain what your PR does and why
- **Tests included**: Add tests for new functionality
- **Documentation updated**: Update README.md or other docs as needed
- **Code quality**: Ensure linting passes and code follows project standards
- **Small, focused changes**: Keep PRs focused on a single feature/fix

## Testing Guidelines

- Write tests for all new functionality
- Maintain or improve test coverage
- Use descriptive test names
- Include both positive and negative test cases
- Test edge cases and error conditions

## Project Structure

```
wakatimer/
├── wakatimer.py          # Main application code
├── tests/                # Test files
│   ├── conftest.py      # Pytest configuration
│   ├── test_all.py      # General and integration tests
│   └── test_utils_visual.py # Utility and visual function tests
├── templates/           # Project templates
├── requirements.txt     # (Not explicitly used for runtime dependencies; handled by setup.py)
├── requirements-test.txt # Development dependencies
├── setup.py            # Package setup
├── pytest.ini         # Pytest configuration
├── .gitignore         # Git ignore rules
├── README.md          # Project documentation
├── CHANGELOG.md       # Version history
├── LICENSE            # License information
└── CONTRIBUTING.md    # This file
```

## Reporting Issues

When reporting issues:

1. Use a clear, descriptive title
2. Provide steps to reproduce the issue
3. Include your environment details (OS, Python version)
4. Share relevant error messages or logs
5. Include minimal code examples if applicable

## Feature Requests

For feature requests:

1. Check if the feature already exists or is planned
2. Clearly describe the feature and its use case
3. Explain why it would be valuable
4. Consider contributing the implementation!

## Questions?

Feel free to open an issue for questions about:
- How to use wakatimer
- Development setup
- Contributing guidelines
- Feature ideas

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
