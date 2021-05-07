import os
import sys
sys.path.insert(1, './oauth')
sys.path.insert(1, './authorization')
sys.path.insert(1, "./tickets_handler")

from dotenv import load_dotenv
load_dotenv()

# database
from database_generator import generate_database

from datetime import timedelta
from flask import Flask, session, render_template
from user_session import authorization
from login_required import login_required
from tickets import tickets_handler

app = Flask(__name__, static_url_path="", static_folder="web/static",
            template_folder="web/templates")

app.register_blueprint(authorization)
app.register_blueprint(tickets_handler)

app.secret_key = os.getenv("APP_SECRET_KEY")
app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=15)


@app.route('/')
@login_required
def home():
    print("*** DEBUG:", dict(session))
    return render_template("home.html", user=dict(session)['profile'], tickets=16)


def main():
    generate_database()
    app.run(debug=True)


if __name__ == "__main__":
    main()
