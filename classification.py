"""La logique de classification, partagée par le site (app.py) et le terminal (5_tester_email.py).

Un e-mail passe par 3 filtres :
  1. RÈGLE « trop court » : moins de MIN_MOTS mots, ou aucune lettre  -> Spam / Hors sujet
  2. LE MODÈLE : calcule une probabilité pour chacune des 6 catégories
  3. RÈGLE « pas sûr du tout » : confiance sous SEUIL_HORS_SUJET       -> Spam / Hors sujet
"""
import re
from config import MIN_MOTS, SEUIL_CONFIANCE, SEUIL_HORS_SUJET, SPAM


def compter_mots(texte):
    return len(re.findall(r"[^\W\d_]+", texte))   # suites de lettres (accents compris)


def classer(modele, texte):
    """Retourne un dictionnaire : categorie, confiance, incertain, raison, probabilites."""
    texte = (texte or "").strip()
    classes = list(modele.classes_)

    # Filtre 1 : trop court ou vide
    if compter_mots(texte) < MIN_MOTS:
        proba = {c: 0.0 for c in classes}
        proba[SPAM] = 100.0
        return dict(categorie=SPAM, confiance=100.0, incertain=False,
                    raison=f"Moins de {MIN_MOTS} mots : pas assez de contenu pour être un vrai e-mail.",
                    probabilites=proba)

    # Filtre 2 : le modèle
    p = modele.predict_proba([texte])[0]
    proba = {c: round(float(x) * 100, 1) for c, x in zip(classes, p)}
    i = p.argmax()
    categorie, confiance = classes[i], round(float(p[i]) * 100, 1)

    # Filtre 3 : le modèle n'est sûr de rien -> aucune catégorie ne convient
    if confiance < SEUIL_HORS_SUJET and categorie != SPAM:
        return dict(categorie=SPAM, confiance=confiance, incertain=True,
                    raison=f"Aucune catégorie n'atteint {SEUIL_HORS_SUJET} % de confiance : message classé hors sujet.",
                    probabilites=proba)

    raison = ""
    if categorie == SPAM:
        raison = "Le modèle reconnaît un message hors sujet, publicitaire ou sans contenu."
    return dict(categorie=categorie, confiance=confiance,
                incertain=confiance < SEUIL_CONFIANCE, raison=raison, probabilites=proba)


def predire_liste(modele, textes):
    """Pour évaluer : la catégorie finale (règles comprises) de chaque e-mail."""
    return [classer(modele, t)["categorie"] for t in textes]
