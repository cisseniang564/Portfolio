"""Portfolio Streamlit - Cisse Niang, Actuaire & Data Scientist."""
import streamlit as st

from ui import inject_css

st.set_page_config(
    page_title="Cissé Niang — Actuaire & Data Scientist",
    page_icon="📐",
    layout="wide",
)

inject_css()  # une seule fois ici : s'applique a toutes les pages

accueil = st.Page("views/accueil.py", title="Accueil", default=True)
parcours = st.Page("views/parcours.py", title="Parcours")
projet = st.Page("views/projet_actuariat.py", title="Projet actuariat")

pg = st.navigation([accueil, parcours, projet], position="top")

with st.container(key="mobile_nav"):
    c1, c2, c3 = st.columns(3)
    c1.page_link(accueil, label="Accueil")
    c2.page_link(parcours, label="Parcours")
    c3.page_link(projet, label="Projet")

pg.run()
