import streamlit as st
import pandas as pd
from PIL import Image

favicon = Image.open('/app/image2.jpg')
st.set_page_config(
        page_title="Biblioteka",
        page_icon=favicon,
        layout="wide",
    )

spacer, right_column = st.columns([0.9, 0.1])  # Adjust the ratio as needed to push the button to the right

with right_column:
    # Check if the key 'toggle' exists in session state, if not, initialize it to 0
    if 'toggle' not in st.session_state:
        st.session_state['toggle'] = 0

    # When the button is clicked, increment the 'toggle' count
    if st.button("Dhuro nje liber"):
        st.session_state['toggle'] += 1

    # If the 'toggle' count is odd, display the message
    if st.session_state['toggle'] % 2 == 1:
        st.write("Per te dhuruar nje liber na kontakto ne sqiriazi23@gmail.com")
    else:
        # If the 'toggle' count is even, do not display anything (or you can clear the previous message)
        st.write("")

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
# Display the image using st.image
st.image(image)

# Title of the site
st.title('Biblioteka e shkollës "Sevasti Qiriazi"')

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
    search_term = st.text_input("Kerko për një libër ose një autor", key="search", on_change=None)

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
        'border-color': 'grey',
    }).set_table_styles([{
        'selector': 'th',
        'props': [('background-color', '#414141'), ('color', 'white')]
    }])

st.dataframe(style_dataframe(df_display), use_container_width=True)
