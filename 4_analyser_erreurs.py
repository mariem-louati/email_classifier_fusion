"""ÉTAPE 4 : comprendre OÙ le modèle se trompe (tableau, graphique, liste)."""
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from config import DONNEES, MODELE, MATRICE

pd.set_option("display.width", 250)
pd.set_option("display.max_columns", None)

modele = joblib.load(MODELE)
df = pd.read_csv(DONNEES)
d = df[df["split"] == "test_manuel"].copy()
d["prediction"] = modele.predict(d["email_text"])

print("Tableau des erreurs (lignes = vraie catégorie, colonnes = réponse du modèle) :")
print(pd.crosstab(d["category"], d["prediction"]))
MATRICE.parent.mkdir(exist_ok=True)
ConfusionMatrixDisplay.from_predictions(
    d["category"], d["prediction"], xticks_rotation=30, cmap="Blues"
)
plt.title("Résultats sur les 60 e-mails écrits à la main")
plt.xlabel("Réponse du modèle")
plt.ylabel("Vraie catégorie")
plt.tight_layout()
plt.savefig(MATRICE, dpi=130)
print("\nGraphique sauvegardé :", MATRICE)

print("\nE-mails où le modèle se trompe :")
for _, ligne in d[d["category"] != d["prediction"]].iterrows():
    print("-", ligne["email_text"])
    print("   vrai :", ligne["category"], "| répondu :", ligne["prediction"])
