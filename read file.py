import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("C:\\Users\\Admin\\Pictures\\tree.jpg")
cv2.imwrite("C:\\Users\\Admin\\Pictures\\tree1.jpg",img)
RGB_img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(RGB_img)
plt.waitforbuttonpress()
plt.close('all')
