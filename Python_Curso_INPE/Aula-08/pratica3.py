# Função para o calculo da distância de Haversine

import numpy
import math
from math import *

def Haversine(l1, l2):
    
    o1 = l1["latitude"]
    o2 = l2["latitude"]
    y1 = l1["longitude"]
    y2 = l2["longitude"]

    #Calculo da Distância de Haversine
    H = (2*6371) * numpy.arcsin(math.sqrt(sin((o2-o1)/2)**2 + cos(o1)*cos(o2) * sin((y2-y1)/2)**2))

    return H

# Localização de "São José dos Campos" em grau decimal
sjc = { "longitude" : -45.88, "latitude" : -23.17 }

# Localização de "Ouro Preto" em grau decimal
ouro_preto = { "longitude": -43.50, "latitude": -20.38 }

x = Haversine(sjc, ouro_preto)

print(x)