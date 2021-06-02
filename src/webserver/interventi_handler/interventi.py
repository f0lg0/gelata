import time

from flask import Blueprint, current_app, render_template, request, redirect, session, abort
from login_required import login_required

from database_ops import dbops_save_intervento, dbops_update_intervento, dbops_delete_intervento

interventi_handler = Blueprint("interventi_handler", __name__)


@interventi_handler.route("/carica", methods=["GET", "POST"])
@login_required
def upload_intervento():
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


@interventi_handler.route("/modifica", methods=["POST"])
@login_required
def update_intervento():
    # TODO: this is dummy data, we will eventually use form data

    data = {
        "id": 1,
        "note": "nuove note",
        "sede": {
            "descrizione": "nuova descrizione sede",
        },
        "plesso": {
            "descrizione": "nuova descrizione plesso",
        },
        "vano": {
            "codice": 99,
            "descrizione": "nuova descrizione vano",
        },
        "attività": {
            "descrizione": "nuova descrizione attività",
            "frequenza": {
                "descrizione": "nuova descrizione evento",
            },
        },
        "prodotto": {
            "descrizione": "nuova descrizione prodotto",
        },
        "attrezzatura": {
            "descrizione": "nuova descrizione attrezzatura",
        }
    }

    result = dbops_update_intervento(data, session["profile"]["email"])
    return result


@interventi_handler.route("/elimina", methods=["POST"])
@login_required
def delete_intervento():
    try:
        intervento_id = int(request.form.get("iid"))
        return dbops_delete_intervento(intervento_id, session["profile"]["email"])
    except:
        abort(400)
