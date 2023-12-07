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
    def euler_method(dy, y0, ti, tf, h):
        t = sp.symbols('t')
    # Definimos los vectores donde almacenaremos el resultado.
        x = np.arange(ti, tf + h, h)
        y = np.empty_like(x)
        y[0] = y0

        columnas = ['it', 't', 'yi', 'yi+1']
        tabla = pd.DataFrame(columns=columnas)
    
        for i in range(0, len(y) - 1):
            y[i + 1] = y[i] + h * dy.subs({t: x[i]})
            nueva_fila = pd.DataFrame(data={'it': [i + 1], 't': [round(x[i], 2)], 'yi': [round(y[i], 2)], "yi+1": [round(y[i + 1], 2)]})
            tabla = pd.concat([tabla, nueva_fila], ignore_index=True)

        return x, y, tabla

    # Interfaz de Streamlit
    st.title("Método de Euler para Ecuaciones Diferenciales")
    st.sidebar.markdown("# Parámetros")
    y0 = st.sidebar.number_input("Condición inicial (y0)", value=0.0)
    ti = st.sidebar.number_input("Tiempo inicial", value=0.0)
    tf = st.sidebar.number_input("Tiempo final", value=0.6)
    h = st.sidebar.number_input("Paso de integración (h)", value=0.1)
    st.sidebar.markdown("# Ecuación Diferencial")
    dy_str = st.sidebar.text_input("Ecuación diferencial (dy/dt)", "2*t")
    dy = sp.sympify(dy_str)

# Cálculo del método de Euler
    x, y, tabla = euler_method(dy, y0, ti, tf, h)

# Visualización de resultados   
    st.markdown("## Resultados del Método de Euler")
    st.write(tabla.head())

# Gráfica comparativa
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o', label="Método de Euler")
    t_values = np.linspace(ti, tf, 100)
    dy_lambda = sp.lambdify(sp.symbols('t'), dy, 'numpy')
    plt.plot(t_values, dy_lambda(t_values) + y0, label="Real")  # Asumiendo que y0 es el valor de la constante de integración
    plt.grid()
    plt.legend()
    st.pyplot()


    #codigo aqui

with tabs[1]:
    st.markdown("# Método de Runge Kutta para solución de ecuaciones diferenciales ❄️")
    st.image('https://bioaiteamlearning.github.io/Metodos_2023_03_UAM/_images/eaefdee41b297ebe9fe67a5133ab07001134b5cc8fcdb2b0b048dca3091a2ff9.png',width=500)
    #codigo aqui

