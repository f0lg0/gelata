from flask import Blueprint, current_app, render_template, request, redirect
from login_required import login_required

tickets_handler = Blueprint("tickets_handler", __name__)


@tickets_handler.route("/carica", methods=["GET", "POST"])
@login_required
def serve_tickets_page():
    if request.method == "GET":
        return render_template("carica.html")
    if request.method == "POST":
        print(request.form)  # estraendo lo username inserito
        return redirect("/")
