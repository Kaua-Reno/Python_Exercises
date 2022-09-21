#sequência de Fibonacci

n = int(input("digite um número da sequência de Fibonacci:"))

f1 = 0
fa = 1
fb = 1

if n == 1 :
    print("0")
elif n == 2:
    print("0", "\n1")
elif n == 3:
    print("0", "\n1", "\n1")
else:
    print("0", "\n1", "\n1")
    for i in range(1, n-2):
        f1 = fb + fa
        fa = fb
        fb = f1
        print(f1)