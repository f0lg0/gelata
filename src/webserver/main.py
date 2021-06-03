import os
import sys
sys.path.append("./oauth")
sys.path.append("./authorization")
sys.path.append("./interventi_handler")
sys.path.append("./db")

from dotenv import load_dotenv
load_dotenv()

# database
from database_generator import generate_database
from database_ops import dbops_init

from datetime import timedelta
from flask import Flask, session, render_template
from user_session import authorization
from login_required import login_required
from interventi import interventi_handler
from database_ops import dbops_get_interventi_by_user

app = Flask(__name__, static_url_path="", static_folder="web/static",
            template_folder="web/templates")

app.register_blueprint(authorization)
app.register_blueprint(interventi_handler)

app.secret_key = os.getenv("APP_SECRET_KEY")
app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=15)


@app.route('/')
@login_required
def home():
    print("*** DEBUG:", dict(session))

    # retreive first 10 entries
    res = dbops_get_interventi_by_user(session["profile"]["email"])
    print(res)

    if res["success"]:
        return render_template("home.html", user=dict(session)['profile'], interventi=res["interventi"])
    else:
        return render_template("home.html", user=dict(session)['profile'], interventi=[])


def main():
    generate_database()
    dbops_init("../database/gelata.db")
    app.run(debug=True)


if __name__ == "__main__":
    main()
