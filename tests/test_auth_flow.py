import os
import sys
import tempfile
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app, init_db


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    db_fd, db_path = tempfile.mkstemp(suffix='.sqlite3')
    os.close(db_fd)
    app.config['DATABASE'] = db_path
    init_db(app)
    with app.test_client() as client:
        yield client
    try:
        os.remove(db_path)
    except Exception:
        pass


def test_full_auth_flow(client):
    # Register new user
    resp = client.post('/register', data={
        'username': 'alice',
        'email': 'alice@example.com',
        'password': 'securepwd',
        'submit': 'Register'
    }, follow_redirects=True)
    assert b'You are logged in' in resp.data

    # Logout
    resp = client.get('/logout', follow_redirects=True)
    assert b'User Login' in resp.data

    # Login with credentials
    resp = client.post('/login', data={
        'username': 'alice',
        'password': 'securepwd',
        'submit': 'Login'
    }, follow_redirects=True)
    assert b'You are logged in' in resp.data


def test_duplicate_user_and_email_rejected(client):
    # Create initial user
    resp = client.post('/register', data={
        'username': 'bob',
        'email': 'bob@example.com',
        'password': 'anotherpwd',
        'submit': 'Register'
    }, follow_redirects=True)
    assert b'You are logged in' in resp.data

    # Attempt to register with same username
    resp = client.post('/register', data={
        'username': 'bob',
        'email': 'bob2@example.com',
        'password': 'anotherpwd',
        'submit': 'Register'
    }, follow_redirects=True)
    assert b'Username is already taken' in resp.data

    # Attempt to register with same email
    resp = client.post('/register', data={
        'username': 'bob2',
        'email': 'bob@example.com',
        'password': 'anotherpwd',
        'submit': 'Register'
    }, follow_redirects=True)
    assert b'Email is already registered' in resp.data
