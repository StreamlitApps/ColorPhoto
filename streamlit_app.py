import streamlit as st
import requests
st.markdown("<h1 style='text-align: center; color: black;'>PhotoColor - Beta</h1>", unsafe_allow_html=True)
st.write("Una implementación de un front end para el API de DeepAI para colorizar fotos, por Jorge E. Caballero R.")
image=st.file_uploader(label= "Selecciona las fotos", accept_multiple_files=True)
if image:
    if st.button("Colorizar"):
        st.markdown("<h2 style='text-align: center; color: black;'>Resultados:</h2>", unsafe_allow_html=True)

        for n, i in enumerate(image):
            r = requests.post("https://api.deepai.org/api/colorizer",
                    files={'image': i,},
                    headers={'api-key': 'd1011249-94e6-4e17-8dbc-090b1da5db17'})
            st.markdown("<h3 style='text-align: center; color: black;'>Foto "+str(1+n)+"</h3>", unsafe_allow_html=True)
            st.image(r.json()['output_url'])
    
        
           
