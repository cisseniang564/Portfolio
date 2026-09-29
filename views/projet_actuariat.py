from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from ui import GOLD, GREEN, LINE, NAVY, NAVY_2, TEXT, WINE, euro, hero, reading, section, stats

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
FONT = "Inter, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif"


@st.cache_data
def load_csv(name: str) -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / name)


def style_fig(fig: go.Figure, height: int = 360) -> go.Figure:
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


def spaced(n: int) -> str:
    return f"{n:,}".replace(",", "\u202f")


PRETTY_POSTE = {
    "PSAP normes sociales (non actualisee)": "PSAP normes sociales (non actualisée)",
    "Best Estimate (actualise)": "Best Estimate (actualisé)",
    "Risk Margin": "Risk Margin",
    "Provisions techniques Solvabilite II (BE + RM)": "Provisions Solvabilité II (BE + RM)",
    "SCR risque de reserve": "SCR risque de réserve",
}


def pretty_var(v: str) -> str:
    if v.startswith("classe_age"):
        return "Âge " + v[len("classe_age"):]
    if v.startswith("zone"):
        return "Zone " + v[4:]
    if v.startswith("puissance"):
        return "Puissance " + v[9:]
    if v == "bonus_malus":
        return "Bonus-malus (par point)"
    return v


hero(
    "Projet phare",
    "Provisionnement, tarification, réassurance et Solvabilité II",
    "Pipeline actuariel complet, codé en parallèle en R et en SAS sur un portefeuille IARD auto "
    "synthétique de 30 000 polices et 2 381 sinistres — avec des contrôles de cohérence croisés "
    "à chaque étape. Les graphiques ci-dessous sont interactifs.",
)

try:
    cl = load_csv("resultats_chain_ladder_R.csv")
    comp = load_csv("comparaison_CL_BF_R.csv")
    boot_tot = load_csv("bootstrap_PSAP_totale_R.csv").set_index("statistique")["valeur"]
    solva = load_csv("synthese_solvabilite2_R.csv")
    solva["poste"] = solva["poste"].map(PRETTY_POSTE).fillna(solva["poste"])
    solva_s = solva.set_index("poste")["montant"]

    stats([
        (euro(cl["PSAP_CL"].sum()), "PSAP Chain-Ladder (normes sociales)"),
        (euro(boot_tot["Moyenne"]), "Moyenne du bootstrap (validation croisée)"),
        (euro(solva_s["Best Estimate (actualisé)"]), "Best Estimate actualisé"),
        (euro(solva_s["Provisions Solvabilité II (BE + RM)"]), "Provisions Solvabilité II"),
    ])
except Exception as exc:
    st.warning(f"Les indicateurs n'ont pas pu être chargés ({exc}).")
    st.stop()

st.write("")
tab_prov, tab_sto, tab_tarif, tab_reas, tab_solva = st.tabs(
    ["Provisionnement", "Stochastique", "Tarification", "Réassurance", "Solvabilité II"]
)

# ------------------------------------------------------------------ Provisionnement
with tab_prov:
    section("Triangle de développement")
    tri = load_csv("triangle_cumule_R.csv")
    dev_cols = [c for c in tri.columns if c.startswith("dev_")]
    z = tri[dev_cols].values / 1000
    text = [["" if pd.isna(v) else spaced(round(v)) for v in row] for row in z]
    fig = go.Figure(go.Heatmap(
        z=z, x=[f"Période {i}" for i in range(len(dev_cols))],
        y=tri["annee_survenance"].astype(str), text=text, texttemplate="%{text}",
        colorscale=[[0, "#E8EDF5"], [1, NAVY_2]], showscale=False, xgap=3, ygap=3,
        hovertemplate="Survenance %{y}<br>%{x}<br>%{text} k€<extra></extra>",
    ))
    fig.update_yaxes(autorange="reversed")
    show(style_fig(fig, 340))
    reading("<b>Lecture :</b> charge cumulée (en k€) par année de survenance et période de "
            "développement. La partie inférieure droite est inconnue : c'est ce que les méthodes de "
            "provisionnement doivent projeter.")

    section("Chain-Ladder et Bornhuetter-Ferguson")
    fig = go.Figure()
    fig.add_bar(x=comp["annee_survenance"].astype(str), y=comp["PSAP_CL"], name="Chain-Ladder", marker_color=NAVY_2)
    fig.add_bar(x=comp["annee_survenance"].astype(str), y=comp["PSAP_BF"], name="Bornhuetter-Ferguson", marker_color=GOLD)
    fig.update_layout(barmode="group")
    fig.update_yaxes(tickformat=",.0f", title="PSAP (€)")
    show(style_fig(fig, 340))
    reading(f"<b>Lecture :</b> les deux méthodes concordent sur les générations matures et divergent sur les "
            f"plus récentes, où Chain-Ladder est le plus instable. PSAP totale : "
            f"<b>{euro(comp['PSAP_CL'].sum())}</b> (Chain-Ladder) contre <b>{euro(comp['PSAP_BF'].sum())}</b> "
            f"(Bornhuetter-Ferguson).")

