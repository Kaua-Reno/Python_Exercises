#Programa para calcular a menor distância entre um ponto e uma reta, apartir da forma normal de Hassean para retas**2

import math

x = int(input("Digite o valor de x do ponto: "))
y = int(input("Digite o valor de y do ponto: "))

xa = int(input("Digite o valor de x do ponto 1 que pertence a  reta: "))
ya = int(input("Digite o valor de y do ponto 1 que pertence a reta: "))

xb = int(input("Digite o valor de x do ponto 2 que pertence a reta: "))
yb = int(input("Digite o valor de y do ponto 2 que pertence a reta: "))

h = abs((yb - ya) * (x - xa) - (xb - xa) * (y - ya) / math.sqrt(pow(xb - xa, 2) + pow(yb - ya, 2)))

if h > 0:
    print("A menor distancia entre o ponte e a reta citada é de:", h)
else:
    print("Coordenadas incorretas")