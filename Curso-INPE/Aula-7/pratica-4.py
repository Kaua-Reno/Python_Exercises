print("Número primo??")

x = int(input("Digite um número para ver se ele é primo: "))

if (x == 2) or (x == 3) or (x == 5) or (x == 7):
    print(f"o número {x} é primo")
elif (x % 2 == 0) or (x % 3 == 0) or (x % 5 == 0) or (x % 7 == 0):
    print(f"o número {x} não é primo")
else:
    print(f"o número {x} é primo")