# ------------------------------------------------------------------ Stochastique
with tab_sto:
    section("Distribution de la PSAP (bootstrap ODP)")
    stats([
        (euro(boot_tot["Moyenne"]), "Moyenne"),
        (euro(boot_tot["Ecart-type"]), "Écart-type"),
        (f"{boot_tot['CV'] * 100:.1f}".replace(".", ",") + "\u202f%", "Coefficient de variation"),
        (euro(boot_tot["Quantile 99.5%"]), "Quantile 99,5 % (VaR)"),
    ])
    sims = load_csv("bootstrap_simulations_R.csv")
    col = "reserve_totale" if "reserve_totale" in sims.columns else sims.select_dtypes("number").columns[0]
    fig = go.Figure()
    fig.add_histogram(x=sims[col], nbinsx=40, marker_color=NAVY_2, opacity=0.9, name="Simulations")
    fig.add_vline(x=sims[col].mean(), line_dash="dash", line_color=GREEN, line_width=3,
                  annotation_text="Moyenne", annotation_position="top left")
    fig.add_vline(x=sims[col].quantile(0.995), line_dash="dot", line_color=WINE, line_width=3,
                  annotation_text="VaR 99,5 %", annotation_position="top right")
    fig.update_layout(showlegend=False, bargap=0.04)
    fig.update_xaxes(tickformat=",.0f", title="PSAP totale simulée (€)")
    fig.update_yaxes(title="Nombre de simulations")
    show(style_fig(fig, 340))
    reading("<b>Lecture :</b> 2 000 simulations combinant incertitude d'estimation (ré-échantillonnage des "
            "résidus) et incertitude de process (loi Gamma). La moyenne coïncide avec la PSAP "
            "déterministe : c'est le test de cohérence attendu. Le quantile à 99,5 % alimente le SCR.")

# ------------------------------------------------------------------ Tarification
with tab_tarif:
    section("Relativités des modèles GLM")
    choix = st.radio("Modèle", ["Fréquence (Poisson)", "Coût moyen (Gamma)"], horizontal=True,
                     label_visibility="collapsed")
    fichier = "relativites_frequence_R.csv" if choix.startswith("Fréq") else "relativites_cout_moyen_R.csv"
    rel = load_csv(fichier)
    rel = rel[rel["variable"] != "(Intercept)"].copy()
    rel["label"] = rel["variable"].map(pretty_var)
    rel = rel.sort_values("relativite")
    fig = go.Figure()
    for _, r in rel.iterrows():
        fig.add_shape(type="line", x0=1, x1=r["relativite"], y0=r["label"], y1=r["label"],
                      line=dict(color=NAVY_2, width=2))
    fig.add_trace(go.Scatter(x=rel["relativite"], y=rel["label"], mode="markers",
                             marker=dict(color=WINE, size=11),
                             hovertemplate="%{y} : ×%{x:.2f}<extra></extra>"))
    fig.add_vline(x=1, line_dash="dash", line_color="#9AA5B4")
    fig.update_layout(showlegend=False)
    fig.update_xaxes(title="Relativité (1 = modalité de référence, survolez un point pour la valeur exacte)",
                     showgrid=True, gridcolor="#E9ECF1")
    fig.update_yaxes(showgrid=False)
    show(style_fig(fig, 400))
    reading("<b>Lecture :</b> un coefficient de ×1,50 signifie 50 % plus cher que la modalité de référence "
            "(zone 1, âge inférieur à 25 ans, puissance A). L'effet de l'âge est en U — il est donc traité par "
            "classes et non en continu. Dans le modèle de coût moyen, la zone est sans effet significatif, "
            "conformément à la simulation.")

