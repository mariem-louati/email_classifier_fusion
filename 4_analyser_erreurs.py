"""ÉTAPE 4 : comprendre OÙ le modèle se trompe (tableau, graphique, liste)."""
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from classification import predire_liste
from config import DONNEES, MODELE, MATRICE

pd.set_option("display.width", 250)
pd.set_option("display.max_columns", None)

modele = joblib.load(MODELE)
df = pd.read_csv(DONNEES)
d = df[df["split"] == "test_manuel"].copy()
d["prediction"] = predire_liste(modele, d["email_text"])  # règles de sécurité comprises

print("Tableau des erreurs (lignes = vraie catégorie, colonnes = réponse du modèle) :")
print(pd.crosstab(d["category"], d["prediction"]))

MATRICE.parent.mkdir(exist_ok=True)
affichage = ConfusionMatrixDisplay.from_predictions(
    d["category"], d["prediction"], xticks_rotation=30, cmap="Blues"
)
affichage.figure_.set_size_inches(10, 8)
plt.setp(affichage.ax_.get_xticklabels(), ha="right", rotation_mode="anchor")
plt.title(f"Résultats sur les {len(d)} e-mails écrits à la main")
plt.xlabel("Réponse du modèle")
plt.ylabel("Vraie catégorie")
plt.tight_layout()
plt.savefig(MATRICE, dpi=130)
print("\nGraphique sauvegardé :", MATRICE)

print("\nE-mails où le modèle se trompe :")
for _, ligne in d[d["category"] != d["prediction"]].iterrows():
    print("-", ligne["email_text"])
    print("   vrai :", ligne["category"], "| répondu :", ligne["prediction"])