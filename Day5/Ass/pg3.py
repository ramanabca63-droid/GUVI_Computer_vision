import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("Ass/sample.jpg")

blur=cv2.blur(img,(5,5))
gaussian=cv2.GaussianBlur(img,(5,5),0)

median=cv2.medianBlur(img,3)
plt.imshow(cv2.cvtColor(blur,cv2.COLOR_BGR2RGB))
plt.show()