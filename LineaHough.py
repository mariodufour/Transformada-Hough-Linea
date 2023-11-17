# cv2 proporciona herramientas para realizar operaciones de procesamiento de imágenes
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Leer la imagen
imagen = cv2.imread('C:/Users/marit/OneDrive/Documentos/imagenHough/motor2.jpg')
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detección de bordes
bordes = cv2.Canny(gris, 50, 150, apertureSize=3)

# Transformada de Hough para detectar líneas
lineas = cv2.HoughLines(bordes, 1, np.pi / 180, 150)

# Dibujar las líneas detectadas en la imagen
for linea in lineas:
    rho, theta = linea[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(imagen, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Mostrar la imagen con las líneas detectadas
plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
plt.title('Líneas detectadas')
plt.show()