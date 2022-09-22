# Código para potenciação sem o uso de blibioteca e do "**"

n1 = int(input("digite um número: "))
n2 = int(input("digite outro número: "))

r = 1

for k in range(0, n2):
    p = r * n1
    r = p
    print(p)