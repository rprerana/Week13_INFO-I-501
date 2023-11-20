import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_IMDB_1=pd.read_csv('IMDB_Dataset_50KPolarity_pt1.csv')
df_IMDB_2=pd.read_csv('IMDB_Dataset_50KPolarity_pt2.csv')
df_IMDB_new = pd.concat([df_IMDB_1,df_IMDB_2])

fig1 = px.histogram(df_IMDB_new, x='subjectivity', color= "sentiment", title="Subjectivity of positive and negative reviews")
fig1.update_layout(template='plotly_white')
fig2 = px.histogram(df_IMDB_new, x='polarity', color= "sentiment", title="Polarity of positive and negative reviews")
fig2.update_layout(template='plotly_white')

st.title(':blue[Quantitative Question]')
st.subheader(':red[How does the distribution of sentiment polarity scores vary between positive and negative movie reviews?]')
st.plotly_chart(fig2)

st.subheader(':rainbow[From the above graph we can see that there is a difference in the number of reviews based on the polarity]')


st.title(':blue[Data]')
st.dataframe(df_IMDB_new)  
