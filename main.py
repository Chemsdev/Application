import streamlit as st
import pandas as pd
from functions import send_data_to_api, create_tables, traitement_formulaire, background_front



def main():
    
    # ======================= FRONT =========================== #
    background_front(url="https://wallpaperaccess.com/full/1704480.jpg")
    
    # ======================== SQL ============================ #
    create_tables(table_name_1="features", table_name_2="predictions")
    
    # ===================== FORMULAIRE ======================== #
    st.title("Trouver l'emploie de vos rêves")
    st.markdown("")
    submitted, data = traitement_formulaire()
    if submitted:
        st.write(data)
        send_data_to_api(data)
    
main()



