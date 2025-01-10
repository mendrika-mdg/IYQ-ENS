import streamlit as st  # type: ignore
import pandas as pd  # type: ignore
import numpy as np # type: ignore

# Set page configuration
st.set_page_config(
    page_title="Séminaire IYQ ENS 2025",
    page_icon="⚛",
    layout="wide",
)

# Custom CSS for fixed header and footer
st.markdown(
    """
    <style>
        /* General body styling */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stSidebar"] {
            background-color: white !important;
            color: black !important;
        }

        /* Fixed Footer */
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: black !important;            
            color: white;
            padding: 10px;
            border-top: 1px solid #ddd;
            text-align: center;
            z-index: 1000;
        }

        /* Remove any padding or margin for the content */
        .content {
            padding-top: 0;
            margin-top: 0;
        }

        /* Ensure the header and body start right at the top without any space */
        .streamlit-expanderHeader {
            margin-top: 0;
        }

    </style>
    """,
    unsafe_allow_html=True,
)

# You can replace the paths below with your own local paths or URLs for the logos.
logo_iyq = "./images/logo-horizontal-white-bg.png"  
logo_spa = "./images/logo-spa.png"                 
logo_hk = "./images/logo-hk.png" 
logo_aepcens = "./images/logo-aepcens-inverted.png"
partners = "./images/partners-updated.png"
logo_itatra = "./images/logo-itatra.png"

st.image(partners, use_container_width=True)

# Content Section
st.markdown('<div class="content">', unsafe_allow_html=True)

# Seminar Information
seminar_title = "Célébration de la Science Quantique et Hommage aux Fondateurs du Parcours Physique-Chimie de l'ENS Antananarivo"
date = "16 janvier 2025"
time = "13:15 - 15:15 (UTC+3)"
location = "Hybride (Zoom & Petit Amphi ENS Ampefiloha)"
description = (
    "Rejoignez-nous pour célébrer l'Année Internationale des Sciences et Technologies Quantiques, "
    "avec des conférences et des discussions passionnantes sur la physique quantique, la physique des lasers, "
    "l'intelligence artificielle, l'astronomie et la vulgarisation.\n\n"
    "Dans le cadre de cet événement, nous organisons une cérémonie pour honorer les membres fondateurs du parcours Physique-Chimie — **Dr Charles Ratsifaritana**, **Dr Faneva Randrianandraina**, **Dr René Rasoanaivo**, **Dr Henri Rasolondramanitra**, **Dr Herimanda Ramilison**, **Prof. Judith Razafimbelo** et **Prof. Christiane Rakotobe** — pour leurs contributions inestimables à l’établissement de ce parcours à l’ENS Antananarivo. "
    "Leur vision collective et leur dévouement ont été déterminants dans la création d’une base académique solide, "
    "permettant à de nombreux étudiants de se former, de s’inspirer et, à leur tour, d’impacter les élèves malgaches. "
    "Nous aimerions leur exprimer notre plus profonde gratitude."
)


# Header
st.title(seminar_title)
st.markdown("\n \n")

st.header(f"𝄜  {date} | ⏰ {time} | 📍 {location}")
st.write(description)

# Programme Section
st.markdown("## 📋 Programme du Séminaire")

programme_data = [
    ["Dr. RIJARIMANANA Tiana", "Chef Parcours PC, ENS", "Prise de parole", "5"],
    ["M. RAOGNINIRINA Joseph Carthy", "Président de l’AEPCENS", "Prise de parole", "5"],
    ["Représentant de l’ENS", "ENS", "Prise de parole", "5"],
    ["Dr RATSIFARITANA Charles", "Enseignant fondateur du parcours PC", "Physique Quantique & Histoire du Parcours PC", "30"],
    ["Dr RANDRIANANDRAINA Faneva", "Enseignant fondateur du parcours PC", "Astrophysique", "15"],
    ["M. RAJAONARIVELO Andoniaina", "Ancien Élève ENS, Directeur de l’observatoire de Besely", "Astronomie Observationnelle", "10"],
    ["M. Herimampionona Zeze Franckie", "Président de l’association Sciences Physiques et Avenir", "Outreach & Education", "10"],
    ["M. RAKOTOMANGA Mendrika", "Ancien Élève ENS, University of Leeds", "Intelligence Artificielle et Data Science", "10"],
    ["Dr RATSIMANDRESY Dina Miora", "Ancienne Élève ENS, MRC-LMB, Cambridge", "Physique des Lasers & Biologie Moléculaire", "10"],
    ["Equipe organisatrice", "N/A", "Cérémonie de remerciement", "15"],
    ["Tous les Invités", "N/A", "Prise de Photo", "5"],
    ["Tous les Invités", "N/A", "Cocktail", "30"],
]

# Generate HTML for the table
table_html = """
<table border="1" style="width: 100%; border-collapse: collapse; text-align: left;">
    <thead>
        <tr style="background-color: #4CAF50; color: white;">
            <th>Intervenant</th>
            <th>Affiliation</th>
            <th>Thème</th>
            <th>Durée (minutes)</th>
        </tr>
    </thead>
    <tbody>
"""
for row in programme_data:
    table_html += "<tr>"
    for cell in row:
        table_html += f"<td style='padding: 8px;'>{cell}</td>"
    table_html += "</tr>"

table_html += """
    </tbody>
</table>
"""

# Display the table in Streamlit
st.markdown(table_html, unsafe_allow_html=True)
# Add Join Information
st.markdown("## 🔗 Rejoindre le Séminaire")
st.write(
    """
    Le séminaire est hybride. Utilisez les liens ci-dessous pour rejoindre en ligne ou accéder à l'enregistrement :

    - [Rejoindre via Zoom](https://us02web.zoom.us/j/85923106189?pwd=8khEtmsE1WuSRLDkVyTg7aQOjlBFqb.1)
    - [Regarder l'Enregistrement (Disponible après l'événement)](#)
    """
)


st.markdown("""
    ## 🗂️ Organisateur et comité scientifique
    - Dr Andriniaina Rasoanaivo
    - Andoniaina Rajaonarivelo
    - Mendrika Rakotomanga
    - Zeze Franckie Herimampionona
    - Francia Mamitahiry
    - Association des Etudiants en PC de l'ENS
    """)

# Closing Remarks Section
st.markdown("## 📝 Remarques et Invitations")
st.write(
    """
    Nous avons hâte d'accueillir tous les participants à ce séminaire. 
    Ensemble, nous célébrerons le passé et explorerons l'avenir de la physique 
    et de ses applications.
    """
)

# Custom success message with black text
st.markdown(
    """
    <div style="background-color: #dff0d8; color: black; padding: 10px; border-radius: 5px; font-weight: bold;">
        L'entrée est gratuite et tout le monde est le bienvenue.
    </div>
    """, 
    unsafe_allow_html=True
)


st.markdown("")

# Custom warning message with black text
st.markdown(
    """
    <div style="background-color: #fcf8e3; color: black; padding: 10px; border-radius: 5px; font-weight: bold;">
        Veuillez contacter <a href="mailto:mendrika@aims.ac.za" style="color: blue;">mendrika@aims.ac.za</a> ou 
        <a href="mailto:andoniainarajaonari@gmail.com" style="color: blue;">andoniainarajaonari@gmail.com</a> 
        pour toutes requêtes.
    </div>
    """, 
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)

# Fixed Footer
st.markdown(
    """
    <div class="footer">
        © Mendrika Rakotomanga 2025 | <a href="mailto:mendrika@aims.ac.za">mendrika@aims.ac.za</a>
    </div>
    """,
    unsafe_allow_html=True,
)
