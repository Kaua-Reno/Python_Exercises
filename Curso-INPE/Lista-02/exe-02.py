# triangulo

l1 = int(input("Digite o tamanho do primeiro lado: "))
l2 = int(input("Digite o tamanho do segundo lado: "))
l3 = int(input("Digite o tamanho do terceiro lado: "))

if (l1 + l2 > l3) and (l3 + l2 > l1) and (l1 + l3 > l2):
    print("Os tres lado formam um triângulo")
    if (l1 == l2 != l3) or (l1 == l3 != l2) or (l3 == l2 != l1):
        print("E esse triângulo é isósceles")
    elif (l1 == l2 == l3):
        print("E esse triângulo é equilátero")
    else:
        print("E esse triângulo é escaleno")
else:
    print("Os tres lado não formam um triângulo")