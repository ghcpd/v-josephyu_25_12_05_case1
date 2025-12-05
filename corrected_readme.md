# Corrected README — Flask User Login & Registration App

This corrected README aligns with the current implementation in app.py, auth.py, and models.py.

## 1. Requirements
- Python 3.10+
- pip installed
- Create and activate a virtual environment and install dependencies from requirements.txt before running the app or tests.

## 2. Installation & Run (Windows PowerShell examples)
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Start the app (optional flags to change host/port)
python app.py --host=0.0.0.0 --port=8080

Default behavior (when run without flags):
- Binds to http://127.0.0.1:5000/ (Flask default)
- Use --host and --port to change bind address and port.

## 3. Configuration
### Secret Key
app.config['SECRET_KEY'] is used for sessions and CSRF protection. Set FLASK_SECRET to override in production.

### Database
- Database file name: `app.db`
- Location: project root (file `app.db`)
- To change location, update app.config['DATABASE'] in app.py and ensure the target directory exists.

## 4. Registration & Login
- `email` is required and must be a valid email address.
- Minimum password length for development: 6 characters (enforced by validators in auth.py)

## 5. Sessions
- The current implementation uses server-side sessions via Flask; Redis is not configured by default. If you want Redis-backed sessions, add configuration and the Redis session extension.

## 6. Routes
- `GET /` — root, redirects to `/dashboard` if authenticated, otherwise `/login`
- `GET /login`, `POST /login`, `GET /register`, `POST /register`, `GET /logout`, `GET /dashboard`.

