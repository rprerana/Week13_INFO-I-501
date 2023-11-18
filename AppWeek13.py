import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_IMDB_1=pd.read_csv('IMDB_Dataset_50KPolarity_pt1.csv')
df_IMDB_2=pd.read_csv('IMDB_Dataset_50KPolarity_pt2.csv')
df_IMDB_new = pd.concat([df_IMDB_1,df_IMDB_2],ignore_index = True)

df_IMDB_positive=df_IMDB_new[df_IMDB_new['sentiment']==1]
df_IMDB_negative=df_IMDB_new[df_IMDB_new['sentiment']==0]

fig1 = px.histogram(df_IMDB_new, x='subjectivity', color= "sentiment", title="Subjectivity of positive and negative reviews")
fig1.update_layout(template='plotly_white')
fig2 = px.histogram(df_IMDB_new, x='polarity', color= "sentiment", title="Polarity of positive and negative reviews")
fig2.update_layout(template='plotly_white')

st.title('Quantitative Question')
st.caption('red:[This is a string that explains something above.]')

st.plotly_chart(fig1)
st.plotly_chart(fig2)
