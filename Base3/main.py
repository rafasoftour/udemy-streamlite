import streamlit as st
st.set_page_config(layout="wide")  # Activa el modo ancho

import pathlib
from card import custom_card





# Load csss
def load_css(file_css):
    with open(file_css) as css:
        st.html(f"<style>{css.read()}</style>")

css_path = pathlib.Path("styles.css")
load_css(css_path)



st.title("CSS style")

with st.sidebar:
    st.subheader("Sidebar")


st.button("Streamlit button", type="primary")
st.button("Success", key="success")
st.button("Warning", key="warning")
st.button("Info", key="info")
st.button("Danger", key="danger")

st.text_input("Search", placeholder="Search...")
st.text_input("Input", placeholder="Input...")

with st.container(border=True):
    st.title("Es un contenedor")

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

custom_card("Titulo 1", lorem, "yellow")