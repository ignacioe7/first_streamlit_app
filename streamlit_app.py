import streamlit as st

st.title('Página de inicio')


st.subheader('Bienvenido a nuestra aplicación web')


nombre = st.text_input('Introduce tu nombre')
if st.button('Saludar'):
    st.write(f'Hola, {nombre}!')