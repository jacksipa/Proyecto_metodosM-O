import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sp
import pandas as pd

import matplotlib.animation as animation
st.title('metodo cerrado')

st.markdown('# metodo de la biseccion')
# @title iteremos hasta que el error sea de 1%

def calculate_y(x_value, expression):
  return [expression.subs({x: xi})for xi in x_value]

##############
x =st.sidebar.text_input( "ingrese la variable", "x")
x= sp.symbols('x')
entra = st.text_input('ingrese la ecuacion ', x**3 - x)
y=sp.sympify(entra)


xl,xu =st.sidebar.slider(
    'selecciona el rango de valores. ',
    0.0,10.0, (0.0,1.7)
)
#print('rango de selecionado: ', xl , xu)
##############

tol = st.number_input('tolerancia', 0.0,1.0,0.1,0.1)

xr = None
xr_ant = xu
error = tol+1
it = 1

columnas = ['Xl','Xu','Xr','er(%)','f(Xl)','f(Xu)','f(Xr)']
tabla = pd.DataFrame(columns=columnas)

fig_placeholder =st.empty()
tablita = st.empty()
while error > tol:
  #Evaluamos la función en los puntos del intervalo.
  fxl= round(y.subs({x:xl}),4)
  fxu= round(y.subs({x:xu}),4)

  ##################
  plt.figure()
  fig, ax = plt.subplots()

  r = np.linspace(xl, xu,100)
  fx = calculate_y(r,y)

  ax.plot(r,fx,color='blue',label="${y}$")
  ## Plano cartesiano (Ejes)
  ax.vlines(x=0,ymin=round(min(fx),4)-0.5,ymax=round(max(fx),4)+0.5,color='k')
  ax.hlines(y=0,xmin=round(min(r),4)-0.5,xmax=round(max(r),4)+0.5,color='k')

  ax.set_title("${y}$")
  ax.grid()

  ##################

  ## Límites xl y xu
  ax.vlines(x=xl, ymin=0, ymax=fxl, color='k', linestyle='--',label=f'$x_l=${xl}')
  ax.vlines(x=xu, ymin=0, ymax=fxu, color='k', linestyle='--',label=f'$x_u=${xu}')

  #Calculamos la raíz
  xr = round((xl + xu)/2,4)
  fxr = round(y.subs({x:xr}),4)

  ## Pintamos el punto intermedio
  ax.plot(xr,fxr,color='red',label=f'$Raíz=${xr}',marker='o')
  ax.legend()
  

  error = np.abs((xr-xr_ant)/(xr))*100

  nueva_fila = {'Xl': xl, 'Xu': xu, 'Xr': xr, 'er(%)': error, 'f(Xl)': fxl, 'f(Xu)': fxu, 'f(Xr)':fxr}
  nueva_fila = pd.DataFrame([nueva_fila])

  tabla = pd.concat([tabla, nueva_fila], ignore_index=True)
  tablita =st.dataframe(tabla.head(it))  

  st.dataframe(tabla.head(it))

  if (fxl * fxr) < 0:
    xu = xr
  elif (fxl*fxr) > 0:
    xl = xr
  elif (fxl*fxr) == 0:
    st.success(f"La raiz está en: ({xr},{fxr})")
    break

  xr_ant = xr
  it+=1

  #mostrar la figura en el espacio reservado 
  
  fig_placeholder.pyplot(fig)
   #borrar la figura para la siguiente iteracion
  plt.close(fig)






