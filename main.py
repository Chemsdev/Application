import streamlit as st
import pandas as pd
from functions import send_data_to_api, get_data_from_api, background, css_page

def main():
    
    # ======================= FRONT =========================== #
    background(url="https://img.freepik.com/premium-photo/male-hands-typing-laptop-using-smartphone-abstract-dark-black-office-desk_232693-407.jpg?w=1060")
    css_page()
    
    # ===================== FORMULAIRE ======================== #
    st.title("Formulaire Prédiction")
    data = {
        "feature_0": st.text_input("**Feature 1**",  key=1),
        "feature_1": st.text_input("**Feature 2**",  key=2),
        "feature_2": st.text_input("**Feature 3**",  key=3),
        "y_pred"   : st.text_input("**Prediction**", key=4)
    }
    if st.button("Envoyer"):
        send_data_to_api(data)
        get_data_from_api()
    
main()