red_values = ( 168, 398, 451, 337, 186, 232,262, 349, 189, 204, 220, 220, 207, 239, 259,258, 242, 331, 251, 323, 106, 1055, 170 )

nir_values = ( 2346, 4431, 4638, 4286, 2752, 3521, 2928, 3087, 2702, 2685, 2702, 2865, 2835, 2955, 3019, 3391, 2986, 4042, 3050, 3617, 2478, 3361, 2613 )

timeline = ( "2015-01-01", "2015-01-17", "2015-02-02", "2015-02-18", "2015-03-06", "2015-03-22", "2015-04-07", "2015-04-23", "2015-05-09", "2015-05-25", "2015-06-10", "2015-06-26", "2015-07-12", "2015-07-28", "2015-08-13", "2015-08-29", "2015-09-14", "2015-09-30", "2015-10-16", "2015-11-01", "2015-11-17", "2015-12-03", "2015-12-19" )

print("Série temporal NDVI: \n----------------------\ndata -> NDVI -> média")

# lista com o calculo do NDVI
ndvi = [(x-y)/(x+y) for x,y in zip(nir_values, red_values )]

#printando o NDVI e o tempo em que ele ocorre
for t, n in zip(timeline, ndvi): 
    print(t, n) 

#Achando o menor e maior valor
min = min(ndvi)
max = max(ndvi)

#Achando a posição do menor e maior valor
tmin = ndvi.index(min)
tmax = ndvi.index(max)

#printando o menor e maior valor
print("Maior valor -> tempo\n", max,timeline[tmax])
print("Menor valor -> tempo\n", min,timeline[tmin])

