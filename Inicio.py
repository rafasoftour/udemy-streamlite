import streamlit as st
st.set_page_config(layout="wide", page_title="Curso streamlit", page_icon="😊")
st.title("Bienvenido al curso de Streamlite")
st.sidebar.success("Tutoriales")


pages = {
    "Widgets Elements": [
        st.Page("paginas/1_widgets.py", title="Widgets elements", icon=":material/home:"),
        st.Page("paginas/botones.py", title="Buttons elements", icon=":material/menu:"),
        st.Page("paginas/inputs.py", title="Inputs elements", icon=":material/add_circle:"),
    ],
    "Text and Multimedia": [
        st.Page("paginas/textos.py", title="Texto elements", icon=":material/apps:"),
        st.Page("paginas/multimedia.py", title="Mutimedia elements", icon=":material/restart_alt:")
    ],
    "Config": [
        st.Page("paginas/pagina1.py", title="Página 1", icon=":material/apps:"),
        st.Page("paginas/pagina2.py", title="Página 2", icon=":material/restart_alt:")
    ]
}

pg = st.navigation(pages, position="sidebar", expanded=True)
pg.run()