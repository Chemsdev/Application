import streamlit as st
from functions import send_data_to_api, traitement_formulaire, background_front, style_text, get_data_from_api,columns_DataFrame
from functions import css_page_front, encadrer_texte_css




def rechercher():
    
    # ======================= FRONT =========================== #
    background_front(url="https://nano.scrolller.com/abstract-wallpaper-9nyw4ngmg1.jpg")
    css_page_front()
        
    # ===================== FORMULAIRE ======================== #
    style_text(title="Trouve l'emploi de tes rêves", size=45)
    st.markdown("")
    submitted, data = traitement_formulaire()
    
    # ===================== PREDICTION ======================== #
    if submitted:
        send_data_to_api(data)
        features, predictions = get_data_from_api()
        style_text(title="Voici une offre qui vous correspond :", size=25)
        prediction = str(columns_DataFrame(data1=features, data2=predictions, pred=True))
        encadrer_texte_css(
            prediction, 
            couleur_bordure='#DAA520', 
            epaisseur_bordure='2px',
            couleur_fond='transparent', 
            padding='20px', 
            texte_css='font-size: 18px; text-align: center;'
        )

rechercher()



