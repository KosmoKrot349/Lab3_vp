import cv2
import numpy as np

img = cv2.imread('123.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
equ = cv2.equalizeHist(img_gray)
cv2.imwrite('2.png',equ)