print("Tabela de Multiplicação de 1 a 10!!")
x = 0
for k in range(1, 11):
    x = x + 1
    y = 1
    print(f"\n Tabuada do {x}\n")
    for k in range(1, 11):
        z = y * x
        print(f" {y} x {x} = {z}")
        y = y + 1