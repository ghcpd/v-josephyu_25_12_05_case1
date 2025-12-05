# Flask User Login & Registration App (Corrected)

This document corrects and clarifies the original README so the documented commands and behavior match the repository implementation.

Key corrections:
- The SQLite database path used by the code is `app.config['DATABASE'] = 'app.db'`, not `data/database.sqlite3`.
- Sessions are managed by Flask's session cookie and Flask-Login; there is no Redis integration in this repository.
- `SESSIONLESS_MODE` is not implemented; setting it has no effect.
- Password minimum length enforced by the application is 6 characters (WTForms validator), not 3.
- The registration form requires an `email` (DataRequired), it is not optional.
- The app does not implement a `/profile` route.
- Running `python app.py --host=... --port=...` will not change bind options unless you modify `app.py` to parse command-line args (see example below).

-- Installation & Run (Windows PowerShell) --

Create virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Start the app (default behavior from `app.py`):

```powershell
python app.py
# This will run with debug=True and default host=127.0.0.1 port=5000
```

If you want to run with a specific host/port, either use `flask run` or extend `app.py`.

With flask run (recommended for development):

```powershell
set FLASK_APP=app
flask run --host=0.0.0.0 --port=8080
```

Or modify `app.py` to use argparse to accept CLI host/port options; for example:

```python
if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('--host', default='127.0.0.1')
	parser.add_argument('--port', default=5000, type=int)
	args = parser.parse_args()
	app.run(debug=True, host=args.host, port=args.port)
```

-- Behavior Notes --

- Database: `app.db` at project root by default. You can change `app.config['DATABASE']` to another path or set up a `data/` directory and adjust the config.
- Passwords are required to be at least 6 characters long.
- Email is required on registration.
- There is no `/profile` route implemented.

-- Tests and Setup Scripts --

- `test_files/test_app.py` contains pytest tests that validate the application behavior and document mismatches.
- Use `setup.ps1` / `setup.sh` to create the venv and install requirements.
- Use `run_tests.ps1` / `run_tests.sh` to run pytest.

