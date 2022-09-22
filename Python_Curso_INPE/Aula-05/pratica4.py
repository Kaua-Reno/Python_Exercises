# código para checar se um número é primo

n = int(input("Verificar numeros primos ate: "))
mult=0

if n == 1:
    print("Número inválido!!")
else:
    for count in range(2,n):
        if (n % count == 0):
            mult += 1

    if(mult==0):
        print("É primo")
    else:
        print("não é primo")