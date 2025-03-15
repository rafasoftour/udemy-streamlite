import streamlit as st
st.title("Multimedia")
st.divider()

st.subheader("Imagenes")

# Raiz
st.image("assets/emoji.jpg",
         caption="Lindo emoji", width=200)
# Web
st.image("https://cdn.pixabay.com/photo/2022/10/11/16/43/french-bulldog-7514725_1280.jpg",
         width=300)
# Local
file = st.file_uploader("Elegir imagen", type=["jpg","png"],
                        accept_multiple_files=True)
if file is not None:
    st.image(file)

st.subheader("Video")

st.video("https://cdn.pixabay.com/video/2024/12/29/249475_large.mp4")

# Uso de la cache

