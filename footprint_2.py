import cv2
import numpy as np
from matplotlib import pyplot as plt

#-----Reading the image-----------------------------------------------------
img = cv2.imread('foot1.jpeg', 1)
plt.subplot(121)
plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

#-----Converting image to LAB Color model----------------------------------- 
lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
plt.subplot(122),plt.imshow(lab,cmap = 'gray')
# #-----Splitting the LAB image to different channels-------------------------
l, a, b = cv2.split(lab)
plt.subplot(221),plt.imshow(l,cmap = 'gray')
plt.subplot(222),plt.imshow(a,cmap = 'gray')
plt.subplot(321),plt.imshow(b,cmap = 'gray')

# #-----Applying CLAHE to L-channel-------------------------------------------
# clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
# cl = clahe.apply(l)
# cv2.imshow('CLAHE output', cl)

# #-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
# limg = cv2.merge((cl,a,b))
# cv2.imshow('limg', limg)

# #-----Converting image from LAB Color model to RGB model--------------------
# final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
# cv2.imshow('final', final)

plt.show()
#_____END_____#