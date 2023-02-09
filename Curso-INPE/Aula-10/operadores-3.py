import numpy as np

# as funções sum, min e max funcionam para ndarrays
a = np.random.random((2,3))

print(f"\n{a}")

print(f"\n{a.sum()}")

print(f"\n{a.min()}")

print(f"\n{a.max()}")

# a função reshape altera a estrutura do ndarray

b = np.arange(12).reshape(3,4)

print(f"\n{b}")

print(f"\n{b.sum(axis=0)}")

print(f"\n{b.min(axis=1)}")

# soma cumulativa

print(f"\n{b.cumsum(axis=1)}")