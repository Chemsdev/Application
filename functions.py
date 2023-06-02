# =======================================================================================================================================>
#                                                            *UTILITAIRES*
# =======================================================================================================================================>

# Import des librairies.
import streamlit as st
import requests
import pandas as pd
import streamlit as st
from PIL import Image
    
# =======================================================================================================================================>
#                                                           *SQL API*
# =======================================================================================================================================>

# Fonction pour récupérer les données depuis l'API.
def send_data_to_api(data:dict, url="http://nlpindiselchems.azurewebsites.net/data/post"):
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return 
    # st.success("Données insérées avec succès.")
    return st.error("Erreur lors de l'insertion des données.")

# Fonction pour afficher les données depuis l'API.
def get_data_from_api(url="http://nlpindiselchems.azurewebsites.net/data/get"):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json().get("data")
        return data
    return st.error("Erreur lors de la récupération des données.")

# Fonction pour supprimer les données via l'API.
def delete_data_via_api(url="http://nlpindiselchems.azurewebsites.net/data/delete"):
    response = requests.delete(url)
    if response.status_code == 200:
        print("Les données ont été supprimées avec succès.")
    else:
        print("Erreur lors de la suppression des données.")

# =======================================================================================================================================>
#                                                            *FRONT*
# =======================================================================================================================================>

# Fonction permettent de créer un encadrer pour la prédiction.
def encadrer_texte_css(texte, couleur_bordure='#000000', epaisseur_bordure='1px', 
                       couleur_fond='transparent', padding='10px', texte_css=''):
    style = f'''
        border: {epaisseur_bordure} solid {couleur_bordure};
        background-color: {couleur_fond};
        padding: {padding};
        border-radius:40px
        {texte_css}
    '''

    encadrement = f'<div style="{style}">{texte}</div>'
    st.markdown(encadrement, unsafe_allow_html=True)
    
# =======================================================================================================================================>

# Fonction permettent de mettre un background.
def background_front(url:str):
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url({url});
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
    )
    
# =======================================================================================================================================>

# Fonction permettent d'apporter du style au site web.
def css_page_front():
    st.markdown("""
    <style>
        body {
        background-size: cover;
        }
        h1 {
            text-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5);
            font-color : #F5F5DC;
            font-size:67px;
        }
        p {
            text-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5);
            font-size:16px;
            font-weight:bold;
        }
    </style>
    """, unsafe_allow_html=True)
    
# =======================================================================================================================================>
    
# Fonction permettent d'apporter du style aux titres.
def style_text(title:str, size):
    css = f"""
        <style>
        .animate-character {{
            text-transform: uppercase;
            background-image: linear-gradient(-225deg, #231557 0%, #44107a 29%, #ff1361 67%, #fff800 100%);
            background-size: auto auto;
            background-clip: border-box;
            background-size: 200% auto;
            color: #fff;
            background-clip: text;
            text-fill-color: transparent;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: textclip 2s linear infinite;
            display: inline-block;
            font-size: {size}px;
            font-weight:bold;
        }}

        @keyframes textclip {{
            to {{
                background-position: 200% center;
            }}
        }}
        </style>
        """
    st.markdown(css, unsafe_allow_html=True)
    st.markdown(f'<p class="animate-character">{title}</p>', unsafe_allow_html=True)
    
# =======================================================================================================================================>
#                                                       *FORMULAIRE & AUTRES*
# =======================================================================================================================================>

# Fonction permettent de mettre les noms de colonnes aux DataFrames et faire un merge.
def columns_DataFrame(data1, data2, pred=False):
    columns_features=["id", "schedule_type", "search_term", "search_location", "description_tokens", "YEAR", "MONTH"]
    columns_prediction=["id","id_fk","y_pred"]
    features   = pd.DataFrame(data1, columns=columns_features)
    prediction = pd.DataFrame(data2, columns=columns_prediction)
    data = pd.merge(features, prediction, left_on='id', right_on='id_fk')
    data = data.drop(["id_y", "id_fk", "id_x"], axis=1)
    if pred:
        return data["y_pred"].iloc[-1]
    return data

# =======================================================================================================================================>

# Fonction permettent de créer le formulaire.
def traitement_formulaire():
    col1, col2 = st.columns(2)
    with st.form("formulaire"):
        with col1:
            data = {
                "schedule_type"  : st.selectbox('Type de contrat', options=['Full-time', 'Internship', 'Contractor', 'Part-time']),                
                "search_term"    : st.selectbox("Type de job", options=['data analyst']),        
                "search_location": st.selectbox('Localisation Travail', options=['United States']),                                                      
            }
        with col2:
            data2 = {
                "description_tokens": st.multiselect('Soft-Skills', ['Python', 'JavaScript', 'Java', 'C++', 'C#', 
                                                        'PHP', 'Ruby', 'Go', 'Swift', 'Rust', 'TypeScript', 
                                                        'Kotlin', 'Perl', 'Objective-C', 'Scala', 'Haskell', 
                                                        'Lua', 'Shell', 'HTML', 'CSS', 'SQL', 'Symfony', 'React', 
                                                        "Laravel", "VueJS", "django", "Flask", "Excel", "Word", 
                                                        "Tableau", "PowerBI", "Word", "PowerPoint"
                                                    ]),
                "YEAR":  st.selectbox('Années', options=["2022", "2023"]),     
                "MONTH": st.selectbox('Mois',   options=[str(i) for i in range(1, 13)]),
            }
        description_tokens = [f"{i}" for i in data2["description_tokens"]]
        data2["description_tokens"] =  ', '.join(description_tokens)
        submitted = st.form_submit_button("Envoyer")  
    data.update(data2)
    data["Prediction"] = "data scientist"
    return submitted, data

# =======================================================================================================================================>

# Fonction permettent de lire les images.
def read_picture(width:int, image:str, format:str):
    image = Image.open(f'images/{image}.{format}')
    return st.image(image, width=width)


