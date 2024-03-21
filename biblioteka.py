import streamlit as st
import pandas as pd
from PIL import Image

# Assuming 'your_image.png' is the image file you want to display at the top of the page.
# Make sure to provide the correct path to your image file.

st.set_page_config(
        page_title="Biblioteka",
        page_icon="books",
        layout="wide",
    )

st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)


image = Image.open('/app/image2.jpg')
image = image.resize((200, 200))
st.image(image)
# Display the image using st.image

st.title('Biblioteka e shkollës Sevasti Qiriazi')

# Path to the Excel file
file_path = '/app/books.xlsx'
# Read the Excel file
df = pd.read_excel(file_path)

# Placeholder for the search functionality
search_container = st.container()
with search_container:
    st.markdown("""
        <style>
            input[data-baseweb="input"] {
                font-size: 25px !important;  # Set the size as needed
            }
        </style>
    """, unsafe_allow_html=True)
    search_term = st.text_input("Kerko per një libër ose një autor", key="search", on_change=None)

def normalize_text(text):
    replacements = {'ç': 'c', 'ë': 'e'}
    return ''.join(replacements.get(ch, ch) for ch in text)

# Apply the normalize function to the search term
normalized_search_term = normalize_text(search_term.lower())

# Filter the DataFrame based on the normalized search term
if normalized_search_term:
    df_display = df[df.apply(lambda row: normalized_search_term in normalize_text(str(row['Titulli i Librit']).lower()) or 
                             normalized_search_term in normalize_text(str(row['Autori']).lower()), axis=1)]
else:
    df_display = df


def style_dataframe(dataframe):
    return dataframe.style.set_properties(**{
        'background-color': '#0e1117',  # Dark background for cells.
        'color': 'white',  # Bright text color for readability.
        'border-color': 'grey',
    }).set_table_styles([{
        'selector': 'th',
        'props': [('background-color', '#414141'), ('color', 'white')]
    }])

st.dataframe(style_dataframe(df_display), use_container_width=True)
