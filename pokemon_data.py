# imports
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd


df = pd.read_csv("pokemon.csv")

st.write("# Pokemon Dataset")
st.dataframe(df, use_container_width=True)

for generation in range(1, 7):
    # Filter Pokémon for the current generation
    gen_df = df[df['Generation'] == generation]

    # Count the number of Pokémon with one type and two types
    one_type_count = gen_df['Type 2'].isna().sum()
    two_types_count = (~gen_df['Type 2'].isna()).sum()

    # Create a pie chart
    labels = ['One Type', 'Two Types']
    explode = (0.1, 0)
    colors = ['#D04848', '#6895D2']
    sizes = [one_type_count, two_types_count]
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.pie(sizes, explode=explode, labels=labels, colors=colors, shadow=True, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  
    ax.set_title(f'Generation {generation} Pokémon: One Type vs Two Types')

    # Reduce padding around the pie chart
    plt.tight_layout(pad=1.0)

    # Display the chart in Streamlit
    st.write(f"## Generation {generation} Pokémon:")
    st.pyplot(fig)