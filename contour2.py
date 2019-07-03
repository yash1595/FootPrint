import cv2 
import numpy as np 


IMAGE = "cropped.jpeg"
# Let's load a simple image with 3 black squares 
gray = cv2.imread(IMAGE) 
cv2.waitKey(0) 
  
# Grayscale 
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

linek = np.zeros((11,11),dtype=np.uint8)
linek[5,...]=1
x=cv2.morphologyEx(gray, cv2.MORPH_OPEN, linek ,iterations=1)
gray-=x

# Find Canny edges 
edged = cv2.Canny(gray, 0, 200) 
cv2.waitKey(0) 
  
# Finding Contours 
# Use a copy of the image e.g. edged.copy() 
# since findContours alters the image 
contours = cv2.findContours(edged,  
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 

cv2.imshow('Canny Edges After Contouring', edged) 
cv2.waitKey(0) 
  
print("Number of Contours found = " + str(len(contours))) 
  
# Draw all contours 
# -1 signifies drawing all contours 
cv2.drawContours(image, contours, -1, (0, 255, 0), 3) 
  
cv2.imshow('Contours', image) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 