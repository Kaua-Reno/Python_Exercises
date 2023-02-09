import numpy as np

# o operador * calcula o produto por elemento, e não por matriz (para isso usa-­se a função dot)


a = np.array([[1,1], [0,1]])

b = np.array([[2,0], [3,4]])

c = a * b

print(f"\n{c}")

a = a.dot(b)

print(f"\n{a}")

# operações como += e *= modificam a própria matriz

a = np.ones((2,3))

# é o mesmo que a = a * 3
a *= 3 

print(f"\n {a}")

b = np.random.random((2,3))

b += a

print(f"\n{b}")