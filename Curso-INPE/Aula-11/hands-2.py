import numpy as np
import matplotlib.pyplot as plt

# criar a banda

banda = np.arange(100).reshape([10,10])

# definir o offset

offset = 200

# aplicar o offset

banda += offset
banda[banda > 255] = 255
banda[banda < 0] = 0

# desenhat na tela 

plt.imshow(banda, cmap='gray')
plt.show()