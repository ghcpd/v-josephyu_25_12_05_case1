# Flask User Login & Registration App

This project is a simple Flask-based user registration and login example. It includes:

- User registration, login, and logout
- A login-protected dashboard page at `/dashboard`
- A local SQLite database file `app.db`
- Session management via Flask-Login

This README describes the current implementation of the app based on the existing code in `app.py`, `auth.py`, and `models.py`.

**Note:** This is a CORRECTED version. See `defects.txt` for issues found in the original README.

---

## 1. Requirements

- Python 3.10+ (examples below use Windows PowerShell)
- `pip` installed
- Recommended: a virtual environment to isolate dependencies

---

## 2. Project Structure

```text
.
├─ app.py               # App entrypoint, blueprints, login config, Flask startup
├─ auth.py              # Auth blueprint: register, login, logout
├─ models.py            # Database models and initialization logic
├─ templates/
│  ├─ base.html         # Base layout
│  ├─ login.html        # Login page
│  ├─ register.html     # Registration page
│  └─ dashboard.html    # Dashboard page after login
├─ requirements.txt     # Python dependencies
├─ test_full_app.py     # Comprehensive test suite
├─ setup.ps1            # Windows PowerShell setup script
├─ setup.sh             # Bash setup script (Linux/macOS)
├─ run_tests.ps1        # Windows PowerShell test runner
├─ run_tests.sh         # Bash test runner (Linux/macOS)
└─ README.md            # This documentation
```

---

## 3. Installation & Run

The following commands assume Windows PowerShell. First, change to the project directory.

### 3.1 Option A: Automatic Setup (Recommended)

**Windows PowerShell:**
```powershell
.\setup.ps1
```

**Linux/macOS (Bash):**
```bash
bash setup.sh
```

This script will:
1. Create and activate virtual environment
2. Install dependencies
3. Initialize the database
4. Display startup instructions

### 3.2 Option B: Manual Setup

#### Create and Activate Virtual Environment (Windows PowerShell)

```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.\\.venv\\Scripts\\Activate.ps1
```

#### Create and Activate Virtual Environment (Linux/macOS)

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate
```

#### Install Dependencies

Preferred: use `requirements.txt`:

```powershell
pip install -r requirements.txt
```

### 3.3 Start the App

**CORRECTED:** The app runs on the default Flask port (5000) with debug mode enabled.

```powershell
python app.py
```

**Output:**
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000/
 * Press CTRL+C to quit
```

**Note:** Command-line arguments (`--host`, `--port`) are NOT supported. To change the host or port, modify `app.py`:

```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)  # Example: run on all interfaces, port 8080
```

### 3.4 Access the Application

Open in your browser:

- Root (auto-redirect): `http://127.0.0.1:5000/`
- Login page: `http://127.0.0.1:5000/login`
- Register page: `http://127.0.0.1:5000/register`
- Dashboard (after login): `http://127.0.0.1:5000/dashboard`

---

## 4. Configuration

All critical configuration lives in `app.py`.

### 4.1 Secret Key

Used for sessions and CSRF protection:

```python
app = Flask(__name__)
app.config['SECRET_KEY'] = 'replace-with-a-strong-secret-key'
```

**CORRECTED:** The current implementation uses a hardcoded secret key. For production, implement environment variable support:

```python
import os
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET', 'replace-with-a-strong-secret-key')
```

- For production: Set `FLASK_SECRET` environment variable with a strong, random value
- For development: The default value is used if environment variable is not set

### 4.2 Database

The project uses a SQLite database configured in `app.py`:

```python
app.config['DATABASE'] = 'app.db'
```

**CORRECTED - Database Configuration:**
- **Database file name:** `app.db`
- **Location:** Project root (NOT in a `data/` subdirectory as previously documented)
- **Automatic initialization:** `init_db(app)` creates the database and tables on startup if they do not exist

#### Database Location
```
project-root/
├─ app.db          # ← Database file (created automatically)
├─ app.py
├─ auth.py
├─ models.py
└─ templates/
```

### 4.3 Sessions & Login

- Uses `Flask-Login` to manage user login state
- **CORRECTED - Session Storage:** Sessions use Flask's default secure cookie-based session store (NOT Redis as previously documented)
- Login view name: `auth.login`, mapped to `/login`
- For development: Default in-memory session handling is sufficient
- For production: Consider implementing persistent session storage

