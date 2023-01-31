xg = int(input("Digite o valor de grenn: "))
xn = int(input("Digite o valor de nir: "))
xr = int(input("Digite um valor para red: "))

NDWI = (xg-xn)/(xg+xn)

NDVI = (xn-xr)/(xn+xr)

print("Os valores de NSWI e NDVI são respectivamente", NDWI, " e ", NDVI)