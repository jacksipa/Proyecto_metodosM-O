import streamlit as st
import numpy as np
import pandas as pd
st.title('hola mundo cruel')

st.header('este sera el proyecto')
st.subheader('se lograra? ')
st.text('mas texto por aca')


st.markdown('no entiendo')
st.markdown('# no entiendo')
st.latex('y_{n+1}=y_n')

st.radio('cual es tu lenguaje de programacion favorito?',('python','Java','C++'))
entrada_texto= st.text_input('cual es tu  nombre? ',value= 'escribe aqui tu nombre')
print(entrada_texto)
number=st.number_input('cual es tu edad',min_value=0, max_value=150,value=25)

st.image('https://static.vecteezy.com/ti/photos-gratuite/p2/6860456-geometrique-noir-et-blanc-fond-3d-fond-d-ecran-sombre-avec-lignes-blanches-gratuit-photo.jpg',width=300,caption='logo lindo')
#subir archivo

file=st.file_uploader('suve tu archivo csv',type='csv')
print(file)

print(type(file))

matriz= np.asarray(file)
print(matriz)


st.success('this is a success message')
st.info('this is a info message')
st.warning('this is a warning message')
st.error('this is a error message! ')
st.exception('this is a exception message ')

st.write('escribe esto: ', range(10))
st.write('escribe esto: ', range(10), 2.5, {'key':'value'})

df = pd.DataFrame({'col1': [1,4,7,0], 'col2': [2,5,8,1], 'col3': [3,5,9,2]})
st.dataframe(df)


##elementos interactivos

st.checkbox('Mostrar mapa')
st.slider('seleccione los valores del 1-100',min_value=0, max_value=100,value=50,step=5)


st.radio('radio',options=['opcion 1','opcion 2'])

st.multiselect('miltiselect', options=['opcion1', 'opcion2'])

st.select_slider('esta es el selector slider', options= ['opcion 1', 'option 2'])
st.date_input('area de fecha')
st.time_input('entrada de tiempo')
st.color_picker('color picker')

st.markdown('## Columns')
col1,col2 = st.columns(2)
col1.markdown('columna 1 ')
col1.button('boton1')
col2.markdown('columna 2 ')
col2.button('boton2')

st.markdown('## Expander')
expander = st.expander('expander')
expander.markdown('this is a expander')


st.markdown('## taps')
tabs= st.tabs(['tap1','tap2'])
with tabs[0]:
    st.markdown('this is a tab 1')
with tabs[1]:
    st.markdown('this is a tab 2')

st.markdown('## line chart')

st.line_chart({'data':[1,2,3,4,5]})
st.markdown('##area chart')
st.area_chart({'data':[1,2,3,4,5]})
st.markdown('## bar chart')
st.bar_chart({'data':[1,2,3,4,5]})

