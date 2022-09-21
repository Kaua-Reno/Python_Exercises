# código para testar se as medidas fornecidas pelo usúario formam um triangulo e qual é sua classificação: isósceles, escaleno ou equilátero

l1 = int(input("Digite a medida para o primeiro lado:"))
l2 = int(input("Digite a medida do segundo lado:"))
l3 = int(input("Digite a medida do terceiro lado:"))

#para 3 medidas formarem um triângulo, a soma dos dois menores lados devem ser maior que o tamanho do maior lado

if l1+l2>l3 and l2+l3>l1 and l1+l3>l2:
    print("As medidas fornecidas formar um triângulo")
    if l1 == l2 == l3:
        print("E esse triângulo é equilátero")
    elif l1 == l2 != l3 or l3 == l2 != l1 or l1 == l3 != l2:
        print("E esse triângulo é isósceles")
    else:
        print("E esse triângulo é escaleno")


