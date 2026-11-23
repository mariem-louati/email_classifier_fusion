"""ÉTAPE 3 : mesurer la note du modèle sur des e-mails qu'il n'a jamais vus."""
import json
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from classification import predire_liste
from config import DONNEES, MODELE, SCORES

modele = joblib.load(MODELE)
df = pd.read_csv(DONNEES)

noms = {
    "test_ami": "E-mails courts (style administratif)",
    "test_synth": "E-mails longs (style commerce)",
    "test_manuel": "E-mails écrits à la main",
}
scores = {}
for cle, libelle in noms.items():
    d = df[df["split"] == cle]
    score = accuracy_score(d["category"], predire_liste(modele, d["email_text"]))
    libelle = f"{libelle} ({len(d)} e-mails)"     # le nombre vient des données
    scores[libelle] = round(score * 100, 1)
    print(f"{libelle:50s}: {scores[libelle]} %")

d = df[df["split"] == "test_manuel"]
print("\nDétail par catégorie (test manuel) :")
print(classification_report(d["category"], predire_liste(modele, d["email_text"])))

SCORES.write_text(json.dumps(scores, ensure_ascii=False, indent=2), encoding="utf-8")