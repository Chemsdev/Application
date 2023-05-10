import streamlit as st
import pandas as pd
import requests


# =======================================================================>
# Fonction pour récupérer les données depuis l'API.
def send_data_to_api(data, url="http://localhost:8000/data/post"):
    response = requests.post(url, json=data)
    if response.status_code == 200:
        st.success("Données insérées avec succès.")
    else:
        st.error("Erreur lors de l'insertion des données.")
# =======================================================================>
# Fonction pour afficher les données depuis l'API.
def get_data_from_api(url="http://localhost:8000/data/get"):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json().get("data")
        st.success("Données récupérées avec succès.")
        return data
    else:
        return st.error("Erreur lors de la récupération des données.")
# =======================================================================>

def main():
    
    data = {
        "feature_0": st.text_input("Saisir feature",     key=1),
        "feature_1": st.text_input("Saisir feature",     key=2),
        "feature_2": st.text_input("Saisir feature",     key=3),
        "y_pred"   : st.text_input("Saisir predictions", key=4)
    }
    
    if st.button("envoyer"):
        send_data_to_api(data)
        get_data_from_api()

main()

