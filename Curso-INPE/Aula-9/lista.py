cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Ouro Preto"]
print(cidades)

# Ordenando a lista
cidades.sort()
print(cidades)

# Gera uma nova lista "ordenada ao contrário"
nova_lista = sorted(cidades, reverse=True)

print(nova_lista)

print(cidades)

cidades.append("São José dos Campos")
print(cidades)

del cidades[1]
print(cidades)

cidades.extend( [ "Ouro Preto", "Mariana" ] )
print(cidades)

cidades.reverse()
print(cidades)