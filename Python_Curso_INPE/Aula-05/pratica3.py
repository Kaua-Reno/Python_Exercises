# Código para potenciação sem o uso de blibioteca e do "**"

n1 = int(input("digite um número: "))
n2 = int(input("digite outro número: "))

p = 1

for k in range(0, n2):
    p = p * n1
    print(p)