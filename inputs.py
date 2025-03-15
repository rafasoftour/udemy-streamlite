import streamlit as st
from datetime import datetime as dt

st.title("Input widgets")
st.divider()

texto = st.text_input("Escribe algo...", 
              placeholder="Escribe aqui...", 
              key="txt1",
              max_chars=30)
st.write(texto)

st.number_input("Numero", 
                step=1,
                min_value=10,
                max_value=100)

st.text_area("Area de texto",
             height=68)

st.time_input("Tiempo",
              step=3600)

min_date = dt(1900,1,1)
max_date = dt(2050,12,12)

st.date_input("Fecha",
              min_value=min_date,
              max_value=max_date)

st.subheader("Formularios")
with st.form("my_form"):
    nombre = st.text_input("Nombre")
    correo = st.text_input("Correo electrónico")
    submit = st.form_submit_button("Enviar")
    if submit:
        if not nombre or not correo:
            st.error("Faltan datos del formulario")
        else:
            st.write(f"El nombre es: {nombre} y el correo es:{correo}")

st.chat_input("Chat")