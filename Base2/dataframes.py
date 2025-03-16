import streamlit as st
import pandas as pd
from io import BytesIO

def dataframes():
    st.title("Dataframes")
    file = st.file_uploader("Load csv",type=["csv"])
    if file is not None:
        csv = pd.read_csv(file)
        field = st.selectbox("Seleccion columna por la que filtrar", options=csv.columns)
        search = st.text_input("Criterio para el filtrado", placeholder="Search...", autocomplete="off")
        if search:
            #filter_data = csv[csv.apply(lambda row: row.astype(str).str.contains(search, case=False).any(), axis=1)]
            filter_data = csv[csv.apply(lambda row: search.lower() in str(row[field]).lower(), axis=1)]
        else:
            filter_data = csv
        st.subheader("Cars")
        st.write(f"Results: {len(filter_data)}")
        st.dataframe(
            filter_data,
            hide_index=True,
            width=1000,
            column_order=["model","car","color"],
            column_config={
                "car": "CARS",
                "model": "MODELS",
                "color": "COLORS"
            }
            )
        excel_buffer = BytesIO()
        filter_data.to_excel(excel_buffer, index=False, engine="openpyxl")
        excel_buffer.seek(0)
        st.download_button(
            label="Download excel",
            data=excel_buffer,
            file_name="file.xlsx",
            mime="application/vnd.openxmlformat=officedocument.spreadsheetml.sheet"
        )
    else:
        st.info("Load csv file")