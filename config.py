"""Réglages communs à tous les fichiers du projet (chemins, catégories, design)."""
from pathlib import Path

DOSSIER = Path(__file__).parent
DONNEES = DOSSIER / "data" / "emails_fusion.csv"
MODELE = DOSSIER / "modele" / "email_classifier.pkl"
SCORES = DOSSIER / "modele" / "scores.json"
MATRICE = DOSSIER / "static" / "matrice_confusion.png"

# En dessous de ce pourcentage, le site dit "je ne suis pas sûr"
SEUIL_CONFIANCE = 40

# --- TA TOUCHE : change ces lignes pour personnaliser le site ---
NOM_PROJET = "Classification des e-mails"
AUTEUR = "Ton nom ici"
SOUS_TITRE = "Colle un e-mail, l'IA trouve sa catégorie en une seconde."

# Une couleur et un emoji par catégorie (le site s'adapte tout seul)
CATEGORIES = {
    "Réclamation":            {"emoji": "📢", "couleur": "#E4572E"},
    "Demande d'information":  {"emoji": "ℹ️", "couleur": "#2E86E4"},
    "Demande de rendez-vous": {"emoji": "📅", "couleur": "#8E44AD"},
    "Demande administrative": {"emoji": "📄", "couleur": "#17A589"},
    "Urgence":                {"emoji": "🚨", "couleur": "#C0392B"},
}
