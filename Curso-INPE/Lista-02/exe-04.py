# calculadora básica
i = "s"
while i != "n":
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite o segundo número: "))

    print("\nEscolha a função que deseja realizar:")
    print("1 para Adição")
    print("2 para Subtração")
    print("3 para Multiplicação")
    print("4 Divisão")
    x = int(input("\nDigite o número referente a operação que deseja realizar: "))

    if (x == 1):
        n3 = n1 + n2
        print(f"{n1} + {n2} = {n3}")
    elif (x == 2):
        n3 = n1 - n2
        print(f"{n1} - {n2} = {n3}")
    elif (x == 3):
        n3 = n1 * n2
        print(f"{n1} x {n2} = {n3}")
    else:
        n3 = n1 / n2
        print(f"{n1} / {n2} = {n3}")
    
    i = str(input("Você quer fazer outra operação?(s/n) "))