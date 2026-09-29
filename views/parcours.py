import streamlit as st

from content import CERTIFICATIONS, EMAIL, EXPERIENCES, FORMATIONS, GITHUB, LINKEDIN
from ui import chips, esc, experience_card, hero, section

hero(
    "Parcours",
    "Expérience et formation",
    "Du pilotage technique actuariel et de l'inventaire Santé / Prévoyance à "
    "l'automatisation de la donnée en infocentre : cinq missions en assurance et mutuelle.",
)

st.write("")
section("Expérience professionnelle")
for e in EXPERIENCES:
    experience_card(e["role"], e["org"], e["when"], e["bullets"], e["tags"])

section("Formation")
for f in FORMATIONS:
    experience_card(f["role"], f["org"], f["when"], f["bullets"], f["tags"])

section("Certifications")
st.html(
    '<div class="card"><ul style="margin:0;padding-left:20px;">'
    + "".join(f'<li style="margin-bottom:6px;font-size:14.5px;">{esc(c)}</li>' for c in CERTIFICATIONS)
    + "</ul></div>"
)

section("Contact")
c1, c2, c3 = st.columns(3)
c1.link_button("LinkedIn", LINKEDIN, width="stretch")
c2.link_button("GitHub", GITHUB, width="stretch")
c3.link_button(EMAIL, f"mailto:{EMAIL}", width="stretch")
