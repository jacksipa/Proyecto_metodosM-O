import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import pandas as pd



st.markdown('## Sistemas de ecuaciones Lineales ')
st.sidebar.markdown("# Page 6.1 ❄️")
# Crear widgets interactivos en Streamlit
eq_text = st.text_input('Ecuación dy/dt:', '2*t')
y0 = st.slider('y0:', -10.0, 10.0, 0.0)
h = st.slider('Paso h:', 0.01, 3.0, 0.1)
tf = st.slider('Tiempo final:', -2.0, 2.0, 0.6)
tabs= st.tabs(['Método de euler para integración numérica','Regla trapezoidal para integración numérica.','Regla trapezoidal multiple','Regla de Simpson 1/3'])
with tabs[0]:
    st.markdown("# Método de euler para integración numérica ❄️")
    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Metodo_de_Euler.png/500px-Metodo_de_Euler.png',width=500)
    #codigo aqui
 


# Función para calcular la integración de Euler
    def calculate_integration(eq, y0, h, tf):
        t = sp.symbols('t')
        dy = sp.sympify(eq)
        x = np.arange(0, tf + h, h)
        y = np.empty_like(x)
        y[0] = y0

        for i in range(0, len(y) - 1):
            y[i + 1] = y[i] + h * dy.subs({t: x[i]})

    # Visualización en Streamlit
        st.pyplot(plt.figure())
        plt.grid()
        plt.plot(x, y, marker='o', label="Método Euler")
        plt.plot(x, x**2, label="Real")
        plt.legend()
        st.pyplot(plt)

# Llamar a la función en Streamlit
    st.title("Visualizador del Método de Euler")
    st.write("Esta aplicación muestra la integración numérica mediante el método de Euler.")
    calculate_integration(eq_text, y0, h, tf)


with tabs[1]:
    st.markdown("# Regla trapezoidal para integración numérica ❄️")
    st.image('https://multimedia.uned.ac.cr/pem/metodos_numericos_ensenanza/modulo4/img/des/trapecio3.jpg',width=500)
    #codigo aqui

# Crear widgets interactivos en Streamlit
    start_range = st.sidebar.slider("Inicio del rango", -10.0, 20.0, 0.1)
    end_range = st.sidebar.slider("Fin del rango", -10.0, 20.0, 2.0)
    var = st.sidebar.text_input("Variable", "x")
    func = st.sidebar.text_input("Función", "x**2")
# Ingresar los límites
    a = st.sidebar.number_input("Límite inferior", -10.0, 20.0, 0.2, 0.1)
    b = st.sidebar.number_input("Límite superior", -10.0, 20.0, 1.7, 0.1)
    tol = st.sidebar.number_input('Cual es la tolerancia ', 0.0, 1.0, 0.5, 0.1)
    x = sp.symbols(var)
    y = sp.sympify(func)
    I = None
    error = tol + 1
    it = 1

    columnas = ['a', 'b', 'I', 'Error']
    tabla = pd.DataFrame(columns=columnas)

# Espacio reservado para la figura
    fig_placeholder = st.empty()
    tablita = st.empty()

    while error > tol:
        fa = y.subs({x: a}).evalf()
        fb = y.subs({x: b}).evalf()

        I = ((b - a) / 2) * (fa + fb)

        error = np.abs((2.333 - I) / 2.333) * 100

        nueva_fila = {'a': a, 'b': b, 'I': I, 'Error': error}
        tabla = pd.concat([tabla, pd.DataFrame([nueva_fila])], ignore_index=True)

        it += 1

# Mostrar la figura en el espacio reservado
    x_vals = np.linspace(start_range, end_range, 100)
    y_vals = [y.subs({x: val}).evalf() for val in x_vals]

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, color='blue', label=f"${sp.latex(y)}$")
    ax.grid()

    ax.vlines(x=a, ymin=0, ymax=fa, color='r', linestyle='--', label=f'$a={a}$')
    ax.vlines(x=b, ymin=0, ymax=fb, color='g', linestyle='--', label=f'$b={b}$')

    ax.fill([a, a, b, b], [0, fa, fb, 0], 'purple', alpha=0.2)

    plt.grid(True)
    plt.legend()
    fig_placeholder.pyplot(fig)
    tablita.dataframe(tabla)
    plt.close(fig)


with tabs[2]:
    st.markdown("# Regla trapezoidal multiple ❄️")
    st.image('https://www.neurochispas.com/wp-content/uploads/2022/12/Regla-de-los-trapecios-ejercicio-3-grafica.jpg',width=500)
    #codigo aqui

# Crear widgets interactivos en Streamlit
    start_range = st.sidebar.slider("Inicio del rango", -10.0, 20.0, 0.1)
    end_range = st.sidebar.slider("Fin del rango", -10.0, 20.0, 2.0)
    var = st.sidebar.text_input("Variable", "x")
    func = st.sidebar.text_input("Función", "x**2")
