# a pasta models tem: entidades e DAOs
import json

class Cliente:
    # o classmethod deve ser criado quando a classe tem uma variável
    def __init__(self, id, nome, email, fone):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone

    # getters e setters
    def set_id(self, id):
        if id == "": raise ValueError("Este campo não pode estar vazio")
        self.__id = id

    def get_id(self):
        return self.__id
    
    def set_nome(self, nome):
        if nome == "": raise ValueError("O campo não pode estar vazio")
        self.__nome = nome

    def get_nome(self):
        return self.__nome
    
    def set_email(self, email):
        if email == "": raise ValueError("O campo não pode estar vazio")
        self.__email = email

    def get_email(self):
        return self.__email
    
    def set_fone(self, fone):
        if fone == "": raise ValueError("O campo não pode estar vazio")
        self.__fone = fone

    def get_fone(self):
        return self.__fone

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

    # JSON
    # retorna um dicionário com os dados de um cliente
    def to_json(self): # vai pra um json
        dicionario = {"id": self.__id, "nome": self.__nome, "email": self.__email, "fone": self.__fone}
        return dicionario

    # retorna um cliente com base no dicionário informado
    # usa-se quando a classe não possui atributo
    @staticmethod
    def from_json(dicionario): # quem chama o método é a classe
       return Cliente(dicionario["id"], dicionario["nome"], dicionario["email"], dicionario["fone"])
    

class ClienteDAO:
    __objetos = []

    @classmethod
    def inserir(cls, objeto):
        pass
    def listar(cls, objeto):
        pass
    def listar_id(cls, objeto):
        pass
    def atualizar(cls, objeto):
        pass
    def excluir(cls, objeto):
        pass
    def abrir(cls, objeto):
        pass
    def salvar(cls, objeto):
        pass
    

