"""ÉTAPE 2 : entraîner le modèle et le sauvegarder (rien d'autre)."""
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline, make_union
from config import DONNEES, MODELE

df = pd.read_csv(DONNEES)
train = df[df["split"] == "train"]

modele = make_pipeline(
    make_union(
        # 1) compte les mots et les paires de mots
        TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True),
        # 2) compte les morceaux de lettres : robuste aux fautes et aux variantes
        TfidfVectorizer(analyzer="char_wb", ngram_range=(2, 5), sublinear_tf=True, min_df=2),
    ),
    LogisticRegression(max_iter=2000, C=10, random_state=42),
)
modele.fit(train["email_text"], train["category"])

MODELE.parent.mkdir(exist_ok=True)
joblib.dump(modele, MODELE)
print("Modèle entraîné avec", len(train), "e-mails et sauvegardé dans", MODELE)
