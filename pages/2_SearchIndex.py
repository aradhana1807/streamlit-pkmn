import streamlit as st
import pandas as pd

df = pd.read_csv("pokemon.csv")
with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
st.title("Search Pokémon and their stats")

pokemon_name = st.text_input(label="Search here!", placeholder="Enter Pokémon name")

filtered_df = df[df['Name'].str.contains(pokemon_name, case=False)]

st.write(filtered_df)

