# imports
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Pokémon Dataset",
    page_icon="🔴",
)

df = pd.read_csv("pokemon.csv")

st.title("Pokémon Data Analysis")

multi_type = '''### Type I and Type I/II

A small inference about the pie chart depicting Pokémon with one type versus those 
with two types based on generations could reveal an interesting trend. 
For instance, it might show that in earlier generations, 
there was a higher prevalence of Pokémon with only one type, 
indicating simpler designs or gameplay mechanics. 


Conversely, in later generations, there could be a more balanced 
distribution or even a slight increase in Pokémon with two types, 
reflecting a desire for more complexity and diversity in Pokémon 
designs and battles as the franchise evolved.
'''
st.markdown(multi_type)
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
                color_discrete_sequence=colors, values=values
                ,title=f'Generation {generation} Pokémon: Type I vs Type I/II')
    
    # Display the chart in Streamlit
    st.plotly_chart(fig,use_container_width=True)



multi_gen = '''### Type I and Type I/II

A small inference about the pie chart depicting Pokémon with one type versus those 
with two types based on generations could reveal an interesting trend. 
For instance, it might show that in earlier generations, 
there was a higher prevalence of Pokémon with only one type, 
indicating simpler designs or gameplay mechanics.
'''
st.markdown(multi_gen)
# Group data by Generation and count the number of Pokémon in each generation
generation_counts = df['Generation'].value_counts().reset_index()
generation_counts.columns = ['Generation', 'Total Number of Pokémon']

# Sort the data by Generation
generation_counts = generation_counts.sort_values(by='Generation')

# Create bar plot using Plotly Express
fig = px.bar(generation_counts, x='Generation', y='Total Number of Pokémon', title='Total Number of Pokémon in Each Generation')

# Display the plot using Streamlit
st.plotly_chart(fig)