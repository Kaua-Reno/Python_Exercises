#código para ver se o número digitado é divisivel por 2 e 3

n = int(input("Digite um número maior que 0:"))

if n%2 == 0 and n%3 == 0:
    print("O número", n,"é divisível por 2 e 3")
elif n%2 == 0 and n%3 == 1:
    print("O número", n,"é divisível apenas por 2")
elif n%3 == 0 and n%2 == 1:
    print("O número", n,"é divisível apenas por 3")  
else:
    print("O número", n,"não é dívisivel por 2 e 3")  