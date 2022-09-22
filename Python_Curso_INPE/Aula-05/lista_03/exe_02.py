#Calculadora
i = 2

while i >= 1:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))

    soma = n1 + n2
    subt = n1 - n2
    mult = n1 * n2
    divi = n1 / n2

    print("Selecione a função que deseja realizar: \n",
    "\n Soma : +",
    "\n Subtração : -",
    "\n Multiplicação : *",
    "\n Divisão : /")

    resp = str(input("\nfunção: "))

    if resp == "+":
        print("O resultado da soma entre", n1,"e", n2,"é:", soma)
    elif resp == "-":
        print("O resultado da subtração entre", n1,"e", n2,"é:", subt)
    elif resp == "*":
        print("O resultado da multiplicação entre", n1,"e", n2," é: ", mult)
    else:
        print("O resultado da divisão entre", n1,"e",n2,"é:", divi)

    k = str(input("Quer realizar outra conta?[s/n]: "))
    if k == "n":
        i = i - 2
    else:
        i = 2