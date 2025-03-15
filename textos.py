import streamlit as st

st.set_page_config(layout="wide", page_title="Curso streamlit", page_icon="😊")

st.title("Bienvenido al curso de Streamlit")
st.header("Soy un Header")
st.subheader("Soy un SubHeader")
st.caption("Caption")
st.text("Párrafo")

"Hola mundo"

# 123
# 4+5
# print("Valor con print")
# Esto es un comentario

# Concatenar
nombre = "Juan"
edad= 34
st.text("Hola mi nombre es " + nombre+ " y tengo " + str(edad))

st.text(f"Hola me llamo {nombre} y tengo {str(edad)}")

# Markdown
st.subheader("Markdow ----")
st.markdown("# Un titulo H1")
st.markdown("## Un titulo H2")
st.markdown("### Un titulo H3")

st.markdown("Este es un texto normal de Markdown solo que más largo")

st.markdown("Este texto tiene **negritas**")
st.markdown("Este texto tiene *cursiva*")
st.markdown("Este texto tiene ***cursiva negritas***")

st.markdown("[Google](https://google.com)")
st.markdown("---")
st.divider()

# guía markdown https://www.markdownguide.org/

# Expresiones matemáticas
st.subheader("Latex")
st.latex("E = mc^2")
st.latex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")
st.latex(r"""
\begin{matrix}
        a & b \\
        c & d
\end{matrix}
""")
st.latex(r"CH_4 + 2O_2 \rightarrow CO_2 + 2H_2O")
st.latex(r"\def\foo{x^2} \foo + \foo")

# Información adicional https://katex.org/

# JSON / CODES
st.subheader("JSON / CODES")
json = {"Nombre": "Maria", "Edad": 45, "Nacionalidad": "España"}
st.json(json)

code = """
function hello() {
    console.log("Hello")
}
"""
st.code(code, language="javascript")

# WRITE
st.subheader("WRITE")
st.write("## Soy un título con write")
st.write(json, nombre, edad)

# METRIC
st.subheader("METRIC")
st.metric(label="Ventas del mes", value="1500€", delta="35%")
st.metric(label="Dolar", value="0.8€", delta="-12% Respecto al último mes")