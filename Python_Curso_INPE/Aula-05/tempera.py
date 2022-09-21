# Converter de ºF para ºC os graus de 20 até 300, pulando de 20 em 20

for fahr in range(0, 320, 20):
    celsius = 5 * (fahr - 32) / 9 
    print(fahr, celsius) 