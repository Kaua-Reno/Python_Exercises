import numpy as np

a = np.array([20, 30, 40, 50])

print(f"\n{a}")

b = np.arange(4)

print(f"\n{b}")

c = a - b

print(f"\n{c}")

b = b**2

print(f"\n{b}")

d = 10*np.sin(a)

print(f"\n{d}")

print(f"\n{a<35}")