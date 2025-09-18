from datetime import date, datetime

class Paciente:
    def __init__(self, nome, cpf, tel, d_nasc):
        self.__nome = nome
        self.__cpf = cpf
        self.__tel = tel
        self.__d_nasc = d_nasc
    
    def idade(self):
        hoje = date.today()
        anos = hoje.year - self.__d_nasc.year
        meses = hoje.month - self.__d_nasc.month
        if meses < 0:
            anos -= 1       # ainda não completou o ano
            meses += 12     # converte a diferença de meses para positivo
        return f"{anos} anos e {meses} meses"
    
    # getters e setters
    def set_nome(self, nome):
        if nome == "": raise ValueError("O campo não pode estar vazio")
        self.__nome = nome
        
    def get_nome(self):
        return self.__nome
    
    def set_cpf(self, cpf):
        if cpf == "": raise ValueError("O campo não pode estar vazio")
        self.__cpf = cpf

    def get_cpf(self):
        return self.__cpf

    def set_tel(self, tel):
        if tel == "": raise ValueError("O campo não pode estar vazio")
        self.__tel = tel

    def get_tel(self):
        return self.__tel
    
    def set_d_nasc(self, data_nascimento):
        if data_nascimento == "": raise ValueError("O campo não pode estar vazio")

        try:
            self.__d_nasc = date.strptime(data_nascimento, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Data inválida! Use o formato dd/mm/yyyy")
    
    def get_d_nasc(self):
        return self.__d_nasc

    def __str__(self):
        return f"Nome:{self.__nome} - CPF: {self.__cpf} - Tel.: {self.__tel} - Nascimento: {self.__d_nasc.strftime('%d/%m/%Y')}"
        