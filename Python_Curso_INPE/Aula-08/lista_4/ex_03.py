a = "Gilberto"
b = "sensoriamento remoto"
c = "GilberTo"
d = "ser347@dpi.inpe.br"
e = "CBER_4_PAN5M_2018308"
f = "Gilberto@@@"
g = "@@Gilberto@@@"

#Funções
def Concatena(x):
    x = "++" + x + "++"
    return x

def PrimeiraM(x):
    return x[0].upper() + x[1:]

def InicialM(x):
    return x.title()

def Minusculo(x):
    return x.lower()

def Concatena2(x):
    return x + "**"

def Concatena3(x):
    return "**" + x

def Normal(x):
    return x

def Separa(x):
    return x.partition("@")

def Separa2(x):
    return x.split("_", 3)

def Remove(x):
    return x.replace("@", "")


#Entradas
conc = Concatena(a)
print(conc)

prim = PrimeiraM(b)
print(prim)

ini = InicialM(b)
print(ini)

min = Minusculo(c)
print(min)

conca = Concatena2(a)
print(conca)

con = Concatena3(a)
print(con)

nor = Normal(a)
print(nor)

sep = Separa(d)
print(sep)

sepa = Separa2(e)
print(sepa)

rem = Remove(f)
print(rem)

rem1 = Remove(g)
print(rem1)