import cv2

img = cv2.imread('opencv.png',0)# Load an image 

cv2.imshow('image',img)#displays an image
cv2.waitKey(10) # it waits idefinitely for a key stroke
cv2.imwrite('cv1.png',img)# rename the filename and save as newfile    
cv2.destroyAllWindows()# simple destroy all we created windows
