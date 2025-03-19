import streamlit as st
import pyperclip
import pyshorteners as pysh

def shortener():
    st.subheader("URL Shortener")

    def copy_url(url):
        pyperclip.copy(url)

    shortener = pysh.Shortener()
    if "url_to_short" not in st.session_state:
        st.session_state.url_to_short = ""
    
    def clean():
        st.session_state.url_to_short = ""
    
    with st.container(border=True):
        c1, c2, c3 = st.columns([7,1,1], vertical_alignment="bottom")
        c1.text_input("", placeholder="URl here: https://google.com", autocomplete="off", key="url_to_short")
        c2.button("",icon=":material/cancel:", on_click=clean)
        submit = c3.button("Short", type="primary")
        if submit:
            if st.session_state.url_to_short != "":
                try:
                    shorted_url = shortener.tinyurl.short(st.session_state.url_to_short)
                    cc1, cc2, _ = st.columns(3, vertical_alignment="bottom")
                    cc1.write(shorted_url)
                    cc2.button("", icon=":material/file_copy:", on_click=copy_url(shorted_url))
                except Exception as e:
                    print(e)
                    st.error("Type a valid url")
            else:
                st.warning("Type a url")
