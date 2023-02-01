print("Fatoração!!")

x = int(input("Digite um número de 1 a 10: "))
print(x)
z = x
for k in range(1, x):
    t = x - 1    
    z = z * t
    x = t
    print(z)
