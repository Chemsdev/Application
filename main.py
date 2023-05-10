import streamlit as st
from bdd import create_tables, data_insert, get_data_from_api
import requests


def main():
    
    # ======================= DATA =============================>
    create_tables(table_name_1="table_A", table_name_2="table_B")
    data_insert(table_name_1="table_a", table_name_2="table_b")
    
    # ======================= API ==============================>
    data = get_data_from_api()
    st.write("Données récupérées depuis la base de données :")
    if data:
        st.write(str(data))
    else:
        st.write("Aucune donnée disponible.")
        
main()

