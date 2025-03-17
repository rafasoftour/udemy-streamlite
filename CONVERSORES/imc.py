import streamlit as st
import pandas as pd

def imc():
    st.subheader("Indice de masa corporal")
    st.latex(r"\text{IMC} = \frac{\text{Peso(Kg)}}{\text{Altura(m)}^2}")

    st.markdown("**Tabla del IMC según la OMS**")
    datos_imc = {
        "Categoria": [
            "Peso insuficiente",
            "Peso normal",
            "Sobrepeso",
            "Obesidad grado 1",
            "Obesidad grado 2",
            "Obesidad grado 3 (mórbida)"
        ],
        "Rango del IMC": [
            "Menos de 18.5",
            "18.5 - 24.9",
            "25 - 29.9",
            "30 - 34.9",
            "35 - 39.9",
            "40 - mas"
        ]
    }
    tabla_imc = pd.DataFrame(datos_imc)
    st.dataframe(tabla_imc, hide_index=True)

    c1, c2 = st.columns(2)
    peso = c1.number_input("Peso", step=1)
    altura = c2.number_input("Altura")
    def imc_calc(peso, altura):
        if altura <= 0 or peso <= 0:
            return "La altura y peso deben ser mayores a 0"
        else:
            imc_res = peso / (altura ** 2)
            return f"Tu IMC es : {imc_res: .2f}"
    if st.button("Calcular", type="primary"):
        imc = imc_calc(peso, altura)
        st.title(f":green[{imc}]")