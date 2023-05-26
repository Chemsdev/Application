import streamlit as st
from functions import background_front, get_data_from_api, columns_DataFrame, delete_data_via_api, style_text


def data():
         
    # ========================= API SQL ==============================>
    features, predictions = get_data_from_api()
    
    # ========================== PAGE ================================>
    background_front(url="https://nano.scrolller.com/abstract-wallpaper-9nyw4ngmg1.jpg")
    data = columns_DataFrame(data1=features, data2=predictions)
    style_text(title="Consultation de la Data", size=45)
    st.write(data)  
    if st.button("Supprimer toutes les données"):
        delete_data_via_api()        
    
data()





