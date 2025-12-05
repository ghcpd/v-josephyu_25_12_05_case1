"""
Manual Testing Guide for Flask Login Application

This file documents manual test cases to validate the application works as expected.
Run these tests after starting the app with: python app.py

All tests should be performed on: http://127.0.0.1:5000
"""

# TEST CASE 1: Access Login Page
# ==============================
# Steps:
#   1. Navigate to http://127.0.0.1:5000/login
#   2. Verify login form is displayed
#   3. Form should contain: Username field, Password field, Submit button, Register link
# Expected Result: ✓ PASS - Login page displays correctly


# TEST CASE 2: Access Register Page
# ==================================
# Steps:
#   1. Navigate to http://127.0.0.1:5000/register
#   2. Verify registration form is displayed
#   3. Form should contain: Username, Email, Password fields, Submit button
# Expected Result: ✓ PASS - Registration page displays correctly


# TEST CASE 3: Root Redirect (Unauthenticated)
# =============================================
# Steps:
#   1. Clear browser cookies (or use private mode)
#   2. Navigate to http://127.0.0.1:5000/
# Expected Result: ✓ PASS - Should redirect to /login


# TEST CASE 4: Register New User
# ===============================
# Steps:
#   1. Navigate to /register
#   2. Enter username: test_user_001
#   3. Enter email: testuser001@example.com
#   4. Enter password: TestPassword123
#   5. Click Submit
# Expected Result: ✓ PASS - Redirects to dashboard, user is logged in


# TEST CASE 5: Register with Duplicate Username
# ==============================================
# Steps:
#   1. Register user1 with username "duplicate_test"
#   2. Try to register another user with same username
#   3. Observe error message
# Expected Result: ✓ PASS - Error message: "Username is already taken"


# TEST CASE 6: Login with Valid Credentials
# ==========================================
# Steps:
#   1. Navigate to /login
#   2. Enter username: test_user_001 (from TEST CASE 4)
#   3. Enter password: TestPassword123
#   4. Click Submit
# Expected Result: ✓ PASS - Redirects to /dashboard, shows welcome message


# TEST CASE 7: Login with Invalid Password
# =========================================
# Steps:
#   1. Navigate to /login
#   2. Enter username: test_user_001
#   3. Enter password: WrongPassword
#   4. Click Submit
# Expected Result: ✓ PASS - Error message: "Invalid username or password"


# TEST CASE 8: Login with Nonexistent User
# =========================================
# Steps:
#   1. Navigate to /login
#   2. Enter username: nonexistent_user
#   3. Enter password: anypassword
#   4. Click Submit
# Expected Result: ✓ PASS - Error message: "Invalid username or password"


# TEST CASE 9: Dashboard Access (Authenticated)
# =============================================
# Steps:
#   1. Login successfully (TEST CASE 6)
#   2. Verify dashboard displays
#   3. Dashboard should show: Welcome message with username, Logout button
# Expected Result: ✓ PASS - Dashboard displays user info and logout button


# TEST CASE 10: Dashboard Access (Unauthenticated)
# ================================================
# Steps:
#   1. Clear all cookies or use private browser window
#   2. Navigate directly to http://127.0.0.1:5000/dashboard
# Expected Result: ✓ PASS - Redirects to /login (protected route)


# TEST CASE 11: Logout Functionality
# ==================================
# Steps:
#   1. Login successfully (TEST CASE 6)
#   2. Click "Log Out" button on dashboard
#   3. Observe redirect
# Expected Result: ✓ PASS - Redirects to /login, session is cleared


# TEST CASE 12: Username Validation (Too Short)
# =============================================
# Steps:
#   1. Navigate to /register
#   2. Enter username: ab (2 characters)
#   3. Enter email: valid@example.com
#   4. Enter password: password123
#   5. Click Submit
# Expected Result: ✓ PASS - Validation error (username must be 3+ chars)


# TEST CASE 13: Username Validation (Maximum Length)
# =================================================
# Steps:
#   1. Navigate to /register
#   2. Enter very long username (> 32 chars)
#   3. Submit form
# Expected Result: ✓ PASS - Validation error (username must be <= 32 chars)


# TEST CASE 14: Email Validation
# ==============================
# Steps:
#   1. Navigate to /register
#   2. Enter username: valid_user
#   3. Enter email: not-an-email (invalid format)
#   4. Click Submit
# Expected Result: ✓ PASS - Validation error (invalid email format)


# TEST CASE 15: Password Validation (Too Short)
# ============================================
# Steps:
#   1. Navigate to /register
#   2. Enter username: new_user
#   3. Enter email: valid@example.com
#   4. Enter password: short (5 chars)
#   5. Click Submit
# Expected Result: ✓ PASS - Validation error (password must be 6+ chars)


# TEST CASE 16: Duplicate Email Registration
# ==========================================
# Steps:
#   1. Register user1 with email "duplicate@example.com"
#   2. Register user2 with different username but same email
# Expected Result: ✓ PASS - Error message about email already registered


# TEST CASE 17: Database Persistence
# ==================================
# Steps:
#   1. Register a user
#   2. Stop the Flask app (Ctrl+C)
#   3. Start the app again (python app.py)
#   4. Try to login with the same user
# Expected Result: ✓ PASS - User data persists in app.db


# TEST CASE 18: CSRF Protection
# =============================
# Steps:
#   1. Get the login form (GET /login)
#   2. Observe hidden CSRF token
#   3. Submit form without CSRF token
# Expected Result: ✓ PASS - Request should include CSRF token for security


# TEST CASE 19: Form Error Display
# ================================
# Steps:
#   1. Navigate to /register
#   2. Leave all fields empty
#   3. Click Submit
# Expected Result: ✓ PASS - Error messages displayed for all required fields


# TEST CASE 20: Session Timeout
# =============================
# Steps:
#   1. Login successfully
#   2. Wait for session to timeout (Flask default is 1 month)
#   3. Try to access /dashboard
# Expected Result: ✓ PASS - May redirect to login depending on session timeout


# AUTOMATED TEST EXECUTION
# ========================
# Run all tests automatically with:
#   Windows: .\run_tests.ps1
#   Linux/macOS: bash run_tests.sh
#
# Individual test class execution:
#   python -m pytest test_full_app.py::TestLogin -v
#   python -m pytest test_full_app.py::TestRegistration -v
#   python -m pytest test_full_app.py -v


# SUMMARY
# =======
# Total Manual Test Cases: 20
# Total Automated Test Cases: 26
# Expected Result: ALL PASS
