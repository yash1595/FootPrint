import cv2
pic = "foot2.jpeg"
img = cv2.imread(pic)
height, width = img.shape[:2]
print("width")
print(width)
print("height")
print(height)
width_half = int(width/2)
height_half = height/2

# 320, 240
crop_img = img[100:height, 110:500]
cv2.imwrite("cropped.jpeg",crop_img)
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)