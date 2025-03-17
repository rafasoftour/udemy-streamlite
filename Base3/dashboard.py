import streamlit as st
st.set_page_config(page_title="Dashboard", layout="wide")
import pathlib
from faker import Faker
import pandas as pd
import numpy as np



# Load csss
def load_css(file_css):
    with open(file_css) as css:
        st.html(f"<style>{css.read()}</style>")

css_path = pathlib.Path("styles.css")
load_css(css_path)

faker = Faker('es_ES')


with st.container():
    st.title("Dashboard")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.success(faker.company())
        # Formatear el precio con símbolo de euro y coma como separador de miles
        precio = faker.random_number(digits=5)
        delta = faker.random_number(digits=2)
        st.metric("Price", value=f"€{precio:,.2f}", delta=f"€{delta:,.2f}", border=True)
    with c2:
        st.warning(faker.company())
        precio = faker.random_number(digits=5)
        delta = faker.random_number(digits=2)
        st.metric("Price", value=f"€{precio:,.2f}", delta=f"€{delta:,.2f}", border=True)
    with c3:
        st.info(faker.company())
        precio = faker.random_number(digits=5)
        delta = faker.random_number(digits=2)
        st.metric("Price", value=f"€{precio:,.2f}", delta=f"€{delta:,.2f}", border=True)

    col1, col2 = st.columns([2,1])
    with col1:
        st.info("Balance")
        chart_data = pd.DataFrame(np.random.randn(20,3), columns=["a", "b", "c"])
        st.bar_chart(chart_data)
    with col2:
        st.info("Capital flow")
        chart_data = pd.DataFrame(np.random.randn(20,3), columns=["a", "b", "c"])
        st.line_chart(chart_data)

    data = {
        "Bank:": [faker.company() for _ in range(10)],
        "City:": [faker.city() for _ in range(10)],
        "Phone:": [faker.phone_number() for _ in range(10)],
    }

    df = pd.DataFrame(data)
    st.success("### Banks ###")
    st.dataframe(df, hide_index=True)