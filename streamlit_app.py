import streamlit as st
import pandas as pd


df = pd.read_csv("candy-data.csv")

st.title("Halloween Candy Recommender")
sugar_level = st.slider("Sugar Level: ", 0, 10)
