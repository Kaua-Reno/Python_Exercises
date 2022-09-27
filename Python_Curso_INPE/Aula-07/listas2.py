cidades = ["São Paulo", "Rio de Janeiro",
"Belo Horizonte", "Ouro Preto"]

#Adicionou um novo campo
cidades.append("São José dos Campos")
print(cidades)

#Deletou o segundo campo da lista
del cidades[1]
print(cidades)

#Adicionou uma lista de dois campos
cidades.extend( ["Ouro Preto", "Mariana"] )
print(cidades)

#Colocou aocontrário a lista
cidades.reverse()
print(cidades)