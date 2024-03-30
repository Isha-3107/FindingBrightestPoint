import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread("star.jpg")

img_gray = np.copy(img)

img_gray = cv2.cvtColor(img_gray, cv2.COLOR_BGR2GRAY)

plt.imshow(img_gray)
i = cv2.minMaxLoc(img_gray)
print("The co-ordinates of the position of the brightest star are",i[3])