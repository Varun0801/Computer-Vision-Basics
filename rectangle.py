import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv2.rectangle(img,(200,100),(300,0),(255,0,255),5)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
