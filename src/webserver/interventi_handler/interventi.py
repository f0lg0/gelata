import time

from flask import Blueprint, current_app, render_template, request, redirect, session, abort
from login_required import login_required

from database_ops import dbops_save_intervento, dbops_update_intervento, dbops_delete_intervento

interventi_handler = Blueprint("interventi_handler", __name__)


@interventi_handler.route("/carica", methods=["GET", "POST"])
@login_required
def upload_intervento():
    if request.method == "GET":
        return render_template("carica.html", user=session['profile'])
    if request.method == "POST":
        data = {
            "note": request.json["note"],
            "sede": {
                "descrizione": "Ghedi",
            },
            "plesso": {
                "descrizione": "*Plesso da definire*"
            },
            "vano": {
                "codice": "*Codice vano da definire*",
                "descrizione": "*Descrizione del vano da definire"
            },
            "attività": {
                "descrizione": ', '.join(request.json["checkboxs"]),
                "frequenza": {
                    "descrizione": f"{request.json['orario']['ora_inizio']}/{request.json['orario']['ora_fine']}"
                }
            },
            "prodotto": {
                "descrizione": "*Prodotti da definire*"
            },
            "attrezzatura": {
                "descrizione": request.json['attrezzatura']
            }
        }

        print(data)

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
