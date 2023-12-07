import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import pandas as pd



st.markdown('## Ecuaciones diferenciales ordinarias ')
st.image('https://lambdai.files.wordpress.com/2011/12/lorenz1.jpg',width=500)
st.sidebar.markdown("# Page 5 ❄️")
tabs= st.tabs(['Método de euler para ecuaciones diferenciales','Método de Runge Kutta para solución de ecuaciones diferenciales'])
with tabs[0]:
    st.markdown("#Método de euler para ecuaciones diferenciales ❄️")
    st.image('https://github.com/BioAITeamLearning/Metodos_2023_03_UAM/blob/main/_static/images/Euler.png?raw=true',width=500)
    
    st.image('https://github.com/BioAITeamLearning/Metodos_2023_03_UAM/blob/main/_static/images/Euler2.png?raw=true',width=500)
    #codigo aqui

    #codigo aqui

with tabs[1]:
    st.markdown("# Método de Runge Kutta para solución de ecuaciones diferenciales ❄️")
    st.image('https://bioaiteamlearning.github.io/Metodos_2023_03_UAM/_images/eaefdee41b297ebe9fe67a5133ab07001134b5cc8fcdb2b0b048dca3091a2ff9.png',width=500)
    #codigo aqui

    #codigo aqui



