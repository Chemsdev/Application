import streamlit as st
from bdd import create_bdd_and_table

def main():
    
    # Création de la base de données et la table.
    create_bdd_and_table(
        table_name="test", 
        bdd_name="linkedin", 
        password="", 
        user="root"
    )
    
main()