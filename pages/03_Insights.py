import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from functions import background_front, style_text



# DATASET ==============================================================
background_front(url="https://nano.scrolller.com/abstract-wallpaper-9nyw4ngmg1.jpg")
df = pd.read_csv("data/gsearch_jobs.csv")

graph = st.sidebar.radio(label='Pages graphs', options=('1', '2', '3'))

if graph == '1':
    style_text(title='Top 10 Titres de poste', size=30)

    top10_job_title = df['title'].value_counts()[:10]
    fig = px.bar(y=top10_job_title.values,
                 x=top10_job_title.index,
                 color=top10_job_title.index,
                 color_discrete_sequence=px.colors.sequential.PuBuGn,
                 text=top10_job_title.values,
                 title='Top 10 Job Titles')

    fig.update_layout(
        xaxis_title="Job Titles",
        yaxis_title="Count",
        font=dict(size=12, family="Franklin Gothic")
    )

    st.plotly_chart(fig)
    
elif graph == '2':
    style_text(title='Top 10 des compagnies', size=30)
    top10_comp_location = df['company_name'].value_counts()[:10]
    fig = px.bar(y=top10_comp_location.values, 
                 x=top10_comp_location.index, 
                 color = top10_comp_location.index,
                 color_discrete_sequence=px.colors.sequential.PuBuGn,
                 text=top10_comp_location.values,
                 title= 'Top 10 Compagnies')
    fig.update_layout(
        xaxis_title="Locations",
        yaxis_title="count",
        font = dict(size=12,family="Franklin Gothic"))
    st.plotly_chart(fig)

    
elif graph == '3':
    style_text(title='Distribution horaires', size=30)
    work_h = df['schedule_type'].value_counts()
    fig = px.pie(values=work_h.values, 
                 names=work_h.index, 
                 color_discrete_sequence=px.colors.sequential.PuBu,
                 title= 'Work schedule distribution for Data Analysts')
    fig.update_traces(textinfo='label+percent', textfont_size=18,
                      marker=dict(line=dict(color='#100000', width=0.2)))

    fig.data[0].marker.line.width = 2
    fig.data[0].marker.line.color='gray'
    fig.update_layout(
        font=dict(size=20,family="Franklin Gothic"))
    st.plotly_chart(fig)
    
    