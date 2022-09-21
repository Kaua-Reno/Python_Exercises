# equação geral da reta

a = 3
b = 2
c = 6
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

reta = a*x - b*y - c

if reta == 0:
    print("Os valores passados formam uma reta")
    print(reta)
else:
    print("Os valores passado não formam uma reta")

