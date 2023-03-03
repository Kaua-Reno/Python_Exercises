import numpy as np

# Utilize funções NumPy para calcular a distância euclidiana entre as séries

# definindo as series

serie_1 = np.array((168, 398, 451, 337, 186, 232, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258, 242, 331, 251, 323, 106, 1055, 170))

serie_2 = np.array((168, 400, 451, 300, 186, 200, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258, 242, 331, 251, 180, 106, 1055, 200))

#aplicar o calculo

subtracao = serie_1 - serie_2
quadrado =  subtracao**2
somatorio = np.sum(quadrado)
distancia_euclidiana = np.sqrt(somatorio)

print(f'{distancia_euclidiana}')