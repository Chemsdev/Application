
# Import des librairies.
import streamlit as st
import numpy as np
import pymysql
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect
import mysql.connector


# Fonction permettent de créer une table en base de données.
def create_bdd_and_table(host:str, password:str, user:str, bdd_name:str):
    
    # Créer la base de données.
    cnx = mysql.connector.connect(
        user="chemsdine", 
        password=password, 
        host=host, 
        port=3306, 
        database=bdd_name, 
        # ssl_ca="{ca-cert filename}", 
        ssl_disabled=False)
    
    cursor = cnx.cursor()
    cursor.execute(f"CREATE DATABASE {bdd_name}")