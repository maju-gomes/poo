import streamlit as st
from paciente import Paciente
# aqui na class UI (interface do usuário) também importamos o Streamlit, como no index.py (onde o programa roda)

class PacienteUI:
    # a classe UI não tem método construtor. Por quê?
    def main():
        st.header("Dados do Paciente")
        nome = st.text_input("Nome:")
        cpf = st.text_input("CPF:")
        telefone = st.text_input("Telefone:")
        nascimento = st.text_input("Data de nascimento:")
        if st.button("Idade"):
            data_de_nascimento = str(Paciente.get_d_nasc())

    paciente = Paciente("Miguel", 12345678901, 99999999, "25/07/2023")