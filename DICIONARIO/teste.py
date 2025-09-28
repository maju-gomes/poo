dicionario = {"RN": "Natal", "PB": "João Pessoa", "PE": "Recife"}

# recupera item - cada um é um obj da classe tuple
for item in dicionario.items():
    print(item)

# recupera em diferentes variáveis as chaves e os valores
for key, value in dicionario.items():
    print(key, value)
#  items() é um método da classe dict

# recuperar chave e valor, respect.
for key in dicionario.keys():
    print(key)

for value in dicionario.values():
    print(value)
# .keys() e .values() são métodos da classe dict 

# COPIAR DICIONÁRIO
novo_dicionario = dicionario.copy()
print(novo_dicionario)

# outro dicionario
dic = {"AL": "Alagoas"}

# ATUALIZAR DICIONÁRIO OU JUNTAR DOIS
novo_dicionario.update(dic)
print(novo_dicionario)