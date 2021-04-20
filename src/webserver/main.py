import os
import sys
sys.path.insert(1, './oauth')
sys.path.insert(1, './authorization')

from dotenv import load_dotenv
load_dotenv()

from datetime import timedelta
from flask import Flask, session, render_template
from user_session import authorization
from login_required import login_required

app = Flask(__name__)
app.register_blueprint(authorization)

app.secret_key = os.getenv("APP_SECRET_KEY")
app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

@app.route('/')
@login_required
def home():
    email = dict(session)['profile']['email']
    return render_template("index.html", email=email)

if __name__ == "__main__":
    app.run(debug=True)