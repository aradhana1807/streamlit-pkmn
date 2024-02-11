# imports
import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv("pokemon.csv")

st.write("# Pokemon Dataset")
st.dataframe(df, use_container_width=True)

# Define colors for each type
type_colors = {'Type I': '#ee1515', 'Type I/II': '#f0f0f0'}

for generation in range(1, 7):
    # Filter Pokémon for the current generation
    gen_df = df[df['Generation'] == generation]

    # Count the number of Pokémon with one type and two types
    one_type_count = gen_df['Type 2'].isna().sum()
    two_types_count = (~gen_df['Type 2'].isna()).sum()

    # Create a pie chart with Plotly
    labels = ['Type I', 'Type I/II']
    values = [one_type_count, two_types_count]
    
    # Custom colors
    colors = [type_colors[label] for label in labels] 
    fig = px.pie(names=labels, 
                 height=400, width=500, hole=0.2, 
                color_discrete_sequence=colors, values=values, 
                title=f'Generation {generation} Pokémon: Type I vs Type I/II')
    
    # Display the chart in Streamlit
    st.write(f"## Generation {generation} Pokémon:")
    st.plotly_chart(fig,use_container_width=True)