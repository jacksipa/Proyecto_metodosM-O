import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import pandas as pd

st.markdown('## Metodos Cerrados')
st.image('https://bioaiteamlearning.github.io/Metodos_2023_03_UAM/_images/014ec9c5da7850b12b002cf32807b8aac8c1e14713a78331b81a90d7ebdcec3a.png',width=800)
tabs= st.tabs(['Bisección','Falsa Posición'])
st.sidebar.markdown("# Page 2 ❄️")
# Definir el rango de entrada
start_range = st.sidebar.slider("Inicio del rango", -10.0, 20.0, 0.1)
end_range = st.sidebar.slider("Fin del rango", -10.0, 20.0, 2.0)
var = st.sidebar.text_input("Variable", "x")
func = st.sidebar.text_input("Función", "x**3 - x")
# Ingresar los límites
xl = st.sidebar.number_input("Límite inferior", -10.0, 20.0, 0.2, 0.1)
xu = st.sidebar.number_input("Límite superior", -10.0, 20.0, 1.7, 0.1)
tol = st.sidebar.number_input('Cual es la tolerancia ',0.0, 1.0, 0.5 , 0.1)

with tabs[0]:
    st.markdown("# Biseccion ❄️")   
    st.image('https://bioaiteamlearning.github.io/Metodos_2023_03_UAM/_images/89af5755c2f4b18c08633856f93063c8da44170b4a35d5f286647cdb6a6f2df1.png',width=500)
    #codigo aqui

# Función para calcular y
    def calculate_y(x_values, expression):
       return [expression.subs({x: xi}) for xi in x_values]
# Configuración de la página
    st.title("Visualizador de Métodos cerrados")
    st.write("Esta aplicación muestra la gráfica de Biseccion.")
# Ingresar la función 
    x = sp.symbols(var) 
    y = sp.sympify(func)
# Tolerancia y valores iniciales
    #tol = 1
    xr = None
    xr_ant = xu
    error = tol + 1
    it = 1
    # Dataframe para almacenar los resultados
    columnas = ['Xl', 'Xu', 'Xr', 'er(%)', 'f(Xl)', 'f(Xu)', 'f(Xr)']
    tabla = pd.DataFrame(columns=columnas)

# Espacio reservado para la figura
    fig_placeholder = st.empty()
    tablita = st.empty()
    while error > tol:
        # Evaluamos la función en los puntos del intervalo
        fxl = y.subs({x: xl}).evalf()
        fxu = y.subs({x: xu}).evalf()

        # Crear la figura
        fig, ax = plt.subplots()
        r = np.linspace(start_range, end_range, 100)
        fx = calculate_y(r, y)

        ax.plot(r, fx, color='blue', label=f"${sp.latex(y)}$")
        ax.vlines(x=0, ymin=min(fx)-0.5, ymax=max(fx)+0.5, color='k')
        ax.hlines(y=0, xmin=min(r)-0.5, xmax=max(r)+0.5, color='k')
        ax.set_title(f"${sp.latex(y)}$")
        ax.grid()

        # Límites xl y xu
        ax.vlines(x=xl, ymin=0, ymax=fxl, color='k', linestyle='--', label=f'$x_l=${xl}')
        ax.vlines(x=xu, ymin=0, ymax=fxu, color='k', linestyle='--', label=f'$x_u=${xu}')

    # Calculamos la raíz
        xr = round((xl + xu) / 2, 4)
        fxr = y.subs({x: xr}).evalf()

    # Pintamos el punto intermedio
        ax.plot(xr, fxr, 'ro', label=f'Raíz={xr}')
        ax.legend()

    # Actualizamos el error y la tabla
        error = np.abs((xr - xr_ant) / xr) * 100 if xr != 0 else 0
        nueva_fila = {'Xl': xl, 'Xu': xu, 'Xr': xr, 'er(%)': error, 'f(Xl)': fxl, 'f(Xu)': fxu, 'f(Xr)': fxr}
        tabla = pd.concat([tabla, pd.DataFrame([nueva_fila])], ignore_index=True)
    # Actualizamos los límites
        if fxl * fxr < 0:
            xu = xr
        elif fxl * fxr > 0:
            xl = xr
        elif fxl * fxr == 0:
            st.success(f"La raíz está en: ({round(xr,4)}, {round(fxr,4)})")
            break

        xr_ant = xr
        it += 1

        # Mostrar la figura en el espacio reservado
        fig_placeholder.pyplot(fig)
        tablita.dataframe(tabla)
        # Borra la figura para la siguiente iteración
        plt.close(fig)

    st.success(f"La raíz está en: ({round(xr,4)}, {round(fxr,4)})")
    xl, xu = st.sidebar.slider(
        'Selecciona el rango de valores.',
        0.0, 10.0, (0.0, 1.7)
)

    print(xl, xu)

    
