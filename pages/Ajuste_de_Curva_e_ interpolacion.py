import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import pandas as pd



st.markdown('## Ajuste de curva e interpolación ')
st.image('https://bioaiteamlearning.github.io/Metodos_2023_03_UAM/_static/images/interpolacion.png',width=300)
   
st.sidebar.markdown("# Page 4 ❄️")

start_range = st.sidebar.slider("Inicio del rango", -10.0, 20.0, 0.1)
end_range = st.sidebar.slider("Fin del rango", -10.0, 20.0, 2.0)
var = st.sidebar.text_input("Variable", "x")
func = st.sidebar.text_input("Función", "x**3 - x")
xl = st.sidebar.number_input("Límite inferior", -10.0, 20.0, 0.2, 0.1)
xu = st.sidebar.number_input("Límite superior", -10.0, 20.0, 1.7, 0.1)
tol = st.sidebar.number_input('Cual es la tolerancia ', 0.0, 1.0, 0.5, 0.1)
tabs= st.tabs(['Metodo de regrecion por Minimos cuadrados','Interpolacion de Lagranje'])
with tabs[0]:
    st.markdown("# Metodo de regrecion por Minimos cuadrados ❄️")
    st.image('https://www.marionomics.com/content/images/image/fetch/w_1200,h_600,c_limit,f_jpg,q_auto:good,fl_progressive:steep/https-3a-2f-2fsubstack-post-media.s3.amazonaws.com-2fpublic-2fimages-2f742471f3-2dc4-498c-9a0d-b45cfb400ebb_1024x768.jpg',width=500)
    x = sp.symbols(var)
    y = sp.sympify(func)

# Generar puntos aleatorios para simular datos
    np.random.seed(42)
    num_points = 50
    x_points = np.linspace(xl, xu, num_points)
    y_points = np.array([y.subs({x: xi}).evalf() for xi in x_points])
    x_points = np.array(x_points, dtype=np.float64)
    y_points = np.array(y_points, dtype=np.float64)
# Calcular el polinomio de regresión por mínimos cuadrados
    coefficients = np.polyfit(x_points, y_points, deg=2)
    poly = np.poly1d(coefficients)
    x_range = np.linspace(start_range, end_range, 100)
    y_range = poly(x_range)

# Gráfico de regresión por mínimos cuadrados
    plt.figure(figsize=(8, 6))
    plt.plot(x_points, y_points, 'bo', label='Datos reales')    
    plt.plot(x_range, y_range, 'r-', label='Regresión por Mínimos Cuadrados')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Regresión por Mínimos Cuadrados')
    plt.legend()
    st.pyplot(plt)

    # Mostrar ecuación del polinomio
    st.write(f"Ecuación de regresión por mínimos cuadrados: {sp.latex(sp.Poly(poly, x).as_expr())}")

with tabs[1]:
    st.markdown("# Interpolacion de Lagranje ❄️")
    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Lagrange_polynomial.svg/500px-Lagrange_polynomial.svg.png',width=500)
   
    #codigo aqui
    x = sp.symbols(var)
    y = sp.sympify(func)

# Generar puntos para la interpolación
    np.random.seed(42)
    num_points = 5
    x_points = np.linspace(xl, xu, num_points)
    y_points = np.array([y.subs({x: xi}).evalf() for xi in x_points])

# Calcular el polinomio de interpolación de Lagrange
    lagrange_poly = 0
    for i in range(num_points):
        term = y_points[i]
        for j in range(num_points):
            if i != j:
               term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        lagrange_poly += term

    # Convertir el polinomio sympy a un polinomio numpy para evaluarlo en un rango
    poly_func = sp.lambdify(x, lagrange_poly, 'numpy')
    x_range = np.linspace(start_range, end_range, 100)
    y_range = poly_func(x_range)

    # Gráfico de interpolación de Lagrange
    plt.figure(figsize=(8, 6))
    plt.plot(x_points, y_points, 'bo', label='Puntos de interpolación')
    plt.plot(x_range, y_range, 'r-', label='Interpolación de Lagrange')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interpolación de Lagrange')
    plt.legend()
    st.pyplot(plt)

# Mostrar el polinomio de interpolación
    st.write(f"Polinomio de interpolación de Lagrange: {sp.latex(lagrange_poly)}")




