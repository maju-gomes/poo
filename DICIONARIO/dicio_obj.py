# recuperar dicionário a partir dos dados de um objeto

class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.id} - {self.nome}"
    
cliente1 = Cliente(1, "Douglas Crockford")
cliente2 = Cliente(2, "Jon Bosak")

# print(cliente1.__dict__)
# print(vars(cliente2))