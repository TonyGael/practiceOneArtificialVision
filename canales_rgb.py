# Importar las librerías:
import cv2
import matplotlib.pyplot as plt

# Tratamos la imagen:
# Creamos la matriz principal

img = cv2. imread("LEC.png")

# Coreggimos el color
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Vamos a extraer los canales
# R = img[:, :, 0]
# G = img[:, :, 1]
# B = img[:, :, 2]

print(img)

# para extraer la imagen desestructurando
R, G, B = cv2.split(img)

# Vamos a  mostrar los canales
fig = plt.figure()

# Canal rojo:
ax1 = fig.add_subplot(2, 2, 1)
ax1.imshow(R, cmap="gray")
ax1.set_title("CANAL ROJO")

# canar verde:
ax2 = fig.add_subplot(2, 2, 2)
ax2.imshow(G, cmap="gray")
ax2.set_title("CANAL VERDE")

# cANAL AZUL:
ax3 = fig.add_subplot(2, 2, 3)
ax3.imshow(B, cmap="gray")
ax3.set_title("CANAL AZUL")

# RECONSTRUIMOS LA IMAGEN:
imgre = cv2.merge((R, G, B))

# iagen original:
ax4 = fig.add_subplot(2, 2, 4)
ax4.imshow(imgre)
ax4.set_title("IMAGEN ORIGINAL")
# plt.imshow(img)

plt.show()
