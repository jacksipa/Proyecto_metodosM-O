import streamlit as st
import numpy as np
import pandas as pd
import matplotlib
st.title('                Métodos Numéricos y Optimización')
st.header('Proyecto final')
st.subheader('Jacobo Castaño Sipagauta & Santiago Sivera')
st.markdown('En la barra latera escoge el método que quieras implementar.')
st.image('https://mf.b37mrtl.ru/actualidad/public_images/2021.10/thumbnail/6162c13fe9ff714b1b191be8.jpg',width=800,caption='logo lindo')
enlace_markdown = "https://drive.google.com/file/d/1i-Q1q5ZIrgN21hRSlWfRTTEdZSAQCKV_/view?ts=65722f56"

# Mostrar el enlace en Streamlit

boton= st.button('Explicacion de Métodos E uso de la Web')
if boton: 
    st.text('click aqui. ')
    st.markdown(enlace_markdown)
    