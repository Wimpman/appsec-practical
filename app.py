from flask import Flask, request, render_template, redirect, url_for
import sqlite3, os

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "P@ssw0rd123!"
STRIPE_TEST_SECRET = "sk_test_51MvJQI1234567890abcdefg"

USER_PICS = {
    "admin": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=160&h=160&fit=crop&crop=faces",
    "alice": "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?w=160&h=160&fit=crop&crop=faces",
    "bob":   "https://images.unsplash.com/photo-1502685104226-ee32379fefbe?w=160&h=160&fit=crop&crop=faces",
    "guest": "https://images.unsplash.com/photo-1587019152955-1d1c5d74e28f?w=160&h=160&fit=crop&crop=faces"
}

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('example.db')
    cur  = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users
                   (id INTEGER PRIMARY KEY, username TEXT,
                    password TEXT, status TEXT)''')
    cur.execute("""INSERT OR IGNORE INTO users
                   (username, password, status)
                   VALUES (?, ?, ?)""",
                (ADMIN_USERNAME, ADMIN_PASSWORD, 'Administrator'))
    conn.commit(); conn.close()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST':
        user = request.form['username']
        pwd  = request.form['password']
        conn = sqlite3.connect('example.db')
        cur  = conn.cursor()
        try:
            q = f"SELECT * FROM users WHERE username = '{user}' AND password = '{pwd}'"
            row = cur.execute(q).fetchone()
            if row:
                return redirect(url_for('profile', username=row[1]))
            cur.execute(f"SELECT 1 FROM users WHERE username = '{user}'")
            if cur.fetchone():
                error = 'Incorrect password for this user'
            else:
                error = 'Username does not exist'
        except sqlite3.Error:
            error = 'Invalid credentials'
        finally:
            conn.close()
    return render_template('login.html', error=error)

@app.route('/profile')
def profile():
    user = request.args.get('username', 'guest')
    conn = sqlite3.connect('example.db')
    cur  = conn.cursor()
    cur.execute(f"SELECT status FROM users WHERE username='{user}'")
    status = (cur.fetchone() or ('No status',))[0]
    pic = USER_PICS.get(user, USER_PICS['guest'])
    return render_template('profile.html',
                           user=user, status=status, pic=pic)

if __name__ == '__main__':
    if not os.path.exists('example.db'):
        init_db()
    app.run(debug=True)