import requests
import streamlit as st


# ========= *API*
# =======================================================================>

# Fonction pour récupérer les données depuis l'API.
def send_data_to_api(data, url="http://localhost:8000/data/post"):
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return st.success("Données insérées avec succès.")
    return st.error("Erreur lors de l'insertion des données.")
        
# =======================================================================>

# Fonction pour afficher les données depuis l'API.
def get_data_from_api(url="http://localhost:8000/data/get"):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json().get("data")
        st.success("Données récupérées avec succès.")
        return data
    return st.error("Erreur lors de la récupération des données.")
    
# =======================================================================>

# ========== *FRONT*
# =======================================================================>

# Fonction permettent de placer une image de fond pour site web.
def background(url:str):
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url({url});
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
    )
    
# =======================================================================>

# Fonction permettent d'apporter du CSS à nos pages.
def css_page():
    st.markdown("""
    <style>
        body {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        }
        
        h1 {
            font-family: 'Comic Sans MS', cursive, sans-serif;
            text-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5);
        }
    </style>
    """, unsafe_allow_html=True)

# =======================================================================>
