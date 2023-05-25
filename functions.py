# =======================================================================================================================================>
#                                                            *UTILITAIRES*
# =======================================================================================================================================>

# Import des librairies.
import streamlit as st
import mysql.connector
import requests
import pandas as pd
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
    schedule_type TEXT,
    search_term TEXT,
    search_location TEXT,
    description_tokens TEXT,
    YEAR  INTEGER,
    MONTH INTEGER)
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
#                                                           *SQL API*
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
#                                                            *FRONT*
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
    
# Fonction permettent d'apporter du style aux titres.
def style_text(text:str):
    css = """
    <style>
    .animate-character {
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
        font-size: 45px;
        font-weight:bold;
    }

    @keyframes textclip {
        to {
            background-position: 200% center;
        }
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
    st.markdown(f'<p class="animate-character">{text}</p>', unsafe_allow_html=True)
    
# =======================================================================================================================================>
#                                                       *FORMULAIRE & DATA*
# =======================================================================================================================================>

# Fonction permettent de mettre les noms de colonnes aux DataFrames et faire un merge.
def columns_DataFrame(data1, data2):
    columns_features=["id", "schedule_type", "search_term", "search_location", "description_tokens", "YEAR", "MONTH"]
    columns_prediction=["id","id_fk","y_pred"]
    features   = pd.DataFrame(data1, columns=columns_features)
    prediction = pd.DataFrame(data2, columns=columns_prediction)
    data = pd.merge(features, prediction, left_on='id', right_on='id_fk')
    data = data.drop(["id_y", "id_fk", "id_x"], axis=1)
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
                "YEAR":  st.selectbox('Années', options=[2022, 2023]),     
                "MONTH": st.selectbox('Mois', options=[i+1 for i in range(12)]),
            }
        description_tokens = [f"{i}" for i in data2["description_tokens"]]
        data2["description_tokens"] =  ', '.join(description_tokens)
        submitted = st.form_submit_button("Envoyer")  
    data.update(data2)
    data["Prediction"] = "data scientist"
    return submitted, data

