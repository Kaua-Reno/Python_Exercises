n = int(input("Digite um número:"))

#Código série Lucas
if n == 0:
    print("2\n")
elif n == 1:
    print("1\n")
else:
    luc = 1
    cas = 2
    print("2 \n1")
    for l in range(1, n-1):
        lu = luc + cas
        cas = luc
        luc = lu
        print(lu)

print("\n")

#Código série Pell
if n == 0:
    print("0\n")
elif n == 1:
    print("1\n")
else:
    pel = 1
    ell = 0
    print("0 \n1")
    for p in range(1, n-1):
        pe = 2*pel + ell
        ell = pel
        pel = pe
        print(pe)

print("\n")

#Código série Triangular
for t in range(0, n):
    tri = t*(t+1)/2
    print(tri)

print("\n")

#Código série Square
for s in range(0,n):
    squ = pow(s,2)
    print(squ)

print("\n")

#Código série Pentagonal
for pt in range(0, n):
    pent = (3*pow(pt,2)-pt)/2
    print(pent)