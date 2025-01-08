import streamlit as st  # type: ignore
import pandas as pd  # type: ignore
import numpy as np # type: ignore

# Set page configuration
st.set_page_config(
    page_title="Séminaire IYQ 2025",
    page_icon="⚛",
    layout="wide",
)


# Custom CSS for fixed header and footer
st.markdown(
    """
    <style>
        /* General body styling */
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: white;
        }

        .header {
            display: flex;
            justify-content: space-evenly;
            align-items: center;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 100;
            background-color: white;
            padding: 10px 0;
            text-align: center;
        }

        /* Fixed Footer */
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: black;
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
logo1 = "./images/logo-horizontal-white-bg.png"  # Example path
logo2 = "./images/logo-spa.png"  # Example path
logo3 = "./images/logo-hk.png"  # Example path

# Display the logos
col1, col2, col3, col4, col4 = st.columns(5)
with col1:
    st.image(logo1, width=300, use_column_width='auto')
with col2:
    st.empty()  
with col3:
    st.image(logo2, width=150)
with col4:
    st.empty()  
with col4:
    st.image(logo3, width=300, use_column_width='auto')

    

# Content Section
st.markdown('<div class="content">', unsafe_allow_html=True)

# Seminar Information
seminar_title = "Célébration de la Science Quantique et Hommage aux fondateurs du parcours Physique-Chimie de l'ENS"
date = "16 janvier 2025"
time = "13:15 - 15:15 (UTC+3)"
location = "Hybride (En ligne & Petit Amphi de l'ENS Ampefiloha)"
description = (
    "Rejoignez-nous pour célébrer l'Année Internationale des Sciences et Technologies Quantiques, "
    "avec des conférences et des discussions passionnantes sur la physique quantique, la physique des lasers, "
    "l'apprentissage automatique, l'astronomie et la vulgarisation.\n\n"
    "Dans le cadre de cet événement, nous organisons une cérémonie pour honorer les membres fondateurs du parcours Physique-Chimie — **Dr Charles Ratsifaritana**, **Dr Faneva Randrianandraina**, **Dr René Rasoanaivo**, **Dr Henri Rasolondramanitra**,  **Dr Herimanda Ramilison**, **Prof. Judith Razafimbelo** et **Prof. Kristiane Rakotobe** — pour leurs contributions inestimables à l’établissement de ce parcours à l’ENS Antananarivo. "
    "Leur vision collective et leur dévouement ont été déterminants dans la création de la base académique qui a permis à de nombreux étudiants de se former, et nous souhaitons leur exprimer notre plus profonde gratitude."
)


# Header
st.title(seminar_title)
st.markdown("\n \n")

st.header(f"𝄜  {date} | ⏰ {time} | 📍 {location}")
st.write(description)

# Programme Section
st.markdown("## 📋 Programme du Séminaire")

# Programme Table
programme_data = {
    "Intervenant": [
        "M. RIJARIMANANA Tiana, PhD",
        "M. RAOGNINIRINA Joseph Carthy",
        "Représentant de l’ENS",
        "M. RATSIFARITANA Charles, PhD",
        "M. Herimampionona Zeze Franckie",
        "M. RAKOTOMANGA Mendrika",
        "Mme. RATSIMANDRESY Dina Miora, PhD",
        "M. RAJAONARIVELO Andoniaina",
        "M. RANDRIANANDRAINA Faneva, PhD",
        "Equipe organisatrice",
        "Tous les Invités",
        "Tous les Invités",
    ],
    "Affiliation": [
        "Chef Parcours PC, ENS",
        "Président de l’AEPCENS",
        "ENS",
        "Professeur fondateur du parcours PC",
        "Président de l’association Sciences Physiques et Avenir",
        "Ancien Élève ENS, University of Leeds",
        "Ancienne Élève ENS, MRC-LMB, Cambridge",
        "Ancien Élève ENS, Directeur de l’observatoire de Besely",
        "Professeur fondateur du parcours PC",
        "N/A",
        "N/A",
        "N/A",
    ],
    "Thème": [
        "Prise de parole",
        "Prise de parole",
        "Prise de parole",
        "Physique Quantique & Histoire du Parcours PC",
        "Outreach & Education",
        "Intelligence Artificielle et Apprentissage Automatique",
        "Physique des Lasers & Biologie Moléculaire",
        "Astronomie Observationnelle",
        "Astrophysique",
        "Cérémonie de remerciement",
        "Prise de Photo",
        "Cocktail",
    ],
    "Durée (minutes)": [
        5, 5, 5, 30, 10, 10, 10, 10, 15, 15, 5, "N/A"
    ],
}

# Display the table as a DataFrame
programme_df = pd.DataFrame(programme_data, index=1+np.arange(len(programme_data["Affiliation"])))
st.table(programme_df)

# Add Join Information
st.markdown("## 🔗 Rejoindre le Séminaire")
st.write(
    """
    Le séminaire est hybride. Utilisez les liens ci-dessous pour rejoindre en ligne ou accéder à l'enregistrement :

    - [Rejoindre via Zoom](#)
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

    L'entree est gratuite et tout le monde est le bienvenue.

    Veuillez contacter mendrika@aims.ac.za ou andoniaina@gmail.com pour toutes requetes.
    """
)

# Closing Content Div
st.markdown('</div>', unsafe_allow_html=True)

# Fixed Footer
st.markdown(
    """
    <div class="footer">
        Conçu par Mendrika Rakotomanga | <a href="mailto:mendrika@aims.ac.za">mendrika@aims.ac.za</a>
    </div>
    """,
    unsafe_allow_html=True,
)
