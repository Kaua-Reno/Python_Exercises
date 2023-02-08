import numpy as np

a = np.arange(15).reshape(3, 5)

print(f"\n{a}")

print(f"\n{a.shape}")

print(f"\n{a.ndim}")

print(f"\n{a.dtype.name}")

print(f"\n{a.itemsize}")

print(f"\n{a.size}")

print(f"\n{type(a)}")

b = np.array([6, 7, 8])

print(f"\n{b}")

print(f"\n{type(b)}")