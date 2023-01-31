import math
import numpy

r = 6371
lat1 = int(input("Digite em graus decimais a primeira latitude: "))
lat2 = int(input("Digite em graus decimais a segunda latitude: "))
long1 = int(input("Digite em graus decimais a primeira longitude: "))
long2 = int(input("Digite em graus decimais a segunda longitude: "))

h = 2*r * numpy.arcsin(pow(((math.sin((lat2-lat1)/2))**2)+math.cos(lat1)*math.cos(lat2)*((math.sin(long2-long1)/2)**2),2))

print(h)