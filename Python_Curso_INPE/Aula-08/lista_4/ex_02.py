# Código para testar uma senha, ver se possuí caracteres maiúculos e minúsculos, e se tem pelo menos 8 caracteres.

x = str(input("Digite sua senha: "))
z = 0 
t = 0
if len(x) >= 8:
    for y in x:
        if y.isupper() == True:
            z = z +1

        if y.islower() == True:
            t = t +1

    if z >= 1 and t >= 1:
        print("Está senha é forte")
    else:
        print("Senha fraca, adicione caracteres maiúsculos e minúculos")
        
else:
    print("Senha muito curta")