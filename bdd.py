
# Import des librairies.
import streamlit as st
import numpy as np
import mysql.connector
import pandas as pd
import random
import requests

# =======================================================================================================================================>

# Les paramètres de connexion (à changer !!).
cnx = mysql.connector.connect(
    user="chemsdine", 
    password="Ounissi69800", 
    host="myserverchems.mysql.database.azure.com", 
    port=3306, 
    database="linkedin_bdd", 
    ssl_disabled=False
)

# Url app Fast
api_url = "http://localhost:8000/data/"

# =======================================================================================================================================>

# Fonction permettent de créer les tables dans une base de données.
def create_tables(table_name_1:str, table_name_2:str, connexion=cnx):    
    cursor = connexion.cursor()
    col_names = ['feature_' + str(i) for i in range(3)]
    col_names_str = ','.join([f'{i} REAL' for i in col_names])
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name_1}
                (id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, {col_names_str})''')
    print(f"Table '{table_name_1}' créée avec succès.")
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name_2}
                (id_fk int NOT NULL DEFAULT 0,
                y_pred TEXT,
                FOREIGN KEY (id_fk) REFERENCES {table_name_1}(id))''')
    print(f"Table '{table_name_2}' créée avec succès.")
    connexion.commit()
    
# =======================================================================================================================================>

# Fonction permettent d'insérer des données dans les tables cible.
def data_insert(table_name_1: str, table_name_2: str, connexion=cnx):
    cursor = connexion.cursor()
    code_id = "".join([str(random.randint(0, 10)) for _ in range(5)])  
    table1_columns = ["id",  "feature_0",  "feature_1",  "feature_2"]
    table1_values  = [code_id,     "0",          "1",          "2"]
    table1_sql = f"INSERT INTO {table_name_1} ({', '.join(table1_columns)}) VALUES ({', '.join(['%s' for i in range(4)])})"
    cursor.execute(table1_sql, table1_values)
    table2_columns = ["id_fk",  "y_pred"]
    table2_values  = [code_id,  "Data Scientist"]
    table2_sql = f"INSERT INTO {table_name_2} ({', '.join(table2_columns)}) VALUES ({', '.join(['%s' for i in range(2)])})"
    cursor.execute(table2_sql, table2_values)
    connexion.commit()
    
# =======================================================================================================================================>

# Fonction permettent récupérer les données depuis votre API FastAPI
def get_data_from_api(api_url=api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()["data"]
        return data
    st.error("Une erreur s'est produite lors de la récupération des données.")

# =======================================================================================================================================>