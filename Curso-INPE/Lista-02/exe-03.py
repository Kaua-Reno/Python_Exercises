#Séries númericas

n = int(input("Digite um número: "))

#Lucas
l1 = 2
l2 = 1
if(n == 0):
    print(f"Lucas {l1}")
elif(n == 1):
    print(f"Lucas {l1}")
    print(f"Lucas {l2}")
else:
    print(f"Lucas {l1}")
    print(f"Lucas {l2}")
    for k in range(1, n):
        l = l1 + l2
        print(f"Lucas {l}")
        l1 = l2
        l2 = l
print("\n")

#Pell

p1 = 0
p2 = 1
if(n == 0):
    print(f"Pell {p1}")
elif(n == 1):
    print(f"Pell {p1}")
    print(f"Pell {p2}")
else:
    print(f"Pell {p1}")
    print(f"Pell {p2}")
    for j in range(1, n):
        p = p2*2 + p1
        print(f"Pell {p}")
        p1 = p2
        p2 = p
print("\n")

#Triangular

for m in range(-1, n):
    t = m + 1
    t = (t*(t+1))/2
    print(f"Triangular {t}")
print("\n")

#Square

for o in range(1, n+1):
    s = o**2
    print(f"Square {s}")
print("\n")

#Pentagonal

for w in range(1, n+1):
    pe = (3*(w**2)-w)/2
    print(f"Pentagonal {pe}")
print("\n")