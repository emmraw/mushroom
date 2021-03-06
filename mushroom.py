import streamlit as st
import pandas as pd
import plotly.express as px
import datetime

st.title('Mushroom :mushroom:')

df = pd.read_csv('df_mush.csv')

check = st.checkbox("Tick to see data")

if check:
  df
  
st.write("Here's our first attempt at importing a data table:")

click = st.button("You can click this button to see the ratio of poisonous mushrooms to edible")

if click:
  fig = px.pie(values = df['class'].value_counts(), names = ['edible','poisonous'])  # make sure the labels are the right way round
  st.plotly_chart(fig)
  
option = st.selectbox(
     'which feature would you like to look at?',
     ('odor', 'population', 'habitat'))

st.write('You selected:', option)  

fig = px.bar(df, x = option)
st.plotly_chart(fig)

d = st.date_input(
     "When's your birthday",
     datetime.date(2000, 3, 1))
st.write('Your birthday is:', d)