# ------------------------------------------------------------------ Reassurance
with tab_reas:
    section("Effet du programme de réassurance sur le ratio S/P")
    reas = load_csv("synthese_reassurance_annuelle_R.csv")
    fig = go.Figure()
    for colonne, couleur, nom in [("SP_brut", NAVY_2, "S/P brut"), ("SP_net_xs", GOLD, "Net de XS"),
                                  ("SP_net_final", WINE, "Net final (XS + stop-loss)")]:
        fig.add_trace(go.Scatter(x=reas["annee_survenance"].astype(str), y=reas[colonne], mode="lines+markers",
                                 name=nom, line=dict(color=couleur, width=3), marker=dict(size=8)))
    fig.update_yaxes(tickformat=".0%", title="Ratio S/P")
    show(style_fig(fig, 340))
    reading("<b>Lecture :</b> 2020 est l'année la plus chargée (S/P brut de 84 %). C'est aussi celle où le "
            "stop-loss intervient le plus, ramenant le S/P net à 65 %. Le stop-loss ne se déclenche pas "
            "tous les ans : c'est une protection contre les années exceptionnelles.")
    eff = load_csv("efficacite_programme_R.csv")
    eff_fmt = pd.DataFrame({
        "Couche": eff["couche"],
        "Charge cédée (6 ans)": eff["charge_cedee_totale"].map(euro),
        "Prime cédée estimée par an": eff["prime_cedee_estimee_an"].map(euro),
        "S/P de cession": eff["ratio_S_sur_P_cession"].map(lambda v: f"{v:.2f}".replace(".", ",")),
    })
    st.dataframe(eff_fmt, width="stretch", hide_index=True)

# ------------------------------------------------------------------ Solvabilite II
with tab_solva:
    section("Des provisions sociales aux provisions Solvabilité II")
    ordre = solva.iloc[::-1]
    couleurs = [GOLD if "Provisions" in p else NAVY_2 for p in ordre["poste"]]
    fig = go.Figure(go.Bar(x=ordre["montant"], y=ordre["poste"], orientation="h", marker_color=couleurs,
                           text=[euro(v) for v in ordre["montant"]], textposition="outside", cliponaxis=False))
    fig.update_xaxes(tickformat=",.0f", showgrid=True, gridcolor="#E9ECF1", range=[0, ordre["montant"].max() * 1.25])
    fig.update_yaxes(showgrid=False)
    fig.update_layout(showlegend=False)
    show(style_fig(fig, 320))
    reading("<b>Lecture :</b> les provisions Solvabilité II sont inférieures à la PSAP en normes sociales : "
            "l'écart vient de l'actualisation des flux futurs, la Risk Margin (coût du capital de 6 %) restant "
            "faible sur un run-off court. Le SCR de risque de réserve est dérivé directement de la "
            "distribution bootstrap (VaR 99,5 % moins la moyenne).")

    section("Échéancier des flux futurs")
    ech = load_csv("echeancier_flux_futurs_R.csv")
    fig = go.Figure()
    fig.add_bar(x=ech["annee_calendaire"].astype(str), y=ech["flux"], name="Flux nominal", marker_color="#9FB1C9")
    fig.add_bar(x=ech["annee_calendaire"].astype(str), y=ech["flux_actualise"], name="Flux actualisé (2,5 %)",
                marker_color=NAVY_2)
    fig.update_layout(barmode="group")
    fig.update_yaxes(tickformat=",.0f", title="Flux (€)")
    show(style_fig(fig, 320))

st.caption("Pile technique : R · SAS (DATA step, PROC SQL, PROC GENMOD) · Shiny · cette page en Python / Streamlit.")
