import streamlit as st
import pandas as pd
from functions import send_data_to_api, create_tables, traitement_formulaire, background_front, style_text



def main():
    
    # ======================= FRONT =========================== #
    background_front(url="https://nano.scrolller.com/abstract-wallpaper-9nyw4ngmg1.jpg")
    
    # ======================== SQL ============================ #
    create_tables(table_name_1="features", table_name_2="predictions")
    
    # ===================== FORMULAIRE ======================== #
    style_text(text="Trouve l'emploi de tes rêves")
       
    st.markdown("")
    submitted, data = traitement_formulaire()
    if submitted:
        send_data_to_api(data)
    
main()



