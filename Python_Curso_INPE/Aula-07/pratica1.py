serie_ndvi = [0.3, -0.3, 0.2, None, 0.9, 0.8, 0.8, None, 0.2, 0.2]

p = serie_ndvi.count(None)
m = len(serie_ndvi)

#printar a quantidadde de valores inválidos e válidos
print(p)
print(m-p)