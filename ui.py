"""Interface du portfolio : feuille de style et composants HTML reutilisables.

IMPORTANT : tout le HTML/CSS personnalise passe par st.html() et NON par
st.markdown(). Le Markdown interprete les lignes vides et l'indentation, ce qui
coupe les blocs <style> en morceaux et affiche du CSS en texte brut a l'ecran.
"""
import html

import streamlit as st

NAVY = "#0F1E33"
NAVY_2 = "#1B3A5C"
GOLD = "#B8925A"
GOLD_LIGHT = "#D8B77E"
WINE = "#8A3B3B"
GREEN = "#1F6F4A"
BG = "#F6F7F9"
LINE = "#E3E7EE"
TEXT = "#1F2937"
TEXT_SOFT = "#5B6779"

FONT_STACK = ("'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, "
              "'Helvetica Neue', Arial, sans-serif")

CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {{ background: {BG}; }}
.stApp, .stApp p, .stApp li, .stApp label, .stApp h1, .stApp h2, .stApp h3, .stApp h4,
.stApp [data-testid="stMarkdownContainer"], .stApp [data-testid="stCaptionContainer"] {{
    font-family: {FONT_STACK};
    color: {TEXT};
}}
[data-testid="stMainBlockContainer"] {{
    max-width: 1080px; padding-top: 2.4rem; padding-bottom: 4rem;
}}
#MainMenu, footer, [data-testid="stDecoration"] {{ visibility: hidden; }}
.stAppDeployButton, [data-testid="stAppDeployButton"] {{ display: none; }}

/* navigation de secours visible uniquement sur mobile (la nav du haut y est repliee) */
.st-key-mobile_nav {{ display: none; }}
@media (max-width: 720px) {{
    .st-key-mobile_nav {{ display: block; background: #fff; border: 1px solid {LINE};
        border-radius: 10px; padding: 4px 8px; margin-bottom: 14px; }}
}}

/* ---------- hero ---------- */
.hero {{
    background: linear-gradient(135deg, {NAVY} 0%, {NAVY_2} 100%);
    border-radius: 16px; padding: 46px 46px 40px 46px; color: #fff;
}}
.hero .kicker {{ font-size: 12px; font-weight: 600; letter-spacing: .16em;
    color: {GOLD_LIGHT}; text-transform: uppercase; }}
