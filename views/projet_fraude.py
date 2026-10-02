import plotly.graph_objects as go
import streamlit as st

from ui import GOLD, GREEN, LINE, NAVY_2, TEXT, WINE, chips, hero, reading, section, stats

FONT = "Inter, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif"

# Resultats reels, obtenus sur le jeu de donnees du projet (11 565 sinistres,
# 1994-1996) — split stratifie 70/30, sur-echantillonnage applique
# uniquement sur le train (jamais sur le test, pour ne pas biaiser
# l'evaluation). Verifies lors du developpement de l'app dediee.
MODELES = ["Régression logistique", "Random Forest", "XGBoost"]
BRUT = {
    "accuracy": [94.1, 94.1, 94.2],
    "rappel": [0.0, 0.0, 1.9],
    "precision": [0.0, 0.0, 100.0],
}
EQUILIBRE = {
    "accuracy": [66.6, 73.8, 85.3],
    "rappel": [88.8, 73.3, 40.8],
    "precision": [13.9, 15.0, 17.8],
}


def style_fig(fig: go.Figure, height: int = 340) -> go.Figure:
    fig.update_layout(
        height=height, margin=dict(l=8, r=8, t=24, b=8),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family=FONT, size=13, color=TEXT),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0),
        hoverlabel=dict(font_family=FONT),
    )
    fig.update_xaxes(showgrid=False, linecolor=LINE)
    fig.update_yaxes(gridcolor="#E9ECF1", zeroline=False)
    return fig


def show(fig: go.Figure) -> None:
    st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})


hero(
    "Machine Learning · Assurance",
    "Détection de fraude à l'assurance auto",
    "Pipeline complet de classification — exploration, preprocessing, entraînement et "
    "évaluation de 3 modèles — sur un jeu de 11 565 sinistres réels (1994-1996), avec "
    "un déploiement en application Streamlit interactive permettant d'évaluer un "
    "nouveau sinistre en direct.",
)

stats([
    ("11\u202f565", "sinistres, 34 variables déclarées"),
    ("5,9\u202f%", "taux de fraude réel — fortement déséquilibré"),
    ("3", "modèles comparés : Logistique, Random Forest, XGBoost"),
    ("2", "scénarios : données brutes et ré-équilibrées"),
])

section("Le piège du déséquilibre de classe")
st.html(
    '<p class="lead">Sur données brutes, la fraude est rare : un modèle qui prédit '
    "toujours « pas de fraude » obtient déjà ~94 % d'accuracy — sans détecter un seul "
    "cas réel. C'est pourquoi le rappel (recall) sur la classe frauduleuse est la "
    "métrique qui compte ici, pas l'accuracy globale.</p>"
)
fig = go.Figure()
fig.add_bar(x=MODELES, y=BRUT["accuracy"], name="Accuracy", marker_color=NAVY_2)
fig.add_bar(x=MODELES, y=BRUT["rappel"], name="Rappel (fraude)", marker_color=WINE)
fig.update_layout(barmode="group")
fig.update_yaxes(title="%", range=[0, 100])
show(style_fig(fig))
reading(
    "<b>Lecture :</b> Régression logistique et Random Forest ont un rappel de 0 % — "
    "elles ne détectent littéralement aucune fraude malgré 94 % d'accuracy. Seul "
    "XGBoost décroche un signal (1,9 % de rappel, 100 % de précision) : il devine "
    "juste quelques cas, mais sans jamais se tromper quand il le fait."
)

section("Après ré-équilibrage par sur-échantillonnage")
st.html(
    '<p class="lead">Le sur-échantillonnage de la classe minoritaire — appliqué '
    "uniquement sur les données d'entraînement, jamais sur le test, pour ne pas "
    "biaiser l'évaluation — change complètement l'équilibre précision/rappel.</p>"
)
fig = go.Figure()
fig.add_bar(x=MODELES, y=EQUILIBRE["rappel"], name="Rappel (fraude)", marker_color=GREEN)
fig.add_bar(x=MODELES, y=EQUILIBRE["precision"], name="Précision (fraude)", marker_color=GOLD)
fig.update_layout(barmode="group")
fig.update_yaxes(title="%", range=[0, 100])
show(style_fig(fig))
reading(
    "<b>Lecture :</b> la régression logistique détecte 88,8 % des fraudes réelles "
    "(au prix d'une précision faible, 13,9 % — beaucoup de fausses alertes). "
    "Random Forest offre le meilleur compromis opérationnel (73,3 % de rappel, "
    "15,0 % de précision). XGBoost reste le plus prudent (40,8 % de rappel) mais "
    "le plus précis des trois sur ce scénario."
)

section("Pipeline")
st.html(
    '<div class="card"><h3>De la donnée brute à la prédiction en direct</h3>'
    "<p>Preprocessing fidèle à la méthodologie d'un notebook de référence : encodage "
    "ordinal pour les variables à modalités ordonnées, one-hot pour les variables "
    "nominales, imputation généralisée à toute colonne (pas seulement celles "
    "anticipées) pour ne jamais laisser de valeur manquante atteindre les modèles. "
    "Split stratifié 70/30, sur-échantillonnage du train, entraînement des 3 "
    "modèles sur les deux scénarios, puis formulaire de prédiction en direct sur un "
    "nouveau sinistre.</p>"
    + chips(["Pandas", "scikit-learn", "XGBoost", "Streamlit", "Plotly"])
    + "</div>"
)

st.caption(
    "Application dédiée disponible séparément — code source sur demande "
    "(preprocessing, entraînement et formulaire de prédiction entièrement "
    "fonctionnels, testés sur le jeu de données réel)."
)
