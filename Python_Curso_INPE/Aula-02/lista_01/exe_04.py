# código para realizar a fórmula de Haversine**2

import numpy
from math import *

o1 = numpy.radians(float(input("Digite em graus a primeira latitude: ")))

o2 = numpy.radians(float(input("Digite em graus a segunda latitude: ")))

y1 = numpy.radians(float(input("Digite em graus a primeira longitude: ")))

y2 = numpy.radians(float(input("Digite em graus a segunda longitude: ")))

H = (2*6371) * numpy.arcsin(sin((o2-o1)/2)**2 + cos(o1)*cos(o2) * sin((y2-y1)/2)**2)

print("A distancia entre os dois pontos citados apartir do cálculo da fórmula de Haversine é de: ")
print(H)