import json
from dicio_obj import Cliente

# DUMP - SALVA ARQUIVO
# json.dump(objeto, arquivo, default = função)

# LOAD - LÊ ARQUIVO
# json.load(arquivo)

# parametros:
# obj q será salvo
# arquivo onde será salvo/lido
# função que gera dicionário do obj que está sendo salvo 

# ---------

# ACESSO A UM ARQUIVO NO DISCO - open()
# open(arquivo, mode = modo_de_acesso)

# modos de acesso:
# "r": read
# "w": write

# ---------

# SALVANDO OS OBJS DO ARQUIVO
a = Cliente(1, "Maju")
b = Cliente(2, "Miguel")
clientes = [a, b]

with open("clientes.json", mode="w") as arquivo:
    json.dump(clientes, arquivo, default = vars)

# LENDO OS OBJS DO ARQUIVO
with open("clientes.json", mode="r") as arquivo:
    clientes_json = json.load(arquivo)
    for obj in clientes_json:
        c = Cliente(obj["id"], obj["nome"])
        clientes.append(c)

print(clientes_json)