with tabs[1]:
    st.markdown("# Falsa posicion ❄️")
    st.image('https://docplayer.es/docs-images/87/95843293/images/35-0.jpg',width=500)
    st.title("Visualizador de Métodos cerrados")
    st.write("Esta aplicación muestra la gráfica de Biseccion.")
    def calculate_y(x_values, expression):

        return [expression.subs({x: xi}) for xi in x_values]
    # Ingresar la función 
    x = sp.symbols(var) 
    y = sp.sympify(func)
    xr = None
    error = tol + 1
    it = 1

    columnas = ['Xl', 'Xu', 'Xr', 'er(%)', 'f(Xl)', 'f(Xu)', 'f(Xr)']
    tabla = pd.DataFrame(columns=columnas)

    # Espacio reservado para la figura
    fig_placeholder = st.empty()
    tablita = st.empty()

    while error > tol:
        # Evaluamos la función en los puntos del intervalo
        fxl = y.subs({x: xl}).evalf()
        fxu = y.subs({x: xu}).evalf()

    # Crear la figura
        fig, ax = plt.subplots()
        r = np.linspace(start_range, end_range, 100)
        fx = calculate_y(r, y)

        ax.plot(r, fx, color='blue', label=f"${sp.latex(y)}$")
        ax.vlines(x=0, ymin=min(fx)-0.5, ymax=max(fx)+0.5, color='k')
        ax.hlines(y=0, xmin=min(r)-0.5, xmax=max(r)+0.5, color='k')
        ax.set_title(f"${sp.latex(y)}$")
        ax.grid()

    # Límites xl y xu
        ax.vlines(x=xl, ymin=0, ymax=fxl, color='k', linestyle='--', label=f'$x_l=${xl}')
        ax.vlines(x=xu, ymin=0, ymax=fxu, color='k', linestyle='--', label=f'$x_u=${xu}')

    # Calculamos la raíz
        xr = round(xu - (fxu * (xl - xu)) / (fxl - fxu), 4)
        fxr = y.subs({x: xr}).evalf()

    # Pintamos el punto intermedio
        ax.plot(xr, fxr, 'ro', label=f'Raíz={xr}')
        ax.legend()

    # Actualizamos el error y la tabla
        error = np.abs((xr - xl) / xr) * 100 if xr != 0 else 0
        nueva_fila = {'Xl': xl, 'Xu': xu, 'Xr': xr, 'er(%)': error, 'f(Xl)': fxl, 'f(Xu)': fxu, 'f(Xr)': fxr}
        tabla = pd.concat([tabla, pd.DataFrame([nueva_fila])], ignore_index=True)

    # Actualizamos los límites
        if fxl * fxr < 0:
            xu = xr
        elif fxl * fxr > 0:
            xl = xr
        elif fxl * fxr == 0:
            st.success(f"La raíz está en: ({round(xr, 4)}, {round(fxr, 4)})")
            break

        it += 1

    # Mostrar la figura en el espacio reservado
    fig_placeholder.pyplot(fig)
    tablita.dataframe(tabla)
    # Borra la figura para la siguiente iteración
    plt.close(fig)

    


