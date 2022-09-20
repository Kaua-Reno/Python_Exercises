# Programa que pede os valores de green, nir e red e imprime como resultado os valores de NDWI

green = float(input("Digite o valor de green: "))

nir = float(input("Digite o valor de nir: "))

red = float(input("Digite o valor de red: "))

NDWI = ((green - nir) / (green + nir))

NDVI = ((nir - red) / (nir + red))

print('O valor de NSWI e NDVI são:')
print(NDWI, NDVI)
