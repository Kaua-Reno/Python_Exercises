print("Potenciação sem o uso do ** e de alguma função!!")

x = int(input("Digite o número a ser elevado: "))
y = int(input("Digite a potencia: "))
print(x)
t = x

for k in range(1, y):
    z = t
    t = x * z
    print(t)