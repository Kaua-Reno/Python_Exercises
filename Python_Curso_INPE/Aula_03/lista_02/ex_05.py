#código para práticar condicionais com interação com usuário

a = "Lucas"
b = "Pell"
c = "Triangular"
d = "Square"
e = "Pentagonal"

print("Séries:")
print("0 Lucas")
print("1 Pell")
print("2 Triangular")
print("3 Square")
print("4 Pentagonal")

comp = int(input("Qual série você deseja computar? "))

if comp == 0:
    print("Você escolheu computar a série ", a)
elif comp == 1:
    print("Você escolheu computar a série ", b)
elif comp == 2:
    print("Você escolheu computar a série ", c)
elif comp == 3:
    print("Você escolheu computar a série ", d)
else:
    print("Você escolheu computar a série ", e)