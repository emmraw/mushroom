import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Mushroom')

df = pd.read_csv('df_mush.csv')

check = st.checkbox("Tick to see data")

if check:
  df
  
st.write("Here's our first attempt at importing a data table:")

click = st.button("You can click this button to see the ratio of poisonous mushrooms to edible")

if click:
  fig = px.pie(values = df['class'].value_counts(), names = ['poisonous','edible'])
  st.plotly_chart(fig)
  