# Ingresar los límites
    a = st.sidebar.number_input("Límite inferior", -10.0, 20.0, 0.2, 0.1)
    b = st.sidebar.number_input("Límite superior", -10.0, 20.0, 1.7, 0.1)
    n = st.sidebar.number_input('Número de segmentos (n)', 1, 100, 5, 1)
    tol = st.sidebar.number_input('Cual es la tolerancia ', 0.0, 1.0, 0.5, 0.1)

    x = sp.symbols(var)
    y = sp.sympify(func)
    I = None
    error = tol + 1
    it = 1

    columnas = ['a', 'b', 'n', 'I', 'Error']
    tabla = pd.DataFrame(columns=columnas)

# Espacio reservado para la figura
    fig_placeholder = st.empty()
    tablita = st.empty()

    while error > tol:
        h = (b - a) / n
        t = np.arange(a, b + h, h)
        y_vals = [float(y.subs({x: ti})) for ti in t]

        I = h / 2 * (y_vals[0] + 2 * sum(y_vals[1:n]) + y_vals[n])

        error = np.abs((2.333 - I) / 2.333) * 100

        nueva_fila = {'a': a, 'b': b, 'n': n, 'I': I, 'Error': error}
        tabla = pd.concat([tabla, pd.DataFrame([nueva_fila])], ignore_index=True)

        it += 1

# Mostrar la figura en el espacio reservado
    x_vals = np.linspace(start_range, end_range, 100)
    y_vals = [y.subs({x: val}).evalf() for val in x_vals]

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, color='blue', label=f"${sp.latex(y)}$")
    ax.grid()

    ax.vlines(x=a, ymin=0, ymax=float(y.subs({x: a}).evalf()), color='r', linestyle='--', label=f'$a={a}$')
    ax.vlines(x=b, ymin=0, ymax=float(y.subs({x: b}).evalf()), color='g', linestyle='--', label=f'$b={b}$')

    t_vals = np.linspace(a, b, n + 1)
    y_vals = [float(y.subs({x: val}).evalf()) for val in t_vals]

    for i in range(n):
        ax.vlines(x=t_vals[i], ymin=0, ymax=y_vals[i], color='r', linestyle='--')
        ax.plot([t_vals[i], t_vals[i + 1]], [y_vals[i], y_vals[i + 1]], color='r', linestyle='--')
        ax.fill([t_vals[i], t_vals[i], t_vals[i + 1], t_vals[i + 1], t_vals[i]],
                [0, y_vals[i], y_vals[i + 1], 0, 0], 'r', alpha=0.2)

    plt.grid(True)
    plt.legend()
    fig_placeholder.pyplot(fig)
    tablita.dataframe(tabla)
    plt.close(fig)
    #codigo aqui
with tabs[3]:
    st.markdown("# Regla de Simpson 1/3 ❄️")
    st.image('https://www.freecodecamp.org/news/content/images/2020/02/sim01.jpg',width=500)
    #codigo aqui
    
# Widget para ingresar la función
    funcion_input = st.text_input("Ingresa la función f(x):", "x**2")
    try:
        x = sp.symbols('x')
        funcion = sp.sympify(funcion_input)
    except Exception as e:
        st.error(f"Error: {e}")
        st.stop()

# Definir la función en Python
    funcion_python = sp.lambdify(x, funcion, "numpy")

# Widgets para los límites de integración y número de segmentos
    a = st.number_input("Ingresa el límite inferior (a):", value=0.0)
    b = st.number_input("Ingresa el límite superior (b):", value=2.0)
    n = st.number_input("Ingresa el número de segmentos (n):", value=4, step=2)

# Verificar que n sea un número par para la regla de Simpson 1/3
    if n % 2 != 0:
        st.error("El número de segmentos (n) debe ser par para aplicar la regla de Simpson 1/3.")
        st.stop()

# Calcular la integral usando la regla de Simpson 1/3
    h = (b - a) / n
    suma_impares = sum(funcion_python(a + i * h) for i in range(1, n, 2))
    suma_pares = sum(funcion_python(a + i * h) for i in range(2, n-1, 2))
    resultado = (h / 3) * (funcion_python(a) + 4 * suma_impares + 2 * suma_pares + funcion_python(b))

# Calcular el valor real de la integral y el error
    integral_real = sp.integrate(funcion, (x, a, b)).evalf()
    error = abs(integral_real - resultado)

# Crear la gráfica
    x_vals = np.linspace(a, b, 100)
    y_vals = funcion_python(x_vals)
    plt.plot(x_vals, y_vals, 'b', linewidth=2)
    plt.fill_between(x_vals, y_vals, color='blue', alpha=0.2)
    plt.title('Regla de Simpson 1/3')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.text(0.2, 0.8, f'Área aproximada: {resultado:.4f}', fontsize=12, transform=plt.gca().transAxes)
    plt.text(0.2, 0.7, f'Error: {error:.4f}', fontsize=12, transform=plt.gca().transAxes)

# Mostrar la gráfica en Streamlit
    st.pyplot(plt)

# Mostrar resultados en Streamlit
    st.write(f"Área aproximada: {resultado:.4f}")
    st.write(f"Valor real de la integral: {integral_real:.4f}")
    st.write(f"Error: {error:.4f}")
   




