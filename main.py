import streamlit as st
from bdd import create_bdd_and_table

def main():
    
    # Création de la base de données et la table.
    create_bdd_and_table(
        password="Ounissi69800", 
        user="chemsdine",
        host="myserverchems.mysql.database.azure.com",
        bdd_name="linkedin_bdd",
        table_name="tesdddt"
    )
    
main()