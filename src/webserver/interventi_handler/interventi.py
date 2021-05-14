import time

from flask import Blueprint, current_app, render_template, request, redirect, session
from login_required import login_required

from database_ops import dbops_save_intervento

interventi_handler = Blueprint("interventi_handler", __name__)


@interventi_handler.route("/carica", methods=["GET", "POST"])
@login_required
def serve_tickets_page():
    if request.method == "GET":
        return render_template("carica.html")
    if request.method == "POST":
        # TODO: this is dummy data, we will eventually use form data

        data = {
            "note": "note",
            "sede": {
                "descrizione": "descrizione sede",
            },
            "plesso": {
                "descrizione": "descrizione plesso",
            },
            "vano": {
                "codice": 123,
                "descrizione": "descrizione vano",
            },
            "attività": {
                "descrizione": "descrizione attività",
                "frequenza": {
                    "descrizione": "descrizione evento",
                },
            },
            "prodotto": {
                "descrizione": "descrizione prodotto",
            },
            "attrezzatura": {
                "descrizione": "descrizione attrezzatura",
            }
        }
        result = dbops_save_intervento(data, session['profile']['email'])
        return result
