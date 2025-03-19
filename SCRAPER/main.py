import streamlit as st
from shortener import shortener
from scraper import scrapper

st.set_page_config(page_title="Scraper")

tab1, tab2 = st.tabs(["URL Shortener", "Wikipedia Web Scraper"])

with tab1:
    shortener()

with tab2:
    scrapper()