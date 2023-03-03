import numpy as np

b = np.arange(3)

print(f"\n{b}")

print(f"\n {np.exp(b)}")

#raiz quadrada

print(f"\n {np.sqrt(b)}")

#para acessar os elementos do array, podemos usar um índice por eixo
c = np.arange(12).reshape(3,4)

print(f"\n {c}")

print(f"\n {c[1,2]}")

#print(f"\n {c[3,4]}")

print(f"\n {c[-1]}")