# Flask User Login & Registration App (corrected)

This document corrects and clarifies the original README for the present code in this repository. Use these instructions to set up and run the app exactly as implemented.

Requirements
------------
- Python 3.10+ (examples in Windows PowerShell are shown where relevant)
- pip installed
- Recommended: a virtual environment (example uses `.venv`)

Project files
-------------
app.py - entrypoint and small Flask app
auth.py - authentication blueprint (register/login/logout)
models.py - SQLite models and initialization
templates/ - Jinja2 templates (login, register, dashboard, base)
requirements.txt - Python dependencies (this file has been fixed)

Quick setup (Windows PowerShell)
--------------------------------
1. Create virtual environment

```powershell
python -m venv .venv
```

2. Activate virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies

```powershell
pip install -r requirements.txt
```

Start the app
-------------
The `app.py` in this repository is a simple entrypoint. Running `python app.py` starts the development server with the default host (127.0.0.1) and port (5000):

```powershell
python app.py
# server binds to http://127.0.0.1:5000 by default
```

If you'd like to start the server on a different host/port, prefer the `flask` CLI which supports CLI host/port options. Set the environment variable first (or use your OS equivalent):

Windows PowerShell:
```powershell
$env:FLASK_APP = 'app'
flask run --host=0.0.0.0 --port=8080
```

Configuration notes
-------------------
- Database: the application uses a SQLite database file configured via `app.config['DATABASE']`. By default the code stores the DB in `app.db` at the project root (not `data/database.sqlite3`).
- Secret Key: `app.config['SECRET_KEY']` is set in `app.py` to a placeholder string. For production, load a secret from an environment variable.
- Sessions & login: this small example uses Flask's default cookie-based sessions and Flask-Login for login state. The code does not include a Redis backend.

Routes and behavior
-------------------
- `GET /` — redirects to `/dashboard` if authenticated, otherwise to `/login`.
- `GET /login` — display login form
- `POST /login` — process login
- `GET /register` — registration form (email is required in current code)
- `POST /register` — process registration; on success the user is logged in and redirected to `/dashboard`.
- `GET /logout` — logout user
- `GET /dashboard` — login-protected page showing welcome message

Notes about validation & behavior
---------------------------------
- Registration requires `email` (RegisterForm uses DataRequired on email). The field is also enforced UNIQUE NOT NULL in the SQLite schema.
- Password minimum length is enforced at 6 characters by `auth.RegisterForm` (contrary to a prior note saying 3 characters in some docs).
- The documentation previously referenced a `/profile` page — that route is not implemented in this codebase.

Testing
-------
Unit tests (pytest) are provided in `tests/test_app.py` and validate the core register/login/dashboard flows. To run the tests locally:

```powershell
.\.venv\Scripts\Activate.ps1
pytest -q
```

Wrap-up
-------
This corrected README reflects the actual implementation in `app.py`, `auth.py`, and `models.py`. If you would like, I can either:

- alter the code to match the original (example: switch DB path, add Redis sessions, implement `/profile` route, add CLI host/port parsing), or
- keep the code unchanged and update any additional docs to match the implementation.

If you want runnable examples that differ from current implementation (for example, to add Redis sessions or a profile route), I can implement those changes and re-run the verification. 
