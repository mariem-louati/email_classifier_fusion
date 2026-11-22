"""ÉTAPE 5 : tester un e-mail dans le terminal, sans le site."""
import joblib
from config import MODELE

modele = joblib.load(MODELE)
print("Écris un e-mail (ou tape q pour quitter)")

while True:
    texte = input("\nE-mail : ")
    if texte.lower() == "q":
        break
    proba = modele.predict_proba([texte])[0]
    print("Catégorie :", modele.classes_[proba.argmax()], "(confiance :", round(max(proba) * 100), "%)")
