#Código de uma calculadora que soma, subtrai, divide e multiplica

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

soma = n1 + n2
subt = n1 - n2
mult = n1 * n2
divi = n1 / n2

print("Selecione a função que deseja realizar: \n",
"\n Soma : digite 1",
"\n Subtração : digite 2",
"\n Multiplicação : digite 3",
"\n Divisão : digite 4")

resp = int(input("\n número da função: "))

if resp == 1:
    print("O resultado da soma entre", n1,"e", n2,"é:", soma)
elif resp == 2:
    print("O resultado da subtração entre", n1,"e", n2,"é:", subt)
elif resp == 3:
    print("O resultado da multiplicação entre", n1,"e", n2," é: ", mult)
else:
    print("O resultado da divisão entre", n1,"e",n2,"é:", divi)