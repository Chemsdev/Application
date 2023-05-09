
# Import des librairies.
import streamlit as st
import numpy as np
import pymysql
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect


# Fonction permettent de créer une table en base de données.
def create_bdd_and_table(table_name:str, bdd_name:str, password:str, user:int):
    
    # Créer la base de données.
    conn=pymysql.connect(host='localhost', port=int(3306), user=user, passwd=password, db='neuronal_convolutif')
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE {bdd_name}")
    engine=create_engine(f'mysql+pymysql://root:@localhost/{bdd_name}')
    inspector=inspect(engine)

    # On vérifie si la table existe.
    if not table_name in inspector.get_table_names():
        
        # Initialisation des colonnes.
        df = pd.DataFrame({'Feature_1':[], 'Feature_2':[] , 'Feature_3':[], "Feature_4":[]})
        
        # Typage des colonnes de la Table SQL.
        df['Feature_1'] = df['Feature_1'].astype('str')
        df['Feature_2'] = df['Feature_2'].astype('str')
        df['Feature_3'] = df['Feature_3'].astype('str')
        df['Feature_4'] = df['Feature_4'].astype('str')
        
        # envoie du DataFrame sur SQL.
        df.to_sql(name=table_name, con=engine, if_exists='fail', index=False)
    print(f"Création de la table {table_name} avec succès.")