import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import pandas as pd



st.markdown('## Programación Lineal ')
st.sidebar.markdown("# Page 7 ❄️")
tabs= st.tabs(['Método Gráfico: Un Enfoque Visual','Método Simplex: Solución para Casos Complejos','Regla trapezoidal multiple','Regla de Simpson 1/3'])
with tabs[0]:
    st.markdown("# Método Gráfico: Un Enfoque Visual ❄️")
    st.image('data:image/png;base64,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',width=500)
    #codigo aqui

# Definición de restricciones
    x, y = sp.symbols('x y')
    restriccion1 = x + 2*y - 20
    restriccion2 = 3*x + 4*y - 12

# Convertir restricciones a funciones para y
    y_restriccion1 = sp.solve(restriccion1, y)[0]
    y_restriccion2 = sp.solve(restriccion2, y)[0]

# Convertir a funciones numéricas
    func_restriccion1 = sp.lambdify(x, y_restriccion1, modules=['numpy'])
    func_restriccion2 = sp.lambdify(x, y_restriccion2, modules=['numpy'])

# Interfaz de Streamlit
    st.title("Gráfico de Restricciones y Optimización")
    st.markdown("## Restricciones")

# Rango para las variables
    x_vals = np.linspace(0, 30, 100)

# Gráfico de restricciones
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, func_restriccion1(x_vals), label=sp.latex(restriccion1))
    plt.plot(x_vals, func_restriccion2(x_vals), label=sp.latex(restriccion2))
    plt.xlim(0, 30)
    plt.ylim(0, 30)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.axhline(0, color='black', lw=2)
    plt.axvline(0, color='black', lw=2)
    plt.fill_between(x_vals, func_restriccion1(x_vals), func_restriccion2(x_vals), where=(x_vals <= 30), color='gray', alpha=0.3,label="Región Factible")

# Puntos de vértices
    vertices = [
    (0, 3),
    (4, 0),
    (0, 10),
    (20, 0)
    ]

# Encontrar y mostrar la solución óptima
    optimo = max(vertices, key=lambda punto: 3*punto[0] + 2*punto[1])   
    plt.plot(optimo[0], optimo[1], 'ro', label="Solución Óptima")

    plt.legend()
    st.pyplot()

    st.markdown("## Coordenadas del Punto Óptimo")
    st.write(f"Coordenadas del punto óptimo: {optimo}")
    #codigo aqui

with tabs[1]:
    st.markdown("#Método Simplex: Solución para Casos Complejos ❄️")
    st.image('https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrXcP6z77LAuWpyCEFfjd102XshQiVVjM1uTm1Of6rDn5tS9G9bg90yslI_q009LvdKvD6jZPVwB4u2ItIc1GpYaZacKes9pmhJpIEv-hhvymHXOtLhQupPeyYMQRiG2VgjCLMnEAmz60-o4KPeEW5LbA_DDSjsw24jn7twugTRv9VLwCGpCnzfeyR/s953/SIMPLEX.png',width=500)
    #codigo aqui

# Ingreso de datos para el problema de programación lineal
    num_variables = st.sidebar.number_input("Número de Variables", min_value=1, step=1, value=2)
    num_restricciones = st.sidebar.number_input("Número de Restricciones", min_value=1, step=1, value=2)

# Coeficientes de la función objetivo
    st.sidebar.markdown("### Función Objetivo")
    coef_objetivo = []
    for i in range(num_variables):
        coef = st.sidebar.number_input(f"Coeficiente x{i + 1}", value=1.0, step=0.1)
        coef_objetivo.append(coef)

# Coeficientes de las restricciones
    st.sidebar.markdown("### Restricciones")
    coef_restricciones = []
    for i in range(num_restricciones):
        coef_restriccion = []
        st.sidebar.markdown(f"#### Restricción {i + 1}")
        for j in range(num_variables):
            coef = st.sidebar.number_input(f"Coeficiente x{j + 1}", value=1.0, step=0.1)
            coef_restriccion.append(coef)
        coef_restricciones.append(coef_restriccion)

# Lados derechos de las restricciones
    lados_derechos = []
    for i in range(num_restricciones):
        lado = st.sidebar.number_input(f"Lado Derecho Restricción {i + 1}", value=0.0, step=0.1)
        lados_derechos.append(lado)

# Convertir a formato adecuado para la función linprog de SciPy
    c = np.array(coef_objetivo)
    A = np.array(coef_restricciones)
    b = np.array(lados_derechos)

# Calcular el método Simplex
    result = np.linprog(c, A_ub=A, b_ub=b, method='revised simplex')

# Mostrar resultados
    st.markdown("## Resultados del Método Simplex")
    st.write("Solución Óptima:", result.x)
    st.write("Valor Óptimo:", result.fun)

    #codigo aqui

with tabs[2]:
    st.markdown("# Regla trapezoidal multiple ❄️")
    st.image('https://www.neurochispas.com/wp-content/uploads/2022/12/Regla-de-los-trapecios-ejercicio-3-grafica.jpg',width=500)
    #codigo aqui
    #codigo aqui
with tabs[3]:
    st.markdown("# Regla de Simpson 1/3 ❄️")
    st.image('https://www.freecodecamp.org/news/content/images/2020/02/sim01.jpg',width=500)
    #codigo aqui

    #codigo aqui




