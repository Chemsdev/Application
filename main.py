import streamlit as st
import pandas as pd
from functions import send_data_to_api, create_tables, traitement_formualaire, background_front



def main():
    
    # ======================= FRONT =========================== #
    background_front(url="https://wallpapercave.com/wp/wp3460663.jpg")
    
    # ======================== SQL ============================ #
    create_tables(table_name_1="features", table_name_2="predictions")
    
    # ===================== FORMULAIRE ======================== #
    submitted, data = traitement_formualaire()
    
    if submitted:
        send_data_to_api(data)
    
main()