.hero h1 {{ font-size: 46px; font-weight: 800; line-height: 1.1; letter-spacing: -.02em;
    margin: 12px 0 14px 0; padding: 0; color: #fff; }}
.hero p {{ font-size: 17px; line-height: 1.6; color: #CBD5E4; max-width: 660px; margin: 0 0 26px 0; }}
.hero .links a {{ display: inline-block; font-size: 14px; font-weight: 600; text-decoration: none;
    padding: 9px 18px; border-radius: 8px; margin: 0 10px 8px 0;
    background: {GOLD_LIGHT}; color: {NAVY}; }}
.hero .links a.ghost {{ background: transparent; color: #fff; border: 1px solid rgba(255,255,255,.35); }}

/* ---------- tuiles chiffres ---------- */
.stats {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin: 18px 0 8px 0; }}
.stat {{ background: #fff; border: 1px solid {LINE}; border-radius: 12px; padding: 18px 20px; }}
.stat .v {{ font-size: 26px; font-weight: 700; color: {NAVY}; line-height: 1.2; }}
.stat .l {{ font-size: 13px; color: {TEXT_SOFT}; margin-top: 5px; line-height: 1.45; }}
.stats.three {{ grid-template-columns: repeat(3, 1fr); }}

/* ---------- titres de section ---------- */
.section-h {{ font-size: 22px; font-weight: 700; color: {NAVY}; margin: 14px 0 12px 0;
    display: flex; align-items: center; gap: 12px; }}
.section-h::before {{ content: ""; width: 5px; height: 22px; background: {GOLD}; border-radius: 3px; }}
.lead {{ font-size: 16px; line-height: 1.7; color: {TEXT}; margin: 0 0 8px 0; }}
.muted {{ color: {TEXT_SOFT}; font-size: 14px; line-height: 1.6; }}

/* ---------- pastilles ---------- */
.chips {{ margin-top: 4px; }}
.chips span {{ display: inline-block; background: #EAEFF7; color: {NAVY_2}; border-radius: 999px;
    padding: 4px 12px; font-size: 12.5px; font-weight: 500; margin: 0 6px 7px 0; }}

/* ---------- cartes ---------- */
.card {{ background: #fff; border: 1px solid {LINE}; border-radius: 12px; padding: 22px 24px; margin-bottom: 14px; }}
.card h3 {{ font-size: 17px; font-weight: 700; color: {NAVY}; margin: 0 0 6px 0; padding: 0; }}
.card p {{ font-size: 14.5px; line-height: 1.6; color: {TEXT}; margin: 0 0 10px 0; }}
.skill-group {{ margin-bottom: 14px; }}
.skill-group .t {{ font-size: 12px; font-weight: 700; letter-spacing: .08em; color: {WINE};
    text-transform: uppercase; margin-bottom: 6px; }}

/* ---------- experiences ---------- */
.exp {{ background: #fff; border: 1px solid {LINE}; border-left: 4px solid {GOLD};
    border-radius: 12px; padding: 22px 26px; margin-bottom: 16px; }}
.exp-head {{ display: flex; justify-content: space-between; align-items: flex-start; gap: 16px; flex-wrap: wrap; }}
.exp-role {{ font-size: 18px; font-weight: 700; color: {NAVY}; line-height: 1.3; }}
.exp-org {{ font-size: 14.5px; font-weight: 600; color: #8C6A2F; margin-top: 3px; }}
.exp-when {{ font-size: 13px; font-weight: 500; color: {TEXT_SOFT}; background: #F1F3F7;
    padding: 5px 11px; border-radius: 6px; white-space: nowrap; }}
.exp ul {{ margin: 14px 0 10px 0; padding-left: 20px; }}
.exp li {{ margin-bottom: 6px; color: {TEXT}; font-size: 14.5px; line-height: 1.6; }}
.exp li ul {{ margin: 6px 0 4px 0; }}

/* ---------- mini frise (accueil) ---------- */
.frise-row {{ display: flex; gap: 18px; padding: 12px 0; border-top: 1px solid {LINE}; align-items: baseline; }}
.frise-row:last-child {{ border-bottom: 1px solid {LINE}; }}
.frise-when {{ width: 150px; flex: none; font-size: 13px; color: #8C6A2F; font-weight: 600; }}
.frise-what {{ font-size: 15px; font-weight: 600; color: {NAVY}; }}
.frise-org {{ font-size: 13.5px; color: {TEXT_SOFT}; }}

/* ---------- lecture des graphiques ---------- */
.reading {{ background: #fff; border: 1px solid {LINE}; border-left: 4px solid {NAVY_2};
    border-radius: 8px; padding: 12px 16px; font-size: 14px; line-height: 1.6; color: {TEXT}; margin: 6px 0 14px 0; }}
.reading b {{ color: {NAVY}; }}

@media (max-width: 720px) {{
    .hero {{ padding: 30px 24px; }}
    .hero h1 {{ font-size: 34px; }}
    .stats, .stats.three {{ grid-template-columns: repeat(2, 1fr); }}
    .frise-row {{ flex-direction: column; gap: 2px; }}
    .frise-when {{ width: auto; }}
    .exp {{ padding: 18px 18px; }}
}}
"""


def inject_css() -> None:
    st.html(f"<style>{CSS}</style>")


def esc(text: str) -> str:
    return html.escape(str(text), quote=False)


def chips(items) -> str:
    return '<div class="chips">' + "".join(f"<span>{esc(i)}</span>" for i in items) + "</div>"


def section(title: str) -> None:
    st.html(f'<div class="section-h">{esc(title)}</div>')


def hero(kicker: str, title: str, text: str, links=None) -> None:
    links_html = ""
    if links:
        links_html = '<div class="links">' + "".join(
            f'<a class="{"ghost" if ghost else ""}" href="{esc(url)}" target="_blank" '
            f'rel="noopener noreferrer">{esc(label)}</a>'
            for label, url, ghost in links
        ) + "</div>"
    st.html(
        f'<div class="hero"><div class="kicker">{esc(kicker)}</div>'
        f"<h1>{esc(title)}</h1><p>{esc(text)}</p>{links_html}</div>"
    )


def stats(items, three: bool = False) -> None:
    cls = "stats three" if three else "stats"
    st.html(
        f'<div class="{cls}">'
        + "".join(f'<div class="stat"><div class="v">{esc(v)}</div><div class="l">{esc(l)}</div></div>'
                  for v, l in items)
        + "</div>"
    )


def experience_card(role, org, when, bullets, tags) -> None:
    def render(items):
        out = "<ul>"
        for it in items:
            if isinstance(it, tuple):
                head, subs = it
                out += f"<li>{esc(head)}{render(subs)}</li>"
            else:
                out += f"<li>{esc(it)}</li>"
        return out + "</ul>"

    st.html(
        '<div class="exp"><div class="exp-head"><div>'
        f'<div class="exp-role">{esc(role)}</div><div class="exp-org">{esc(org)}</div></div>'
        f'<div class="exp-when">{esc(when)}</div></div>'
        f"{render(bullets)}{chips(tags)}</div>"
    )


def reading(text_html: str) -> None:
    """Encadre de lecture d'un graphique. text_html est du HTML de confiance (contenu statique)."""
    st.html(f'<div class="reading">{text_html}</div>')


def euro(x: float) -> str:
    return f"{x:,.0f}".replace(",", "\u202f") + "\u00a0\u20ac"
