# Test Data Files for Flask Login Application

This directory contains test files and scripts for validating the Flask Login application.

## Files

### Test Cases Documentation

**valid_users.json** - Valid user data for registration/login tests
**invalid_inputs.json** - Invalid inputs to test form validation
**integration_tests.py** - Integration test scenarios

## Usage

1. Use these test files to validate the application manually
2. Run the automated test suite with: `python -m pytest test_full_app.py`

## Test Coverage

- ✓ User Registration (valid/invalid)
- ✓ User Login (valid/invalid credentials)
- ✓ User Logout
- ✓ Dashboard Access (authenticated only)
- ✓ Form Validation
- ✓ Database Operations
- ✓ Session Management
- ✓ CSRF Protection

All tests should pass when run with: `.\run_tests.ps1` (Windows) or `bash run_tests.sh` (Linux/macOS)
