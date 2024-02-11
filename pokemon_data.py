# imports
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv("pokemon.csv")

st.write("# Pokemon Dataset")
st.dataframe(df, use_container_width=True)

for generation in range(1, 7):
    # Filter Pokémon for the current generation
    gen_df = df[df['Generation'] == generation]

    # Count the number of Pokémon with one type and two types
    one_type_count = gen_df['Type 2'].isna().sum()
    two_types_count = (~gen_df['Type 2'].isna()).sum()

    # Create a pie chart with Plotly
    labels = ['One Type', 'Two Types']
    values = [one_type_count, two_types_count]
    fig = px.pie(names=labels, values=values, title=f'Generation {generation} Pokémon: One Type vs Two Types')

    # Display the chart in Streamlit
    st.write(f"## Generation {generation} Pokémon:")
    st.plotly_chart(fig)