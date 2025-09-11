import streamlit as st
from retangulo import Retangulo

class RetanguloUI:
    def main():
        st.header("Cálculos com retângulo")
        base = st.text_input("Valor da base")
        altura = st.text_input("Valor da altura")
        if st.button("Calcular"):
            base = float(base)
            altura = float(altura)

            # instanciação
            retangulo = Retangulo(base, altura)

            st.write(retangulo)
            st.write(retangulo.calc_area())
            st.write(retangulo.calc_diagonal())