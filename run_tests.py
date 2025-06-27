#!/usr/bin/env python3
"""
Test runner script for wakatimer.py tests.
This script runs the complete test suite and generates coverage reports.
"""

import sys
import subprocess
import os
from pathlib import Path


def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"\n{'='*60}")
    print(f"{description}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running: {cmd}")
        print(f"Exit code: {e.returncode}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        return False


def check_dependencies():
    """Check if required test dependencies are installed."""
    print("Checking test dependencies...")
    
    required_packages = ['pytest', 'pytest-cov', 'pytest-mock', 'coverage']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"Missing packages: {', '.join(missing_packages)}")
        print("Installing missing packages...")
        
        install_cmd = f"{sys.executable} -m pip install {' '.join(missing_packages)}"
        if not run_command(install_cmd, "Installing test dependencies"):
            print("Failed to install dependencies. Please install manually:")
            print(f"   pip install {' '.join(missing_packages)}")
            return False
    
    print("All test dependencies are available")
    return True


def run_tests():
    """Run the complete test suite."""
    if not check_dependencies():
        return False
    
    # Change to the project directory
    project_dir = Path(__file__).parent
    os.chdir(project_dir)
    
    print(f"Working directory: {project_dir}")
    
    # Run tests with coverage
    test_commands = [
        # Run unit tests
        (
            "python -m pytest tests/ -v --tb=short --cov=wakatimer --cov-report=term-missing --cov-report=html",
            "Running unit tests with coverage"
        ),
        
        # Generate detailed coverage report
        (
            "python -m coverage report --show-missing",
            "Generating detailed coverage report"
        ),
        
        # Run specific test categories
        (
            "python -m pytest tests/test_all.py -v",
            "Running general function and integration tests"
        ),
        
        (
            "python -m pytest tests/test_utils_visual.py -v",
            "Running utility and visual function tests"
        ),
    ]
    
    success_count = 0
    total_commands = len(test_commands)
    
    for cmd, description in test_commands:
        if run_command(cmd, description):
            success_count += 1
        else:
            print(f"Command failed: {description}")
    
    # Summary
    print(f"\n{'='*60}")
    print(f"TEST SUMMARY")
    print(f"{'='*60}")
    print(f"Successful commands: {success_count}/{total_commands}")
    
    if success_count == total_commands:
        print("All tests completed successfully!")
        print(f"Coverage report available at: {project_dir}/htmlcov/index.html")
        return True
    else:
        print(f"{total_commands - success_count} commands failed")
        return False


def main():
    """Main function."""
    print("WAKATIMER TEST SUITE")
    print("=" * 60)
    
    if run_tests():
        print("\nTest suite completed successfully!")
        sys.exit(0)
    else:
        print("\nTest suite completed with errors!")
        sys.exit(1)


if __name__ == "__main__":
    main()
