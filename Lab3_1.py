import cv2
import numpy as np
img = cv2.imread('123.png')
img[img == 255] = 254
img2 = img

n = img2.shape[0] * img2.shape[1] * img2.shape[2]
for i in range(0, img2.shape[0]):
    for j in range(0, img2.shape[1]):
        color = img2[i, j]
        r = 0
        for jj in range(0, color[0]):
            nr = np.count_nonzero(img2 == jj)
            r = r + nr / n
        r *= 255

        g = 0
        for jj in range(0, color[1]):
            ng = np.count_nonzero(img2 == jj)
            g = g + ng / n
        g *= 255

        b = 0
        for jj in range(0, color[2]):
            nb = np.count_nonzero(img2 == jj)
            b = b + nb / n
        b *= 255
        img2[i, j] = (r, g, b)
cv2.imwrite('1.png', img2)