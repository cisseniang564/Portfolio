# Portfolio — Cissé Niang, Actuaire & Data Scientist

Portfolio interactif Streamlit : profil détaillé, 5 expériences professionnelles,
formation, et démonstration en direct du projet fil rouge (provisionnement,
tarification, réassurance, Solvabilité II).

## Lancer en local

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Déployer gratuitement (Streamlit Community Cloud)

1. Pousser ce dossier sur GitHub (`cisseniang564/portfolio` par exemple) :
   ```bash
   git init && git add . && git commit -m "Portfolio"
   git branch -M main
   git remote add origin https://github.com/cisseniang564/portfolio.git
   git push -u origin main
   ```
2. Sur [share.streamlit.io](https://share.streamlit.io), se connecter avec le
   compte GitHub `cisseniang564`, cliquer **New app**, choisir le dépôt et
   `app.py`, déployer.
3. L'URL publique (`https://<nom>.streamlit.app`) se met à jour à chaque
   `git push`.

## Structure

```
portfolio_streamlit/
├── app.py                     # Point d'entree, navigation en haut de page
├── ui.py                      # CSS (injecte via st.html) + composants HTML
├── content.py                 # Source unique : experiences, formation, competences
├── views/
│   ├── accueil.py              # Profil, competences, apercu du parcours
│   ├── parcours.py             # 5 experiences detaillees + formation + certifs
│   └── projet_actuariat.py     # Demonstration interactive (5 onglets)
├── data/                       # Donnees de demonstration du projet actuariat
└── .streamlit/config.toml      # Theme natif Streamlit
```

## Ce qui a changé depuis la première version

La première version affichait le CSS en texte brut sur la page (bug de fond :
`st.markdown` interprète les lignes vides à l'intérieur d'un bloc `<style>` et
le découpe en morceaux). Tout le HTML/CSS passe maintenant par `st.html()`,
qui ne fait aucune interprétation Markdown. Le contenu a aussi été entièrement
repris à partir du CV détaillé : 5 expériences (dont SADA Assurances et
La Mutuelle Générale) avec leurs missions complètes, au lieu de 3 lignes
résumées.

## Personnalisation

- **Contenu** (expériences, formation, compétences, liens) : uniquement dans
  `content.py` — aucune autre page ne contient de texte en dur.
- **Couleurs / styles** : constantes en tête de `ui.py` (`NAVY`, `GOLD`, `WINE`).
- **Nouvel onglet du projet** : ajouter un `with st.tabs(...)` dans
  `views/projet_actuariat.py`.

## Tests effectués avant livraison

- `streamlit.testing.v1.AppTest` : navigation complète entre les 3 pages et
  les 5 onglets du projet, sans exception.
- Serveur réel lancé + **captures d'écran automatisées** (Playwright/Chromium,
  desktop et mobile) sur chaque page et chaque onglet, avec détection
  automatique de texte parasite, débordement horizontal et exceptions
  affichées à l'écran.
- Un bug réel trouvé et corrigé pendant ces tests : `st.page_link` testé hors
  contexte de navigation lève une erreur qui n'apparaît pas dans l'app réelle
  (faux positif de test, vérifié en testant le vrai point d'entrée `app.py`).
