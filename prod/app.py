from turtle import width
import streamlit as st
from extraction_texte import creation_images, decomposition_img

sidebar = st.sidebar.image('assets/logos/9_1_1.png')

col1, col2 = st.columns([2, 4])

col1.image('assets/logos/cap_logo.png', width = 200)
col1.image('assets/logos/logo_ia_pau.png', width = 200)
col2.title("IA Pau 4")

with open("texte/description_asso_ia_pau.txt", 'r') as f:
    description_asso = f.readlines()

col2.text("".join(description_asso))

st.markdown('## Equipe')

st.markdown('## Sujet')

with open("texte/description_challenge.txt", 'r') as f:
    description_sujet = f.readlines()

st.text("".join(description_sujet))

uploaded_file = st.file_uploader("Page PDF à classifier")
if uploaded_file:

    bytes_data = uploaded_file.read()
    with open("pdf/mon_pdf.pdf", 'wb') as f:
        description_asso = f.write(bytes_data)

    creation_images("pdf","pdf/mon_pdf.pdf")
    liste_img = decomposition_img('pdf/mon_pdf.jpeg')
    

st.markdown('## OCR')

st.write("Nous avons preprocessé les images")

col1, col2, col3, col4 = st.columns([2, 2, 2, 2])

col1.image('pdf/mon_pdf.jpeg')
col2.image('pdf/blur_1.jpeg')
col3.image('pdf/canny.jpeg')
col4.image('pdf/contour.jpeg')

st.markdown('## Classification')

st.markdown('## Conclusion')