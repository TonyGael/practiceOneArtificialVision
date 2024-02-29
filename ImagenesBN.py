# Primero importamos las librerías que vamos a usar:

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Para crear la imágen negra:
img = np.zeros((10, 10, 1), np.uint8)

# vamos a cargar / modificar algunos pixeles de la imagen
img[0,1] = 30
img[2,3] = 50
img[4,5] = 200
img[6,7] = 140

# presentamos los valores numéricos de la imágen
print(img)

# Ahora ploteamos la imágen
plt.imshow(img, cmap='gray')
plt.show()
