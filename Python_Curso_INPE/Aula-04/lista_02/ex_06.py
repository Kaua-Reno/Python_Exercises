# Código para retornar o conceito de uma nota(A+= excepcional, A= Excelente,...,etc)

conc = str(input("Digite o seu conceito final(A+,A,A-,B+,B,B-,C+,C,C,D) de alguma disciplina: "))

A = " Excepcional"
A1 = " Excelente"
B = " Bom"
C = " Regular"
D = " Reprovação"

if conc == "A+":
    print("Esse é o significado em desempenho desse conceito final:", A)
elif conc == "A" or conc == "A-":
    print("Esse é o significado em desempenho desse conceito final:", A1)
elif conc == "B+" or conc == "B" or conc == "B-":
    print("Esse é o significado em desempenho desse conceito final:", B)
elif conc == "C+" or conc == "C" or conc == "C-":
    print("Esse é o significado em desempenho desse conceito final:", C)
else:
    print("Esse é o significado em desempenho desse conceito final:", D)