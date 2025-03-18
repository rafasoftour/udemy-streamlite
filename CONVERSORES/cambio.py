import streamlit as st
import requests as req
# https://apilayer.net/api/live?access_key=85b0aa6e6595a840bc65b0e614e7de4d&currencies=EUR,GBP,CAD,PLN&source=USD&format=1

def cambio():
    st.subheader("Tipo de cambio")
    currencies = [
    ('USD', 'Dólar Estadounidense'),
    ('EUR', 'Euro'),
    ('JPY', 'Yen Japonés'),
    ('GBP', 'Libra Esterlina'),
    ('AUD', 'Dólar Australiano'),
    ('CAD', 'Dólar Canadiense'),
    ('CHF', 'Franco Suizo'),
    ('CNY', 'Yuan Chino'),
    ('MXN', 'Peso Mexicano'),
    ('BRL', 'Real Brasileño'),
    ]

    cc1, cc2, cc3 = st.columns(3)
    moneda = cc1.number_input("Cantidad", step=1, value=1)
    with cc2:
        moneda_origen = st.selectbox("Moneda origen", options=[item[1] for item in currencies])
        codigo_origen = next(item[0] for item in currencies if item[1] == moneda_origen)
        st.write(codigo_origen)
    with cc3:
        moneda_destino = st.selectbox("Moneda destino", options=sorted([item[1] for item in currencies]))
        codigo_destino = next(item[0] for item in currencies if item[1] == moneda_destino)
        st.write(codigo_destino)

    api_key = st.secrets["general"]["API_KEY"]
    url = f"https://apilayer.net/api/live?access_key={api_key}&currencies={codigo_destino},PLN&source={codigo_origen}&format=1"

    if (st.button("Convertir", type="primary")):
        response = req.get(url)
        data = response.json()
        tipo_cambio = data["quotes"][f"{codigo_origen}{codigo_destino}"]
        res_moneda = moneda * tipo_cambio
        st.subheader(f"{moneda} {moneda_origen} equivale a :orange[{res_moneda:.2f}] {moneda_destino}")