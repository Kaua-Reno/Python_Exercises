import numpy as np
from numpy import pi

# a função linspace gera um intervalo de números com um tamanho específico
a = np.linspace(0, 2, 9)

print(f"\n{a}")

# 100 números entre 0 e 2pi
b = np.linspace(0, 2*pi, 100)

print(f"\n{b}")

# seno de todos os números, calculados de uma só vez
c = np.sin(b)

print(f"\n{c}")