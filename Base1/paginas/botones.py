import streamlit as st
st.title("Botones y Callbacks")

# btn = st.button("Boton", key="btn1")
# st.write(btn)
# st.divider()
# texto = "Un texto cualquiera"
# if st.button("Mostrar texto"):
#     texto = "Un nuevo texto agregado"
# st.write(texto)

# st.divider()
# contador = 0
# if st.button("Incrementar"):
#     contador += 1
# st.write("# ", contador)

# Session state
if "texto" not in st.session_state:
    st.session_state.texto = "Un texto"

def cambiar_texto():
    st.session_state.texto = "Un nuevo texto agregado"

st.write(st.session_state.texto)

st.button("Cambiar texto", on_click=cambiar_texto)

st.write(st.session_state.texto)

st.divider()

def incrementa():
    state.incrementar += 1
def decrementa():
    state.incrementar -= 1

state = st.session_state
if "incrementar" not in state:
    state.incrementar = 0



st.write("# Z ", state.incrementar)
st.button("Incrementar", on_click=incrementa)
st.button("Decrementar", on_click=decrementa)
st.write("# ", state.incrementar)

st.divider()
st.subheader("Link button")
st.link_button("Ir a google", "https://google.com")

texto_descargar = "Texto a descargar"
st.download_button("Descargar", texto_descargar)

with open("assets/emoji.jpg", "rb") as file:
    st.download_button(
        "Desargar imagen",
        data=file, 
        file_name="emoji.jpg",
        mime="image/jpg"
    )
