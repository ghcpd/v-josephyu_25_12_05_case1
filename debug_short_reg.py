from app import app, init_db
import tempfile, os
app.config['TESTING']=True
app.config['WTF_CSRF_ENABLED']=False
fd, path = tempfile.mkstemp(suffix='.sqlite3')
os.close(fd)
app.config['DATABASE']=path
init_db(app)
with app.test_client() as c:
    resp = c.post('/register', data={'username':'rtest','email':'rtest@example.com','password':'abc','submit':'Register'}, follow_redirects=True)
    print('STATUS', resp.status)
    print(resp.data.decode())
