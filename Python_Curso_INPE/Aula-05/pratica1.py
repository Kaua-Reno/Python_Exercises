#Calculando fatorial

n = int(input("Digite um número entre 1 e 10 para ser fatorado: "))

fat = 1

while n >= 1:
    fat = fat * n
    print(n, fat)
    n = n - 1