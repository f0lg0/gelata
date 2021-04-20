import os
import sys
sys.path.insert(1, './oauth')

from dotenv import load_dotenv
load_dotenv()

from datetime import timedelta
from flask import Flask, redirect, url_for, session
from login_required import login_required
from oauth_wrapper import OAuthWrapper

# wrapping Flask app into a REST API
app = Flask(__name__)

app.secret_key = os.getenv("APP_SECRET_KEY")
app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

oauth_wrapper = OAuthWrapper(app)
oauth_objects = oauth_wrapper.get_auth_object()
oauth = oauth_objects[0]
google = oauth_objects[1]

@app.route('/')
@login_required
def home():
    email = dict(session)['profile']['email']
    return f"Hello, {email}"


@app.route('/login')
def login():
    google = oauth.create_client('google')  # create the google oauth client
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')  # create the google oauth client
    # Access token from google (needed to get user info)
    token = google.authorize_access_token()
    # userinfo contains stuff u specificed in the scrope
    resp = google.get('userinfo')
    user_info = resp.json()
    user = oauth.google.userinfo()  # uses openid endpoint to fetch user info
    # Here you use the profile/user data that you got and query your database find/register the user
    # and set ur own data in the session not the profile from google
    session['profile'] = user_info
    # make the session permanant so it keeps existing after broweser gets closed
    session.permanent = True
    return redirect('/')


@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
