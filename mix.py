import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

img = cv2.imread('images/img5.jpeg',0)


height, width = img.shape[:2]
print("width")
print(width)
print("height")
print(height)
width_half = int(width/2)
height_half = height/2

crop_img = img[100:height, 50:530]
cv2.imwrite("cropped.jpeg",crop_img)

IMAGE = "cropped.jpeg"
img=cv2.imread(IMAGE)
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

print(hsv.shape)
height, width = img.shape[:2]

lower_white = np.array([0,0,0], dtype=np.uint8)
upper_white = np.array([0,0,255], dtype=np.uint8)

# # Threshold the HSV image to get only white colors
mask = cv2.inRange(hsv, lower_white, upper_white)
# # Bitwise-AND mask and original image
res = cv2.bitwise_and(hsv,hsv, mask= mask)

v  = hsv[:, :, 0]
v_mask_new = hsv[:, :, 2] < 220

v[v_mask_new]=255
v[~v_mask_new]=100

cv2.imwrite('hsvimg.jpeg',hsv)

height, width = img.shape[:2]
print("cropped width")
print(width)
print("cropped height")
print(height)

edges = cv2.Canny(crop_img,200,255)
inv_edges = np.invert(edges)

# plt.subplot(121),plt.imshow(crop_img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(inv_edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

alpha = 0.2
beta  = 1-alpha

img2 = cv2.imread('hsvimg.jpeg',0)
dst = cv2.addWeighted(img2, alpha, inv_edges, beta, 0.0)
cv2.imwrite('outline.jpeg',dst)

cv2.imshow('Pressure Points',hsv)
cv2.imshow('Outlines',dst)

cv2.waitKey(0)

