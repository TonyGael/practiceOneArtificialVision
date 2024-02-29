# # Importamos las librerías
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Leemos las imagees con lectura en grises:
# img_gray = cv2.imread("LEC.png", 0)  # 0 para escala de grises un solo canal una sola matriz
#
# # leemos a color:
# img_rgb = cv2.imread("LEC.png", 1)  # 1 para rgb,3 canales, 3 matrices
#
# # lectura completa de la imagen:
# img = cv2.imread("LEC.png")  # lectura por default 3 canales 3 matrices
#
# # Extraemos atributos de la imagen en grises:
# tama_gray = img_gray.shape
# tipo = img_gray.dtype
# print(f'Tamano de la imagén en grises: {tama_gray}.\nTipo de dato: {tipo}')
#
# # Extraemos atributos principales de la imagen en rgb:
# tama_rgb = img_rgb.shape
# tipo_rgb = img_rgb.dtype
# print(f'Tamano de la imágen RGB: {tama_rgb}.\nTipo de la imágen RGB: {tipo_rgb}')
#
# # PLoteamos las imágenes:
# cv2.imshow("GRAY", img_gray)
# cv2.imshow("RGB", img_rgb)
# cv2.imshow("IMG", img)
#
# # Corregimos el color
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#
# # Ploteamos la imagen
# plt.imshow(img)
# plt.show()
#
# # Esperamos un evnto de teclado para pasar la imagen:
# # cv2.waitKey(0)

# Importamos las librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt


# Lectura de imagenes
# Lectura en Gray
imggray = cv2.imread("LEC.png", 0)  # 1 CANAL 1 MATRIZ

# Lectura a color
imgRGB = cv2.imread("LEC.png",1)  # 3 CANALES 3 MATRICES

# Lectura
img = cv2.imread("LEC.png")   # 3 CANALES 3 MATRICES

# Extraer atributos principales
tama = imggray.shape
tipo = imggray.dtype
print("Tamaño Gray | Tipo de Dato |", tama, tipo)

# Extraer atributos principales
tamargb = imgRGB.shape
tiporgb = imgRGB.dtype
print("Tamaño RGB | Tipo de Dato |", tamargb, tiporgb)

# Mostramos las imagenes
cv2.imshow("GRAY", imggray)
cv2.imshow("RGB", imgRGB)
cv2.imshow("IMG", img)

# Correccion COLOR
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Mostramos nuestra imagen
plt.imshow(img)
plt.show()


# Con el teclado pasamos la imagen
cv2.waitKey(0)