# Solicitar al usuario ingresar las condiciones iniciales y el rango de tiempo
    condiciones_iniciales_rk = [st.number_input(f"Ingrese la condición inicial para y{i + 1}(0):") for i in range(2)]
    rango_tiempo_rk = (st.number_input("Ingrese el tiempo inicial:"), st.number_input("Ingrese el tiempo final:"))  
    paso_tiempo_rk = st.number_input("Ingrese el tamaño del paso (dt):")

    tabs= st.tabs(['Runge Kutta orde 2','Runge Kutta orde 3', 'Runge Kutta orde 4'])
    with tabs[0]:

        def runge_kutta_2(funcs, y0, t_range, dt):
            valores_tiempo = np.arange(t_range[0], t_range[1], dt)
            valores_y = [np.array(y0)]

            for t in valores_tiempo[:-1]:
                y_actual = valores_y[-1]

                k1 = np.array([f(t, *y_actual) for f in funcs])
                k2 = np.array([f(t + dt, *(y_actual + dt * k1)) for f in funcs])

                y_siguiente = y_actual + (dt/2) * (k1 + k2)
                valores_y.append(y_siguiente)

            return valores_tiempo, np.array(valores_y).T

    # Funciones para el sistema de ecuaciones diferenciales
        def func1(t, y1, y2):
            return y1 - y2

        def func2(t, y1, y2):
            return y1 + y2

    # Interfaz de usuario con Streamlit
        st.title("Runge-Kutta de Orden 2 para Sistema de Ecuaciones Diferenciales")


    # Solución aproximada para y(t) usando el Método de Runge-Kutta de orden 2
        valores_tiempo_rk, valores_y_rk = runge_kutta_2([func1, func2], condiciones_iniciales_rk, rango_tiempo_rk, paso_tiempo_rk)

    # Graficando la solución aproximada
        st.pyplot(plt.figure(figsize=(8, 6)))
        plt.plot(valores_tiempo_rk, valores_y_rk[0], label='Aproximado y1(t)')
        plt.plot(valores_tiempo_rk, valores_y_rk[1], label='Aproximado y2(t)')
        plt.xlabel('Tiempo')
        plt.ylabel('Variables y(t)')
        plt.title('Solución usando Runge-Kutta de orden 2')
        plt.grid(True)
        plt.legend()
        st.pyplot(plt)

    with tabs[1]:
        def runge_kutta_3(funcs, y0, t_range, dt):
            valores_tiempo = np.arange(t_range[0], t_range[1], dt)
            valores_y = [np.array(y0)]

            for t in valores_tiempo[:-1]:
                y_actual = valores_y[-1]

                k1 = np.array([f(t, *y_actual) for f in funcs])
                k2 = np.array([f(t + dt/2, *(y_actual + (dt/2) * k1)) for f in funcs])
                k3 = np.array([f(t + dt, *(y_actual - dt*k1 + 2*dt*k2)) for f in funcs])

                y_siguiente = y_actual + (dt/6) * (k1 + 4*k2 + k3)
                valores_y.append(y_siguiente)

            return valores_tiempo, np.array(valores_y).T

        # Funciones para el sistema de ecuaciones diferenciales
        def func1(t, y1, y2):
            return y1 - y2

        def func2(t, y1, y2):
            return y1 + y2
        # Interfaz de usuario con Streamlit
        st.title("Runge-Kutta de Orden 3 para Sistema de Ecuaciones Diferenciales")


        # Solución aproximada para y(t) usando el Método de Runge-Kutta de orden 3
        valores_tiempo_rk, valores_y_rk = runge_kutta_3([func1, func2], condiciones_iniciales_rk, rango_tiempo_rk, paso_tiempo_rk)

        # Graficando la solución aproximada
        st.pyplot(plt.figure(figsize=(8, 6)))
        plt.plot(valores_tiempo_rk, valores_y_rk[0], label='Aproximado y1(t)')
        plt.plot(valores_tiempo_rk, valores_y_rk[1], label='Aproximado y2(t)')
        plt.xlabel('Tiempo')
        plt.ylabel('Variables y(t)')
        plt.title('Solución usando Runge-Kutta de orden 3')
        plt.grid(True)
        plt.legend()
        st.pyplot(plt)

with tabs[2]:
    def runge_kutta_4(funcs, y0, t_range, dt):
        valores_tiempo = np.arange(t_range[0], t_range[1], dt)
        valores_y = [np.array(y0)]

        for t in valores_tiempo[:-1]:
            y_actual = valores_y[-1]

            k1 = np.array([f(t, *y_actual) for f in funcs])
            k2 = np.array([f(t + dt/2, *(y_actual + (dt/2) * k1)) for f in funcs])
            k3 = np.array([f(t + dt/2, *(y_actual + (dt/2) * k2)) for f in funcs])
            k4 = np.array([f(t + dt, *(y_actual + dt * k3)) for f in funcs])

            y_siguiente = y_actual + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)
            valores_y.append(y_siguiente)

        return valores_tiempo, np.array(valores_y).T

    # Funciones para el sistema de ecuaciones diferenciales
    def func1(t, y1, y2):
        return y1 - y2

    def func2(t, y1, y2):
        return y1 + y2

    # Interfaz de usuario con Streamlit
    st.title("Runge-Kutta de Orden 4 para Sistema de Ecuaciones Diferenciales")

    # Solución aproximada para y(t) usando el Método de Runge-Kutta de orden 4
    valores_tiempo_rk, valores_y_rk = runge_kutta_4([func1, func2], condiciones_iniciales_rk, rango_tiempo_rk, paso_tiempo_rk)

    # Graficando la solución aproximada
    st.pyplot(plt.figure(figsize=(8, 6)))
    plt.plot(valores_tiempo_rk, valores_y_rk[0], label='Aproximado y1(t)')
    plt.plot(valores_tiempo_rk, valores_y_rk[1], label='Aproximado y2(t)')
    plt.xlabel('Tiempo')
    plt.ylabel('Variables y(t)')
    plt.title('Solución usando Runge-Kutta de orden 4')
    plt.grid(True)
    plt.legend()
    st.pyplot(plt)
    #codigo aqui



