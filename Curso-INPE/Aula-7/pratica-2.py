print("Fibonacci")
x = int(input("Digite o número de Fibonacci que você quer: "))
y = 0
z = y + 1
t = 0

if(x == 1):
    print(y)
elif(x == 2):
    print(y)
    print(z)
else:
    print(y)
    print(z)
    for k in range(2, x):
        y = t + z
        print(y)
        t = z
        z = y
        