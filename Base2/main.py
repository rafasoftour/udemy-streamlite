import streamlit as st
from tables import tables as t
import dataframes
import charts

if "menu" not in st.session_state:
    st.session_state.menu = "Tables"

with st.sidebar:
    st.session_state.menu = st.selectbox("Menu", ["Tables", "Dataframes", "Charts"])

if st.session_state.menu == "Tables":
    t()
elif st.session_state.menu == "Dataframes":
    dataframes.dataframes()
elif st.session_state.menu == "Charts":
    charts.charts()