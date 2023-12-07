import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import pandas as pd



st.markdown('## Optiizacion Irrestricta ')
st.image('https://www.disfrutalasmatematicas.com/algebra/images/function-max-min.svg',width=500)
st.sidebar.markdown("# Page 6 ❄️")
tabs= st.tabs(['Sección Dorada','Interpolación cuadrática','Algoritmo de newton-Raphson para óptimización','Método del gradiente'])
with tabs[0]:
    st.markdown("# Sección Dorada ❄️")
    st.image('https://static.filadd.com/files/f%2317954/html/external_resources/bg8.png',width=500)
    #codigo aqui

with tabs[1]:
    st.markdown("# Interpolación cuadrática ❄️")
    st.image('https://static.filadd.com/files/f%2317954/html/external_resources/bgf.png',width=500)
    #codigo aqui

with tabs[2]:
    st.markdown("# Algoritmo de newton-Raphson para óptimización ❄️")
    #codigo aqui
with tabs[3]:
    st.markdown("# Método del gradiente❄️")
    st.image('https://www.codificandobits.com/img/posts/2018-07-02/concepto-de-gradiente.png',width=500)
    #codigo aqui




