serie_modis = [7000, 6000, 3000, 3000, 
10000, 2000, 5000, 500, 7500, 3000]

p = len(serie_modis)

lista = [serie_modis[x]/10000 for x in range (0, p)]
print(lista)