import streamlit as st

image_path = "images\pokemon.png"
st.image(image_path)

centered_markdown = """
<div>
    <h1>Pokémon Dataset Exploration</h1>
    <p>
    Pokémon Master, welcome to the analysis of your favorite friends! 🌟
    <br>
    <br>Are you ready to dive into the world of Pokémon and explore the data behind your favorite Pokémon? 
    <br>Whether you're a seasoned trainer or just starting your journey, this is the place to be!
    </p>
</div>
"""

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
# Display centered markdown
st.markdown(centered_markdown, unsafe_allow_html=True)
