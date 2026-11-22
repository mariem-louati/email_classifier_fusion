"""Le site web (Flask). Lance avec : python app.py"""
import json
import joblib
from flask import Flask, jsonify, render_template, request
from classification import classer as classer_email
from config import AUTEUR, CATEGORIES, MATRICE, MODELE, NOM_PROJET, SCORES, SOUS_TITRE

app = Flask(__name__)
modele = joblib.load(MODELE)  # chargé une seule fois au démarrage

contexte = dict(nom_projet=NOM_PROJET, auteur=AUTEUR, sous_titre=SOUS_TITRE, categories=CATEGORIES)


@app.route("/")
def accueil():
    return render_template("index.html", **contexte)


@app.route("/evaluation")
def evaluation():
    scores = json.loads(SCORES.read_text(encoding="utf-8")) if SCORES.exists() else {}
    return render_template("evaluation.html", scores=scores, matrice=MATRICE.exists(), **contexte)


@app.route("/api/classer", methods=["POST"])
def classer():
    texte = ((request.get_json(silent=True) or {}).get("email") or "").strip()
    if not texte:
        return jsonify(erreur="Écris le contenu d'un e-mail d'abord."), 400
    if len(texte) > 5000:
        return jsonify(erreur="E-mail trop long (5000 caractères maximum)."), 400
    return jsonify(classer_email(modele, texte))


if __name__ == "__main__":
    app.run(debug=True)
