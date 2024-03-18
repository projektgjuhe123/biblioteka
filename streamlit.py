import streamlit as st
import pandas as pd
from PIL import Image

# Assuming 'your_image.png' is the image file you want to display at the top of the page.
# Make sure to provide the correct path to your image file.

image = Image.open('/home/mac/projekt/images/image2.jpg')
image = image.resize((200, 200))
st.image(image)
# Display the image using st.image

st.title('Biblioteka e shkolles Sevasti Qiriazi')

# Path to the Excel file
file_path = '/home/mac/books.xlsx'

# Read the Excel file
df = pd.read_excel(file_path)

# Placeholder for the search functionality
search_term = st.text_input("Kerko per nje liber ose nje autor", key="search")

# Filter the DataFrame based on the search term
if search_term:
    df_display = df[df.apply(lambda row: search_term.lower() in str(row['Titulli I Librit']).lower() 
                             or search_term.lower() in str(row['Autori']).lower(), axis=1)]
else:
    df_display = df

# Display the filtered DataFrame
st.dataframe(df_display)
