import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

img = cv2.imread('images/img1.jpeg',0)
import matplotlib.patches as mpatches


img = cv2.imread("images/img5.jpeg")
height, width = img.shape[:2]
print("width")
print(width)
print("height")
print(height)
width_half = int(width/2)
height_half = height/2

crop_img = img[100:height, 90:530]
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


RED 	= 	[255, 0, 0]	
ORANGE  = 	[255, 127, 0]	
YELLOW  = 	[255,255,0]
GREEN   = 	[0,255,0]
BLUE    = 	[0,0,255]
WHITE   = 	[255,255,255]

copy_of_hsv = hsv
inv_hsv = np.invert(hsv)

for i in range(height):
	for j in range(width):
		if(j>180 and j<280):
			inv_hsv[i][j] = WHITE
		elif(inv_hsv[i][j][2]>=0 and inv_hsv[i][j][2]<5):
			inv_hsv[i][j] = RED											#RED
		elif(inv_hsv[i][j][2]>=5 and inv_hsv[i][j][2]<10):
			inv_hsv[i][j] = ORANGE										#ORANGE
		elif(inv_hsv[i][j][2]>=10 and inv_hsv[i][j][2]<15):
			inv_hsv[i][j] = YELLOW										#YELLOW
		elif(inv_hsv[i][j][2]>=15 and inv_hsv[i][j][2]<30):
			inv_hsv[i][j] = GREEN										#GREEN
		elif(inv_hsv[i][j][2]>=30 and inv_hsv[i][j][2]<100):
			inv_hsv[i][j] = BLUE										#BLUE
		else:
			inv_hsv[i][j] = WHITE										#WHITE

v = inv_hsv[:, :, 2]

plt.imshow(inv_hsv)
red_patch = mpatches.Patch(color='red', label='Highest pressure')
orange_patch = mpatches.Patch(color='orange', label='High pressure')
yellow_patch = mpatches.Patch(color='yellow', label='Medium pressure')
green_patch  = mpatches.Patch(color='green', label='Low pressure')
blue_patch = mpatches.Patch(color='blue', label='Lowest pressure')

plt.legend(handles=[red_patch, orange_patch, yellow_patch, green_patch, blue_patch])

plt.show()

plt.close()
