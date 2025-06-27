# Changelog

## [2.0.2] - 2025-06-27

### 🔧 Improvements
- Updated command usage in main function and improved argument handling

## [2.0.1] - 2025-06-26

### 🧪 Testing Improvements & Documentation

- Added `run_tests.py` script for automated test running and coverage reporting.
- Updated README with detailed testing and coverage instructions.
- Fixed all script references to use `wakatimer.py` (not `wakatimer_simulator.py`).
- Ensured all test files in `tests/` are included in the test suite.
- Improved developer setup instructions for testing and coverage.


## [2.0.0] - 2024-12-25

### 🎉 Major Release - Complete Rewrite

#### ✨ New Features

**Interactive Experience**
- Beautiful ASCII logo and branding
- Interactive setup mode with guided configuration
- Real-time visual progress bars with language-specific icons
- Project analysis and execution plan preview

**Project Templates**
- Web Application template (optimized for frontend/backend)
- Data Science template (optimized for ML/analytics)
- Custom template support with JSON configuration
- Template-specific typing speeds and behavior patterns

**Resume Capability**
- Save and resume long simulations
- Session state persistence with pickle
- Automatic cleanup on completion
- Progress tracking across sessions

**Advanced Simulation**
- Testing cycles (write → test → fail → fix → pass)
- Research pauses for complex problems
- Copy-paste simulation for realistic speed variations
- Enhanced refactoring phases with multiple file revisits

**File Management**
- Flexible ignore patterns via command line
- Smart file dependency analysis and ordering
- Partial simulation support
- Better binary file handling

**Analytics & Reporting**
- Visual timeline charts with hourly breakdowns
- Enhanced CSV exports with detailed metrics
- Comprehensive JSON reports
- Language-specific productivity analysis
- Session statistics and performance metrics

#### 🔧 Improvements

**Core Engine**
- Better language detection (40+ languages)
- Complexity-aware typing speeds
- Improved grace period compliance
- More realistic human behavior patterns

**User Experience**
- Comprehensive command line options
- Better error handling and validation
- Detailed progress feedback
- Professional output formatting

**Performance**
- Optimized file processing
- Reduced memory usage for large projects
- Faster binary file handling
- Configurable feature toggles

#### 🐛 Bug Fixes
- Fixed grace period violations in long delays
- Improved file path handling on Windows
- Better error recovery for corrupted sessions
- Fixed typing speed calculations for edge cases

#### 📚 Documentation
- Complete README rewrite with examples
- Command line reference guide
- Troubleshooting section
- Development setup instructions

---

## [1.0.0] - 2024-12-20

### 🚀 Initial Release

#### ✨ Features
- Basic auto and manual simulation modes
- Language detection and file analysis
- Human-like typing patterns with delays
- Grace period compliance for WakaTime compatibility
- Simple analytics and reporting
- File categorization (code vs binary)
- Basic refactoring simulation
- CSV export functionality

#### 🎯 Core Capabilities
- Retroactive time tracking data generation
- Realistic coding behavior simulation
- Multiple programming language support
- Configurable typing speeds
- Basic debugging phase simulation

---

## Versioning

This project follows [Semantic Versioning](https://semver.org/):
- **MAJOR** version for incompatible API changes
- **MINOR** version for backwards-compatible functionality additions  
- **PATCH** version for backwards-compatible bug fixes

## Contributing

See [README.md](README.md) and [CONTRIBUTING.md](CONTRIBUTING.md)  for contribution guidelines and development setup instructions.
