import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_IMDB_1=pd.read_csv('IMDB_Dataset_50KPolarity_pt1.csv')
df_IMDB_2=pd.read_csv('IMDB_Dataset_50KPolaritpt2y.csv')

df_IMDB_positive=df_IMDB_new[df_IMDB_new['sentiment']==1]
df_IMDB_negative=df_IMDB_new[df_IMDB_new['sentiment']==0]

fig1 = px.histogram(df_IMDB_positive, x='subjectivity', title="Subjectivity of positive reviews",nbins=10)
fig1.update_layout(template='plotly_white')
fig2 = px.histogram(df_IMDB_negative, x='subjectivity', title="Subjectivity of negative reviews",nbins=10)
fig2.update_layout(template='plotly_white')
fig3 = px.scatter(df_IMDB_new, y='subjectivity', x='polarity', title="Subjectivity vs Polarity")
fig3.update_layout(template='plotly_white')
st.plotly_chart(fig3)
st.plotly_chart(fig1)
st.plotly_chart(fig2)
