import streamlit as st

image_path = "images/pokemon.png"
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


nav_markdown = """
<h3>
You can explore using below links!
</h3>

"""

st.markdown(nav_markdown, unsafe_allow_html=True)
# Function to generate buttons
def page_link_button(page_name, button_label):
    return f'<a href="/{page_name}" style="text-decoration: none;"><button class="transparent-button">{button_label}</button></a>'

# Define your pages
pages = {
    '2_SearchIndex': 'Search Index',
    '3_PokemonAnalysis': 'Pokemon Analysis',
    # Add more pages as needed
}

# Display buttons for each page
for page_name, button_label in pages.items():
    st.markdown(page_link_button(page_name, button_label), unsafe_allow_html=True)
