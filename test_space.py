import numpy as np

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images/test1.jpg', cv2.IMREAD_COLOR)
img2 = img[..., ::-1]
plt.imshow(img2, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()