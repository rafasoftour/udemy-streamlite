import streamlit as st
st.title("Widgets")
st.subheader("Select-box")

opcion = st.selectbox("Escoge un color", ["Rojo", "Amarillo", "Verde", "Azul"])
st.write(opcion)

st.subheader("Multiselect")
options = st.multiselect(
    "Elige varias opciones",
    ["Rojo", "Amarillo", "Verde", "Azul"]
)
st.write(options)

st.subheader("Radio")
radio = st.radio(
    "Elige una opcion",
    ["Rojo", "Amarillo", "Verde", "Azul"],
    captions=["Op 1","Op 2","Op 3","Op 4"]
)
st.write(radio)

st.subheader("Checkbox, toggle y status")
acepto = st.checkbox("Aceptar términos y condiciones de uso")
if acepto:
    st.success("Términos aceptados")

rechazo = st.toggle("No acepto los términos")
if rechazo:
    st.error("No acepto los términos")

st.subheader("Color picker")
color = st.color_picker("Escoge un color", "#6c95e4")
st.write(color)

st.subheader("Sliders")
edad = st.slider("Cual es tu edad", 0, 120, 18)
st.write("Tu edad es: ", edad)

rango = st.slider("Rango", value=(100, 200))
st.write(rango)

color_slider = st.select_slider(
    "Selecciona tus colores",
    options = [
        "Rojo",
        "Amarillo",
        "Azul",
        "Rosa"
    ]
)
st.write("Tu color", color_slider)