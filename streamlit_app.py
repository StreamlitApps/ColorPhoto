import streamlit as st
import requests

image=st.file_uploader(label= "Subir aca las fotos", accept_multiple_files=True)

if st.button("Colorizar"):
    for i in image:
        r = requests.post("https://api.deepai.org/api/colorizer",
                files={'image': i,},
                headers={'api-key': 'd1011249-94e6-4e17-8dbc-090b1da5db17'})
        st.image(r.json()['output_url'])
           
  
        
           