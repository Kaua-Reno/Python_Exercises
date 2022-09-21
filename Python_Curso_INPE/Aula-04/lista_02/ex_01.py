# código para saber qual é o maior número digitado

n1 = int(input("Digite um número:"))
n2 = int(input("Digite um número:"))
n3 = int(input("Digite um número:"))

if n1 >= n2 and n1 >= n3:
    if n2 >= n3:
        print('maior: ', n1,'menor: ', n3)
    else:
        print('maior: ', n1,'menor: ', n2)
elif n2 >= n1 and n2 >= n3:
    if n1 >= n3:
        print('maior: ', n2,'menor: ', n3)
    else:
        print('maior: ', n2,'menor: ', n1)
else:
    if n2 >= n1:
        print('maior: ', n3,'menor: ', n1)
    else:
        print('maior: ', n3,'menor: ', n2)