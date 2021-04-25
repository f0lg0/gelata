from flask import Blueprint, current_app, url_for, redirect, session, render_template
from oauth_wrapper import OAuthWrapper
from login_required import login_required

oauth_wrapper = OAuthWrapper(current_app)
oauth_objects = oauth_wrapper.get_auth_object()
oauth = oauth_objects[0]
google = oauth_objects[1]

authorization = Blueprint("authorization", __name__)


@authorization.route("/login")
def login():
    google = oauth.create_client("google")
    redirect_uri = url_for("authorization.authorize", _external=True)
    return google.authorize_redirect(redirect_uri)


@authorization.route("/authorize")
def authorize():
    google = oauth.create_client("google")
    token = google.authorize_access_token()

    resp = google.get("userinfo")
    user_info = resp.json()
    user = oauth.google.userinfo()
    session["profile"] = user_info

    session.permanent = True
    return redirect("/")


@authorization.route("/logout")
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect("/")


@authorization.route("/profilo")
@login_required
def user_profile():
    return render_template("profilo.html", user=dict(session)["profile"])