**Note:** `SESSIONLESS_MODE` environment variable mentioned in previous documentation is NOT implemented in the current code.

---

## 5. Routes & Behavior

### 5.1 Available Routes

Blueprints and entry routes defined in `app.py`:

- `/` (root): 
  - If user is authenticated: redirects to `/dashboard`
  - If not authenticated: redirects to `/login`
- `/dashboard`: login-protected homepage (shows username)

Authentication routes via `auth_bp` (defined in `auth.py`):

- `/register`: User registration page (GET / POST)
- `/login`: User login page (GET / POST)
- `/logout`: Log out current user (requires login)

### 5.2 Complete Route Summary

| Route | Method | Authentication | Purpose |
|-------|--------|-----------------|---------|
| `/` | GET | - | Redirect based on login state |
| `/login` | GET | - | Display login form |
| `/login` | POST | - | Process login |
| `/register` | GET | - | Display registration form |
| `/register` | POST | - | Process registration |
| `/logout` | GET | Required | Log out user |
| `/dashboard` | GET | Required | Show authenticated user dashboard |

**Note:** The `/profile` route mentioned in some documentation is NOT currently implemented.

---

## 6. Forms and Validation Rules

The exact implementations live in `auth.py` and `models.py`. The following summarizes the expected behavior based on the current code.

### 6.1 Registration (`/register`)

**CORRECTED Validation Rules:**

| Field | Required | Min Length | Max Length | Rules |
|-------|----------|-----------|-----------|-------|
| Username | Yes | 3 | 32 | Must be unique |
| Email | Yes | - | 255 | Must be valid email format, must be unique |
| Password | Yes | 6 | 128 | Stored as secure hash (bcrypt-compatible) |

**Validation Details:**
- `username`: 3-32 characters, alphanumeric + common symbols
- `email`: Must be valid email format (validates domain structure)
- `password`: Minimum 6 characters (NOT 3 as previously documented)
- Both username and email must be unique in the database

**Example Registration:**
```
Username: john_doe
Email: john@example.com
Password: SecurePassword123
```

### 6.2 Login (`/login`)

**Validation Rules:**

| Field | Required | Rules |
|-------|----------|-------|
| Username | Yes | Exact match with registered username |
| Password | Yes | Must match stored password hash |

**Login Logic:**
1. User enters username and password
2. System looks up user by username
3. If found, verify password against stored hash
4. On success: Log user in and redirect to `/dashboard`
5. On failure: Display error message "Invalid username or password"

**Example Login:**
```
Username: john_doe
Password: SecurePassword123
```

---

## 7. Data Model & Persistence

`models.py` is responsible for:

- Creating connections to the SQLite database
- Defining the `User` model with fields: `id`, `username`, `email`, `password_hash`
- Providing user operations:
  - `User.create(conn, username, password, email)` - Create new user
  - `User.get_by_id(conn, user_id)` - Retrieve user by ID
  - `User.get_by_username(conn, username)` - Retrieve user by username
  - `User.verify_password(password)` - Verify password against hash

`app.py` wires up `Flask-Login` with a `user_loader` function:

```python
@login_manager.user_loader
def load_user(user_id):
    conn = get_connection(app)
    user = User.get_by_id(conn, int(user_id))
    conn.close()
    return user
```

### 7.1 User Table Schema

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
```

**Fields:**
- `id`: Auto-incrementing primary key
- `username`: Unique, required, text
- `password_hash`: Required, text (bcrypt hash)
- `email`: Unique, required, text

### 7.2 Password Security

Passwords are hashed using Werkzeug's security utilities (PBKDF2 based):
- Never stored in plain text
- Verified using constant-time comparison
- Hash includes salt to prevent rainbow table attacks

---

## 8. Testing

### 8.1 Run All Tests

**Windows PowerShell:**
```powershell
.\run_tests.ps1
```

**Linux/macOS (Bash):**
```bash
bash run_tests.sh
```

### 8.2 Run Specific Test Class

```powershell
python -m pytest test_full_app.py::TestLogin -v
```

### 8.3 Run with Coverage

```powershell
python -m pytest test_full_app.py --cov=app --cov=auth --cov=models
```

### 8.4 Test Coverage

The test suite (`test_full_app.py`) covers:
- ✅ Application startup and configuration
- ✅ Route accessibility and redirects
- ✅ User registration (valid/invalid cases)
- ✅ User login (valid/invalid credentials)
- ✅ Logout functionality
- ✅ Form validation
- ✅ Database operations (CRUD)
- ✅ Password hashing security
- ✅ Documentation compliance

**Expected Test Results:** All 25 tests should pass.

---

## 9. Development Workflow

### 9.1 First Time Setup

```powershell
# 1. Clone/download project
# 2. Navigate to project directory
cd path/to/project

