import streamlit as st
from bdd import create_bdd_and_table, insert_data

def main():
    
    # Création de la base de données et la table.
    # create_bdd_and_table(table_name="test_oui")
    
    # Insertion des données
    insert_data(table_name="test_oui")

    
main()

