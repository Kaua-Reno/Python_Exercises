x = int(input("Digite um valor para x: "))
y = int(input("Digite um valor para y: "))

a = 3
b = -2
c = -6

equacao = a*x+b*y+c
if (equacao == 0):
    print("Sobre a reta")
elif(equacao >= 1):
    print("Acima da reta")
else:
    print("Abaixo da reta")

print("Equação da reda igual a:", equacao)