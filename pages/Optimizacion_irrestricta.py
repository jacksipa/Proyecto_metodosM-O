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

    st.latex(r"l_0 = l_1 + l_2")
    st.latex(r"\\frac{l_1}{l_0} = \\frac{l_2}{l_1}")
    st.latex(r"\\frac{l_1}{l_1 + l_2} = \\frac{l_2}{l_1}")
    st.latex(r"\\frac{l_1}{l_2} = \\frac{l_1 + l_2}{l_1}")
    st.latex(r"\\frac{l_1}{l_2} = 1+ \\frac{l_2}{l_1}")
    st.markdown(r"Hacemos $R = \\frac{l_2}{l_1}$")

    st.latex(r"\\frac{1}{R} = 1 + R")
    st.latex(r"1 = R (1 + R)")
    st.latex(r"1 = R + R^2")
    st.latex(r"0 = -1 + R + R^2")
    st.markdown("Resolvemos por formula cuadrática y tomamos solo el positivo")
    st.latex(r"R = \\frac{\sqrt{5}-1}{2}")
    st.latex(r"R = 0.61803")
    st.markdown("A) calcular d como:")
    st.latex(r"d = R(x_u - x_l)")
    st.markdown("B) Calculamos $x_1$ y $x_2$ con la formula:")
    st.latex(r"x_1 = x_l + d")  
    st.latex(r"x_2 = x_u - d")
    st.markdown("Siempre $x_1 > x_2$ por la sección dorada.")
    st.markdown("""C)1 . Si $f(x_1) > f(x_2)$, el máximo está entre $x_2$ y $x_u$. Entonces,
             $x_l = x_2$, $x_2 = x_1$, $x_0 = x_1$ y se recalcula $x_1 = x_l + d$""")
    st.markdown("""2. Si $f(x_1) < f(x_2)$, el máximo está entre $x_l$ y $x_1$. Entonces, 
            $x_u = x_1$, $x_1 = x_2$, $x_0 = x_2$ y se recalcula $x_2 = x_u - d$""")
    st.markdown("D) Repetir hasta convergencia")

    st.subheader("Error relativo")
    st.latex(r"e_r = (1-R)*|\frac{x_u - x_l}{x_{0}}| * 100\%")

    st.markdown("""A continuación, se encuentra el metódo de la sección dorada para el hallazgo de puntos maximos""")

    st.subheader(" Método de la sección dorada para maximos")

    fya = st.sidebar.text_input("Ingrese la función","2*sin(x)-((x**2)/10)")
    xla = st.sidebar.slider("Limite inferior Xl", -20.0, 20.0, 0.0)
    xua = st.sidebar.slider("Limite superior Xu", -20.0, 20.0, 4.0)
    tola = st.sidebar.slider("Tolerancia", -5.0, 5.0, 1.0)
    var_inda= st.sidebar.text_input("Variable independiente","x")

    xloa=xla
    xuoa=xua

    x=sp.symbols(var_inda)
    fa=sp.sympify(fya)

    Ra = (np.sqrt(5)-1)/2
    errora = tola + 1
    ita = 1
    x0a = 0.01

    ta = np.linspace(xloa-0.5,xuoa+0.5,100)
    ya = [fa.subs({x:xi}) for xi in ta]

    columnasa = ['xl', 'xu', 'x1', 'x2', 'f(x1)', 'f(x2)', 'x0', 'error(%)']
    tablaa = pd.DataFrame(columns=columnasa)

    fig_placeholder= st.empty()
    tablita= st.empty()

    while errora>tola:
       
        da = Ra*(xua-xla)
        x1a = xla + da
        x2a = xua - da

    fx1a = round(fa.subs({x:x1a}),4)
    fx2a = round(fa.subs({x:x2a}),4)
    fx0a = round(fa.subs({x:x0a}),4)

    plt.figure()
    figa, ax = plt.subplots()

    ax.plot(ta,ya)
    ax.grid()

    ax.vlines(x=0,ymin=min(ya)-0.5,ymax=max(ya)+0.5,color='k')
    ax.hlines(y=0,xmin=min(ta)-0.5,xmax=max(ta)+0.5,color='k')

    ax.vlines(x=xla, ymin=0, ymax=fa.subs({x:xla}), color='g', linestyle='--',label=f"$x_l$ = {round(xla,3)}")
    ax.vlines(x=xua, ymin=0, ymax=fa.subs({x:xua}), color='b', linestyle='--',label=f"$x_u$ = {round(xua,3)}")

    ax.set_title(f"${fya}$")

    ax.vlines(x=x0a, ymin=0, ymax=fx0a, color='orange', linestyle='--')
    ax.vlines(x=x1a, ymin=0, ymax=fx1a, color='r', linestyle='--',label=f"$x_1$ = {round(x1a,3)}")
    ax.vlines(x=x2a, ymin=0, ymax=fx2a, color='purple', linestyle='--',label=f"$x_2$ = {round(x2a,3)}")

    ax.plot([x0a],[fx0a],'*',label=f"$x_0 = ${round(x0a,3)}")

    ax.legend()

    errora = (1-Ra)*np.abs((xua-xla)/x0a)*100

    dataa = {'xl':[xla], 'xu':[xua], 'x1':[x1a], 'x2':[x2a], 'f(x1)':[fx1a], 'f(x2)':[fx2a], 'x0':[x0a], 'error(%)':[round(errora,2)]}
    filaa = pd.DataFrame(data = dataa)
    tablaa = pd.concat([tablaa,filaa],ignore_index=True)

    if fx1a > fx2a:
        xla = x2a
        x2a = x1a
        x0a = x1a
        x1a = xla + da
    elif fx1a < fx2a:
        xua = x1a
        x1a = x2a
        x0a = x2a
        x2a = xua - da

    ita+=1
  
    fig_placeholder.pyplot(figa)
    tablita.dataframe(tablaa)

    plt.close(figa)

    st.success(f"El maximo esta en x= {round(x0a,4)}")

