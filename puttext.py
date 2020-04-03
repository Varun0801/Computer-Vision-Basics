
import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

#cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.rectangle(img,(100,100),(420,410),(0,0,255),1)
cv2.putText(img,'OpenCV',(184,500), 
            font, 2,(255,255,255),
            4)     
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
