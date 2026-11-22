"""ÉTAPE 5 : tester un e-mail dans le terminal, sans le site."""
import joblib
from classification import classer
from config import MODELE

modele = joblib.load(MODELE)
print("Écris un e-mail (ou tape q pour quitter)")

while True:
    texte = input("\nE-mail : ")
    if texte.lower() == "q":
        break
    r = classer(modele, texte)
    print("Catégorie :", r["categorie"], "(confiance :", round(r["confiance"]), "%)")
    if r["raison"]:
        print("Raison :", r["raison"])
