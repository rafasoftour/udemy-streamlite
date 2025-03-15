import streamlit as st
st.set_page_config(layout="wide", page_title="Curso streamlit", page_icon="😊")
st.title("Bienvenido al curso de Streamlite")
st.sidebar.success("Tutoriales")

pages = [
    st.Page("paginas/1_widgets.py", title="Widgets elements", icon=":material/add:")
]
