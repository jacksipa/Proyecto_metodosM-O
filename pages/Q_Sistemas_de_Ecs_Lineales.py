import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import pandas as pd



st.markdown('## Sistemas de ecuaciones Lineales ')
st.sidebar.markdown("# Page 6 ❄️")

n = st.sidebar.slider("Tamaño del sistema", 2, 5, 3)
st.sidebar.write("Ingrese la matriz triangular inferior L y el vector constante b:")
tabs= st.tabs(['Sistemas lineales triangulares','Metodo de eliminacion gaussiana.','Eliminacion gaussiana con piboteo'])
with tabs[0]:
    st.markdown("# Sistemas lineales triangulares❄️")
    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Metodo_de_Euler.png/500px-Metodo_de_Euler.png',width=500)
    #codigo aqui

# Ingresar la matriz triangular inferior y el vector constante
    L = sp.zeros(n)
    b = sp.zeros(n)

# Ingresar la matriz triangular inferior L y el vector constante b
    st.sidebar.write("Ingrese la matriz triangular inferior L y el vector constante b:")
    for i in range(n):
        for j in range(i + 1):
            L[i, j] = st.sidebar.number_input(f"L[{i+1}, {j+1}]", value=0.0, step=0.1)

        b[i] = st.sidebar.number_input(f"b[{i+1}]", value=0.0, step=0.1)

# Resolver el sistema lineal triangular inferior
    x = sp.symbols('x:{}'.format(n + 1))
    solucion = sp.solve(L * sp.Matrix(x) - b, x)

# Mostrar la solución
    st.sidebar.write("Solución:")
    for i, sol in enumerate(solucion):
        st.sidebar.write(f"x{i+1} =", sol)

# Mostrar la matriz y el vector constante
    st.sidebar.write("Matriz triangular inferior L:")
    st.sidebar.write(L)

    st.sidebar.write("Vector constante b:")
    st.sidebar.write(b)

# Mostrar la solución completa
    st.write("La solución del sistema lineal triangular inferior es:")
    for i, sol in enumerate(solucion):
        st.write(f"x{i+1} =", sol)

with tabs[1]:
    st.markdown("# Metodo de eliminacion gaussiana ❄️")
    st.image('https://multimedia.uned.ac.cr/pem/metodos_numericos_ensenanza/modulo4/img/des/trapecio3.jpg',width=500)
    #codigo aqui


# Configuración de la página

    st.write("Esta aplicación resuelve sistemas lineales mediante el método de Eliminación Gaussiana.")

# Ingresar la matriz extendida y el vector constante
    A = np.zeros((n, n))
    b = np.zeros(n)

# Ingresar la matriz extendida A y el vector constante b
    st.sidebar.write("Ingrese la matriz extendida A y el vector constante b:")
    for i in range(n):
        for j in range(n):
            A[i, j] = st.sidebar.number_input(f"A[{i+1}, {j+1}]", value=0.0, step=0.1)

        b[i] = st.sidebar.number_input(f"b[{i+1}]", value=0.0, step=0.1)

# Resolver el sistema lineal mediante eliminación gaussiana
    for i in range(n):
    # Escalonar la matriz
        for j in range(i+1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

# Resolver el sistema triangular superior resultante
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = b[i] / A[i, i]
        b[:i] -= A[:i, i] * x[i]
    x_complete = np.zeros(n)
    for i in range(n-1, -1, -1):
        x_complete[i] = b[i] / A[i, i]

# Mostrar la solución completa
    st.write("La solución completa del sistema lineal es:")
# Mostrar la solución
    for i, sol in enumerate(x_complete):
        st.write(f"x{i+1} =", sol)

# Mostrar la matriz extendida y el vector constante
    st.sidebar.write("Matriz extendida A:")
    st.sidebar.write(A)

    st.sidebar.write("Vector constante b:")
    st.sidebar.write(b)

# Mostrar la solución completa
    st.write("La solución del sistema lineal es:")
    for i, sol in enumerate(x):
        st.write(f"x{i+1} =", sol)




with tabs[2]:
    st.markdown("# Eliminacion gaussiana con piboteo ❄️")
    st.image('https://www.neurochispas.com/wp-content/uploads/2022/12/Regla-de-los-trapecios-ejercicio-3-grafica.jpg',width=500)
    #codigo aqui

# Función para realizar eliminación gaussiana con pivoteo
    def gaussian_elimination_pivot(matrix, b):
        n = len(matrix)
        x = np.zeros(n)

        for i in range(n):
        # Pivoteo parcial: encontrar la fila con el máximo elemento en la columna actual
            max_row = i
            for k in range(i + 1, n):
                if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                    max_row = k
            matrix[[i, max_row]] = matrix[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]

            for j in range(i + 1, n):
                factor = matrix[j][i] / matrix[i][i]
                b[j] -= factor * b[i]
                for k in range(i, n):
                    matrix[j][k] -= factor * matrix[i][k]

        for i in range(n - 1, -1, -1):
            x[i] = b[i]
            for j in range(i + 1, n):
                x[i] -= matrix[i][j] * x[j]
            x[i] /= matrix[i][i]

        return x

# Interfaz de usuario con Streamlit
    def main():

        matrix_input = st.text_area("Matriz (filas separadas por '\\n'):", value="2 1 -1\n0 3 2\n0 0 -2")
        vector_input = st.text_input("Vector b:", value="1 2 -1")
        calculate_button = st.button("Calcular")
        output_area = st.empty()

        if calculate_button:
            matrix_str = matrix_input.strip()
            vector_str = vector_input.strip()

        # Convertir las cadenas de entrada en matrices y vectores
            matrix = np.array([list(map(float, row.split())) for row in matrix_str.split('\n')])
            vector = np.array(list(map(float, vector_str.split())))
            result = gaussian_elimination_pivot(matrix, vector)
            output_area.write("Resultado:")
            output_area.write(result)

    
        main()
    

   




