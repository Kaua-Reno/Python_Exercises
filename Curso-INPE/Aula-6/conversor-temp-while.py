t_min = 0 #Temperatura mínima
t_max = 300 #Temperatura máxima
delta_t = 20 #Delta de temperatura a cada passo

fahr = t_min #temperatura inicial

while fahr <= t_max:
    celcius = 5*(fahr-32)/9

    print(fahr, celcius)

    fahr = fahr + delta_t