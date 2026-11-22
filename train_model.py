import pandas as pd, joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline, make_union
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("data/emails_fusion.csv")
train = df[df["split"] == "train"]

model = make_pipeline(
    make_union(
        TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True),
        TfidfVectorizer(analyzer="char_wb", ngram_range=(2, 5), sublinear_tf=True, min_df=2),
    ),
    LogisticRegression(max_iter=2000, C=10, random_state=42),
)
model.fit(train["email_text"], train["category"])

print("Entraîné sur", len(train), "e-mails\n")
for nom in ["test_ami", "test_synth", "test_manuel"]:
    d = df[df["split"] == nom]
    pred = model.predict(d["email_text"])
    print(f"{nom:12s}: {accuracy_score(d['category'], pred)*100:.1f} %")

d = df[df["split"] == "test_manuel"]
pred = model.predict(d["email_text"])
print("\nDétail sur les 60 e-mails écrits à la main :")
print(classification_report(d["category"], pred))
ConfusionMatrixDisplay.from_predictions(d["category"], pred, xticks_rotation=30, cmap="Blues")
plt.tight_layout(); plt.savefig("matrice_confusion.png")

print("\nE-mails mal classés (test manuel) :")
for t, v, p in zip(d["email_text"], d["category"], pred):
    if v != p:
        print("-", t, "\n   vrai :", v, "| répondu :", p)

joblib.dump(model, "email_classifier.pkl")
print("\nModèle sauvegardé : email_classifier.pkl")