# 3. Run setup script
.\setup.ps1

# 4. Activate environment
.\\.venv\\Scripts\\Activate.ps1

# 5. Start app
python app.py
```

### 9.2 Regular Development

```powershell
# Activate environment
.\\.venv\\Scripts\\Activate.ps1

# Start app (with auto-reload on code changes)
python app.py

# Run tests (separate terminal)
python -m pytest test_full_app.py -v
```

### 9.3 Adding Dependencies

```powershell
# Install new package
pip install package-name

# Update requirements.txt
pip freeze > requirements.txt
```

---

## 10. Troubleshooting

### Issue: "Database is locked"
- **Cause:** Multiple Flask processes accessing database
- **Solution:** Close all instances and restart

### Issue: "Secret key error" when running tests
- **Cause:** Tests require SECRET_KEY to be set
- **Solution:** Already configured in `app.config`

### Issue: "Import Error: No module named 'flask'"
- **Cause:** Virtual environment not activated
- **Solution:** Run `.\\.venv\\Scripts\\Activate.ps1`

### Issue: Email validation fails
- **Cause:** `email_validator` not installed
- **Solution:** Run `pip install email_validator` (included in requirements.txt)

### Issue: Port 5000 already in use
- **Cause:** Another application is using port 5000
- **Solution:** Modify `app.py` line 30: `app.run(debug=True, port=8080)`

---

## 11. Production Deployment Notes

This app is designed for development. For production deployment:

1. **Set SECRET_KEY environment variable** with a strong, random value
2. **Disable debug mode:** Change `debug=True` to `debug=False`
3. **Use a production WSGI server:** (Gunicorn, uWSGI, etc.)
4. **Implement persistent session storage:** (Redis, database, etc.)
5. **Use HTTPS:** Configure proper SSL certificates
6. **Database:** Consider PostgreSQL or MySQL instead of SQLite
7. **Logging:** Implement proper application logging

---

## 12. Summary of Corrections from Original README

**Major Changes:**
1. ✅ **Database Path:** Clarified as `app.db` in project root, NOT `data/database.sqlite3`
2. ✅ **Command-line Arguments:** Documented that `--host` and `--port` are NOT supported; provided code example to modify these
3. ✅ **Password Validation:** Corrected minimum length from "3 characters" to "6 characters"
4. ✅ **Profile Route:** Removed from route list (not implemented)
5. ✅ **Session Storage:** Clarified as Flask secure cookies, NOT Redis
6. ✅ **SECRET_KEY:** Corrected to show hardcoded value (not environment variable in current code)
7. ✅ **Browser URLs:** All consistently show port 5000
8. ✅ **SESSIONLESS_MODE:** Removed references (not implemented)

**Additions:**
- ✅ Added setup scripts (`setup.ps1`, `setup.sh`)
- ✅ Added test runner scripts (`run_tests.ps1`, `run_tests.sh`)
- ✅ Added comprehensive test suite (`test_full_app.py`)
- ✅ Added troubleshooting section
- ✅ Added production deployment notes
- ✅ Added route summary table
- ✅ Added validation rules table

---

## 13. Files Modified/Added

- ✅ `corrected_readme.md` - This file
- ✅ `defects.txt` - Detailed list of defects found
- ✅ `test_full_app.py` - Comprehensive test suite
- ✅ `setup.ps1` - Windows setup script
- ✅ `setup.sh` - Bash setup script
- ✅ `run_tests.ps1` - Windows test runner
- ✅ `run_tests.sh` - Bash test runner

---

## License

This is a demonstration project for educational purposes.

