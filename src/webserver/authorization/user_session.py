from flask import Blueprint, current_app, url_for, redirect, session
from oauth_wrapper import OAuthWrapper

oauth_wrapper = OAuthWrapper(current_app)
oauth_objects = oauth_wrapper.get_auth_object()
oauth = oauth_objects[0]
google = oauth_objects[1]

authorization = Blueprint("authorization", __name__)

@authorization.route('/login')
def login():
    google = oauth.create_client('google')  # create the google oauth client
    redirect_uri = url_for('authorization.authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


@authorization.route('/authorize')
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


@authorization.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')