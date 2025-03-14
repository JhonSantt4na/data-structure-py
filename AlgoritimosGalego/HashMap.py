# Criando um HashMap (dicionário)
hash_map = {}

# Adicionando valores
hash_map["nome"] = "João"
hash_map["idade"] = 25
hash_map["cidade"] = "São Paulo"

# Acessando valores
print(hash_map["nome"])  # Saída: João
print(hash_map.get("idade"))  # Saída: 25

# Removendo um item
del hash_map["cidade"]

# Verificando se uma chave existe
if "cidade" in hash_map:
    print("Chave encontrada!")
else:
    print("Chave não encontrada!")  # Saída: Chave não encontrada!

# Iterando sobre as chaves e valores
for chave, valor in hash_map.items():
    print(f"{chave}: {valor}")
