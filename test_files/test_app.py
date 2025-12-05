import os
import sys
import pytest

# Ensure project root is importable when tests run from nested folder
proj_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if proj_root not in sys.path:
    sys.path.insert(0, proj_root)

from app import app
from models import init_db


@pytest.fixture
def client(tmp_path):
    db_file = tmp_path / "test_db.sqlite"
    app.config['DATABASE'] = str(db_file)
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test-secret'
    # Disable CSRF for testing convenience
    app.config['WTF_CSRF_ENABLED'] = False

    init_db(app)

    with app.test_client() as client:
        yield client


def test_root_redirects_to_login(client):
    resp = client.get('/')
    assert resp.status_code in (302, 303)


def test_register_and_login_flow(client):
    # Register a new user
    resp = client.post('/register', data={
        'username': 'tester',
        'email': 'tester@example.com',
        'password': 'password123',
        'submit': True
    }, follow_redirects=True)
    assert resp.status_code == 200
    assert b'You are logged in' in resp.data or b'Hello, <strong>tester</strong>' in resp.data

    # Logout
    resp = client.get('/logout', follow_redirects=True)
    assert resp.status_code == 200

    # Login with the same user
    resp = client.post('/login', data={
        'username': 'tester',
        'password': 'password123',
    }, follow_redirects=True)
    assert resp.status_code == 200
    assert b'You are logged in' in resp.data or b'Hello, <strong>tester</strong>' in resp.data
