import numpy as np
import matplotlib.pyplot as plt

banda = np.zeros([10, 10])

# modificar alguns pixels da banda

banda[2, 2] = banda[2, -3] = banda[4, 4] = banda[4, 5] = banda[6, 1] = banda[6, -2] = banda[7, 2:8] = 0.25

# para mostrar a matriz como uma imagem

plt.imshow(banda, vmax=255)

plt.show()

# ao não perceber nenhum conteúdo na imagem, pense num ganho ou offset para aplicar na imagem

banda *= 500

plt.imshow(banda, vmax=255)

plt.show()