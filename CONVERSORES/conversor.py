import streamlit as st

def conversor():
    st.subheader("Conversor de unidades")
    def conversor_unidades(valor, origen, destino):
        conversion_unidades = {
            "milimetros": 0.1,
            "centimetros": 1,
            "metros": 100,
            "kilómetros": 100000
        }
        valor_cm = valor * conversion_unidades[origen]
        result = valor_cm / conversion_unidades[destino]
        return result
    unidades = ["milimetros", "centimetros", "metros", "kilómetros"]
    col1, col2, col3 = st.columns(3)
    valor = col1.number_input("Introduce el valor a convertir", min_value=0.0, value=1.0)
    origen = col2.selectbox("Unidad de origen", options=unidades)
    destino = col3.selectbox("Unidad de destino", unidades)
    if st.button("Convertir"):
        result = conversor_unidades(valor, origen, destino)
        st.subheader(f"{valor} {origen} son equivalentes {result} {destino}")