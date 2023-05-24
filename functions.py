# =======================================================================================================================================>
#                                                            *UTILITAIRES*
# =======================================================================================================================================>

# Import des librairies.
import streamlit as st
import mysql.connector
import requests
import pandas as pd
import numpy as np
import streamlit as st

# Paramètre de connexion.
cnx = mysql.connector.connect(
    user="chemsdine", 
    password="Ounissi69800", 
    host="myserverchems.mysql.database.azure.com", 
    port=3306, 
    database="linkedin_bdd", 
    ssl_disabled=False
)
cursor = cnx.cursor()    


# =======================================================================================================================================>
#                                                      *SQL DATABASE*
# =======================================================================================================================================>

# Fonction permettant de créer les tables dans une base de données.
def create_tables(table_name_1:str, table_name_2:str, connexion=cnx, cursor=cursor):
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name_1}
    (id INT AUTO_INCREMENT PRIMARY KEY,
    feature_1 TEXT,
    feature_2 TEXT,
    feature_3 TEXT)
    ''')
    print(f"Table '{table_name_1}' créée avec succès.")    
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name_2}
                (id INT AUTO_INCREMENT PRIMARY KEY,
                id_fk INT,
                y_pred TEXT,
                FOREIGN KEY (id_fk) REFERENCES {table_name_1}(id))''')
    print(f"Table '{table_name_2}' créée avec succès.")
    connexion.commit()
    
# =======================================================================================================================================>
#                                                        *SQL API*
# =======================================================================================================================================>

# Fonction pour récupérer les données depuis l'API.
def send_data_to_api(data:dict, url="http://localhost:8000/data/post"):
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return st.success("Données insérées avec succès.")
    return st.error("Erreur lors de l'insertion des données.")

# Fonction pour afficher les données depuis l'API.
def get_data_from_api(url="http://localhost:8000/data/get"):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json().get("data")
        return data
    return st.error("Erreur lors de la récupération des données.")

# Fonction pour supprimer les données via l'API.
def delete_data_via_api(url="http://localhost:8000/data/delete"):
    response = requests.delete(url)
    if response.status_code == 200:
        print("Les données ont été supprimées avec succès.")
    else:
        print("Erreur lors de la suppression des données.")

# =======================================================================================================================================>
#                                                        *FRONT*
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
            font-size:25px;
            # text-shadow: 1px 1px 2px pink;
        }
    </style>
    """, unsafe_allow_html=True)

# =======================================================================================================================================>

# fonction permettent de créer l'encart pour afficher la prédiction.
def encart_prediction(color:str, predict:str):
    st.markdown("")
    box_style = f"""
        padding: 20px;
        width: 230px;
        height: 80px;
        border: 2px solid {color};
        border-radius: 5px
    """

    text_style = f"""
        color: {color};
        font-size: 18px;
        font-weight: bold;
    """

    st.markdown(
        f'<div style="{box_style}">'
        f'<p style="{text_style}">Votre vol est {predict} !</p>'
        f'</div>',
        unsafe_allow_html=True
    )

# =======================================================================================================================================>

# Fonction permettent de mettre les noms de colonnes aux DataFrames et faire un merge.
def columns_DataFrame(data1, data2):
    columns_features=['id','feature_1', 'feature_2', 'feature_3']
    columns_prediction=["id","id_fk","y_pred"]
    features   = pd.DataFrame(data1, columns=columns_features)
    prediction = pd.DataFrame(data2, columns=columns_prediction)
    data = pd.merge(features, prediction, left_on='id', right_on='id_fk')
    data = data.drop(["id_y", "id_fk", "id_x"], axis=1)
    return data

# =======================================================================================================================================>

# Fonction permettent de créer le formulaire.
def traitement_formualaire():
    st.write("Veuillez remplir le formulaire")
    with st.form(f"formulaire"):
        data = {
            "feature_1" : st.text_input(f'Veuillez saisir la feature 1',  key=1),                
            "feature_2" : st.text_input(f'Veuillez saisir la feature 2',  key=2),        
            "feature_3" : st.text_input(f'Veuillez saisir la feature 3',  key=3),   
            "Prediction" :st.text_input(f'Veuillez saisir la prédiction', key=4),                       
        }
        submitted = st.form_submit_button("Envoyer")
    return submitted, data

