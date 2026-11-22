"""ÉTAPE 1 : vérifier que les données sont propres avant d'entraîner."""
import pandas as pd
from config import DONNEES

df = pd.read_csv(DONNEES)

print("Taille :", df.shape)
print("Colonnes :", df.columns.tolist())
print("\nNombre d'e-mails par catégorie et par jeu :")
print(pd.crosstab(df["category"], df["split"]))
print("\nDoublons :", df.duplicated(subset=["email_text"]).sum())
print("E-mails vides :", df["email_text"].isna().sum())

# Fuite de données : un e-mail du test ne doit JAMAIS être dans le train
train = set(df[df["split"] == "train"]["email_text"])
for nom in ["test_ami", "test_synth", "test_manuel"]:
    commun = len(train & set(df[df["split"] == nom]["email_text"]))
    print(f"E-mails de {nom} déjà vus à l'entraînement :", commun)
