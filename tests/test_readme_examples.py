import os
import sys
import tempfile
import sqlite3
import pytest
# Ensure project root is on sys.path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app, init_db, get_connection


@pytest.fixture
def client():
    app.config['TESTING'] = True
    # Disable CSRF for testing form submissions
    app.config['WTF_CSRF_ENABLED'] = False
    # Use a temp database file
    db_fd, db_path = tempfile.mkstemp(suffix='.sqlite3')
    os.close(db_fd)
    app.config['DATABASE'] = db_path
    # Re-init DB
    init_db(app)
    with app.test_client() as client:
        yield client
    try:
        os.remove(db_path)
    except Exception:
        pass


def test_root_redirects_to_login_when_not_authenticated(client):
    resp = client.get('/')
    assert resp.status_code in (302, 301)
    assert resp.headers['Location'].endswith('/login')


def test_register_rejects_short_password(client):
    # The app requires minimum password length 6; short passwords should fail
    resp = client.post('/register', data={
        'username': 'rtest',
        'email': 'rtest@example.com',
        'password': 'abc',  # too short
        'submit': 'Register'
    }, follow_redirects=True)
    # Registration should not log the user in
    assert b'You are logged in' not in resp.data
    # The form should display a validation error for password (contains 'between 6')
    assert b'between 6' in resp.data


def test_register_requires_email(client):
    # Email is required by the registration form
    resp = client.post('/register', data={
        'username': 'etest',
        'email': '',
        'password': 'abcdef',
        'submit': 'Register'
    }, follow_redirects=True)
    # Registration should not succeed without email
    assert b'You are logged in' not in resp.data
    assert b'This field is required.' in resp.data


def test_database_path_matches_readme():
    # Reload app module to check default configuration (without test fixture override)
    import importlib
    import app as app_module
    importlib.reload(app_module)
    assert app_module.app.config.get('DATABASE') == 'app.db'
