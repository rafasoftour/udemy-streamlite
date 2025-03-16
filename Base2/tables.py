import streamlit as st
import pandas as pd

# mockaroo.com

def tables():
    st.title("Tables")
    file = st.file_uploader("Load csv", type=["csv"])
    if file is not None:
        csv = pd.read_csv(file)
        st.subheader("Cars")
        drop_columns = st.multiselect("Drop columns", options=csv.columns)
        if drop_columns:
            limite = st.slider("Limit rows:", min_value=10, max_value=len(csv), value=10)
            table_limit = csv.head(limite)
            st.write(f"Number rows: {limite}")
            drop = table_limit.drop(columns=drop_columns)
            st.table(drop)
        else:
            hide_columns = ["id","color"]
            csv_final = csv.drop(columns=hide_columns, errors="ignore")
            st.table(csv_final.head(10))
    else:
        st.info("Load a csv file")
