# Makefile for wakatimer project

.PHONY: help install test coverage clean lint format

# Default target
help:
	@echo "Available targets:"
	@echo "  install-dev     - Install development dependencies"
	@echo "  test        - Run tests"
	@echo "  coverage    - Run tests with coverage report"
	@echo "  clean       - Clean temporary files"
	@echo "  lint        - Run code linting"
	@echo "  format      - Format code with black"
	@echo "  build       - Build package"
	@echo "  demo        - Run a quick demo"

# Install dependencies
# install:
# 	pip install -r requirements.txt

# Install development dependencies
install-dev:
	pip install -r requirements-test.txt

# Run tests
test:
	python -m pytest tests/ -v

# Run tests with coverage
coverage:
	python -m pytest --cov=wakatimer --cov-report=term-missing --cov-report=html

# Clean temporary files
clean:
	rm -rf __pycache__/
	rm -rf tests/__pycache__/
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf WakatimerSessions/
	rm -rf .coverage
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/

# Run code linting
lint:
	flake8 wakatimer.py tests/

# Format code
format:
	black wakatimer.py tests/

# Build package
build:
	python setup.py sdist bdist_wheel

# Upload to TestPyPI
upload-test:
	twine upload --repository testpypi dist/*

# Upload to PyPI
upload:
	twine upload dist/*

# Run a quick demo
demo:
	@echo "Creating demo project..."
	@mkdir -p demo/source demo/dest
	@echo "print('Hello, World!')" > demo/source/hello.py
	@echo "console.log('Hello!');" > demo/source/hello.js
	@echo "Running wakatimer demo..."
	python wakatimer.py demo/source demo/dest --mode manual --hours 0.1
	@echo "Demo complete! Check demo/dest/"
