import streamlit as st
import pandas as pd


df = pd.read_csv("candy-data.csv")

st.title("Halloween Candy Recommender")
sugar_level = st.slider("Sugar Level: ", 0, 10)
df["sugar_scale"] = df["sugarpercent"] * 9 + 1

candy_types = ["Chocolate", "Fruity", "Caramel", "Contains Nuts", "Nougat", "Crispy Wafer", "Hard", "Bar", "Pluribus (one of many in a bag/box)"]
selected_types = st.multiselect(
    "What type/s of candy do you prefer?",
    options = candy_types,
    default = ["Chocolate"]
)

btn = st.button("Recommend!")
if btn:
    selected_types_cleaned = clean_types(selected_types)
