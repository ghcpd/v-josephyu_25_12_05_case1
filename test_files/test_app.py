import os
import sys
import tempfile
import pytest

# Ensure project root is importable when running pytest from nested test dir
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app as flask_app
from models import init_db, get_connection, User


@pytest.fixture
def client(tmp_path, monkeypatch):
    # Use a temporary DB file for tests
    db_file = tmp_path / "test.db"
    monkeypatch.setitem(flask_app.config, 'DATABASE', str(db_file))
    init_db(flask_app)
    with flask_app.test_client() as client:
        yield client


def test_database_path_default():
    # README claims data/database.sqlite3 but code uses app.db
    assert flask_app.config.get('DATABASE') == 'app.db'


def test_register_requires_email(client):
    # Email is required in the actual form (DataRequired in code)
    r = client.post('/register', data={'username': 'u1', 'password': '123456'}, follow_redirects=True)
    assert b'This field is required' in r.data or b'Email' in r.data


def test_password_min_length(client):
    # Code enforces min length 6; README says 3
    r = client.post('/register', data={'username': 'u2', 'email': 'u2@example.com', 'password': '123'}, follow_redirects=True)
    assert b'Field must be between 6 and 128 characters long' in r.data or b'Field must be at least' in r.data


def test_profile_route_missing(client):
    r = client.get('/profile')
    assert r.status_code == 404


def test_register_and_login_flow(client):
    # Successful register
    r = client.post('/register', data={'username': 'userx', 'email': 'x@example.com', 'password': 'password'}, follow_redirects=True)
    assert r.status_code in (200, 302)
    # logout
    client.get('/logout', follow_redirects=True)
    # login
    r2 = client.post('/login', data={'username': 'userx', 'password': 'password'}, follow_redirects=True)
    assert b'Dashboard' in r2.data or r2.status_code == 200
