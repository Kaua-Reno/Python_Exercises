#Códigos das anotações da aula 6 - String

#Operador +
a = "Gilberto " + "Ribeiro " + "de " + "Queiroz"
print(a)

#Operador *

b = "Gilberto" * 3
c = -4 * "Gilberto"
print(b)
# * -n -> não retorna nada
print(c)

#Pertinencia in

d = "i" in "Gilberto Ribeiro de Queiroz"
print(d)

#Pertinencia not in

e = "i" not in "Gilberto Ribeiro de Queiroz"
print(e)

#Operador len()

f = len("Gilberto Ribeiro de Queiroz")
print(f)

#Operador [], o primeiro elemento é o [0]
g = "Gilberto Ribeiro de Queiroz"[3]
print(g)

#Operador [x,y]:
h = "Gilberto Ribeiro de Queiroz"[0:3]
print(h)

#Operação str.find()
i = "Gilberto Ribeiro".find("rto")
print(i)

#Operação s.join
j = "-".join( ("Gilberto", "Ribeiro", "de", "Queiroz") )
k = " ".join( ("Gilberto", "Ribeiro", "de", "Queiroz") )
print(j)
print(k)

#Operação s.split
l = "Gilberto Ribeiro de Queiroz".split()
print(l)

#Operação s.replace(old, new[, count])
m = "Gilberto Ribeiro de Queiroz".replace("i", "@")
print(m)

#Operação str.isdigit()
n = "4565757".isdigit()
print(n)

#Operação str.islower()
o = "hdiauhgausdhgksdjghadsu".islower()
print(o)

#Operação str.isupper()
p = "IYGYFTEDRYTGHBNJLK".isupper()
print(p)

#Operação str.lower()
q = "JGFKUashfgayilGLGAYLSJGFASfhuagvQHIUGFLIASG".lower()
print(q)

#Operação str.upper()
r = "JGFKUashfgayilGLGAYLSJGFASfhuagvQHIUGFLIASG".upper()
print(r)