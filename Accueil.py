import streamlit as st
from functions import background_front, style_text, css_page_front, read_picture


def accueil():
    
    # ===================== FRONT ======================== #
    background_front(url="https://nano.scrolller.com/abstract-wallpaper-9nyw4ngmg1.jpg")
    style_text(text="Trouver un job dans la data ?")
    css_page_front()
    
    # ===================== PAGE ========================= #
    st.markdown("""
        Notre entreprise se concentre sur l'accompagnement des personnes à la recherche d'un emploi en leur offrant une solution personnalisée. 
        Nous comprenons que trouver un emploi correspondant à ses compétences et à ses préférences peut être un défi, 
        c'est pourquoi nous avons mis en place un formulaire spécialement conçu pour nos clients. 
    """)
    
    st.markdown("""
        Ce formulaire permet aux individus de renseigner les outils et les logiciels qu'ils maîtrisent, 
        Le type de contrat qu'ils recherchent, la localisation souhaitée et le poste visé, entre autres informations pertinentes. 
        En remplissant ce formulaire, nos clients peuvent obtenir une fiche de poste appropriée à leurs besoins spécifiques.      
    """)
    
    st.markdown("""
        Nous nous engageons à simplifier le processus de recherche d'emploi en offrant une solution sur mesure pour aider nos clients à trouver 
        Le poste idéal correspondant à leurs compétences et à leurs aspirations professionnelles.           
    """)
    
    # =================== LES IMAGES =================== #
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("")
        read_picture(width=220, image="test3", format="png")
    with col2:
        st.header("")
        read_picture(width=200, image="test2", format="png")
    with col3:
        st.header("")
        read_picture(width=220, image="test", format="png")
    if st.button("Visualiser les WorkClouds"):
        style_text(text="Mots clés d'une offre d'emploi")
        read_picture(width=700, image="workcloud_1", format="png")
        style_text(text="Outils du Data Analyst")
        read_picture(width=700, image="workcloud_2", format="png")
        
accueil()
