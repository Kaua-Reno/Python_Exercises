# Qual é o maior? E qual é o menor?

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite mais um número: "))

if (a == b == c):
    print("Os tres números digitados são iguais")
elif (a >= b) and (a >= c):
    print(f"O número {a} é o maior")
    if (b >= c):
        print(f"O número {c} é o menor")
    else:
        print(f"O número {b} é o menor")
elif (b >= a) and (b >= c):
    print(f"O número {b} é o maior")
    if (a >= c):
        print(f"O número {c} é o menor")
    else:
        print(f"O número {a} é o menor")
else:
    print(f"O número {c} é o maior")
    if (a >= b):
        print(f"O número {b} é o menor")
    else:
        print(f"O número {a} é o menor")