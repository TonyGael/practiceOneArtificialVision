# Importamos las librerías:
import cv2
import matplotlib.pyplot as plt

# Tratamos la imagen:
img = cv2.imread("LEC.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# correccion:
imghsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

# eXTRAEMOS LOS CANALES
H, S, V = cv2.split(imghsv)

# mostramos los canales
fig = plt.figure()

# canal Hue:
ax1 = fig.add_subplot(2, 2, 1)
ax1.imshow(H, cmap="gray")
ax1.set_title("CANAL HUE")

# canal Saturation:
ax2 = fig.add_subplot(2, 2, 2)
ax2.imshow(S, cmap="gray")
ax2.set_title("Canal SATURATION")

# Canal Value:
ax3 = fig.add_subplot(2, 2, 3)
ax3.imshow(V, cmap="gray")
ax3.set_title("Canal VALUE")

# reconstruccion de la imagen:
imgre = cv2.merge((H, S, V))

# la imagnew original:
ax4 = fig.add_subplot(2, 2, 4)
ax4.imshow(img)
ax4.set_title("IMAGEN ORIGINAL")

plt.show()

# evento del teclado para pasar la imagen
cv2.waitKey(0)
