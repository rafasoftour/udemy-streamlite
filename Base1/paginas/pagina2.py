import streamlit as st
st.title("Pagina 2")

if "id" in st.session_state:
    st.write("El ID es: ", st.session_state.id)
else:
    st.write("No hay ID")