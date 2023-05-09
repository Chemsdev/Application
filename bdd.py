
# Import des librairies.
import streamlit as st
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine, inspect

# Les paramètres de connexion.
cnx = mysql.connector.connect(
    user="chemsdine", 
    password="Ounissi69800", 
    host="myserverchems.mysql.database.azure.com", 
    port=3306, 
    database="linkedin_bdd", 
    ssl_disabled=False
)

# =======================================================================================================================================>

# Fonction permettent de créer une table en base de données.
def create_bdd_and_table(table_name:str, cnx=cnx):    
    cursor = cnx.cursor()
    create_table_query = f"CREATE TABLE {table_name} (id INT PRIMARY KEY, name_1 VARCHAR(50),  name_2 VARCHAR(50),  name_3 VARCHAR(50))"
    cursor.execute(create_table_query)
    cnx.commit()
    cursor.close()
    cnx.close()    
    print(f"Création de la table{table_name}")
    return cnx, cursor

# =======================================================================================================================================>

# Fonction permettent d'insérer des données dans la table'
def insert_data(table_name:str, cnx=cnx):
    cursor = cnx.cursor()
    columns_table =  ["id", "feature_1", "feature_2", "feature_3"]
    values_table  =  [1,    "0",         "0",         "0"]
    sql = f"INSERT INTO {table_name} ({', '.join(columns_table)}) VALUES ({', '.join(['%s' for i in range(4)])})"
    cursor.execute(sql, values_table)
    cnx.commit()
    cnx.close()

# =======================================================================================================================================>
