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

# Nom de la 6e catégorie : tout ce qui n'est pas un vrai e-mail (bonjour seul, charabia, pub...)
SPAM = "Spam / Hors sujet"

# Règles de sécurité appliquées AVANT et APRÈS le modèle (voir classification.py)
MIN_MOTS = 3             # moins de 3 mots -> Spam / Hors sujet
SEUIL_HORS_SUJET = 30    # confiance (%) en dessous de laquelle aucune catégorie n'est retenue

# Une couleur et un emoji par catégorie (le site s'adapte tout seul)
CATEGORIES = {
    "Réclamation":            {"emoji": "📢", "couleur": "#E4572E"},
    "Demande d'information":  {"emoji": "ℹ️", "couleur": "#2E86E4"},
    "Demande de rendez-vous": {"emoji": "📅", "couleur": "#8E44AD"},
    "Demande administrative": {"emoji": "📄", "couleur": "#17A589"},
    "Urgence":                {"emoji": "🚨", "couleur": "#C0392B"},
    SPAM:                     {"emoji": "🗑️", "couleur": "#7F8C8D"},
}
