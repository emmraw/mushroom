import streamlit as st
import pandas as pd
st.title('Mushroom')

df = pd.read_csv('df_mush.csv')
if df:
  df
