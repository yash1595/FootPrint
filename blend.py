import cv2
import numpy as np
#_____________ Width and height ___________________#
img = cv2.imread("images/img1.jpeg")
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

#_________ Threshold to get desired image___________#
lower_white = np.array([0,0,0], dtype=np.uint8)
upper_white = np.array([0,0,255], dtype=np.uint8)

# # Threshold the HSV image to get only white colors
mask = cv2.inRange(hsv, lower_white, upper_white)
# # Bitwise-AND mask and original image
res = cv2.bitwise_and(hsv,hsv, mask= mask)

v  = hsv[:, :, 0]
v_mask_new = hsv[:, :, 2] < 250

v[v_mask_new]=255
v[~v_mask_new]=0


alpha = 0.0
beta  = 1-alpha

dst = cv2.addWeighted(crop_img, alpha, hsv, beta, 0.0)

#cv2.imshow("images", np.hstack([crop_img, hsv]))
cv2.imshow("images", dst)

cv2.imwrite('hsvimg.jpeg',hsv)
cv2.waitKey(0)

