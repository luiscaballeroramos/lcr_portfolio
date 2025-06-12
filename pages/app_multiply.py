import streamlit as st
from lcr_code.operaciones import sqrt

# Slider de 0 a 100
value = st.slider("Select a value", min_value=0, max_value=100, value=50)

# Llamar a la función del otro archivo
result = sqrt(value)

# Mostrar el resultado en un cuadro de texto
st.text_input("Result square root of value", value=str(result), disabled=True)
