
# Import des librairies.
import streamlit as st
import numpy as np
import pymysql
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine, inspect


# Fonction permettent de créer une table en base de données.
def create_bdd_and_table(host:str, password:str, user:str, bdd_name:str, table_name:str):
    
    # Créer la base de données.
    cnx = mysql.connector.connect(
        user=user, 
        password=password, 
        host=host, 
        port=3306, 
        database=bdd_name, 
        ssl_disabled=False
    )
    
    # Créer une table.
    cursor = cnx.cursor()
    create_table_query = f"CREATE TABLE {table_name} (id INT PRIMARY KEY, name VARCHAR(50))"
    cursor.execute(create_table_query)

    # Fermer la connexion à la base de données.
    cnx.commit()
    cursor.close()
    cnx.close()

    