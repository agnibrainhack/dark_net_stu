import cv2
import matplotlib.pyplot as plt
import numpy as np

product = []
im = cv2.imread('square.jpg')
resized_image = cv2.resize(im, (64, 64))
edges = cv2.Canny(resized_image, 150, 250)


plt.subplot(121), plt.imshow(resized_image, cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
b = edges.flatten()
list_4096 = list(b)
for n, i in enumerate(list_4096):
    if i == 255:
        list_4096[n] = 1
print(list_4096)
plt.show()

