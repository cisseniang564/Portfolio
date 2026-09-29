import streamlit as st

from content import COMPETENCES, EMAIL, EXPERIENCES, GITHUB, LINKEDIN
from ui import chips, esc, hero, section, stats

hero(
    "Actuaire · Data Scientist",
    "Cissé Niang",
    "Consultant actuariat et data en assurance. Je relie le calcul actuariel "
    "réglementaire — provisionnement, tarification, Solvabilité II — à "
    "l'ingénierie de la donnée et au machine learning.",
    links=[
        ("LinkedIn", LINKEDIN, False),
        ("GitHub", GITHUB, True),
        (EMAIL, f"mailto:{EMAIL}", True),
    ],
)

stats([
    ("5", "expériences en assurance et mutuelle depuis 2021"),
    ("2", "masters : Actuariat (Montpellier) et Expertise Statistique (Lorraine)"),
    ("SAS", "spécialiste certifié, plus R, Python, SQL et VBA"),
    ("6", "modules de mon projet phare, codés en R et en SAS"),
])

section("Profil")
st.html(
    '<p class="lead">Actuaire et data scientist, titulaire d\'un Master 2 Actuariat et d\'un DU Big Data. '
    "Mes missions couvrent l'inventaire et le provisionnement (Chain-Ladder, PSAP, PM, CANE), la "
    "tarification IARD, le pilotage technique, les exigences quantitatives de Solvabilité II "
    "(SCR, Best Estimate, QRT) et l'automatisation des chaînes de données (SAS, SQL, VBA, RShiny).</p>"
    '<p class="lead">Le fil conducteur de mon travail : <b>fiabiliser la donnée en amont pour que le '
    "calcul actuariel en aval soit juste.</b></p>"
)

section("Compétences")
col_a, col_b = st.columns(2, gap="large")
for i, (titre, items) in enumerate(COMPETENCES):
    with (col_a if i % 2 == 0 else col_b):
        st.html(f'<div class="skill-group"><div class="t">{esc(titre)}</div>{chips(items)}</div>')

section("Parcours en un coup d'œil")
rows = "".join(
    f'<div class="frise-row"><div class="frise-when">{esc(e["when"])}</div>'
    f'<div><div class="frise-what">{esc(e["role"])}</div><div class="frise-org">{esc(e["org"])}</div></div></div>'
    for e in EXPERIENCES
)
st.html(f"<div>{rows}</div>")
st.page_link("views/parcours.py", label="Voir le détail des missions", icon=":material/arrow_forward:")

section("Projet phare")
st.html(
    '<div class="card"><h3>Provisionnement, tarification, réassurance et Solvabilité II</h3>'
    "<p>Un pipeline actuariel complet, codé en parallèle en R et en SAS sur un portefeuille IARD auto "
    "synthétique (30 000 polices, 2 381 sinistres) : du sinistre individuel jusqu'aux provisions "
    "Solvabilité II, avec des contrôles de cohérence croisés à chaque étape.</p>"
    + chips(["Chain-Ladder", "Bornhuetter-Ferguson", "Bootstrap ODP", "GLM", "Réassurance XS / stop-loss",
             "Best Estimate", "Risk Margin", "SCR", "R", "SAS", "Shiny"])
    + "</div>"
)
st.page_link("views/projet_actuariat.py", label="Explorer les résultats en détail", icon=":material/arrow_forward:")
