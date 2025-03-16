import streamlit as st
import requests
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
st.subheader("Haciendo uso de la cache")
@st.cache_resource
def get_video(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.content

video_url = "https://cdn.pixabay.com/video/2024/12/29/249475_large.mp4"
video_data = get_video(video_url)
st.video(video_data)