import streamlit as st
from functions import background_front, get_data_from_api, columns_DataFrame, delete_data_via_api




def data():
         
    # ========================== API SQL ===============================>
    features, predictions = get_data_from_api()
    data = columns_DataFrame(data1=features, data2=predictions)
    
    
    # ========================== PAGE ================================>
    background_front(url="https://images.hdqwalls.com/download/fox-logo-minimalism-ph-2048x1152.jpg")
    st.title("Consultation des données")
    st.markdown("Les données")
    st.write(data)  
    
    if st.button("Supprimer toutes les données"):
        delete_data_via_api()        
    
data()





