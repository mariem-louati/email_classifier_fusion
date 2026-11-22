# Classification automatique des e-mails (projet fusionné)

5 catégories : Réclamation, Demande d'information, Demande de rendez-vous, Demande administrative, Urgence.

## Données (data/emails_fusion.csv)
- train : 410 e-mails (style administratif/universitaire) + 1500 e-mails (style commerce, 300/classe)
- test_ami (100), test_synth (300), test_manuel (60 écrits à la main) : jamais vus à l'entraînement

## Lancer en local (VS Code)
    pip install -r requirements.txt
    python train_model.py
    streamlit run app.py

## Mettre en ligne (gratuit)
1. Créer un dépôt GitHub avec tout le dossier (email_classifier.pkl inclus).
2. Aller sur https://share.streamlit.io -> New app -> choisir le dépôt, fichier app.py -> Deploy.
3. Lien public obtenu : https://<nom>.streamlit.app
