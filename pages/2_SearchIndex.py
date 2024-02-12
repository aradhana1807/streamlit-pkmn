import streamlit as st
import pandas as pd

df = pd.read_csv("pokemon.csv")
st.title("Search Pokémon and their stats")

pokemon_name = st.text_input(label="Search here!", placeholder="Enter Pokémon name")

filtered_df = df[df['Name'].str.contains(pokemon_name, case=False)]

st.write(filtered_df)

