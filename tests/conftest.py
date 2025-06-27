"""
Test configuration and fixtures for wakatimer tests.
"""
import pytest
import time
import random
import tempfile
import shutil
from pathlib import Path
from unittest.mock import Mock, patch


@pytest.fixture(autouse=True)
def no_sleep(monkeypatch):
    """Disable all real sleeps to make tests fast."""
    monkeypatch.setattr(time, "sleep", lambda s: None)


@pytest.fixture(autouse=True)
def fixed_random(monkeypatch):
    """Make random functions deterministic for predictable tests."""
    # random.random -> always return 0.5 for mid-range behavior
    monkeypatch.setattr(random, "random", lambda: 0.5)
    # random.uniform(a, b) -> always return midpoint
    monkeypatch.setattr(random, "uniform", lambda a, b: (a + b) / 2)
    # random.choice -> always return first item
    monkeypatch.setattr(random, "choice", lambda seq: seq[0] if seq else None)
    # random.randint -> always return midpoint
    monkeypatch.setattr(random, "randint", lambda a, b: (a + b) // 2)


@pytest.fixture
def temp_dirs():
    """Create temporary source and destination directories."""
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        src_dir = temp_path / "source"
        dest_dir = temp_path / "destination"
        src_dir.mkdir()
        dest_dir.mkdir()
        yield src_dir, dest_dir


@pytest.fixture
def sample_project(temp_dirs):
    """Create a sample project structure for testing."""
    src_dir, dest_dir = temp_dirs
    
    # Create various file types
    (src_dir / "main.py").write_text("""
import os
import sys

def main():
    print("Hello World")
    
class Calculator:
    def add(self, a, b):
        return a + b
        
if __name__ == "__main__":
    main()
""")
    
    (src_dir / "utils.js").write_text("""
function formatDate(date) {
    return date.toISOString();
}

const API_URL = 'https://api.example.com';
""")
    
    (src_dir / "styles.css").write_text("""
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
}
""")
    
    (src_dir / "config.json").write_text('{"version": "1.0.0", "debug": true}')
    
    (src_dir / "README.md").write_text("""
# Sample Project

This is a test project for wakatimer.
""")
    
    # Create test file
    (src_dir / "test_main.py").write_text("""
import unittest
from main import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(2, 3), 5)
""")
    
    # Create binary file
    (src_dir / "image.png").write_bytes(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR')
    
    # Create subdirectory
    subdir = src_dir / "lib"
    subdir.mkdir()
    (subdir / "helper.py").write_text("def helper_func(): pass")
    
    # Create files to skip
    skip_dir = src_dir / "__pycache__"
    skip_dir.mkdir()
    (skip_dir / "main.cpython-39.pyc").write_bytes(b'\x00\x01\x02')
    
    return src_dir, dest_dir


@pytest.fixture
def mock_input_sequence():
    """Helper to mock input() with a sequence of responses."""
    def _mock_input_sequence(responses):
        responses_iter = iter(responses)
        return lambda _: next(responses_iter, "")
    return _mock_input_sequence


@pytest.fixture
def mock_time():
    """Mock time.time() to return predictable values."""
    start_time = 1640995200.0  # 2022-01-01 00:00:00 UTC
    with patch('time.time') as mock:
        mock.return_value = start_time
        yield mock
