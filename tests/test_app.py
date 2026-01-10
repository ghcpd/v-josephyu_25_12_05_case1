import os
import tempfile

import pytest

from app import app as flask_app
from models import init_db


@pytest.fixture
def client(tmp_path):
    # Use a temporary file for database to isolate tests
    db_file = tmp_path / "test_db.sqlite3"
    flask_app.config['TESTING'] = True
    # Disable CSRF in tests so posts don't require tokens
    flask_app.config['WTF_CSRF_ENABLED'] = False
    flask_app.config['DATABASE'] = str(db_file)
    # initialize fresh schema
    init_db(flask_app)

    with flask_app.test_client() as client:
        yield client


def test_root_redirects_to_login(client):
    rv = client.get('/', follow_redirects=False)
    assert rv.status_code in (301, 302)
    assert '/login' in rv.headers['Location']


def test_register_and_dashboard_flow(client):
    # register a new user
    rv = client.post('/register', data={
        'username': 'tester1',
        'email': 'tester1@example.com',
        'password': 'password123',
    }, follow_redirects=True)
    # after registration user should be redirected to dashboard and see a welcome message
    assert b'Welcome' in rv.data or b'You are logged in' in rv.data

    # accessing dashboard should succeed when logged in
    rv2 = client.get('/dashboard')
    assert rv2.status_code == 200


def test_duplicate_username_shows_error(client):
    client.post('/register', data={'username': 'dupuser', 'email': 'dup1@example.com', 'password': 'password123'}, follow_redirects=True)
    rv = client.post('/register', data={'username': 'dupuser', 'email': 'dup2@example.com', 'password': 'password123'}, follow_redirects=True)
    # The app should flash a 'Username is already taken' message and render the register page
    assert b'Username is already taken' in rv.data


def test_login_logout_flow(client):
    client.post('/register', data={'username': 'loginuser', 'email': 'login@example.com', 'password': 'password123'}, follow_redirects=True)
    # logout
    rv = client.get('/logout', follow_redirects=True)
    assert b'Login' in rv.data or rv.status_code == 200