with tabs[1]:
    st.markdown("# Interpolación cuadrática ❄️")
    st.image('https://static.filadd.com/files/f%2317954/html/external_resources/bgf.png',width=500)
    #codigo aqui

with tabs[2]:
    st.markdown("# Algoritmo de newton-Raphson para óptimización ❄️")
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

with tabs[3]:
    st.markdown("# Método del gradiente❄️")
    st.image('https://www.codificandobits.com/img/posts/2018-07-02/concepto-de-gradiente.png',width=500)
    #codigo aqui
   
    def gradient_descent_univariate(f, variable, ci=0, learning_rate=0.01, max_iterations=1000, tolerance=1e-6):
    
    # Calcula la derivada de f
        derivative = sp.diff(f, variable)

    # Punto inicial (por simplicidad, usamos ci)
        points = [ci]

    # Convertir f a una función numérica para graficar
        f_lambda = sp.lambdify(variable, f, "numpy")
        x_vals = np.linspace(float(ci) - 10, float(ci) + 10, 400)
        y_vals = f_lambda(x_vals)

        for iteration in range(max_iterations):
            # Calcula el valor de la derivada en el punto actual
            gradient_value = derivative.subs(variable, ci)

        # Actualiza el punto actual
            ci -= learning_rate * gradient_value

        # Guarda el punto actual en la lista de puntos
            points.append(ci)

        # Grafica la función y la trayectoria del punto
            plt.figure(figsize=(10, 6))
            plt.plot(x_vals, y_vals, label=str(f))
            plt.scatter(points, [f_lambda(p) for p in points], color='red')
            plt.title(f"Iteración {iteration + 1}")
            plt.legend()
            st.pyplot()

        # Pausa para visualizar la gráfica
            time=0
            time.sleep(0.1)
            

        # Condiciones de parada
            if abs(gradient_value) < tolerance:
                break

        return points

# Interfaz de Streamlit
    st.title("Descenso de Gradiente Univariable")
    st.sidebar.markdown("# Parámetros")
    learning_rate = st.sidebar.slider("Tasa de aprendizaje", 0.01, 1.0, 0.1)
    max_iter = st.sidebar.number_input("Máx. iteraciones", 100, 5000, 1000)
    tolerance = st.sidebar.number_input("Tolerancia", 1e-7, 1e-4, 1e-6)

    st.sidebar.markdown("# Función a Minimizar")
    variable_name = st.sidebar.text_input("Variable", "x")
    function_input = st.sidebar.text_input("Función", "x**2 + 4*x + 4")

    x = sp.symbols(variable_name)
    function = sp.sympify(function_input)

    st.markdown("## Proceso de Optimización")
    points = gradient_descent_univariate(function, x, learning_rate=learning_rate, max_iterations=max_iter, tolerance=tolerance)
    st.write("Solución:", points[-1])




