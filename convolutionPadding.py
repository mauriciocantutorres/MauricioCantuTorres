import cv2
import numpy as np
kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

def convolucion(imagen, kernel, padding=0, salto=1):

    xKernel = kernel.shape[0]
    yKernel = kernel.shape[1]
    xImagen = imagen.shape[0]
    yImagen = imagen.shape[1]

    xfinal = int(((xImagen - xKernel + 2 * padding) / salto) + 1)
    yfinal = int(((yImagen - yKernel + 2 * padding) / salto) + 1)
    img_final = np.zeros((xfinal, yfinal))

    if padding != 0:
        padded = np.zeros((imagen.shape[0] + padding*2, imagen.shape[1] + padding*2))
        padded[int(padding):int(-1 * padding), int(padding):int(-1 * padding)] = imagen
    else:
        padded = imagen

    for i in range(imagen.shape[1]):
        if i > imagen.shape[1] - yKernel:
            break
        if i % salto == 0:
            for j in range(imagen.shape[0]):
                if j > imagen.shape[0] - xKernel:
                    break
                try:
                    if j % salto == 0:
                        img_final[j, i] = (kernel * padded[j: j + xKernel, i: i + yKernel]).sum()
                except:
                    break

    return img_final

imagen = cv2.imread("home.jpg",0)

final = convolucion(imagen, kernel, padding=5)
cv2.imshow("Imagen final", final)
cv2.waitKey(0)
