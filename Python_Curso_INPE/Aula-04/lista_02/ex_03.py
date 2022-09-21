#Código para ver se um número digitado pelo usuário é impar ou par

n = int(input("Digite um número entre 0 e 10:"))

if n % 2 == 0:
    print("o número ",n," é par")
else:
    print("o número ",n," é ímpar")