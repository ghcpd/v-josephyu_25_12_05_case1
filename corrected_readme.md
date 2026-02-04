# Flask User Login & Registration App (Corrected)

This corrected README aligns commands and configuration with the current project implementation.

Prerequisites
- Python 3.10+

Setup (Windows PowerShell)

```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Install pinned dependencies
pip install -r requirements.txt
```

Quick start (run the app)

```powershell
python app.py --host=0.0.0.0 --port=8080
```

Configuration notes
- Secret key is configured in `app.py` as `app.config['SECRET_KEY']` (you should override from `FLASK_SECRET` env var in production).
- Database path used by the application is `app.config['DATABASE']` and currently defaults to `app.db` (root of project). To change it set `app.config['DATABASE'] = 'data/database.sqlite3'` or set the `DATABASE` key before calling `init_db(app)`.

Sessions
- This project uses Flask's built-in session cookie mechanism. There is no Redis session store or `SESSIONLESS_MODE` flag implemented.

Routes
- `/` — root, redirects to `/dashboard` if authenticated, otherwise `/login`.
- `/login` — login page (GET/POST).
- `/register` — registration page (GET/POST).
- `/logout` — logs out the current user.
- `/dashboard` — login-protected page.

Forms
- Registration form requires `username` (3-32 chars), `email` (required, validated), and `password` (min 6 chars).

Notes about existing code
- `models.init_db` creates a `users` table in the configured database and attempts to add an `email` column if missing. Existing rows will have `NULL` emails after migration; handle carefully in production.

